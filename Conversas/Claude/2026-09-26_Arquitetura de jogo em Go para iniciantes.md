## Sidinei:

Me explique de forma detalhada e em fases como esta decidido a arquitetura decidida do jogo.

Vale ressaltar que sou iniciante em go, e preciso saber de ponta a ponta essa arquitetura eu sei outras linguagens mas o go e o jeito de desenvolver em go eu nao sei bem.

---

## Claude:

Vou seguir o caminho de uma requisição: primeiro o esqueleto do programa, depois o que acontece fora do mundo, depois o que acontece dentro dele. Em cada fase, junto com a decisão do `docs/arquitetura-consolidada.md`, entra o conceito de Go que você precisa para entendê-la.

---

## Fase 0 — O modelo mental

Antes de qualquer pacote, o documento fixa cinco princípios. Todo o resto sai deles:

1. **Servidor autoritativo.** O cliente pede e o servidor decide.
2. **Command → State → Event.** O comando pede, o núcleo valida e muda o estado, e o evento comunica o resultado.
3. **O tempo é do servidor.** Uma ação é uma `Activity` com `StartedAt` e `EndsAt`.
4. **A concorrência segue o ownership.** Primeiro você decide quem é dono do estado. Só depois escolhe o mecanismo.
5. **Escopo pequeno, fronteiras definitivas.**

```text
cliente: "quero coletar wood_01"   (intenção)
            │
            ▼
servidor: valida → muda estado → "coleta começou, termina 10:05"   (fato)
```

**Analogia:** o cliente é quem faz o pedido no balcão, e o servidor é a cozinha. O cliente não escreve na comanda que o prato já está pronto.

---

## Fase 1 — O esqueleto: como um programa Go é organizado

### Conceitos de Go que você precisa aqui

**Pacote = diretório.** Todos os `.go` de `internal/game/` formam o pacote `game`. O nome do arquivo não cria fronteira nenhuma, só o diretório.

**`internal/` é regra do compilador.** Nenhum código fora do módulo consegue importar o que está ali dentro.

**Visibilidade vem da primeira letra.** Nome com maiúscula é exportado, e com minúscula é privado ao pacote. Go não tem `public` nem `private`.

**Não existe classe.** Existe `struct`, existem métodos pendurados nela, e o "construtor" é só uma função chamada `NewX` por convenção.

```go
// internal/game/zone.go
package game

type Zone struct {
    ID   string // exportado: outros pacotes leem
    name string // privado: só o pacote game vê
}

func NewZone(id, name string) *Zone {
    return &Zone{ID: id, name: name}
}
```

**Erro é valor de retorno.** Não existe exceção. Toda função que pode falhar devolve `(resultado, error)`, e quem chama trata na hora com `if err != nil`.

### Decisão 4: `bootstrap` é o composition root

```text
cmd/server/main.go  →  bootstrap.New()  →  Application{Run, Shutdown}
     (quase vazio)       (monta tudo)
```

O `main` só chama `New()` e `Run()`. Quem monta tudo é o `bootstrap`: lê os dados, conecta no Postgres, cria repositories, services e handlers, sobe HTTP e WebSocket e inicia o game loop.

**Por que um pacote só para isso.** Conectar as peças é uma responsabilidade real. Se ela ficar no `main`, o `main` vira um arquivo de 500 linhas. Se ficar espalhada, o domínio acaba importando o Postgres.

A direção de dependência é de mão única: o `bootstrap` conhece todo mundo, ninguém conhece o `bootstrap`, e `game` não conhece infraestrutura.

**Contraste com o que você conhece:** em Node com NestJS ou em Java com Spring, um container de DI faz essa montagem por mágica. Em Go, e explicitamente no projeto (Decisão 11: sem framework de injeção), você faz à mão, com chamadas `NewX(dep)` em sequência. É verboso, mas dá para ler de cima a baixo.

---

## Fase 2 — Dados estáticos: `data → gamedata → bootstrap → game` (Decisão 3)

```text
data/*.json  →  gamedata      →  bootstrap  →  game
 (arquivos)     (lê e parseia)   (converte)    (runtime, estado vivo)
```

Cada peça tem uma única responsabilidade:

- **`gamedata`** sabe ler JSON e conhece o formato dos arquivos. Não conhece `game`.
- **`game`** é o domínio. Nunca lê JSON.
- **`bootstrap`** pega as definições de `gamedata` e constrói o `World` de `game`.

**Por quê.** Definição estática ("a zona X tem estes acampamentos") e estado mutável ("o jogador Y está coletando agora") têm ciclos de vida diferentes. Se você mudar o formato do JSON, só `gamedata` quebra.

**Regras de arquivo:**

- É um arquivo por tipo de entidade, nunca um por instância.
- `data/` fica na raiz do monorepo, não dentro de `backend/`, porque é conteúdo do jogo e não configuração do servidor.
- Nenhuma constante de jogo fica no código.

O documento permite um loader genérico, desde que seja só mecanismo. Aqui entram os generics de Go, com a sintaxe `[T any]`:

```go
// não exportado: não sabe o que é zona
func loadJSON[T any](path string) (T, error) {
    var v T
    b, err := os.ReadFile(path)
    if err != nil {
        return v, err
    }
    err = json.Unmarshal(b, &v)
    return v, err
}

// exportado e específico
func LoadZones(path string) ([]ZoneDef, error) {
    return loadJSON[[]ZoneDef](path)
}
```

`ZoneDef` é um nome ilustrativo meu. O documento não fixa o nome dos tipos de definição.

---

## Fase 3 — Fora do mundo: conta via HTTP (Decisões 5 e 6)

```text
Criar conta:  HTTP → Handler → Service → Repository → Postgres
Jogar:        WS   → Command → Game Core → State → Event → WS
```

São dois fluxos diferentes, de propósito. Conta, login e personagem são identidade persistente, um CRUD legítimo. Gameplay é uma máquina de estado. Forçar os dois pelo mesmo pipeline piora os dois.

O corte do HTTP acontece em "entrar no mundo". Tudo antes disso (criar conta, login, refresh, listar e criar personagem) é requisição e resposta e funciona sem conexão aberta. Tudo depois disso é contínuo.

### O conceito de Go mais diferente do que você conhece: interfaces implícitas

Em Java, você escreve `class PgRepo implements Repository`. Em Go, ninguém declara nada. Se o tipo tem os métodos, ele satisfaz a interface, e o compilador confere isso.

Por isso a interface é definida **no consumidor**, o pacote que precisa dela:

```go
// internal/account/service.go
package account

type Repository interface { // quem precisa define o que precisa
    Create(ctx context.Context, a Account) error
}

type Service struct{ repo Repository }

func NewService(r Repository) *Service { return &Service{repo: r} }
```

```go
// persistence/postgres: não importa account.Repository,
// só tem o método com a assinatura certa
func (r *AccountRepository) Create(ctx context.Context, a account.Account) error { ... }
```

**Analogia:** é uma tomada. O aparelho não precisa de um certificado dizendo que é compatível. Se o pino encaixa, funciona.

**Consequências da Decisão 11:**

- A interface é pequena (1 a 3 métodos), porque só descreve o que aquele consumidor usa.
- Não existe interface antecipada para relógio, gerador de id ou publisher. Você começa com o tipo concreto e só extrai uma interface quando um consumidor real precisar.
- Não existe repository CRUD genérico.

---

## Fase 4 — Entrar no mundo: uma conexão WebSocket e tópicos (Decisões 6 e 9)

```text
jogador ──1 conexão WS──► servidor
                            ├─ inscrito em: zona:X
                            ├─ inscrito em: guilda:Y
                            └─ inscrito em: global
```

Depois de entrar no mundo, uma única conexão WebSocket carrega os dois sentidos: comandos que sobem e eventos que descem. Usar o mesmo canal preserva a ordem entre o que o jogador pediu e o que ele recebe.

**Tópicos, não salas.** A conexão pertence ao jogador, não ao lugar. Quando ele troca de zona, você troca a inscrição dele. O tópico só serve para mandar a mesma mensagem para vários jogadores (fan-out) e nunca é dono de estado de gameplay.

**A conexão cair não para o jogo.** O estado vive no servidor, e a conexão é só o cano.

A escolha de transporte é **reversível**. O Game Core não sabe o que é HTTP nem WebSocket; os dois são adaptadores que produzem `Command`.

---

## Fase 5 — O coração: o game loop single-owner (Decisões 1 e 2)

Esta é a decisão mais importante e a mais "Go".

### O problema

Cada conexão WebSocket roda na sua própria goroutine, uma thread leve gerenciada pelo runtime de Go. Então 1.000 jogadores significam 1.000 goroutines querendo mexer no `GameState` ao mesmo tempo.

### A decisão

Uma única goroutine é dona do estado. As outras não tocam nele: elas mandam um pedido por um channel.

```text
WS 1 ─┐
WS 2 ─┼──► commands chan ──► Game Loop ──► GameState
WS 3 ─┘                     (única que escreve)
```

**Analogia:** é um caixa de banco com uma fila só. Mil pessoas chegam juntas, mas o caixa atende uma de cada vez. Ninguém precisa de cadeado no cofre, porque só o caixa encosta nele.

### Os conceitos de Go

- **`chan`** é uma fila tipada e segura entre goroutines. Enviar é `commands <- cmd`, e receber é `cmd := <-commands`.
- **`select`** espera em vários channels ao mesmo tempo e executa o primeiro que ficar pronto.
- **`go f()`** dispara uma goroutine.

Este é o loop, igual ao do documento:

```go
for {
    select {
    case cmd := <-commands:          // porta 1: pedido do jogador
        publish(engine.Handle(cmd))
    case now := <-ticker.C:          // porta 2: o relógio do servidor
        publish(engine.Tick(now))
    }
}
```

E, só para ilustrar, o lado da conexão (o documento não define essa forma):

```go
go func() {
    for {
        msg, err := readMessage(conn)
        if err != nil {
            return
        }
        commands <- toCommand(playerID, msg) // só enfileira, não toca no estado
    }
}()
```

### Por que o loop tem duas portas

`Tick` não é pedido de ninguém. Se você tratasse o tempo como um `Command` falso, perderia a informação de quem originou a operação.

### Por que não usar mutex

Mutex funciona, e o histórico registra que essa foi a primeira linha de estudo. O custo é que cada operação passa a precisar responder: quem segura o lock, por quanto tempo, e como publicar eventos sem deadlock.

Com um dono só, dois crafts do mesmo jogador são processados em fila, e o segundo já vê o saldo descontado pelo primeiro.

O princípio 4 diz que não se usa channel por ser idiomático. Aqui ele foi escolhido porque o jogo é naturalmente sequencial.

**Limite conhecido:** um loop único é um gargalo global. Se aparecer contenção real, o caminho é particionar o estado, não criar microserviços.

---

## Fase 6 — Tempo: `Activity` e `now` como parâmetro

```text
Activity{StartedAt: 10:00, EndsAt: 10:05}

tick 10:01 → agora < EndsAt → nada
tick 10:05 → agora >= EndsAt → conclui e emite evento
```

O servidor não fica contando milissegundos por jogador. O ticker só pergunta de tempos em tempos se algo já venceu. **O relógio do jogo é o `time.Time`, não o ticker.**

Por isso o engine recebe `now` em vez de chamar `time.Now()`:

```go
// simplificação: percorre todos os jogadores
func (e *Engine) Tick(now time.Time) []Event {
    var evs []Event
    for _, p := range e.state.players {
        if a := p.Activity; a != nil && !now.Before(a.EndsAt) {
            evs = append(evs, e.complete(p, now))
        }
    }
    return evs
}
```

No teste, você passa `time.Date(2026, 1, 1, 10, 5, 0, 0, time.UTC)` e o resultado é sempre o mesmo. Um engine que lê o relógio sozinho é não determinístico e difícil de testar.

---

## Fase 7 — O que desce para o cliente (Decisões 7 e 8)

**Coordenada não é estado de jogo.** O servidor nunca manda posição. Ele diz algo como "coletando `wood_01` na zona X, termina às 10:05". O cliente sabe onde `wood_01` fica no terreno dele e anima o personagem andando até lá.

Isso é possível porque o combate não tem posicionamento: "área" significa número de alvos, não alcance. Posição vira apresentação, e o layout de zona vira conteúdo versionado que vai junto com o cliente.

**Combate em onda fechada, com a luta inteira de uma vez:**

```text
escolhe grupo → onda definida → servidor resolve TUDO → manda linha do tempo → cliente anima
```

Algumas regras completam esse fluxo:

- A onda tem um teto de 50 rodadas. Se estourar, é impasse: ninguém morre e não há loot.
- Se o jogador mandar parar, o servidor corta a linha do tempo naquele ponto. O que não foi animado não aconteceu.
- Para a rede, isso significa um lote por luta, em vez de um fluxo contínuo de pequenos eventos.

---

## Fase 8 — Persistência fora do caminho crítico (Decisão 10)

```text
game loop (RAM, rápido)  ──pontos significativos──►  Postgres
                          login, logout, início/fim de atividade,
                          craft, equipar, morte, troca de zona, checkpoint
```

O banco nunca é atualizado a cada tick, senão ele vira uma extensão lenta da RAM.

O que se salva é o suficiente para reconstruir o estado, não o loop em si. Se o `EndsAt` foi persistido e o servidor reinicia no meio da atividade, o engine continua de onde parou.

**Simplificação aceita (não é provisória):** a sequência muta → salva → publica pode ficar inconsistente se o banco falhar depois que o evento já saiu. Transação e outbox só entram quando um requisito concreto pedir.

---

## A viagem inteira, de ponta a ponta

```text
HTTP: login → lista personagem → "entrar no mundo"
                                        │
WS aberto ─► goroutine da conexão ─► commands chan
                                        │
ticker ───────────────────────────► Game Loop (dono do GameState)
                                        │ Handle / Tick(now)
                                        ▼
                                    []Event ─► publish ─► tópicos ─► WS dos jogadores
                                        │
                              pontos significativos ─► Postgres
```

O documento mostra o `publish(...)` mas não detalha o mecanismo entre o loop e as conexões. Qualquer coisa que eu dissesse sobre isso seria hipótese minha.

**Deliberadamente não decidido:**

- particionamento do estado;
- transação e outbox;
- formato de wire (JSON ou binário);
- versionamento do conteúdo do cliente;
- reconexão no meio de um combate;
- personagem offline (existe só um esboço, a ser decidido quando existir a primeira Activity de coleta).

---

## Onde o código atual diverge do documento

Olhei o `bootstrap/application.go` que está no conhecimento do Project (branch `main`). Não escolho qual lado está certo, só aponto:

1. **Pacote de rede.** A Decisão 11 diz para usar `network` em vez de `network/http` enquanto couber, justamente para não colidir com `net/http`. O código tem `internal/network/http`, importado como `httpnetwork`, que é exatamente o alias que a decisão queria evitar. Ou o doc precisa dizer que a divisão já aconteceu, ou o código volta a ser um pacote só.
2. **Estrutura de pastas.** O doc lista `account/` com `repository.go` e depois `persistence/postgres/`. O código tem `persistence/postgres/repositories/` e dois pacotes que não aparecem na estrutura do doc: `auth/` e `character/`. Provavelmente o doc ficou para trás, mas vale registrar.

E dois pontos de code review que não são conflito com o doc, mas são problemas reais:

3. **`*pgx.Conn` não é seguro para uso concorrente.** O `net/http` atende cada requisição numa goroutine própria, e todos os repositories compartilham essa única conexão. Com duas requisições simultâneas, isso quebra. O tipo certo aqui é `pgxpool.Pool`.
4. **O `Shutdown` está incompleto.** Ele ignora o `ctx` que recebe, não fecha o banco, e o `main` nunca o chama, porque não há tratamento de sinal (`signal.NotifyContext`). A Decisão 11 cita o desligamento gracioso como motivo para o `HTTPServer` ser dono do `*http.Server`.

Se quiser, a próxima conversa pode ser só a Fase 5 com calma: goroutines, channels e `select`, com os erros clássicos de iniciante (channel sem buffer travando, goroutine vazando). É a parte em que Go mais difere das linguagens que você já conhece.

---

## Sidinei:

Me explique agora sem código e sem fluxograma somente texto para que eu coloque no modo tts para ouvir.

---

## Claude:

Vou explicar a arquitetura do Eras do Brasil em fases, seguindo o caminho que um pedido do jogador percorre. Primeiro vem o esqueleto do programa, depois o que acontece antes de o jogador entrar no mundo e, por fim, o que acontece dentro dele. Em cada fase, junto com a decisão registrada no documento de arquitetura consolidada, eu explico o conceito de Go que você precisa para entendê-la.

Fase zero. O modelo mental.

Antes de falar de qualquer pacote, o documento fixa cinco princípios, e todo o resto deriva deles.

O primeiro diz que o servidor é autoritativo. O cliente só expressa intenção, e quem decide o resultado é o servidor. Nada de gameplay é calculado no cliente.

O segundo diz que o jogo funciona como comando, estado e evento, três coisas distintas. O comando é o pedido. O núcleo do jogo valida esse pedido e muda o estado. O evento comunica o que aconteceu.

O terceiro diz que o tempo é do servidor. Toda ação é uma atividade com um horário de início e um horário de fim.

O quarto diz que a concorrência segue a posse do estado, e não o gosto de quem programa. Primeiro você decide quem é o dono do estado, e só depois escolhe o mecanismo.

O quinto diz que o escopo é pequeno, mas as fronteiras já nascem definitivas.

Uma analogia ajuda. O cliente é quem faz o pedido no balcão, e o servidor é a cozinha. O cliente pode pedir o prato, mas não pode escrever na comanda que o prato já está pronto.

Fase um. O esqueleto de um programa Go.

Em Go, pacote é diretório. Todos os arquivos dentro da pasta game formam o pacote game. O nome do arquivo não cria fronteira nenhuma, só a pasta cria.

A pasta chamada internal tem um significado especial para o compilador. Nada fora do módulo consegue importar o que está lá dentro.

A visibilidade é decidida pela primeira letra do nome. Se o nome começa com maiúscula, ele é visível para outros pacotes. Se começa com minúscula, ele é privado ao próprio pacote. Não existe a palavra public nem a palavra private.

Também não existe classe. Existem estruturas de dados, que são as structs, e funções penduradas nelas, que são os métodos. O que você chamaria de construtor é só uma função comum, que por convenção se chama New seguido do nome do tipo.

Erro também é diferente. Não existe exceção. Uma função que pode falhar devolve dois valores, o resultado e um erro, e quem chamou verifica o erro logo em seguida.

Com isso em mente, vem a decisão quatro. O pacote bootstrap é a raiz de composição. A função main fica quase vazia: ela só pede ao bootstrap que monte a aplicação e depois manda a aplicação rodar. É o bootstrap que carrega os dados do jogo, conecta no banco Postgres, cria os repositórios, os serviços e os handlers, sobe o servidor HTTP e o WebSocket e inicia o loop do jogo.

Existe um pacote só para isso porque conectar as peças é uma responsabilidade real. Se ela ficasse no main, o main viraria um arquivo gigante. Se ficasse espalhada, o domínio do jogo acabaria conhecendo o banco de dados.

A dependência tem mão única. O bootstrap conhece todo mundo, ninguém conhece o bootstrap, e o pacote game não conhece nenhuma infraestrutura.

Se você vem de Java com Spring ou de Node com Nest, está acostumado com um container de injeção de dependência montando tudo por trás. No projeto isso é proibido. A montagem é feita à mão, chamando um construtor depois do outro. Fica mais verboso, mas dá para ler de cima a baixo e entender exatamente o que depende do quê.

Fase dois. Os dados estáticos.

A decisão três define três camadas, e nenhuma invade a outra. Os arquivos JSON ficam na pasta data. O pacote gamedata lê esses arquivos e sabe o formato deles, mas não conhece o jogo. O pacote game é o domínio e o estado vivo, e nunca lê JSON. O bootstrap pega o que o gamedata carregou e constrói o mundo do jogo a partir disso.

A razão é que a definição estática e o estado vivo têm ciclos de vida diferentes. A definição diz, por exemplo, que tal zona tem tais acampamentos. O estado vivo diz que tal jogador está coletando agora. Se um dia o formato do JSON mudar, só o gamedata quebra.

Existem algumas regras para os arquivos. É um arquivo por tipo de entidade, nunca um arquivo por instância. A pasta data fica na raiz do repositório, fora do backend, porque é conteúdo do jogo e não configuração do servidor. E nenhuma constante de jogo mora no código.

O documento permite um carregador genérico, desde que ele seja só mecanismo. Aqui entram os generics de Go: uma função privada que sabe ler qualquer JSON e transformá-lo em qualquer tipo, sem saber o que é uma zona ou um diálogo. Para cada tipo de entidade existe uma função pública específica, que usa esse carregador genérico por baixo.

Fase três. Fora do mundo, a conta via HTTP.

A decisão cinco diz que conta não é personagem. Criar conta, fazer login e gerenciar sessão ficam fora do núcleo do jogo. Esse fluxo percorre um caminho clássico, do HTTP para o handler, do handler para o serviço, do serviço para o repositório e do repositório para o Postgres. Jogar é outra coisa: é um comando chegando pelo WebSocket, passando pelo núcleo do jogo, mudando o estado e gerando eventos que voltam pelo WebSocket.

São dois fluxos diferentes de propósito. Conta é identidade persistente e um CRUD legítimo. O jogo é uma máquina de transição de estado. Forçar os dois pelo mesmo caminho pioraria os dois.

A decisão seis define onde fica o corte: no momento de entrar no mundo. Tudo antes disso usa HTTP, porque é naturalmente pergunta e resposta e funciona sem conexão aberta. Isso inclui criar conta, login, renovar a sessão, listar e criar personagem e o próprio pedido de entrar no mundo.

Aqui aparece o conceito de Go mais diferente do que você conhece, que são as interfaces implícitas. Em Java, uma classe declara que implementa uma interface. Em Go, ninguém declara nada. Se um tipo tem os métodos que a interface pede, ele a satisfaz automaticamente, e o compilador confere isso.

Por causa disso, a interface é definida por quem a consome, e não por quem a implementa. O pacote account precisa salvar contas, então é ele que declara uma interface pequena chamada Repository, com só os métodos que usa. O código do Postgres, em outro pacote, simplesmente tem esses métodos, sem mencionar a interface em lugar nenhum.

A analogia é uma tomada. O aparelho não precisa de um certificado dizendo que é compatível. Se o pino encaixa, funciona.

A decisão onze tira três consequências disso. As interfaces são pequenas, com um a três métodos. Não se cria interface antecipada para relógio, gerador de identificador ou publicador de eventos: você começa com o tipo concreto e só extrai uma interface quando aparecer um consumidor real. E não existe repositório genérico de CRUD, porque a lógica do jogo não é CRUD.

Fase quatro. Entrar no mundo, com uma conexão e vários tópicos.

A partir da entrada no mundo, existe uma única conexão WebSocket por jogador, e ela carrega tudo nos dois sentidos: os comandos que sobem e os eventos que descem. Usar o mesmo canal preserva a ordem entre o que o jogador pediu e o que ele recebe.

A decisão nove diz tópicos, não salas. A conexão pertence ao jogador, não ao lugar. O servidor inscreve essa conexão em tópicos, como o tópico da zona, o da guilda e o global. Quando o jogador troca de zona, ele troca de inscrição. O tópico serve apenas para enviar a mesma mensagem a vários jogadores e nunca é dono de estado de jogo.

Se a conexão cair, o jogo não para. O estado vive no servidor, e a conexão é só o cano.

O documento também diz que essa escolha de transporte é reversível. O núcleo do jogo não sabe o que é HTTP nem WebSocket. Os dois são apenas adaptadores que transformam uma mensagem de rede num comando.

Fase cinco. O coração do servidor, o loop com dono único.

Esta é a decisão mais importante e também a mais típica de Go.

O problema é o seguinte. Cada conexão WebSocket roda na sua própria goroutine. Goroutine é uma espécie de thread muito leve, gerenciada pelo próprio Go, e é barato ter milhares delas. Então, se há mil jogadores conectados, há mil goroutines querendo mexer no estado do jogo ao mesmo tempo.

A decisão um resolve isso dando a posse do estado a uma única goroutine, o loop do jogo. As goroutines das conexões nunca tocam no estado. Elas só colocam o comando do jogador num channel.

Channel é uma fila tipada e segura, feita para passar dados de uma goroutine para outra. Uma goroutine coloca algo na fila, e outra retira do outro lado.

A analogia é um caixa de banco com uma fila única. Mil pessoas podem chegar juntas, mas o caixa atende uma de cada vez. Ninguém precisa de cadeado no cofre, porque só o caixa encosta nele.

A decisão dois diz que esse loop tem duas portas de entrada. A primeira é o channel de comandos, por onde chegam os pedidos dos jogadores. A segunda é um relógio interno, chamado ticker, que bate em intervalos regulares. O loop usa uma instrução de Go chamada select, que espera nas duas portas ao mesmo tempo e atende a primeira que tiver algo. Se chegou um comando, o núcleo do jogo trata o comando. Se o relógio bateu, o núcleo do jogo processa a passagem do tempo. Nos dois casos, os eventos resultantes são publicados.

O tempo tem porta própria porque ele não é pedido de ninguém. Se você disfarçasse a passagem do tempo como um comando, perderia a informação de quem originou a operação.

Um mutex também resolveria, e o histórico do projeto registra que essa foi a primeira ideia estudada. O problema é que, com mutex, cada operação precisa responder a perguntas difíceis: quem segura o cadeado, por quanto tempo, e como publicar eventos sem travar tudo. Com um dono único, dois pedidos de craft do mesmo jogador entram na fila em ordem, e o segundo já enxerga o saldo descontado pelo primeiro.

Existe um detalhe importante no princípio quatro. O channel não foi escolhido por ser idiomático em Go. Foi escolhido porque o jogo é naturalmente sequencial.

O limite conhecido é que um loop único é um gargalo global. Se um dia surgir contenção real, o caminho previsto é dividir o estado em partes. Não é criar microserviços.

Fase seis. O tempo e as atividades.

Toda ação demorada é uma atividade com um horário de início e um horário de fim. O servidor não fica contando milissegundos para cada jogador. A cada batida do relógio, ele só pergunta se o horário atual já chegou ao horário de fim de alguma atividade. Se chegou, conclui a atividade e gera um evento.

O ticker não é o relógio do jogo. O relógio do jogo é o horário de verdade. O ticker só serve para perguntar periodicamente se algo venceu.

Por isso o núcleo do jogo recebe o horário atual como parâmetro, em vez de consultar o relógio do sistema por conta própria. Isso torna o núcleo determinístico. Num teste, você passa um horário fixo, como dez e cinco de uma data qualquer, e o resultado é sempre o mesmo. Um núcleo que lê o relógio sozinho dá resultados diferentes a cada execução e fica muito difícil de testar.

Fase sete. O que o servidor manda para o cliente.

A decisão sete diz que coordenada não é estado de jogo. O servidor nunca manda posição. Ele diz algo como: o personagem está coletando o nó de madeira número um da zona tal, e termina em tal horário. O cliente sabe onde esse nó fica no terreno dele e anima o personagem andando até lá.

Isso só é possível porque o combate não tem posicionamento. Quando uma habilidade é de área, isso significa número de alvos, e não formato nem alcance. Sem posição como regra de jogo, a posição vira só apresentação. O layout das zonas passa a ser conteúdo estático, distribuído junto com o cliente, enquanto dano, prata, drop, fama e durabilidade continuam sendo decididos pelo servidor.

A decisão oito diz que o combate é uma onda fechada e que a luta inteira é resolvida de uma vez. O jogador escolhe um grupo, a onda inteira fica definida, o servidor resolve a luta completa e envia a linha do tempo pronta, e o cliente apenas anima. A próxima onda só nasce quando a anterior morre toda.

Existe um teto de cinquenta rodadas por onda. Se a luta passar disso, ela termina em impasse: ninguém morre, não há loot dos sobreviventes e o jogador volta ao terreno da zona.

Se o jogador mandar parar no meio, o servidor corta a linha do tempo naquele ponto e envia o resultado final. O que não chegou a ser animado simplesmente não aconteceu.

Fase oito. A persistência fora do caminho crítico.

A decisão dez diz que o banco não participa do loop do jogo. Salva-se apenas em pontos significativos: login, logout, início e fim de atividade, craft, equipar, morte, troca de zona e um checkpoint periódico. Nunca a cada batida do relógio, porque isso transformaria o banco numa extensão lenta da memória.

O que se salva é o suficiente para reconstruir o estado, não o loop em si. Se uma atividade termina às dez e cinco e o servidor reinicia às dez e três, o horário de fim que foi salvo permite continuar de onde parou.

Existe uma simplificação aceita e documentada. A sequência de mudar o estado, salvar e publicar pode ficar inconsistente se o banco falhar depois que o evento já saiu. O documento diz que isso não é provisório: transação e outbox só entram quando um requisito concreto pedir.

Juntando tudo, a viagem completa fica assim. O jogador faz login por HTTP, lista seus personagens e pede para entrar no mundo. A partir daí, abre-se uma conexão WebSocket. A goroutine dessa conexão lê cada mensagem, transforma em comando e coloca na fila. O loop do jogo, único dono do estado, atende tanto essa fila quanto o relógio, muda o estado e gera eventos. Esses eventos são publicados nos tópicos e chegam às conexões dos jogadores interessados. Em paralelo, nos momentos significativos, o estado é salvo no Postgres.

O documento não detalha o mecanismo exato entre o loop e as conexões na hora de publicar. Qualquer coisa que eu dissesse sobre isso seria hipótese minha.

Alguns pontos ficaram deliberadamente sem decisão: a divisão do estado em partes, transação e outbox na persistência, o formato das mensagens no WebSocket, a forma como o cliente baixa e versiona o conteúdo estático, a reconexão no meio de um combate e o personagem offline. Para o personagem offline existe apenas um esboço, e a decisão fica para quando existir a primeira atividade de coleta.

Por último, quatro pontos do código atual que merecem atenção.

O primeiro é o pacote de rede. A decisão onze diz para usar um pacote chamado apenas network enquanto couber, justamente para não colidir com o pacote http da biblioteca padrão. O código tem um subpacote http dentro de network, importado com um apelido, que é exatamente o que a decisão queria evitar. Ou o documento precisa registrar que essa divisão já aconteceu, ou o código volta a ser um pacote só.

O segundo é a estrutura de pastas. O documento não menciona os pacotes auth e character, nem a subpasta repositories dentro de persistence. Provavelmente o documento ficou para trás, mas vale registrar.

O terceiro é um risco real no código. A aplicação usa uma única conexão do driver pgx, e essa conexão não é segura para uso concorrente. O servidor HTTP atende cada requisição numa goroutine própria, então duas requisições simultâneas podem quebrar. O tipo adequado é o pool de conexões do mesmo driver.

O quarto é o desligamento. A função de desligar ignora o contexto que recebe, não fecha o banco, e o main nunca a chama, porque o programa não escuta os sinais do sistema operacional. A própria decisão onze cita o desligamento gracioso como motivo para o servidor HTTP ser dono do objeto de servidor completo.

---
