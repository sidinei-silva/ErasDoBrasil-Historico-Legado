## Sidinei:

Primeira conversa neste Project. Antes de trabalhar, dois testes rápidos
para eu saber se o repositório está sendo lido:

1. Onde está registrada a decisão da Raiz no skybox durante A Travessia,
   e o que ela diz? Responda a partir do conhecimento do Project, sem eu
   mandar link.
2. Qual é o ponto de entrada do projeto e para que ele serve?

Depois, contexto para o trabalho:

Estou fazendo a fatia 4 (entrar no mundo) numa branch que ainda não teve
merge. O conhecimento do Project está sincronizado com a main, que está
atrás. Para tudo que for da fatia 4, vale a branch; se a main e a branch
divergirem, a branch prevalece.

- Backlog da fatia: docs/backlog/00-mvp/04-entrar-no-mundo.md
- Link da branch: https://github.com/sidinei-silva/eras-do-brasil/tree/04-entrar-no-mundo
- Arquivos principais que já mexi: <links diretos .../blob/<branch>/...>

Não comece a análise ainda. Responda os dois testes, confirme que conseguiu
abrir o diff e me diga em poucas linhas o que entendeu que a fatia 4 entrega.
Aí eu digo por onde seguir.

---

## Claude:

**Teste 1.** Está em `docs/decisoes-de-design.md`, seção "Tutorial — A Travessia", subseção "A Raiz visível durante a Travessia". A decisão é esta: durante toda A Travessia, a Raiz do Mundo aparece no skybox como uma silhueta colossal. Ela fica sempre visível e não tem geometria navegável. Some quando o jogador é expulso para o mundo, na Feitoria da Cruz (Costa do Pau-Brasil), e reaparece lá como o Coração da Raiz. A causa da Ruptura fica em aberto de propósito. O `historico-e-estudos.md` registra que a ideia começou como exploração e virou decisão em 20/09/2026.

**Teste 2.** O ponto de entrada é `docs/contexto-do-projeto.md`. Ele serve para qualquer pessoa ou IA que comece no projeto entender o que é o jogo e o escopo atual, e principalmente saber onde cada assunto vive (a tabela da seção 4), sem duplicar regras. Também traz a hierarquia de fontes: código, depois doc normativo, depois dados, depois histórico. Regras de IA e de commit ficam no `AGENTS.md`.

**Diff.** O GitHub bloqueia a leitura pela web, então clonei o repositório e comparei `main...04-entrar-no-mundo`. São 4 commits e 17 arquivos:

- **Código novo:** `gamedata/` (loader e zonas), `game/` (Game, State, World, Zone, Player, Command, Event) e `bootstrap/` (application e world).
- **Dados:** em `data/mvp/zones.json` saiu o campo `services` e `bossId`/`mobFactionId` mudaram de lugar. Em `npcs.json` saiu `stationsWithoutDialogue`.
- **Docs:** o commit "remove documento" apagou `docs/backlog/00-poc/04-entrar-no-mundo.md`, uma cópia antiga em `00-poc`. O arquivo da fatia em `00-mvp` continua lá, igual ao da main.

Você não colou os links dos arquivos (ficou o placeholder `<links diretos ...>`), então usei o diff inteiro como referência.

Três coisas que notei e que não vou analisar agora:
- O arquivo da fatia marca `World` e `Game` como feitos, mas o `BACKLOG.md` ainda diz "não iniciada".
- Entrou um `docs/instuctions.md` (com erro de digitação no nome) que parece ser uma versão das instruções deste Project dentro do repo.
- Os campos removidos dos JSONs podem ou não ser intencionais.

**O que a fatia 4 entrega.** Um jogador autenticado, com personagem já criado, entra no mundo.

- **HTTP:** autentica, escolhe o personagem e chama `EnterWorld`.
- **Servidor:** valida o `CharacterID` e se o personagem pertence à conta, cria o estado runtime do personagem e o registra no `GameState`. Isso depende de `GameData` carregado, `World` montado e `Game` com loop/tick.
- **Retorno:** devolve o estado inicial e a partir daí a comunicação passa para o WebSocket, seguindo a Decisão 6 da arquitetura (HTTP até entrar no mundo, WebSocket depois).

Pelo backlog, falta `GameState`, tick, a entrada em si, as validações, o registro e o WebSocket.

Por onde quer seguir?

---

## Sidinei:

Eu mesmo resolvi, o backlog atualizei, o instruction eu vou deixar e atualizar ele, os campos removidos foram intencionais.
Vai ser só uma copia guardada e rastredada do que foi atualizado mas ela não sera mencionada para ser lida. E sempre vou deixar ela atualizada dado que não é algo que vai ser sempre atualizado.

---

## Claude:

Entendido: o backlog está atualizado, a remoção dos campos foi intencional e o `instuctions.md` fica como cópia versionada que nada referencia.

Um ponto sobre a cópia. Ela já está desatualizada: a versão na branch é anterior às instruções deste Project. A abertura fala em "meu repositório" e em "a gente discutir", e as seções não batem com as de agora. Se a ideia é manter a cópia fiel, ela já nasce divergente, então vale sincronizar no próximo commit. O nome do arquivo também está com o erro de digitação (`instuctions` → `instructions`).

Nenhuma das duas coisas é problema para mim: como o arquivo não é ponto de leitura, não vou tratá-lo como fonte. Por onde seguimos na fatia 4?

---

## Sidinei:

Veja e a branch de maneira atualizad e mediga qual o proximo passo da fatia 4, eu quero primeiro eu aprendendo a fazer.

---

## Claude:

Atualizei a branch. Seu estado real está um pouco à frente do checklist: `GameState` já existe (`state.go`) e o `Game.EnterWorld` já faz a transição. O que falta é **quem chama isso, e como**.

## Próximo passo: o game loop (single-owner)

### O problema

Hoje `EnterWorld` mexe direto em `g.state.Players`, que é um map. No `net/http` cada requisição roda na sua própria goroutine. Assim que você ligar um handler HTTP ao `Game`, duas entradas simultâneas escrevem no mesmo map. Em Go isso é *data race* e pode até derrubar o processo (`concurrent map writes`).

```text
req A (goroutine) ──┐
                    ├──► g.state.Players[...] = ...   ✗ race
req B (goroutine) ──┘
```

Por isso o loop vem antes de "implementar entrada no mundo": sem ele, qualquer caminho que você ligar nasce errado.

### A arquitetura já decidida

As Decisões 1 e 2 de `arquitetura-consolidada.md` dizem que uma goroutine é dona do `GameState`, que a rede só *enfileira* comandos e que o tick entra pelo mesmo `select`, por outra porta.

```text
handler HTTP ──► commands chan ──► [ loop ] ──► GameState
                                      ▲
                          ticker ─────┘
```

**Analogia:** o loop é o caixa único de uma padaria. Muita gente chega ao mesmo tempo, mas só o caixa mexe na gaveta, um pedido por vez. Por isso ninguém precisa de cadeado.

### O ponto que você vai ter que resolver: a resposta

O diagrama da arquitetura mostra `publish(engine.Handle(cmd))`, que é um fluxo de ida. Só que a entrada no mundo é HTTP: o handler **precisa esperar** a resposta para devolver o estado inicial ou um erro. Como uma goroutine recebe de volta o resultado de algo que outra goroutine processou?

Há duas saídas:

**A) O comando carrega o próprio canal de resposta.**

```text
handler ──(cmd + reply chan)──► loop
handler ◄──────(resultado)───── loop
```

```go
type enterWorldRequest struct {
    cmd   EnterWorldCommand
    reply chan enterWorldResult // buffer 1: o loop nunca bloqueia ao responder
}
```

O handler envia e fica bloqueado lendo `reply`. Na prática é um RPC entre goroutines.

**B) O loop só publica eventos, e quem quer a resposta os escuta.** É o modelo que o WebSocket vai usar depois. Para o HTTP, porém, você teria que correlacionar "este evento é a resposta da minha requisição", e isso é complexidade sem ganho nesta fatia.

| | A — reply chan | B — só eventos |
|---|---|---|
| Serve HTTP (req/resp) | direto | precisa correlacionar |
| Serve WS (fluxo contínuo) | não é o foco | natural |
| Custo | um canal por comando | infraestrutura de publicação |

As duas convivem: **A** para a entrada via HTTP e **B** quando o WebSocket existir. A arquitetura não fixa isso, então é **proposta**, não decisão.

Dois cuidados no A, que é onde se erra:
- **Buffer 1 no `reply`.** Se o handler desistir (timeout, cliente caiu) e ninguém ler o canal, um `reply` sem buffer trava o **loop inteiro**, e com ele o jogo de todo mundo.
- **`ctx.Done()` no handler.** Faça `select` entre `reply` e `ctx.Done()` para não esperar para sempre.

### Onde encaixa

`bootstrap` cria o `Game`, sobe o loop numa goroutine e entrega aos handlers só o que eles precisam para enfileirar. Hoje o `NewGame` não é chamado em lugar nenhum do `application.go`.

## Achados no código atual, para você decidir

1. **`EnterWorldCommand.ZoneID` vem de fora.** O cliente escolher em que zona entra contradiz o servidor autoritativo. O dado já responde isso: `zone-a-beira` tem `"spawn": true`. Só que o `buildZone` **não copia `Spawn`** para o `game.Zone`, então hoje o núcleo nem sabe qual é a zona de spawn.
2. **`Character` não guarda zona.** Nesta fatia, entrar é sempre no spawn. Onde a zona fica persistida depois (a Decisão 10 persiste "mudança de zona") ainda **não está definido**. Não precisa resolver agora, mas é bom saber que o buraco existe.
3. **Ownership conta↔personagem não é assunto do `game`.** É identidade (Decisão 5): o handler valida pelo `CharacterService` e só então monta o comando. O Game Core recebe um `CharacterID` já confiável.

## Sugestão de ordem

1. Loop com `select` (comando + ticker; o `Tick` pode não fazer nada ainda) e `now` passado de fora.
2. Canal de resposta para o `EnterWorld`.
3. Zona de spawn vinda do `World`, não do comando.
4. Handler HTTP: auth, ownership, enfileira e espera.
5. WebSocket.

Para começar o passo 1: antes de escrever o loop, quem você acha que deve **possuir** o canal `commands`? O `Game`, uma struct de loop separada ou o `bootstrap`? Me diga sua escolha e o porquê, e a gente compara.

---
