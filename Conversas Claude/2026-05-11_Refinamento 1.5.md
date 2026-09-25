## Sidinei:

[Anexo:  (4451 bytes)]

---

## Claude:

Contexto recuperado. Antes de redigir o refinamento, abro aqui análise crítica em 3 partes: o que entendi (pra você validar), contradições/furos encontrados, e perguntas que precisam ser respondidas. Resposta longa de propósito — é o ponto onde compensa pensar antes de escrever.

---

## 1. Confirmação de entendimento

### Como `(Block, Poi)` funciona hoje (regra D3 da 1.4)

`Manager.getNpcsInLocation(blockId, poi, npcIdExcluido)` percorre `m.npcs` e retorna os que compartilham `CurrentBlock == blockId && CurrentPoi == poi`, excluindo o próprio. POI vazio (`""`) é tratado como POI virtual "outdoor" do bloco — dois NPCs com `CurrentPoi==""` no mesmo bloco contam como juntos. O método é chamado uma vez por NPC por tick no `ProcessTick`, antes do `ApplyDecay`, e o resultado vira o booleano `hasCompany` que define se Loneliness sobe ou desce.

Existe também `Snapshot.GetNPCsInLocation(blockId, poi)` no pacote `snapshot/`, que faz o mesmo mas sobre a cópia imutável e sem exclusão do "próprio".

### O que o GDD diz (Cap. 8.3, e contradições com 5.3/5.4)

**Cap. 8.3 (canônico):**
- `knowledgeBase` armazena 4 tipos: `RECURSO`, `ENTIDADE` (mob/perigo), `ROTINA_NPC`, e implicitamente `EventoImportante` (mencionado só como exceção de expiração).
- Esquema sugerido: `{type, id, location, seenAt}` — note: `location` é uma string solta, não `(blockId, poiId)`. Isso é pré-1.4.
- Expiração: `(currentTime - seenAt) > memoryLimit`, padrão ~2 dias de tempo de jogo, com EventoImportante isento ou estendido.
- Fofoca: dois NPCs no mesmo bloco trocam 1-2 itens; também atualizam `Relacionamentos` (que a 1.5 explicitamente NÃO entrega).
- Diferença "vi" vs "ouvi falar" só aparece no acesso do jogador, mas o sistema só consegue manter essa diferença se a knowledgeBase **tiver campo de origem** (direta vs fofoca). O GDD descreve a saída ("Eu não vi, mas o Guarda me contou") sem descrever o campo de schema que sustenta isso. **Lacuna.**

**Cap. 5.3:** fala em "+1 ponto de conhecimento mútuo" — texto narrativo legado, contradiz a estrutura tipada do 8.3. O 8.3 é o canônico (a auditoria `99_Meta_e_Backlog/03_Auditoria_GDD.md` registra isso). Vale citar a inconsistência no refinamento e tratar 5.3 como desatualizado.

**Cap. 5.4:** lista "Conhecimento por tipo: Locais, Recursos, Monstros, Outros NPCs". Note **Locais** — não existe no 8.3 (que só tem 4 tipos, e Local é parte de cada entry, não tipo próprio). Mais uma inconsistência menor entre capítulos. Você escolhe se incorpora "Local" como 5° tipo ou se trata 5.4 como descritivo e segue os 4 do 8.3. Eu recomendaria seguir 8.3.

### Onde 1.5 entra no `ProcessTick`

Hoje o loop por NPC é:
1. `getNpcsInLocation` → `hasCompany`
2. `ApplyDecay`
3. Se atividade discreta terminou → `ApplyActivityEffects` + `decideNextActivity`. Se contínua → `decideNextActivity`.
4. `ClampNeeds`

A 1.5 precisa inserir duas operações:
- **Geração de Knowledge "viu outro NPC"**: pode reaproveitar o `getNpcsInLocation` do passo 1 — ele já te dá a lista, é só popular knowledgeBase a partir dela.
- **Fofoca (troca)**: também precisa da lista, mas com lógica adicional (cooldown por par, escolha de itens). Pode rodar logo após a geração, no mesmo passo.
- **Expiração**: roda uma vez por NPC, antes ou depois do bloco acima. Lazy também é opção (ver P4 abaixo).

Ordem dentro do tick continua sequencial; nenhuma dessas operações precisa de I/O ou paralelismo. Custo: O(NPCs × tamanho_médio_da_kb) por tick. Com 3 NPCs e KB pequena, irrelevante.

---

## 2. Contradições e furos na Opção A

### 2.1 O auto-gerador "viu outro NPC" não entrega o que o GDD descreve

O Cap. 8.3 descreve um sistema vivo de **percepção** que armazena recursos, entidades (mobs) e rotinas vistas. A 1.5 só auto-gera o tipo "viu outro NPC". Os outros 3 tipos só existem via `admin_inject_knowledge`. **Isso precisa estar explícito no refinamento** como limitação reconhecida — não é falha de implementação, é recorte de fase deliberado, mas merece estar documentado pra você (ou outro dev futuro) não se confundir.

### 2.2 Com 3 residentes na mesma vila, o auto-gerador produz quase zero variedade

Pelos schedules de Tomas, Ricardo e Naila (do 1.4):
- Almoço/jantar: Tomas e Naila na `taverna_da_vila` (mesmo POI, mesmas janelas). Ricardo no `portao_da_vila` ou no quartel — não coincide.
- Tarde: Tomas e Naila ambos no `mercado_central` (mesmo POI).
- Manhã/madrugada: todos em POIs diferentes (forja, portão, cabana, dormindo).

Ou seja, Tomas e Naila vão se ver no mesmo POI várias vezes por dia (~3-4 encontros), todos com info quase idêntica ("vi Naila na taverna às 12h", "vi Naila na taverna às 13h"). Ricardo praticamente não vê ninguém — fica no portão sozinho a maior parte do dia.

**Consequência prática:** sem dedup ou throttle, a KB do Tomas vai virar uma lista repetitiva de avistamentos de Naila quase no mesmo lugar. Visualmente parece bug. Calibrar admin_inject pra produzir variedade vira mais importante do que parece. **Recomendo planejar cenários de teste no refinamento** (ex: "admin injeta avistamento de recurso na floresta na KB do Ricardo → após troca com Tomas na taverna, Tomas passa a saber").

### 2.3 Confusão semântica: `ROTINA_NPC` ≠ "vi NPC aqui"

O exemplo do GDD pra ROTINA_NPC é:
```
{"type": "ROTINA_NPC", "id": "npc_guarda", "info": "Vai para a taverna ao meio-dia"}
```

Note: `info` é texto inferido, **comportamental** ("ele costuma..."). É conhecimento de padrão.

O que a 1.5 vai gerar é avistamento pontual: "vi Naila no mercado às 13h dia 3". Não é a mesma coisa. Pra fazer ROTINA_NPC de verdade, precisaria observação repetida + inferência ("vi 5 vezes a Naila no mercado entre 12h-13h → infiro que essa é a rotina dela"), o que está fora da 1.5.

**Decisão necessária:** ou (a) trata o tipo da 1.5 como `AVISTAMENTO_NPC` (4° tipo, distinto do `ROTINA_NPC` do GDD, que continua não-implementado), ou (b) re-semantiza `ROTINA_NPC` na 1.5 pra ser "avistamento" e aceita a inconsistência com o GDD até implementar inferência. (a) é mais limpo, (b) economiza tipos. Eu prefiro (a).

### 2.4 "Viu outro NPC" disparado a cada tick = inundação

Sleeping dura 8h de jogo (8 ticks no dev). Trabalho dura 6h+. Se o gerador rodar a cada tick que detecta proximidade, o Tomas registra "vi Naila no mercado" 4 vezes seguidas durante a tarde. Inflar KB com lixo redundante.

**Opções:**
- **Dedup por chave `(Type, EntityId, BlockId, PoiId)`** — entry existe → atualiza `SeenAt`, não duplica. Limpo. Recomendado.
- **Throttle por tempo** — só gera se `currentTime - seenAt > X` minutos de jogo. Mais frágil (precisa calibrar X).
- **Edge-trigger** — só gera quando o par "entra em proximidade" (transição). Precisa de estado adicional (`lastSeenInSamePoi`). Mais código.

Dedup por chave é o caminho. Coincide com como o jogador mentalmente trataria isso: "eu sei que a Naila esteve no mercado, atualizo minha última vez".

### 2.5 Mecânica de troca: semântica do `SeenAt` no destinatário

Cenário: Tomas tem entry "vi minério na mina, SeenAt = dia 1 hora 10". Encontra Ricardo na taverna no dia 2 hora 12. Passa o conhecimento.

**Pergunta:** o `SeenAt` na KB do Ricardo é o `SeenAt` original (dia 1 hora 10) ou o momento da troca (dia 2 hora 12)?

- Se for o **original**: a info expira em todos ao mesmo tempo. Propagação tem janela curta — basicamente inútil. Tomas vê dia 1, conta no dia 2, no dia 3 ambos esquecem.
- Se for o **momento da troca**: info circula eternamente entre os 3 NPCs sem nunca expirar (Tomas conta pra Ricardo no dia 2, Ricardo conta pra Tomas no dia 3, ciclo).

**Solução do GDD (implícita):** dois campos — `OriginalSeenAt` (quando o observador original viu) e `LearnedAt` (quando este NPC soube). Expiração pode rodar contra um, contra outro, ou contra ambos. E ganha de brinde o campo `Source` (resolve furo 2.7 abaixo).

Decisão necessária. Eu recomendo dois campos + expiração contra `LearnedAt`, com `OriginalSeenAt` preservado pra acesso do jogador futuro ("vi pessoalmente" vs "ouvi falar"). Custo: alguns bytes extras por entry, nada relevante.

### 2.6 Cooldown de fofoca por par

"≥2 NPCs no mesmo `(Block, Poi)` por N ticks" — qual o significado?

- **Interpretação A:** N ticks é janela mínima de "ficar junto" antes de trocar (filtra cruzamentos curtos). Depois disso, troca **uma vez**.
- **Interpretação B:** N ticks é frequência da troca enquanto juntos. A cada N ticks juntos, mais 1-2 itens.

A confunde "tempo mínimo de companhia" com "evento de troca". B faz dois NPCs em sleeping de 8h trocarem itens 4 vezes seguidas (irreal e potencialmente problemático com o ciclo de propagação).

Eu recomendo **A + estado `lastGossipedWith[npcId] = tickNumber`**, com cooldown explícito (ex: "não fofoca de novo com o mesmo NPC por X horas de jogo"). Sem isso, o sistema fica frágil a esses cenários longos de proximidade.

### 2.7 Campo `Source` ausente do schema proposto

Você listou: `Knowledge {Type, EntityId, BlockId, PoiId, SeenAt}`. Falta `Source` ("direct" vs "via:npc_id"). Sem isso, o GDD prometeu ao jogador uma distinção que o sistema não consegue manter. Pode adiar pra 1.5+, mas então documentar como dívida explícita.

Eu adicionaria já. O custo é uma string por entry, e elimina retrabalho quando o diálogo do jogador chegar (Fase 3+).

### 2.8 FIFO de tamanho como mecanismo morto

Limite "fila com descarte do mais antigo" + expiração por idade = na prática, expiração quase sempre dispara antes do FIFO. O FIFO vira proteção contra cenários patológicos (admin injeta 1000 entries de uma vez), não comportamento esperado em runtime.

Documente isso explicitamente, e não baseie nenhuma mecânica de jogo no FIFO (ex: "NPCs com KB cheia esquecem mais rápido" não é uma mecânica que emerge de FIFO de tamanho — seria de um lifetime menor).

### 2.9 EventoImportante sem mecanismo de criação na 1.5

O GDD diz que EventoImportante tem expiração estendida ou permanente. Mas o que cria um? StoryManager — fora do escopo. Então, na 1.5, a flag de "importante" existe como campo do struct mas nunca é populada automaticamente. Só admin_inject pode marcar uma entry como importante.

Decisão necessária: a 1.5 implementa o campo agora (e admin pode injetar com flag), ou só implementa o suporte na hora que StoryManager existir? **Recomendo implementar agora** — é um booleano, custa nada, e ter o admin_inject capaz de simular é exatamente o tipo de teste que valida o sistema antes do StoryManager chegar.

### 2.10 Snapshot e admin_get_npc_knowledge

Snapshot é imutável por tick. Quando o admin consulta KB, o read sai do snapshot. Isso quer dizer que **a KB precisa ser copiada na construção do snapshot** (cópia de slice + cópia de struct, sem ponteiros vivos). Detalhe pequeno mas se passar referência o admin vê estado vivo, não snapshot. Vale documentar no refinamento.

### 2.11 Validação de `admin_inject_knowledge`

Admin pode injetar Knowledge com `BlockId` ou `PoiId` inexistente? Hoje a 1.4 valida POI no load com `os.Exit(1)`. Em runtime, o admin pode bypassar? Decisão:
- **Strict:** valida na injeção, rejeita com mensagem clara. Consistente com o load.
- **Loose:** aceita. Admin é root. Permite testar comportamento do sistema com dados "inválidos" (ex: "como o NPC reage se sabe de um POI que não existe?").

Eu recomendo **strict**. Se um dia precisar testar com dados corrompidos, faz outra flag explícita. Loose esconde bugs.

---

## 3. Avaliação das 5 perguntas + 4 novas

### P1 — Onde os tempos de expiração vivem?

**Recomendação:** config externa per-tipo, em arquivo separado (ex: `knowledge_config.json` ou seção do `config.json`). Constante em código mata iteração — você vai querer ajustar esses números durante observação. Per-NPC é over-engineering antes de Traits.

Quando Traits chegar (Fase 4+), trait "Memória de Elefante" multiplica o valor base do tipo (ex: ×3). Estrutura preparada sem custo agora.

### P2 — Granularidade de contagem

**Horas de jogo, com `time.Duration`.** O `GameTime.Time` já é `time.Time`, `SeenAt` é `time.Time`, expiração é `gameTime.Time.Sub(seenAt) > limitDuration`. Trivial.

Período (manhã/tarde/noite/madrugada) é granular demais — 6h de janela é gigante pra uma escala de 2 dias = 48h. Tick é uma unidade técnica que muda entre dev (1h) e prod (talvez 12s ainda mapeando pra 1h de jogo, então tanto faz na verdade) — sempre use a unidade narrativa.

### P3 — Contexto narrativo do esquecimento

**Recomendação: timer puro na 1.5.** "Sono como gatilho de fade" parece bonito mas adiciona dependência (esquecimento depende de quando o NPC dormiu = comportamento de Fatigue + Activity), torna testes não-determinísticos (NPC que pula sono retém memórias mais tempo), e não é observável com 3 NPCs no dev acelerado.

Deixa registrado como possível polish na seção "o que não entra" e segue com timer simples. Quando Mood & Thoughts entrarem (Fase 4+), aí explore. Forçar narrativa agora é gold-plating.

### P4 — Quando a expiração roda

**Recomendação: híbrido pragmático.**
- **Lazy em todo getter** (`admin_get_npc_knowledge`, leitura na fofoca): filtra expirados na leitura. Garante que ninguém nunca vê uma entry vencida.
- **Sweep oportuno** uma vez por NPC no `ProcessTick` (no início, antes do bloco existente): mantém o estado limpo entre ticks pra logs e observabilidade.

Custo de O(N × KB_média) por tick é negligenciável até centenas de NPCs com KB de dezenas de entries. Quando começar a doer (não vai antes da Fase 4), troca pra estrutura ordenada por `SeenAt` (heap/sorted slice) — refactor barato.

Não atrele a sweep a transição de período: cria latência variável de até 6h pra entries esquecerem. Sweep todo tick é mais previsível e barato.

### P5 — Limite de tamanho: idade ou importância?

**Recomendação: FIFO por idade (`SeenAt`), com isenção pra `Importante = true`.** Importância é um booleano, não um score; sem score, não dá pra "ordenar por importância".

Mas reforço: com expiração por idade já em vigor, o FIFO praticamente nunca dispara em runtime normal. Ele existe como guarda contra explosão (admin_inject em massa, bug futuro). É correto ter, mas não construa nenhuma mecânica de jogo em cima dele.

### P6 (nova) — Campo `Source` no schema

Adicionar agora: `Source string` — `"direct"` ou `"npc_id_da_fonte"`. Custo zero, paga a dívida com o GDD ("vi" vs "ouvi"), evita refactor quando diálogo do jogador chegar.

### P7 (nova) — `OriginalSeenAt` vs `LearnedAt`

Adicionar `LearnedAt` separado de `OriginalSeenAt` (renomeio do `SeenAt` atual). Expiração roda contra `LearnedAt`. Acesso do jogador futuro pode mostrar `OriginalSeenAt` ("o Tomas disse que viu há 3 dias").

### P8 (nova) — Cooldown de fofoca por par

Adicionar estado `lastGossipedWith map[string]time.Time` no NPC. Cooldown configurável (ex: 6h de jogo). Sem isso, NPCs em proximidade prolongada (sono compartilhado, almoço de 1h) trocam várias vezes seguidas. Define também: "≥2 NPCs no mesmo POI por **N horas de jogo**" como gatilho de elegibilidade (não N ticks).

### P9 (nova) — Schema final proposto pra discussão

```go
type Knowledge struct {
    Type           KnowledgeType // RECURSO, ENTIDADE, AVISTAMENTO_NPC, EVENTO_IMPORTANTE
    EntityId       string        // id do recurso/mob/npc/evento
    BlockId        string
    PoiId          string        // "" = outdoor
    OriginalSeenAt time.Time     // quando o observador original viu
    LearnedAt      time.Time     // quando ESTE npc soube
    Source         string        // "direct" ou npc_id_da_fonte
    Important      bool          // isenção de expiração e FIFO
}
```

Dedup por chave: `(Type, EntityId, BlockId, PoiId)`.

---

## 4. O que precisa de decisão sua antes de eu redigir o template

Em ordem de impacto:

1. **Schema final**: confirmar adoção de `Source`, `OriginalSeenAt` + `LearnedAt`, `Important`. Ou rejeitar com motivo.
2. **Tipo da 1.5**: `AVISTAMENTO_NPC` separado de `ROTINA_NPC` (preserva o GDD pra implementação futura) ou re-semantiza `ROTINA_NPC` como avistamento na 1.5 (inconsistência com GDD)?
3. **Geração**: dedup por chave (atualiza `LearnedAt`) ou disparo a cada tick (gera lixo)?
4. **Fofoca**: cooldown por par (estado adicional) ou troca a cada tick de proximidade (problemático)?
5. **Expiração**: lazy + sweep todo tick (recomendado), só sweep, ou só lazy?
6. **Configuração**: arquivo `knowledge_config.json` separado, seção em `config.json` existente, ou inline no NPC template?
7. **Admin inject**: strict (valida BlockId/PoiId) ou loose (admin é root)?
8. **EventoImportante na 1.5**: implementa campo + suporte em admin_inject, ou adia pra StoryManager?
9. **Cenários de teste**: o refinamento vai listar cenários concretos com admin_inject que produzem variedade observável? (Eu recomendo fortemente.)
10. **Inconsistência GDD §5.3/§5.4 vs §8.3**: você quer abrir issue separado pra alinhar isso, ou só anota no refinamento e segue?

Resolvido isso, o template do refinamento sai limpo. Quer ir item por item, ou prefere mandar suas escolhas em bloco e eu volto com discordâncias específicas?

---

## Sidinei:

1. Confirmação de entendimento
Podemos sim ter o campo de origem apesar do gdd dizer algo, e entregar o esquema sugerido se o desenvolvimento apontar alguma necessidade não contida no gdd vale o do desenvolvimento, pois o gdd pode esta desatualizado ou ainda não chegou a "ver" o funcionamento.

Cap. 5.4 Quando eu falei de conhecimento por tipo Locais, recursos, monstros, foi pensando assim um conhecimento de local é o npc saber que a maré de tal local sobre e baixa, é saber que em tal local tem uma estatua, que em tal local aconteceu algo, é conhecimento sobre o local de fato, recursos são sobre onde tem tal recurso, pra que server tal recurso, como encontro, o que preciso para coletar, sobre montros é saber onde tem tal monstro. Não sei se continua mantendo o local, ou podemos até fazer os conhecimentos com o desenvolvimento evoluido, por exemplo, como não temos recurso e nem montros, podemos ter conhecimento apenas de local e sobre outros npcs e depois colocamos outros tipos

2.1 O auto-gerador "viu outro NPC" não entrega o que o GDD descreve: Sim acho valido, por isso ainda penso em deixar o conhecimento somente para quanto tiver tudo que o npcs possa conhecer para ja fazer algo certo.

2.2 Com 3 residentes na mesma vila, o auto-gerador produz quase zero variedade: Isso dar para resolver incluindo e gerando mais npcs, sobre se ver varias vezes pode colocar um contador de vi tantas vezes, seria bom tambem colocar quanto tempo passaram juntos, tipo vi naila de x horas até y horas, e isso pode até ajudar a dizer naila fica de tal hora até tal hora ou estou delirando, podemos até listar conhecimentos de tal npc, logs de vistos e ai sim a listagem de vistos deles.

2.3 Confusão semântica: `ROTINA_NPC` ≠ "vi NPC aqui": Eu imagino a rotina do npc ser o resultado da inferencia calculado por `AVISTAMENTO_NPC` e penso até separar o que é conhecimento do que é visto, visto é logar e guardar tudo que viu, e conhecimento é quando tem varios destes visto para formar o conhecimento, tipo como é a comparação de dado x informação o dado sozinho não diz nada precisa da informação ao podemos ter o seguinte: O que o npc ver (dados brutos, que ao ter x do mesmo tipo ele consegue formar um conhecimento), conhecimento do npc (esse pode ser conhecimento formado por ele que são criado a partir do dado bruto, e conhecimento vindo de outro npc que falou após formar seus dados), o de visto ele pode expirar mais rapido e o conhecimento pode demorar mais de expirar, o que pensando aqui não tenho certeza é se compartilho os vistos tambem entre npcs, tipo eu conheço isso e vi essas coisas tambem, para ajudar ao outro npc fazer sua inferencia, exemplo se eu vi 1 lobo na floresta 2 vezes, e o npcs joão viu o lobo na floresta 3 vezes e me falou, logo eu sei que esse lobo foi visto 5 vezes ja sei que é um conhecimento.

 2.5 Mecânica de troca: semântica do `SeenAt` no destinatário: Gosto da ideia que falou de ter 2 -- Solução do GDD (implícita): dois campos — `OriginalSeenAt` (quando o observador original viu) e `LearnedAt` (quando este NPC soube). Expiração pode rodar contra um, contra outro, ou contra ambos. E ganha de brinde o campo `Source` (resolve furo 2.7 abaixo).

2.6 Cooldown de fofoca por par: Gosto da sua recomendação --- Eu recomendo A + estado `lastGossipedWith[npcId] = tickNumber`, com cooldown explícito (ex: "não fofoca de novo com o mesmo NPC por X horas de jogo"). Sem isso, o sistema fica frágil a esses cenários longos de proximidade.

2.7 Campo `Source` ausente do schema proposto: Eu sigo sua recomendação e volto a lembrar o gdd é o farol mas não é a verdade absoluta. 

2.8 FIFO de tamanho como mecanismo morto: Não entendi muito bem mas aceito sua recomendação

2.9 EventoImportante sem mecanismo de criação na 1.5: Sigo sua recomendação -- Recomendo implementar agora — é um booleano, custa nada, e ter o admin_inject capaz de simular é exatamente o tipo de teste que valida o sistema antes do StoryManager chegar.

2.10 Snapshot e admin_get_npc_knowledge -- Concordo

2.11 Validação de `admin_inject_knowledge:`: Aceito sua recomendação -- Eu recomendo strict. Se um dia precisar testar com dados corrompidos, faz outra flag explícita. Loose esconde bugs.

3. Avaliação das 5 perguntas + 4 novas
P1 — Onde os tempos de expiração vivem? Aceito sua recomendação
P2 — Granularidade de contagem: Concordo com você
P3 — Contexto narrativo do esquecimento: Aceito sua recomendação de ser com time simples, a pessoa acordada tambem pode esquecer.
P4 — Quando a expiração roda: Aceito sua recomendação
P5 — Limite de tamanho: idade ou importância?: Aceito sua recomendação
P6 (nova) — Campo `Source` no schema: Sim adicionar
P7 (nova) — `OriginalSeenAt` vs `LearnedAt`: Concordo com você
P8 (nova) — Cooldown de fofoca por par: Aceito sua recomendação

4. O que precisa de decisão sua antes de eu redigir o template

Acho que acima falei de todos veja se falta alguma resposta

---

## Claude:

Antes de fechar e ir pro template, três pontos exigem mais conversa. O resto está alinhado.

---

## Ponto crítico: separar "visto" de "conhecimento" é over-engineering pra 1.5

Você descreveu uma camada de "vistos" (dados brutos, expiram rápido) e outra de "conhecimento" (inferência a partir de X vistos, expira devagar), com compartilhamento entre NPCs também na camada de vistos.

**Isso é uma mudança de escopo significativa, não um ajuste de schema.** Quebrar em pontos concretos pra você ver o que entra:

1. Duas estruturas paralelas no NPC (`Observations []Observation` + `Knowledge []Knowledge`)
2. Regra de "thresholding" pra promover N observações em 1 conhecimento (e isso pra cada tipo, com calibração)
3. Dois decays diferentes, dois sweeps diferentes, dois admin_inject diferentes, dois admin_get diferentes
4. Decisão se fofoca passa observações, conhecimento, ou ambos
5. Se passa observações, regra de "minhas 2 + 3 do João = 5 → vira conhecimento" requer merge de listas com dedup por origem, não só por entidade
6. Comando admin pra inspecionar pré-knowledge ("o que o Tomas tá quase sabendo?")

A 1.5 já estava puxada. Isso dobra ela facilmente. E parte do retorno é cosmético — pra um observador externo, "Tomas sabe sobre Naila no mercado" e "Tomas tem 5 observações de Naila no mercado que somaram conhecimento" produzem o mesmo comportamento observável quando o jogador for conversar com ele.

### A versão moderada que captura ~80% do que você quer

Manter **uma estrutura só**, mas enriquecer o schema com agregados que já entregam a sensação de inferência:

```go
type Knowledge struct {
    Type           KnowledgeType
    EntityId       string
    BlockId        string
    PoiId          string        // "" = outdoor

    FirstSeenAt    time.Time     // primeiro avistamento (na chave dedup)
    LastSeenAt     time.Time     // último avistamento — substitui OriginalSeenAt
    SeenCount      int           // quantas vezes vi/ouvi

    LearnedAt      time.Time     // quando ESTE npc soube pela primeira vez
    Source         string        // "direct" ou "npc_id_da_fonte"
    Important      bool
}
```

Dedup por chave `(Type, EntityId, BlockId, PoiId)`. Quando o gerador detecta proximidade de novo:
- entry existe → `SeenCount++`, `LastSeenAt = agora`
- entry nova → `SeenCount = 1`, `FirstSeenAt = LastSeenAt = agora`

Pra fofoca: passa o struct inteiro. Receptor, ao receber:
- chave nova → cria entry com `SeenCount` recebido, `LearnedAt = agora`, `Source = npc_id`
- chave existente → merge: `SeenCount += SeenCount_recebido` (com cuidado pra não dobrar a sua própria contagem se voltar via terceiro — resolvido pelo cooldown por par + Source).

Isso já te dá:
- "Naila no mercado, 5 vezes, primeira vez dia 1 hora 12, última vez dia 3 hora 13" — toda a estrutura pra inferir rotina sem ter um sistema separado de rotina
- "Tomas viu 2 vezes + ouviu do João que ele viu 3 = sabe que foi visto 5 vezes" — sua intuição da observação, mas sem listas separadas
- Quando você quiser de fato classificar "isso virou conhecimento" (ex: prá liberar pro jogador só se `SeenCount >= 3`), é uma regra de **leitura**, não de schema. Adiciona quando precisar (Fase 3+, diálogo).

**O ciclo de propagação infinita que você quase descreveu** ("eu te passo, você me passa de volta") é exatamente o que o cooldown por par + checar `Source != self.Id` previne. Não precisa de separação visto/conhecimento pra resolver isso.

### Onde isso falha (pra você decidir consciente)

- Se a regra de promoção "vira conhecimento real só com N vistos" tiver que mudar comportamento do NPC em runtime (ex: NPC só conta pro jogador se virou conhecimento), você terá que tomar essa decisão em tempo de leitura cada vez. Custo: trivial. Comparar `SeenCount >= threshold`.
- Se você quiser que "vistos efêmeros" expirem MUITO mais rápido que "conhecimento consolidado", precisaria de dois decays. **Mas isso é justificativa-fantasma**: a expiração já é parametrizada per-tipo. Você pode simplesmente dar a tipos "observacionais" um lifetime curto e a tipos "consolidados" um lifetime longo, sem precisar de duas estruturas.

### Minha recomendação firme

Schema único com `SeenCount + FirstSeenAt + LastSeenAt`. Promoção pra "conhecimento" é regra de leitura, adicionada quando o diálogo do jogador exigir. Adia separação visto/conhecimento explicitamente, com nota clara no refinamento dizendo "se demanda de rotina inferida + threshold de promoção surgir, refatorar pra estrutura dupla".

**Aceita ou quer empurrar pelo modelo de duas camadas?** Se quiser empurrar, eu sigo, mas a 1.5 vai consumir significativamente mais horas e provavelmente quebrar em duas (1.5a observação + 1.5b inferência).

---

## Contradição no que você disse sobre tipos

> "Podemos ter conhecimento apenas de local e sobre outros npcs e depois colocamos outros tipos"

Mas o **único auto-gerador** da 1.5 é "viu outro NPC". Tipo `LOCAL` não tem gerador automático nesta fase — só entraria via `admin_inject_knowledge`.

Dá pra ir por dois caminhos:

**A)** Tipos definidos na 1.5: `AVISTAMENTO_NPC` (auto-gerado) e `LOCAL` (só admin_inject). Recursos e Entidades (mob) ficam pra quando esses sistemas existirem. **Recomendação.**

**B)** Tipos definidos na 1.5: só `AVISTAMENTO_NPC`. Admin_inject também só aceita esse tipo. Mais conservador, mais limpo.

A é mais útil pra testar fofoca com variedade (admin injeta "Tomas sabe que tem uma estátua na capela" → Naila aprende via fofoca). B é mais minimalista. Eu vou de **A**.

Sobre **Locais como conhecimento** (estátua na capela, maré sobe e desce): é semanticamente um tipo válido e cabe na ideia de mundo vivo. Mas como definir? O GDD §8.3 não fala em LOCAL como tipo — só como atributo de cada entry (`location` da entry). Pra evitar conflito, eu sugiro:

- `LOCAL` = info SOBRE um lugar (`EntityId = blockId` ou `EntityId = poiId`, info no campo `Important`/comentário ou via extensão futura)
- `AVISTAMENTO_NPC` = info sobre TER VISTO um npc num lugar

Mas honestamente: a 1.5 não precisa entregar `LOCAL` pra fechar o objetivo (testar geração + troca + expiração). Implementar LOCAL agora sem caso de uso real (não há gerador automático, e admin_inject vai ser usado uma vez pra testar e nunca mais) é YAGNI.

**Recomendação revisada:** só `AVISTAMENTO_NPC` na 1.5 (= caminho B). `LOCAL`, `RECURSO`, `ENTIDADE` entram quando os geradores deles existirem (StoryManager, mobs, recursos coletáveis). Aceita ou prefere A?

---

## Pendências menores

### Cenários de teste

Não respondeu explicitamente. Você quer que o refinamento liste cenários concretos de admin_inject que validam o comportamento? Tipo:

```
Cenário 1: Propagação simples
- T=0: admin injeta "AVISTAMENTO_NPC entity=lobo_alfa block=floresta poi=" na KB do Tomas
       com Important=true, Source="direct"
- T=1: aguarda Tomas e Ricardo coincidirem na taverna (almoço)
- T=2: admin_get_npc_knowledge ricardo → tem entry com Source="npc_ferreiro_tomas"

Cenário 2: Cooldown previne loop
- ...

Cenário 3: Expiração com Important=true
- ...
```

Eu recomendo. Sem isso, "validar a 1.5" vira "deixa rodar e ver se nada quebra", o que é fraco. Aceita?

### Inconsistência GDD §5.3/§5.4 vs §8.3

Você disse "Não sei se continua mantendo o local". Resposta direta: como decidimos que a 1.5 NÃO implementa `LOCAL` agora, a inconsistência **não bloqueia** o refinamento. Mas o GDD continua dizendo coisas conflitantes nos três capítulos.

Duas opções:

**A)** Refinamento 1.5 só anota a inconsistência na seção "Conflitos / decisões herdadas" e segue. Você abre issue separada (ou backlog item) pra alinhar §5.3 e §5.4 com §8.3 numa rodada de revisão de GDD. **Recomendação.**

**B)** Refinamento 1.5 inclui revisão dos capítulos GDD como parte do escopo. Mistura design doc com refinamento técnico — eu evitaria.

Aceita A?

---

## Resumindo o que falta confirmar

1. **Schema único enriquecido** (`SeenCount + FirstSeenAt + LastSeenAt`) ao invés de visto/conhecimento separados — sim ou não?
2. **Tipos na 1.5**: só `AVISTAMENTO_NPC` (caminho B revisado) ou também `LOCAL` via admin_inject (caminho A)?
3. **Cenários de teste explícitos** no refinamento — sim?
4. **Inconsistência GDD §5.3/§5.4 vs §8.3** — só anota e abre backlog separado?

Confirma esses 4 e eu redijo o template do refinamento 1.5. Se preferir empurrar contra alguma das recomendações, manda o argumento que eu respondo antes de redigir.

---

## Sidinei:

Aceito sua recomendação sobre: 

Minha recomendação firme
Schema único com `SeenCount + FirstSeenAt + LastSeenAt`. Promoção pra "conhecimento" é regra de leitura, adicionada quando o diálogo do jogador exigir. Adia separação visto/conhecimento explicitamente, com nota clara no refinamento dizendo "se demanda de rotina inferida + threshold de promoção surgir, refatorar pra estrutura dupla".

Sobre Contradição no que você disse sobre tipos eu não entendi se sua recomendação é opção A ou opção B, primeiro voce falou A depois falou B

Cenários de teste: Sim eu quero que o cenarios concretos de admin_inject
Inconsistência GDD §5.3/§5.4 vs §8.3: Aceito a A, porque depois do desenvolvimento que posso ver o qual ta certo o GDD

---

## Claude:

## Tipos: minha recomendação é B

Você está certo, eu me contradisse. Releu bem.

Sequência do que eu disse:
1. Primeiro recomendei **A** (`AVISTAMENTO_NPC` + `LOCAL` via admin_inject) com argumento "mais útil pra testar variedade"
2. Depois argumentei contra mim mesmo: "implementar LOCAL agora sem caso de uso real é YAGNI"
3. Fechei com "**Recomendação revisada: caminho B**" — só `AVISTAMENTO_NPC`

A recomendação final é **B**. O motivo da revisão foi perceber que:

- `LOCAL` na 1.5 só entraria via admin_inject (sem gerador automático)
- Admin_inject de `LOCAL` seria usado uma ou duas vezes pra testar e abandonado
- Pra testar variedade de **fofoca** (que é o objetivo real), `AVISTAMENTO_NPC` com 3+ NPCs já produz casos suficientes: Tomas vê Naila, conta pro Ricardo que não viu, Ricardo agora tem entry com `Source="npc_ferreiro_tomas"` sobre Naila num POI que Ricardo nunca foi. Isso é a propagação interessante. `LOCAL` adicionaria um tipo no enum sem adicionar comportamento testável distinto.
- Quando `RECURSO`/`ENTIDADE`/`LOCAL` chegarem (com geradores reais), o enum cresce trivialmente. Adicionar um valor de enum em Go é uma linha.

A em palavras simples: "vamos suportar mais tipos agora pra ter cenários ricos de teste."
B em palavras simples: "vamos suportar só o tipo que tem gerador real; cenários ricos vêm da combinação NPC × NPC × cooldown × expiração, não da variedade de tipos."

B é mais limpo porque mantém uma regra: **a 1.5 só implementa o que tem caminho automático de geração**. Admin_inject existe pra forçar cenários (Important=true, propagação cross-NPC, expiração), não pra simular sistemas inexistentes.

Aceita B (recomendação final) ou prefere A pelo argumento original de variedade?

---

## Confirmação consolidada antes do template

Tudo fechado, então:

1. ✅ Schema único: `Type, EntityId, BlockId, PoiId, FirstSeenAt, LastSeenAt, SeenCount, LearnedAt, Source, Important`
2. ⏳ **Tipos: B** (só `AVISTAMENTO_NPC`) — preciso de OK explícito
3. ✅ Cenários concretos de admin_inject no refinamento (vou listar 5-7 cobrindo: geração simples, dedup com SeenCount++, propagação simples, cooldown previne loop, expiração com Important=true, expiração padrão, FIFO em caso patológico)
4. ✅ Inconsistência GDD vai pra "Conflitos herdados" + backlog item separado

Confirma o **2** e eu redijo. Se quiser ajustar mais alguma coisa antes, manda agora.

---

## Sidinei:

Perfeito, confirmado então vamos de opção B, como ficaria o refinamento, dividimos o conhecimento em 2 correto? Como ficaria o backlog também então?

---

## Claude:

Espera — antes de redigir, preciso corrigir uma coisa que pode ser só confusão de leitura mas vale checar:

> "dividimos o conhecimento em 2 correto?"

**Não.** A decisão foi **schema único enriquecido**, não duas estruturas. Você concordou com isso na rodada anterior:

> "Aceito sua recomendação sobre: Schema único com `SeenCount + FirstSeenAt + LastSeenAt`. Promoção pra 'conhecimento' é regra de leitura..."

A intuição que você teve de "visto bruto" vs "conhecimento inferido" fica **toda dentro de uma estrutura só**, usando o campo `SeenCount` pra distinguir entries com pouca confirmação (`SeenCount=1`) de entries com muita (`SeenCount=5+`). Quando o diálogo do jogador (Fase 3+) precisar dizer "isso aqui já é certeza" vs "vi só uma vez", você lê o `SeenCount` no momento da consulta. Não tem duas listas, não tem dois sweeps, não tem dois admin_inject.

Se foi só pergunta de confirmação e você já entendia assim, ignora. Se você estava esperando duas estruturas, fala agora antes de eu redigir porque o documento abaixo vai contra essa expectativa.

Vou assumir que era confirmação e seguir. Se errei, manda parar.

---

# Refinamento 1.5 — Fofoca / KnowledgeBase

> Salvar como `docs/product/refinements/1.5-fofoca-knowledgebase.md`

## 1. O que é

NPCs ganham uma `KnowledgeBase` que registra avistamentos de outros NPCs em `(Block, Poi)`, com dedup, contagem de vezes vistos e timestamps. Quando dois NPCs coincidem num POI, trocam entries da KB respeitando cooldown por par. Entries expiram por idade, com isenção opcional via flag `Important`. Tudo manipulável e inspecionável via comandos admin.

A 1.5 entrega o **substrato** da mecânica de fofoca do GDD §8.3. Auto-geração só cobre `AVISTAMENTO_NPC` (único tipo automático nesta fase). Outros tipos (`RECURSO`, `ENTIDADE`, `LOCAL`, `EVENTO_IMPORTANTE` populado pelo StoryManager) ficam para quando seus respectivos geradores existirem — a 1.5 não os implementa.

## 2. Referência no GDD

- `gdd/01_Livro_de_Regras/08_Mundo_Vivo_e_NPCs.md` §8.3 (Percepção Cognitiva, Esquecimento, Fofoca, Relacionamentos)
- `gdd/01_Livro_de_Regras/05_Exploracao_e_Mundo.md` §5.3 e §5.4 (ciclo de tempo, interação com NPCs)
- `docs/architecture/07-npc-state-machine.md` (visão arquitetural da fofoca incremental)

**Conflitos / decisões herdadas:**

- **§5.3 vs §8.3**: §5.3 fala em "+1 ponto de conhecimento mútuo" — modelo legado, não tipado. §8.3 define struct tipada `{type, id, location, seenAt}`. A 1.5 segue §8.3 e ignora §5.3. Inconsistência registrada no backlog de auditoria do GDD, fora do escopo desta rodada.
- **§5.4 lista "Locais" como tipo de conhecimento**: §8.3 só tem 4 tipos (`RECURSO`, `ENTIDADE`, `ROTINA_NPC`, `EVENTO_IMPORTANTE`). A 1.5 segue §8.3 e descarta "Locais" como tipo nesta fase. Mesma inconsistência, mesmo backlog de auditoria.
- **§8.3 promete diferença "vi pessoalmente" vs "ouvi falar" no acesso do jogador**, mas o schema do GDD não tem campo `Source`. Lacuna do GDD que a 1.5 fecha adicionando `Source` ao schema. GDD desatualizado em relação à implementação — registrar no backlog de auditoria.
- **§8.3 menciona "Relacionamentos NPC↔NPC" como parte do mesmo sistema de fofoca**. A 1.5 NÃO implementa relacionamentos (Fase 3+, junto com diálogo do jogador). Fofoca implementada nesta rodada altera só `KnowledgeBase`, não há `affinity` ou `friendship` tracker.

## 3. Decisões em aberto

### Decisão 3.1 — Estrutura: dupla (visto vs conhecimento) ou única?

- Opções: A) `Observations` + `Knowledge` (dois decays, dois geradores, regra de promoção), B) Estrutura única com `SeenCount` e timestamps agregados
- **Escolhido: B**
- Justificativa: A dobra o escopo da 1.5 sem entregar comportamento observável distinto na fase atual. `SeenCount` num schema único já representa "vi 1 vez" vs "vi 5 vezes" — promoção pra "conhecimento real" é regra de **leitura** (`SeenCount >= N`), aplicada no acesso do jogador (Fase 3+).
- Consequência: Se a Fase 3+ precisar de comportamento divergente entre "visto efêmero" e "conhecimento consolidado" que não dê pra modelar como `SeenCount + lifetime` calibrados, refatora pra estrutura dupla. Nota explícita registrada na seção 10.

### Decisão 3.2 — Tipos suportados na 1.5

- Opções: A) `AVISTAMENTO_NPC` (auto-gerado) + `LOCAL` (só admin_inject), B) Só `AVISTAMENTO_NPC` (auto-gerado + admin_inject)
- **Escolhido: B**
- Justificativa: Regra: a 1.5 só implementa tipo com caminho automático de geração. `LOCAL`, `RECURSO`, `ENTIDADE` sem gerador real entram via admin_inject uma ou duas vezes e morrem — gold-plating. `AVISTAMENTO_NPC` com 3 NPCs já produz cenários suficientes pra testar fofoca + cooldown + propagação + expiração.
- Consequência: Enum `KnowledgeType` tem só um valor agora. Adicionar valores é trivial (uma linha) quando StoryManager / mobs / recursos coletáveis chegarem.

### Decisão 3.3 — Schema da entry

- **Escolhido:**
  ```go
  type KnowledgeType string
  const KnowledgeAvistamentoNPC KnowledgeType = "AVISTAMENTO_NPC"

  type Knowledge struct {
      Type           KnowledgeType
      EntityId       string    // id do NPC visto (no caso de AVISTAMENTO_NPC)
      BlockId        string    // onde foi visto
      PoiId          string    // POI; "" = outdoor virtual
      FirstSeenAt    time.Time // primeiro avistamento na chave dedup
      LastSeenAt     time.Time // último avistamento
      SeenCount      int       // quantas vezes (próprio + ouvido via fofoca)
      LearnedAt      time.Time // quando ESTE npc soube pela primeira vez
      Source         string    // "direct" ou npc_id da fonte
      Important      bool      // isenção de expiração e FIFO
  }
  ```
- Justificativa: `FirstSeenAt`/`LastSeenAt` substituem o "OriginalSeenAt" — `FirstSeenAt` é a primeira vez que a entry foi criada, `LastSeenAt` é a última atualização. `LearnedAt` separa "quando soube" de "quando o original viu" pra acesso futuro do jogador. `Source` paga a dívida com o GDD. `Important` permite simular EventoImportante via admin_inject antes do StoryManager existir.
- Consequência: 10 campos por entry. Custo de memória negligenciável até centenas de NPCs com KB de dezenas de entries.

### Decisão 3.4 — Chave de dedup

- **Escolhido: `(Type, EntityId, BlockId, PoiId)`**
- Justificativa: Cada combinação única é uma "entry". Re-avistamento atualiza `LastSeenAt` e incrementa `SeenCount`. Visto em POI diferente do mesmo bloco = entry nova (informação distinta narrativamente).
- Consequência: KB pode ter várias entries do mesmo NPC se ele aparece em POIs diferentes ("vi Naila na cabana 3 vezes" + "vi Naila no mercado 2 vezes" = duas entries).

### Decisão 3.5 — Gatilho de auto-geração de `AVISTAMENTO_NPC`

- Opções: A) A cada tick em que há NPCs no mesmo POI, B) Apenas na transição para o POI, C) Threshold de tempo de proximidade
- **Escolhido: A (com dedup por chave)**
- Justificativa: A combinado com dedup é equivalente em prática à C: a primeira detecção cria a entry, as subsequentes só incrementam `SeenCount` e atualizam `LastSeenAt`. Mais simples que B (que precisa de estado adicional `lastSeenInSamePoi` por par).
- Consequência: NPCs juntos por 8h de sleeping geram `SeenCount=8` na entry. Comportamento esperado, observável e correto narrativamente ("o Tomas viu a Naila várias vezes no mesmo lugar").

### Decisão 3.6 — Gatilho de fofoca (troca de entries)

- **Escolhido: ≥2 NPCs no mesmo `(Block, Poi)` + cooldown por par expirado**
- Justificativa: Cooldown previne flood em proximidade prolongada (almoço de 1h, sono de 8h) e ciclos de propagação infinita.
- Consequência: Estado adicional no NPC: `LastGossipedWith map[string]time.Time` (chave = npcId, valor = gameTime da última troca com aquele par). Cooldown configurável, default 6h de jogo.

### Decisão 3.7 — Quantas entries trocam por evento de fofoca

- **Escolhido: 1 a 2 entries, escolhidas aleatoriamente da KB do emissor**
- Justificativa: Mantém alinhamento com §8.3 do GDD. Aleatório evita comportamento determinístico previsível. Quantidade pequena evita transferência em massa.
- Consequência: Propagação completa de info entre 3 NPCs pode levar vários encontros. Comportamento desejado (informação se espalha, não se teletransporta).

### Decisão 3.8 — Anti-loop na propagação

- **Escolhido: Emissor não passa entries com `Source = receptor.Id`. Receptor não cria entry duplicada de info que ele mesmo originou (`EntityId` ≠ receptor.Id é checado).**
- Justificativa: Sem isso, Tomas conta pra Ricardo no encontro 1, Ricardo conta pra Tomas no encontro 2, ciclo infinito de re-aprendizado.
- Consequência: NPC nunca aprende sobre si mesmo via fofoca (`EntityId == self.Id` é filtrado). NPC nunca aprende algo que ele mesmo ensinou.

### Decisão 3.9 — Merge na recepção: SeenCount soma ou substitui?

- **Escolhido: Recepção de entry nova (chave inexistente) usa o `SeenCount` recebido. Entry existente NÃO soma SeenCount via fofoca — só atualiza `LastSeenAt` se o recebido for mais recente, e renova `LearnedAt` se quiser tracking de "ouvi de novo".**
- Justificativa: Somar via fofoca cria inflação artificial (Tomas tem `SeenCount=2`, ouve de Ricardo que ele viu 3 vezes → Tomas tem 5? Mas o Ricardo provavelmente também vai ouvir de volta e somar de novo). Manter `SeenCount` como reflexo de **avistamentos próprios** evita esse problema, e mantém a semântica de "contagem confiável de quantas vezes alguém ou alguém-que-eu-confio-falou viu isso" sem dupla contagem.
- Consequência: A intuição "eu vi 1 + ouvi 3 do João = sei que viu 4" não fica explícita no schema. Se quiser isso depois, adiciona `HeardCount` separado. Por ora, suficiente para o objetivo da 1.5 (substrato funcional, sem inferência sofisticada).

### Decisão 3.10 — Onde os tempos de expiração vivem

- **Escolhido: Arquivo `server/data/knowledge_config.json` per-tipo**
- Justificativa: Constante em código mata iteração. Per-NPC é over-engineering antes de Traits.
- Estrutura proposta:
  ```json
  {
    "expirationHours": {
      "AVISTAMENTO_NPC": 48
    },
    "gossipCooldownHours": 6,
    "maxKnowledgeBaseSize": 100,
    "gossipMinExchangePerEvent": 1,
    "gossipMaxExchangePerEvent": 2
  }
  ```
- Consequência: Quando Traits chegar (Fase 4+), trait "Memória de Elefante" multiplica `expirationHours` desse NPC. Estrutura preparada.

### Decisão 3.11 — Granularidade de contagem de expiração

- **Escolhido: Horas de jogo via `time.Duration`**
- Justificativa: `GameTime.Time` é `time.Time`. Comparação `gameTime.Time.Sub(learnedAt) > expirationDuration` é trivial. Período é granular demais (6h numa escala de 48h).

### Decisão 3.12 — Quando a expiração roda

- **Escolhido: Híbrido — lazy em getters + sweep no início do `ProcessTick` de cada NPC**
- Justificativa: Lazy garante que ninguém vê entry vencida. Sweep mantém estado limpo entre ticks para logs e admin queries.
- Consequência: Custo O(N × KB_média) por tick. Negligenciável até Fase 4+.

### Decisão 3.13 — FIFO de tamanho

- **Escolhido: FIFO por idade (`LearnedAt` mais antigo), com isenção pra `Important = true`**
- Justificativa: Em runtime normal, expiração dispara antes do FIFO. FIFO é proteção contra explosão (admin_inject em massa, bug futuro), não comportamento de jogo.
- Consequência: Não construir nenhuma mecânica de jogo em cima do FIFO.

### Decisão 3.14 — Validação de `admin_inject_knowledge`

- **Escolhido: Strict (valida BlockId, PoiId, EntityId no momento da injeção)**
- Justificativa: Loose esconde bugs. Consistente com a validação fatal do loader na 1.4.
- Consequência: Admin recebe erro claro se injetar dado inválido. Não pode simular "dados corrompidos" sem flag explícita (não prevista na 1.5).

### Decisão 3.15 — Snapshot e KB

- **Escolhido: Cópia profunda das entries na construção do snapshot**
- Justificativa: Snapshot é imutável por contrato. Sem cópia, admin vê estado vivo.
- Consequência: Custo extra de cópia de slice + cópia de struct por NPC por tick. Negligenciável.

### Decisão 3.16 — Persistência

- **Escolhido: NÃO persiste entre reinícios do servidor**
- Justificativa: Phase 0. Persistência de KB depende de SQLite que ainda não existe. Consistente com a 1.4 que também não persiste POI atual.
- Consequência: KB reseta a cada `go run`. Aceitável em dev.

---

## 4. Escopo — o que ENTRA

### 4.1 — Struct `Knowledge` e enum `KnowledgeType`

- [ ] `server/npc/knowledge.go` novo arquivo com a struct definida em 3.3
- [ ] Enum `KnowledgeType` com único valor `KnowledgeAvistamentoNPC`
- [ ] Função `NewKnowledge(...)` com defaults sensatos

### 4.2 — `Npc` ganha campos novos

- [ ] `KnowledgeBase []Knowledge` no struct `Npc`
- [ ] `LastGossipedWith map[string]time.Time` no struct `Npc`
- [ ] Construtor `NewNpc` inicializa ambos vazios
- [ ] Methods `addOrUpdateKnowledge(k Knowledge) bool` (retorna true se foi nova entry, false se foi update)
- [ ] Method `getKnowledge(type, entityId, blockId, poiId) (Knowledge, bool)`

### 4.3 — Config de Knowledge

- [ ] `server/data/knowledge_config.json` com estrutura de 3.10
- [ ] Loader em `server/npc/knowledge_config.go`
- [ ] Validação no load (panic se valores zero ou negativos)

### 4.4 — Auto-geração de `AVISTAMENTO_NPC` no `ProcessTick`

- [ ] No início do loop por NPC (antes do `getNpcsInLocation` existente), reutilizar a lista de NPCs co-localizados
- [ ] Para cada par (npc, outro) co-localizado: chamar `npc.addOrUpdateKnowledge` com entry `{Type=AVISTAMENTO_NPC, EntityId=outro.Id, BlockId, PoiId, FirstSeenAt=now, LastSeenAt=now, SeenCount=1, LearnedAt=now, Source="direct", Important=false}`
- [ ] Dedup garante que entry existente só atualiza `LastSeenAt` e incrementa `SeenCount`

### 4.5 — Sweep de expiração no `ProcessTick`

- [ ] Antes da geração de novos avistamentos, varre `KnowledgeBase` do NPC
- [ ] Remove entries com `gameTime.Time.Sub(learnedAt) > expirationDuration[type]` E `Important == false`
- [ ] Log debug com IDs removidas se `config.Log.NPCKnowledge` estiver ativo

### 4.6 — Fofoca

- [ ] Em `ProcessTick`, após auto-geração, para cada par (npc, outro) co-localizado:
  - Checar cooldown: `lastGossipedWith[outro.Id]` + `gossipCooldownHours` < `gameTime.Time`
  - Se elegível, executar troca bidirecional:
    - Escolher 1-2 entries aleatórias da KB do emissor onde `EntityId != receptor.Id` E `Source != receptor.Id`
    - Para cada: criar entry no receptor com `{Source=emissor.Id, LearnedAt=now}` se chave nova; senão atualizar `LastSeenAt` se o recebido for mais recente
    - Atualizar `lastGossipedWith[outro.Id] = gameTime.Time` em ambos
- [ ] Troca rodada **uma vez por par por tick** (não duplicar emissor↔receptor e receptor↔emissor — fazer ambas na mesma iteração)

### 4.7 — Lazy expiration nos getters

- [ ] `Npc.GetActiveKnowledge() []Knowledge` filtra expiradas no momento da leitura
- [ ] Usado por admin_get_npc_knowledge

### 4.8 — FIFO de tamanho

- [ ] Em `addOrUpdateKnowledge`, após inserir entry nova, se `len(KB) > maxKnowledgeBaseSize`:
  - Ordenar por `LearnedAt` ascendente, ignorando entries com `Important=true`
  - Remover a mais antiga não-importante
  - Se todas forem importantes e ainda exceder, log warning mas mantém todas

### 4.9 — Snapshot inclui KB

- [ ] `Snapshot.NPCs[i].KnowledgeBase` populado com cópia profunda das entries
- [ ] `Snapshot.GetNPCKnowledge(npcId string) []Knowledge` helper read-only

### 4.10 — Comandos admin

- [ ] `admin_inject_knowledge` — payload: `{npcId, type, entityId, blockId, poiId, important?}`. Strict validation:
  - `npcId` deve existir
  - `type` deve ser valor válido do enum (no momento, só `AVISTAMENTO_NPC`)
  - `entityId` deve existir como NPC válido para tipo `AVISTAMENTO_NPC` (e ser diferente de npcId)
  - `blockId` deve existir em `blocks.json`
  - `poiId` deve estar em `block.Pois` (ou ser `""`)
  - Erros retornam mensagem clara via notifier; não interrompem servidor
- [ ] `admin_get_npc_knowledge <npcId>` — retorna lista de entries ativas (não expiradas) da KB, com todos os campos
- [ ] `admin_get_npc_full` (existente) — ganha campo `knowledgeBaseSize: int` no DTO (contagem; lista completa fica no comando dedicado pra não inflar payload)

### 4.11 — Logging configurável

- [ ] `config.Log.NPCKnowledge bool` novo flag em `server/config/`
- [ ] Logs: criação de entry, update de entry (SeenCount++), fofoca (com IDs e entries trocadas), expiração, FIFO discard

---

## 5. Escopo — o que NÃO entra

- **Tipos `LOCAL`, `RECURSO`, `ENTIDADE`, `EVENTO_IMPORTANTE` auto-gerados** — esperam StoryManager, mobs e recursos coletáveis. Enum só tem `AVISTAMENTO_NPC` nesta fase. Important pode ser setado via admin_inject.
- **Itinerantes / NPCs que se movem entre blocos** — sem isso, propagação inter-vila não acontece. 1.6+ ou depende de decisão de roadmap.
- **StoryManager / EventoImportante real** — admin_inject simula até existir.
- **Diálogo do jogador com NPC** — Fase 3+. Acesso à KB do NPC só via admin nesta rodada.
- **Sistema de Afinidade / Relacionamentos NPC↔NPC** — Fase 3+ junto com diálogo.
- **Inferência de rotina ("vi Naila 5 vezes no mercado às 13h → ela faz isso sempre")** — Fase 3+ ou quando necessário; será derivada de `SeenCount + LastSeenAt + PoiId` na leitura, sem novo schema.
- **Compartilhamento de `SeenCount` via fofoca** (a intuição "soma minhas observações + as ouvidas") — adiada. Decisão 3.9 documenta o porquê.
- **Persistência de KB entre reinícios** — sem SQLite ainda. KB reseta a cada `go run`.
- **Traits que modificam expiração / decay de KB** ("Memória de Elefante") — Fase 4+ junto com Traits.
- **Separação visto/conhecimento** — adiada. Schema atual suporta promoção via `SeenCount >= N` na leitura sem refactor.

---

## 6. Critérios de aceite

- [ ] Servidor sobe limpo com `knowledge_config.json` válido
- [ ] Servidor falha na inicialização com mensagem clara se `knowledge_config.json` tem valores inválidos (zero, negativos, tipo desconhecido)
- [ ] Após 1 dia de jogo com 3 NPCs, KB de cada NPC tem ≥1 entry (Tomas e Naila verão um ao outro pelo menos no almoço/mercado; Ricardo verá os dois apenas se schedule cruzar em algum ponto — verificar)
- [ ] Re-encontro do mesmo par no mesmo POI incrementa `SeenCount` e atualiza `LastSeenAt`, NÃO cria entry duplicada
- [ ] Auto-geração nunca cria entry com `EntityId == npc.Id` (NPC não se vê)
- [ ] Fofoca: admin injeta entry `Important=true` em Tomas sobre `entityId=npc_curandeira_naila, blockId=floresta_do_norte, poiId=""` (cenário sintético — Naila não vai à floresta, mas Tomas finge ter visto). Após encontro Tomas+Ricardo na taverna, Ricardo tem entry com `Source="npc_ferreiro_tomas"`
- [ ] Cooldown impede flood: Tomas e Ricardo juntos por 8h dormindo (admin força esse cenário) trocam fofoca no máximo 2 vezes (8h / 6h cooldown = 1 troca; com tolerância, no máximo 2)
- [ ] Anti-loop: após Ricardo aprender de Tomas, no próximo encontro Tomas não recebe de volta a mesma entry (Source check)
- [ ] Expiração: entry com `LearnedAt` mais antigo que `expirationHours[AVISTAMENTO_NPC]` é removida do sweep; `Important=true` sobrevive
- [ ] FIFO: admin injeta 101 entries (limite=100); a mais antiga não-importante é descartada; entries `Important=true` ficam intocadas
- [ ] `admin_inject_knowledge` com `blockId` inexistente retorna erro claro
- [ ] `admin_get_npc_knowledge` retorna lista correta de entries ativas, formato JSON tipado
- [ ] `admin_get_npc_full` retorna `knowledgeBaseSize`
- [ ] `go build` e `go vet` limpos

---

## 7. Invariantes e edge cases

**Invariantes:**

- NPC nunca tem entry com `EntityId == self.Id` (não se vê via auto-geração e admin_inject rejeita)
- NPC nunca tem entry com `Source == self.Id` (não tem como aprender de si)
- Entry com `Important=true` nunca é removida por expiração nem por FIFO
- `SeenCount >= 1` sempre que entry existe
- `FirstSeenAt <= LastSeenAt` sempre
- `LearnedAt <= LastSeenAt` para entries `Source="direct"` (NPC só atualiza `LastSeenAt` em encontros próprios, e `LearnedAt` foi setado na criação)
- KB nunca tem duas entries com a mesma chave `(Type, EntityId, BlockId, PoiId)`
- `KnowledgeBase != nil` (slice vazio é ok, mas não nil) — invariante de construção

**Edge cases:**

- NPC sozinho num POI: nenhuma entry gerada, nenhuma fofoca, sweep e lazy ainda rodam (resultado: noop)
- 3+ NPCs no mesmo POI: todos veem todos (3 NPCs → 6 atualizações de KB), fofoca rola entre todos os pares respeitando cooldown individual por par
- NPC com KB cheia (100 entries) recebe entry nova via fofoca: FIFO descarta a mais antiga não-importante antes de inserir
- NPC com KB de 100 entries todas `Important=true` recebe entry nova: log warning, mantém todas, descarta a nova (ou aceita e cresce além do limite? **decisão: descarta a nova com log warning** — invariante de limite tem precedência)
- Admin injeta entry idêntica a uma existente: tratada como update (mesmo path que re-encontro), `SeenCount++`, `LastSeenAt` = momento atual
- Fofoca rola mas emissor não tem entries elegíveis (todas têm `EntityId == receptor.Id` ou `Source == receptor.Id`): cooldown não atualiza (não houve troca real), próximo encontro tenta de novo
- `expirationHours[AVISTAMENTO_NPC] = 0`: efetivamente desabilita expiração desse tipo. Aceitar como configuração válida.

---

## 8. Como validar

### 8.1 — Validações de carga e build

1. Subir servidor com `knowledge_config.json` válido: `go run ./server/cmd/main.go`. Log mostra `loaded knowledge config` sem erro.
2. Editar `knowledge_config.json`: setar `expirationHours.AVISTAMENTO_NPC = -1`. Servidor falha com mensagem clara. Reverter.
3. Editar `knowledge_config.json`: adicionar tipo inexistente `expirationHours.FOO = 24`. Servidor falha. Reverter.

### 8.2 — Cenários concretos de admin_inject

**Cenário 1 — Geração automática simples**

```
Pré-condição: servidor recém-iniciado, KB vazia em todos.
Passos:
1. Deixa rodar até o horário de almoço (12-13h jogo) → Tomas e Naila coincidem em `taverna_da_vila`
2. admin_get_npc_knowledge npc_ferreiro_tomas
3. admin_get_npc_knowledge npc_curandeira_naila
Resultado esperado:
- Tomas tem entry: {Type=AVISTAMENTO_NPC, EntityId=npc_curandeira_naila, BlockId=vila_sao_tome, PoiId=taverna_da_vila, SeenCount=1, Source="direct", Important=false}
- Naila tem entry equivalente sobre Tomas
- Ricardo NÃO tem nenhuma entry (estava no portão)
```

**Cenário 2 — Dedup com SeenCount++**

```
Pré-condição: cenário 1 executado.
Passos:
1. Deixa rodar até o jantar (próximo encontro Tomas+Naila na taverna, ~19h jogo)
2. admin_get_npc_knowledge npc_ferreiro_tomas
Resultado esperado:
- Mesma entry de Naila com SeenCount=2 (ou mais, depende de quantos ticks ficaram juntos)
- LastSeenAt atualizado para o horário do jantar
- FirstSeenAt mantido (horário do almoço original)
- Nenhuma entry duplicada
```

**Cenário 3 — Propagação simples via fofoca**

```
Pré-condição: KB vazia em todos.
Passos:
1. admin_inject_knowledge { npcId: npc_ferreiro_tomas, type: AVISTAMENTO_NPC, entityId: npc_curandeira_naila, blockId: floresta_do_norte, poiId: "", important: true }
   (sintético: Tomas "viu" Naila na floresta — ela nunca vai lá, é teste forçado)
2. Verificar: admin_get_npc_knowledge npc_ferreiro_tomas mostra a entry com Source="direct"
3. Aguardar Tomas e Ricardo coincidirem em `taverna_da_vila` (almoço/jantar)
4. admin_get_npc_knowledge npc_guarda_ricardo
Resultado esperado:
- Ricardo tem entry sobre Naila em floresta_do_norte com Source="npc_ferreiro_tomas"
- Important=true preservado
- LearnedAt = momento do encontro, FirstSeenAt = LearnedAt (Ricardo nunca viu)
```

**Cenário 4 — Cooldown previne flood**

```
Pré-condição: KB de Tomas e Naila com várias entries (pode usar admin_inject pra prepopular).
Passos:
1. Anotar `gameTime` antes do almoço
2. Deixar Tomas e Naila no almoço (1h de jogo juntos na taverna)
3. Contar quantas vezes log de fofoca disparou no par Tomas↔Naila no período
Resultado esperado:
- Exatamente 1 evento de fofoca no par no almoço (cooldown=6h, almoço dura 1h)
- Próximo evento de fofoca só no jantar (6h depois)
```

**Cenário 5 — Expiração padrão**

```
Pré-condição: Tomas tem entry sobre Naila com LearnedAt antigo.
Passos:
1. admin_inject_knowledge com entry, important=false. Tomas tem entry.
2. Manualmente avançar gameTime em > 48h (admin_set_time +49h)
3. Aguardar 1 tick
4. admin_get_npc_knowledge npc_ferreiro_tomas
Resultado esperado:
- Entry foi removida pelo sweep
- Log mostra remoção com motivo "expirada"
```

**Cenário 6 — Important não expira**

```
Pré-condição: igual cenário 5, mas important=true.
Passos: iguais.
Resultado esperado:
- Entry continua na KB após +49h
- Sweep ignora entries Important
```

**Cenário 7 — Anti-loop**

```
Pré-condição: cenário 3 executado (Ricardo aprendeu de Tomas sobre Naila/floresta).
Passos:
1. Aguardar próximo encontro Tomas+Ricardo após cooldown
2. admin_get_npc_knowledge npc_ferreiro_tomas — entry sobre Naila/floresta deve ter Source="direct" (Tomas é dono original)
3. Verificar logs: fofoca pode rolar com OUTRAS entries, mas Tomas NÃO recebe de volta a entry Naila/floresta (Source=tomas → Ricardo não passa de volta)
Resultado esperado:
- Tomas mantém Source="direct" naquela entry
- Logs confirmam que a entry Naila/floresta foi filtrada do conjunto que Ricardo emitiria pra Tomas
```

**Cenário 8 — FIFO em caso patológico**

```
Pré-condição: KB de Tomas vazia.
Passos:
1. Script admin: injetar 101 entries diferentes (variando entityId fictícios via admin_inject), todas important=false
2. admin_get_npc_knowledge npc_ferreiro_tomas
Resultado esperado:
- KB tem exatamente 100 entries
- A entry mais antiga (LearnedAt mais antigo) foi descartada
- Log mostra discard com motivo "FIFO"
```

### 8.3 — Validação de strict do admin_inject

```
1. admin_inject_knowledge { npcId: "inexistente", ... } → erro "npc not found"
2. admin_inject_knowledge { type: "FOO", ... } → erro "invalid type"
3. admin_inject_knowledge { entityId: "npc_inexistente", ... } → erro "entityId not found"
4. admin_inject_knowledge { blockId: "vila_inexistente", ... } → erro "block not found"
5. admin_inject_knowledge { poiId: "poi_inexistente", ... } → erro "poi not in block"
6. admin_inject_knowledge { npcId: "npc_tomas", entityId: "npc_tomas", ... } → erro "npc cannot see itself"
```

### 8.4 — Ordem de execução de implementação sugerida

`4.1 (struct) → 4.3 (config) → 4.2 (campos no NPC) → 4.5 (sweep) → 4.4 (auto-gen) → 4.7 (lazy) → 4.8 (FIFO) → 4.6 (fofoca) → 4.9 (snapshot) → 4.10 (admin) → 4.11 (logging)`

Fofoca é a parte mais complexa — fica depois de tudo que ela depende estar funcionando isoladamente.

---

## 9. O que isso DESTRAVA

- **Fase 3 (Diálogo do jogador)**: jogador pergunta "viu alguém suspeito?" e o NPC responde baseado na KB ativa. Promoção `SeenCount >= N` para "conhecimento real" entra como regra de leitura no diálogo.
- **1.6+ (Itinerantes)**: NPC que muda de bloco carrega KB junto, propaga info entre vilas naturalmente.
- **StoryManager (Fase 3+)**: eventos globais injetam entries com `Important=true` na KB de NPCs próximos. Mesma estrutura, novo gerador.
- **Sistema de afinidade (Fase 3+)**: presença de entries específicas na KB pode modificar afinidade ("ouviu rumor ruim sobre o jogador").
- **Auditoria narrativa**: admin pode reconstituir "o que cada NPC sabia em cada momento" — útil pra debugar comportamento emergente estranho.

---

## 10. O que isso AINDA não resolve

- **Inferência de rotina**: "Naila vai sempre ao mercado às 13h" não é gerada automaticamente. Pode ser derivada na leitura agrupando entries por `(EntityId, PoiId)` e olhando `SeenCount` + variância de `LastSeenAt`, mas não é feito automaticamente.
- **Compartilhamento de SeenCount na fofoca**: decisão 3.9 documenta que `SeenCount` reflete apenas avistamentos diretos. "Eu vi 2 + ouvi João viu 3 = sei que viu 5" não fica no schema. Se a Fase 3+ precisar, adiciona `HeardCount`.
- **Distinção visto/conhecimento como duas estruturas**: schema único atende a fase atual. Se demanda emergente na Fase 3+ (com diálogo) provar que não dá pra modelar como `SeenCount + lifetime` calibrados, refatora pra estrutura dupla — aceito como dívida possível.
- **Persistência**: KB reseta a cada reinício. Quando SQLite entrar, serializar slice de entries é trivial.
- **Inconsistência GDD §5.3/§5.4 vs §8.3**: registrada na seção 2, mas correção do GDD fica em backlog separado (não bloqueia a 1.5).
- **Inferência cross-tipo**: quando outros tipos entrarem (RECURSO, etc), a inferência ainda não cruza tipos (ex: "vi pegadas de lobo no mesmo lugar onde Naila não voltou" → suspeita).
- **Tradução pra texto de diálogo**: entries têm IDs (`npc_curandeira_naila`), não texto natural. Tradução pra "a curandeira" + frase fluida é responsabilidade do sistema de diálogo, fora da 1.5.

---

# Atualização do backlog

> Substituir a entrada `### 1.5 — Fofoca` em `docs/backlog.md` por:

```markdown
### 1.5 — Fofoca / KnowledgeBase (requer 1.4 completo)

> **Refinamento:** [refinements/1.5-fofoca-knowledgebase.md](product/refinements/1.5-fofoca-knowledgebase.md)

- Escopo: substrato funcional de KnowledgeBase com fofoca entre os 3 residentes da Vila. Schema único com `SeenCount + FirstSeenAt + LastSeenAt + LearnedAt + Source + Important`. Auto-geração só para `AVISTAMENTO_NPC` (único tipo automático nesta fase).
- Entradas:
  - [ ] Struct `Knowledge` com 10 campos; enum `KnowledgeType` com único valor `AVISTAMENTO_NPC`
  - [ ] `Npc` ganha `KnowledgeBase []Knowledge` + `LastGossipedWith map[string]time.Time`
  - [ ] `knowledge_config.json` com expiração per-tipo, cooldown de fofoca, tamanho máximo, quantidade trocada por evento
  - [ ] Auto-geração: quando 2+ NPCs no mesmo `(Block, Poi)`, cada um popula entry sobre o outro; dedup por chave `(Type, EntityId, BlockId, PoiId)` incrementa `SeenCount` ao invés de duplicar
  - [ ] Fofoca: ≥2 NPCs co-localizados + cooldown por par expirado → troca 1-2 entries aleatórias; anti-loop via filtro de `Source`
  - [ ] Expiração: lazy nos getters + sweep no início do `ProcessTick`; entries `Important=true` isentas
  - [ ] FIFO de tamanho: descarta entry com `LearnedAt` mais antigo se exceder limite; entries `Important` isentas
  - [ ] Snapshot inclui cópia profunda da KB
  - [ ] Comandos admin: `admin_inject_knowledge` (strict validation), `admin_get_npc_knowledge`, `admin_get_npc_full` ganha `knowledgeBaseSize`
  - [ ] Flag de log `NPCKnowledge`
- Exceções (o que NÃO entra):
  - Tipos `LOCAL`, `RECURSO`, `ENTIDADE`, `EVENTO_IMPORTANTE` auto-gerados (só `AVISTAMENTO_NPC`; outros entram com seus respectivos geradores)
  - Itinerantes / NPCs inter-bloco
  - StoryManager
  - Diálogo do jogador / acesso da KB via NPC
  - Sistema de Afinidade / Relacionamentos NPC↔NPC
  - Inferência de rotina (`ROTINA_NPC` como tipo derivado)
  - Compartilhamento de `SeenCount` via fofoca (dec. 3.9 do refinamento)
  - Persistência da KB entre reinícios
  - Traits que modificam expiração / decay
  - Separação visto/conhecimento como duas estruturas
- Critérios de aceite resumidos:
  - [ ] Servidor sobe com `knowledge_config.json` válido; falha com mensagem clara se inválido
  - [ ] Após 1 dia de jogo: Tomas e Naila têm entries um sobre o outro (no mínimo via almoço/jantar na taverna); re-encontros incrementam `SeenCount` sem duplicar
  - [ ] Fofoca propaga entries respeitando cooldown e anti-loop (`Source != receptor`)
  - [ ] Sweep remove expiradas por `LearnedAt`; `Important=true` sobrevive
  - [ ] Admin: `admin_inject_knowledge` strict, `admin_get_npc_knowledge` retorna entries ativas
  - [ ] `go build` e `go vet` limpos
```

> Adicionar item ao backlog de auditoria de GDD (`gdd/99_Meta_e_Backlog/` ou onde vivem os itens de revisão de GDD):

```markdown
- [ ] **Auditoria GDD — Capítulos 5.3, 5.4 e 8.3 (KnowledgeBase / Fofoca)** —
  Inconsistências detectadas durante refinamento da 1.5:
  - §5.3 fala em "+1 ponto de conhecimento mútuo" (modelo legado, não tipado); §8.3 define struct tipada. Atualizar §5.3 ou remover referência.
  - §5.4 lista "Locais" como tipo de conhecimento; §8.3 só tem 4 tipos. Decidir se "Locais" entra como 5° tipo no §8.3 ou se a menção em §5.4 é removida.
  - §8.3 promete distinção "vi pessoalmente" vs "ouvi falar" no acesso do jogador, mas o schema do GDD não tem campo `Source`. Implementação 1.5 adicionou. Atualizar schema do §8.3 para refletir.
  - §8.3 menciona `ROTINA_NPC` como tipo populado por avistamento; implementação 1.5 usa `AVISTAMENTO_NPC` (avistamento bruto) e deixa `ROTINA_NPC` como tipo derivado/inferido pra fase futura. Atualizar §8.3 com essa distinção.
  AC: §5.3, §5.4 e §8.3 alinhados; schema do §8.3 atualizado com `Source`, `FirstSeenAt`/`LastSeenAt`/`SeenCount`, `LearnedAt`, `Important`.
```

---

## Resumo das mudanças

**Arquivos a criar:**
- `docs/product/refinements/1.5-fofoca-knowledgebase.md` (refinamento completo acima)

**Arquivos a editar:**
- `docs/backlog.md` — substituir entrada `### 1.5 — Fofoca` pelo bloco novo
- `gdd/99_Meta_e_Backlog/BACKLOG.md` (ou arquivo de auditoria equivalente) — adicionar item de auditoria

Posso criar os dois arquivos no `/home/claude` e te entregar via `present_files` se quiser ter como artefato pronto pra copiar pro repo. Quer assim, ou prefere copiar direto da conversa?

Antes disso, dá uma lida no refinamento e me responde:

1. Algum critério de aceite que precise ser mais concreto?
2. Algum cenário que falta ou está descrito de forma confusa?
3. A ordem de execução em 8.4 faz sentido pra você ou tem dependências invertidas?
4. Quer reorganizar alguma seção ou está bom assim?

---

## Sidinei:

Quando falei em dividir queis dizer a tarefa, dividimos a tarefa 1.5 em 2, por causa das coisas que ainda não tinha, em um outro chat foi dito assim: 

Resumindo pro próximo chat:

1. 1.4 está OK pra fechar (com cosmética de chaves de log opcional)
2. 1.5 honesta = fofoca social entre os 3 residentes + comando admin de injeção pra testar variedade
3. Itinerantes (Opção B) e StoryManager (Opção C) ficam adiados conscientemente, com débito documentado


Por isso eu falei de ter dividido, se o que você mandou esta totalmente de acordo com isso, quero que crie os 2 arquivos, em /home/claude para me entregar via present_files. 
Se não reveja e crie pensando nisso. Porque quero saber o que vai vim depois dele, e como ficaria as fases.

---

## Claude:

Entendido. Sim, meu refinamento está **totalmente alinhado** com "1.5 honesta = fofoca social entre os 3 residentes + admin_inject":

- Único tipo automático: `AVISTAMENTO_NPC` (residentes vendo residentes) ✅
- Admin pode injetar entries pra testar variedade ✅
- Itinerantes listados em "NÃO entra" + mencionados em "DESTRAVA" como 1.6+ ✅
- StoryManager listado em "NÃO entra" + Important via admin_inject simula até existir ✅
- Outros tipos de Knowledge (LOCAL, RECURSO, ENTIDADE) também em "NÃO entra" ✅

Vou criar os arquivos e incluir uma proposta de reorganização das próximas tarefas (1.6+) baseada no que foi adiado. Você decide se aceita a reorganização.

Entregues. Resumo do que tem em cada um:

**`1.5-fofoca-knowledgebase.md`** — refinamento completo seguindo o template do projeto. 10 seções, 16 decisões registradas, 8 cenários concretos de admin_inject pra validação, invariantes e edge cases explícitos. Pra salvar em `docs/product/refinements/`.

**`backlog-patch-1.5.md`** — três coisas:

1. **Substituição da entrada 1.5** no `docs/backlog.md` com o escopo refinado
2. **Proposta de reorganização das próximas tarefas** — quatro propostas separadas que você decide caso a caso:
   - Renumerar a 1.6 atual (Ferramentas de dev) pra abrir 1.6 = Itinerantes
   - Adicionar 1.6 = Itinerantes com rascunho de escopo
   - StoryManager fora da Fase 1 (Fase 3 ou 2.5)
   - Ajuste cosmético da intro da Fase 1
3. **Item de auditoria do GDD** pra adicionar no backlog de auditoria

---

Três decisões pendentes que ficaram no patch (seção 4) e preciso da sua resposta pra fechar de fato:

1. **Renumera a 1.6 atual pra abrir Itinerantes?** Hoje 1.6 = ferramentas dev/admin, que é polish fraco. Proposta: 1.6 = Itinerantes, 1.8 (ou seção sem número) = ferramentas. Aceita, recusa, ou propõe outra organização?

2. **Onde StoryManager mora no roadmap?** Sugeri Fase 3 ou criar Fase 2.5. Você pode também simplesmente deixar em "Fase 4+ — Futuro" até decidir. Não tem urgência — só precisa decidir antes de fechar a 1.5 pra deixar registrado pra onde foi.

3. **Quer rascunho da 1.6 (Itinerantes) agora ou só depois de fechar a 1.5?** Eu recomendaria **depois**: implementar a 1.5, observar o comportamento real da KB com os 3 residentes, e só então refinar Itinerantes com aprendizado de campo. Refinar tudo agora é planejamento especulativo — e o argumento "deixa o sistema rodar antes de adicionar próxima camada" foi exatamente o que justificou separar a 1.5 honesta em primeiro lugar.

Manda as 3 respostas e fecho qualquer ajuste final dos arquivos.

---

## Sidinei:

Certo ja fiz algumas coisas, vamos a um checkpoint, veja o log ao roda agora, vou fazer upload dos arquivos que mexi aqui, porque ainda esta na branch da tarefa.

[Anexo:  (91394 bytes)]

[Anexo: npc.go (5838 bytes)]

[Anexo: knowledge.go (1049 bytes)]

[Anexo: knowledge_config.go (3451 bytes)]

[Anexo: manager.go (5863 bytes)]

[Anexo: knowledge_config.json (198 bytes)]

[Anexo: log.go (2586 bytes)]

[Anexo: backlog.md (11253 bytes)]

[Arquivo anexado: 1.5-fofoca-knowledge-base.md]

---

## Claude:

Checkpoint analisado. Vou direto aos pontos.

## Estado do escopo

Do checklist do refinamento (seção 4):

| Item | Status |
|------|--------|
| 4.1 — Struct + enum | ✅ feito |
| 4.2 — KB + LastGossipedWith + addOrUpdate + getKnowledge | ⚠️ parcial (com bugs) |
| 4.3 — Config loader | ⚠️ funciona mas tem cheiros |
| 4.4 — Auto-geração no ProcessTick | ⚠️ funciona com bug crítico |
| 4.5 — Sweep de expiração | ⚠️ funciona "no nada" — não expira porque está bugado |
| 4.6 — Fofoca | ❌ NÃO implementada (campo `LastGossipedWith` existe mas nunca é usado) |
| 4.7 — `GetActiveKnowledge` (lazy) | ❌ |
| 4.8 — FIFO de tamanho | ❌ |
| 4.9 — Snapshot com KB | ❌ |
| 4.10 — Comandos admin | ❌ |
| 4.11 — Log configurável | ✅ feito |

Então é ~5 de 11 entradas, com 4 das 5 contendo bugs. O coração da 1.5 (fofoca) ainda não saiu.

---

## Bug crítico #1: `time.Now()` em vez de `gameTime`

Isso é o que está fazendo o sweep nunca expirar nada no log.

**`knowledge.go`:**
```go
func NewKnowledgeAvistamentoNPC(...) Knowledge {
    now := time.Now()  // ← tempo real
    return Knowledge{
        FirstSeenAt: now,
        LastSeenAt:  now,
        LearnedAt:   now,
        ...
    }
}
```

**`npc.go`:**
```go
npc.KnowledgeBase[i].LastSeenAt = time.Now()  // ← tempo real
```

E o sweep compara contra `gameTime`:
```go
hasExpired := gameTime.Sub(k.LastSeenAt) > time.Duration(expiration)*time.Hour
```

`gameTime` começa em `1500-01-01 06:00:00`. `time.Now()` é 2026. `gameTime.Sub(time.Now())` dá ~ -526 anos (negativo gigante). Nunca é > 1h. Sweep nunca remove nada.

No log dá pra ver isso explícito:
```
LastSeenAt = 2026-05-13 00:01:43 (time.Now)
gameTime   = começou em 1500-01-01 06:00 e avança +1h por tick
has_expired = false (sempre)
```

**Fix:** propagar `gameTime time.Time` como parâmetro para todos os métodos de Knowledge no NPC, e para o constructor.

Sugestão de assinatura:
```go
func NewKnowledgeAvistamentoNPC(entityId, blockId, poiId, source string, gameTime time.Time) Knowledge

func (npc *Npc) addOrUpdateKnowledge(newKnowledge Knowledge, gameTime time.Time)
```

E no `manager.go`:
```go
for _, otherNpc := range npcsInZone {
    knowledge := NewKnowledgeAvistamentoNPC(
        otherNpc.Id, otherNpc.CurrentBlock, otherNpc.CurrentPoi, "direct",
        gameTime.Time,  // ← passa o gameTime
    )
    npc.addOrUpdateKnowledge(knowledge, gameTime.Time)
}
```

Isso é a correção mais importante e bloqueia validar o resto.

---

## Bug crítico #2: iteração da slice durante mutação

`removeExpiredKnowledge`:
```go
for _, k := range npc.KnowledgeBase {
    // ...
    if hasExpired {
        npc.removeKnowledge(k)  // ← reescreve npc.KnowledgeBase inteira
    }
}
```

`removeKnowledge` faz `npc.KnowledgeBase = updatedKnowledgeBase` (slice nova). O `range` em Go captura o slice header no início do loop, então:

1. Não há panic
2. Mas se 3 entries são removidas, são 3 reconstruções O(N) da slice — desperdício total
3. E após cada `removeKnowledge`, o loop continua iterando sobre a slice **antiga** (a cópia capturada), então pode chamar `removeKnowledge` de novo numa entry que já não existe (ineficiente, e o segundo `removeKnowledge` apenas reconstrói a slice sem encontrar o item)

Não é incorrecto, mas é feio e O(N²) pior caso.

**Fix idiomático:**
```go
func (npc *Npc) removeExpiredKnowledge(gameTime time.Time, expirationHours map[KnowledgeType]int) {
    filtered := make([]Knowledge, 0, len(npc.KnowledgeBase))
    for _, k := range npc.KnowledgeBase {
        expiration, exists := expirationHours[k.Type]
        if !exists {
            slog.Warn("Sem config de expiração", "knowledge_type", k.Type)
            filtered = append(filtered, k) // preserva (não sei se devia, decisão)
            continue
        }
        expired := gameTime.Sub(k.LastSeenAt) > time.Duration(expiration)*time.Hour && !k.Important
        if expired {
            if config.Log.NPCKnowledge {
                slog.Debug("Conhecimento expirado removido", "npc_id", npc.Id, "knowledge", k)
            }
            continue
        }
        filtered = append(filtered, k)
    }
    npc.KnowledgeBase = filtered
}
```

Uma passada, O(N), e `removeKnowledge` deixa de ser necessário (pode deletar).

---

## Decisão a revisitar: `LastSeenAt` ou `LearnedAt` para expiração?

No refinamento (seção 4.5) eu escrevi:
> "Remove entries com `gameTime.Time.Sub(learnedAt) > expirationDuration[type]`"

No código você usou `LastSeenAt`:
```go
hasExpired := gameTime.Sub(k.LastSeenAt) > time.Duration(expiration)*time.Hour && k.Important == false
```

**Pensando de novo, acho que você está certo e o refinamento estava errado.** Veja:

- **Contra `LearnedAt`**: entry expira X horas depois do primeiro contato, independente de re-encontros. Resultado: Tomas vê Naila 50 vezes em 2 dias, mas no terceiro dia a memória dela some mesmo continuando a ver ela todo dia. Não faz sentido narrativo.
- **A favor de `LastSeenAt`**: entry expira X horas depois do último contato. Tomas vê Naila todo dia → sempre lembra dela. Para de ver por X horas → esquece. **Semântica humana correta.**

A diferença só importa pra entries que não são re-vistas. Pra avistamentos diretos com re-encontros frequentes, ambos sobrevivem. A diferença prática é em entries adquiridas via fofoca (que nunca atualizam `LastSeenAt` na implementação atual, porque fofoca não existe ainda).

Quando a fofoca for implementada, decisão importante:
- Receptor de fofoca: `LastSeenAt = X` (do emissor) ou `LastSeenAt = gameTime` (renovação)?
- Se renovação, info passada propaga eternamente entre 3 NPCs em ciclo.
- Se preservada do emissor, info "envelhece" mesmo passando.

**Recomendação revisada:**
- Manter `LastSeenAt` como critério de expiração (como você fez)
- Atualizar refinamento (decisão 4.5 e P7 da seção 3 estavam imprecisas)
- No futuro da fofoca: receptor copia `LastSeenAt` do emissor (preserva idade da info) **MAS** seta `LearnedAt = gameTime` (pra saber quando soube)

Confirma essa virada? Se aceitar, ajusto o refinamento depois.

---

## Bugs menores / cheirinhos

### 1. `knowledge_config.go` usa `os.Exit(1)` em vez de retornar erro

```go
if config.GossipCooldownHours <= 0 {
    slog.Error("Valor inválido para gossipCooldownHours", "value", config.GossipCooldownHours)
    os.Exit(1)
}
```

Mas a função já assina `(KnowledgeConfig, error)` e o `NewManager` já trata erro. Inconsistência. Use `return KnowledgeConfig{}, fmt.Errorf("gossipCooldownHours inválido: %d", config.GossipCooldownHours)` — mais testável, comportamento mais previsível, segue convenção do projeto.

### 2. Validação faltando: tipos no ExpirationHours

Se o JSON vier com `expirationHours.FOO=24`, passa. Decisão 3.14 dizia "strict validation". Adicione algo como:
```go
validTypes := map[KnowledgeType]bool{KnowledgeAvistamentoNPC: true}
for kt := range config.ExpirationHours {
    if !validTypes[kt] {
        return KnowledgeConfig{}, fmt.Errorf("tipo de knowledge inválido em expirationHours: %s", kt)
    }
}
```

E também valide que `AVISTAMENTO_NPC` está presente (senão sweep loga Warn em todas e nada expira).

### 3. `k.Important == false` em vez de `!k.Important`

Estilo. Go convencional usa negação direta.

### 4. Log de sweep dispara para TODA entry todo tick

```go
if config.Log.NPCKnowledge {
    slog.Debug("Verificando expiração de conhecimento", ...)
}
```

No log: ~15 linhas por segundo só de "verificando". Quando rodar 1 dia (24 ticks), são 360 linhas. Sugiro logar só quando há ação (entry removida) ou comportamento interessante (entry vai expirar em breve). Considere remover esse log específico — basta o "Conhecimento expirado removido".

### 5. `knowledge_config.json` com `expirationHours.AVISTAMENTO_NPC=1`

1 hora de jogo = 1 tick em dev. Muito agressivo para observar comportamento. O refinamento previa 48h. Aceito que você esteja testando com valor curto pra forçar expiração rápida, mas com o bug do time.Now() esse valor ainda não importa.

Quando o bug crítico #1 for resolvido, recomendo testar primeiro com `48` (valor real previsto) e só baixar pra forçar cenários específicos.

### 6. Backlog tem inconsistência

```markdown
### 1.2 — Blocos e Zonas **PRÓXIMO**
### 1.5 — Fofoca / KnowledgeBase **PRÓXIMO**
```

Duas tarefas marcadas como "**PRÓXIMO**". 1.2 já está com todos os itens marcados `[x]`. Tira o `**PRÓXIMO**` do 1.2.

### 7. NPCSchedule + outros logs declarados mas alguns nunca usados aqui

`config.Log.WorldLoading` — não vi uso no manager. Não é problema desta tarefa, só anotando se você quiser fazer uma faxina geral depois.

---

## Pontos positivos (curtos)

- Schema da struct está fiel ao refinamento
- Dedup funcionando — log mostra `SeenCount` indo de 1→2→3→4→5 corretamente
- Granularidade `(Block, Poi)` separando entries direito (Naila em outdoor, taverna e mercado = 3 entries pra Tomas)
- Ordem sweep → auto-gen no ProcessTick está como o refinamento previu

---

## Ordem recomendada para continuar

Antes de mais qualquer coisa nova:

1. **Fix bug #1** (gameTime everywhere) — sem isso, nada do que vier depois tem comportamento validável
2. **Fix bug #2** (iteração da slice no sweep) — ao mesmo tempo é trivial
3. **Voltar `expirationHours` para 48** e rodar 1 dia (24 ticks) confirmando: entries antigas que não são re-vistas (ex: a entry com `PoiId=""` que o Tomas tem da Naila) eventualmente expiram, e entries com re-encontros sobrevivem

Aí sim, prosseguir com o escopo:

4. **4.7 — `GetActiveKnowledge`** (lazy) — fácil, depende do gameTime já estar correto
5. **4.8 — FIFO de tamanho** — fácil, depende de teste com admin_inject mais tarde
6. **4.10 — Comandos admin** (`admin_inject_knowledge`, `admin_get_npc_knowledge`) — necessário **antes** da fofoca pra você ter como popular cenários de teste e inspecionar
7. **4.6 — Fofoca** — coração da 1.5, o mais complexo, depende de tudo acima
8. **4.9 — Snapshot com KB** — pode ser feito junto com 4.10 (snapshot precisa servir o admin_get_npc_knowledge)

Conscientemente coloquei 4.10 antes de 4.6 porque sem admin_inject você não consegue testar fofoca direito (cenário 3 do refinamento depende de admin_inject pra produzir variedade).

---

Quer que eu detalhe o fix de algum bug específico em mais profundidade, ou esses apontamentos são suficientes pra você implementar?

---

## Sidinei:

Vamos a outro checkin veja se corrigir os pontos mencionados e se esta pronto para ir para o 4.7

[Anexo: backlog.md (11253 bytes)]

[Anexo: admin_router.go (7280 bytes)]

[Anexo: log.go (2586 bytes)]

[Anexo: knowledge_config.json (198 bytes)]

[Anexo: helpers.go (797 bytes)]

[Anexo: knowledge.go (1066 bytes)]

[Anexo: knowledge_config.go (3793 bytes)]

[Anexo: manager.go (7040 bytes)]

[Anexo: npc.go (8428 bytes)]

[Arquivo anexado: 1.5-fofoca-knowledge-base.md]

---

## Claude:

Checkpoint analisado. Antes do veredito, dois bugs sérios que vão te morder em runtime, e cinco coisinhas menores.

---

## Bug crítico #1: tickGossip itera com KB mutada e processa cooldown errado

```go
func (m *Manager) tickGossip(gameTime world.GameTime, npcsInZoneByNPC map[string][]*Npc) {
    processedPairs := make(map[string]struct{})
    for _, npc := range m.npcs {
        for _, otherNpc := range npcsInZoneByNPC[npc.Id] {
            ...
            lastGossipTime, hasGossiped := npc.LastGossipedWith[otherNpc.Id]
            if hasGossiped {
                cooldownDuration := time.Duration(m.knowledgeConfig.GossipCooldownHours) * time.Hour
                if gameTime.Time.Sub(lastGossipTime) < cooldownDuration {
                    continue
                }
            }
            ...
```

Você checa cooldown só de um lado: `npc.LastGossipedWith[otherNpc.Id]`. O lado dual (`otherNpc.LastGossipedWith[npc.Id]`) só é gravado em `exchangeKnowledgeWith`. **Em condições normais essas duas entradas vão sempre estar sincronizadas**, porque sempre são gravadas juntas — então essa simetria está OK na prática.

**Mas há um problema mais sutil:** `processedPairs` está dentro da função, mas o loop externo é `for _, npc := range m.npcs`. Quando você itera Tomas e olha pra Naila, marca o par. Quando depois itera Naila e olha pra Tomas, pula. Bom. Mas isso significa que o par **só é processado a partir do NPC que aparece primeiro no slice `m.npcs`**. Isso é uma decisão silenciosa de ordering — quem fala primeiro? O ferreiro Tomas (porque vem primeiro em `npcs.json`?). Em prática a função `exchangeKnowledgeWith` é bidirecional, então a ordem não muda nada. OK.

**O problema real:** `tickGossip` é executada **depois** de `tickNpcKnowledge` ter rodado em todos os NPCs. Significa que quando a fofoca acontece, as entries `AVISTAMENTO_NPC` criadas **neste mesmo tick** já estão na KB de todos. Tomas vê Naila no mercado nesse tick → cria entry "vi Naila no mercado" → fofoca dispara → Tomas passa pra Naila a entry "vi Naila no mercado". **Naila recebe fofoca sobre si mesma.**

Sua função `eligibleKnowledgeForGossip` já filtra `EntityId != receptorId`, então **não é um bug de propagação** — Naila não vai criar entry sobre si. **Mas é desperdício e ruído**: a candidate list inclui essa entry, ela é potencialmente selecionada na amostragem aleatória, e aí descartada na recepção. Resultado: às vezes a fofoca "trocou" 0 entries efetivas mesmo `exchangeKnowledgeWith` retornando `true` (porque sua função só retorna `false` se ambos os lados produziram lista vazia).

**Mais grave:** quando isso acontece, `LastGossipedWith` ainda é gravado. Cooldown ativa pra um par que efetivamente não trocou nada. Inverte a semântica do refinamento, que dizia "cooldown não atualiza se não houve troca real" (decisão 3.6 e edge case da seção 7).

**Fix:** ou `eligibleKnowledgeForGossip` é chamada **antes** de `tickNpcKnowledge`, ou você filtra `EntityId == receptor.Id || EntityId == emissor.Id` na elegibilidade (defesa em profundidade), ou faz o gating de "fofoca efetiva" baseado em entries que **de fato** entraram na KB do receptor — não na lista escolhida.

A solução mais limpa é a segunda: adicionar `k.EntityId != npc.Id` em `eligibleKnowledgeForGossip`:

```go
func (npc *Npc) eligibleKnowledgeForGossip(receptorId string) []Knowledge {
    eligible := make([]Knowledge, 0, len(npc.KnowledgeBase))
    for _, k := range npc.KnowledgeBase {
        // Filtra: entries sobre receptor, entries vindas do receptor, e entries sobre o próprio emissor
        if k.EntityId == receptorId || k.Source == receptorId || k.EntityId == npc.Id {
            continue
        }
        eligible = append(eligible, k)
    }
    return eligible
}
```

A terceira (`k.EntityId == npc.Id`) tecnicamente é redundante porque o auto-gerador nunca cria essa entry — mas vale como invariante explícita.

---

## Bug crítico #2: `mergeGossipedKnowledge` busca a entry duas vezes

```go
func mergeGossipedKnowledge(receptor *Npc, source *Npc, knowledge Knowledge, gameTime time.Time) {
    if existingK, found := receptor.getKnowledge(...); found {
        if knowledge.LastSeenAt.After(existingK.LastSeenAt) {
            for i, k := range receptor.KnowledgeBase {  // ← LOOP ADICIONAL
                if k.Type == knowledge.Type && ... {
                    receptor.KnowledgeBase[i].LastSeenAt = knowledge.LastSeenAt
                    ...
```

Você chama `getKnowledge` (O(N)) e depois faz outro loop O(N) pra achar o índice. Dois loops onde um basta. `getKnowledge` retorna a entry por valor, não por índice — design da função força esse refazer.

Não é bug de correctness, mas é O(2N) onde poderia ser O(N). Não vai matar com 3 NPCs e KB de 10 entries; vai começar a doer quando KB encher.

**Sugestão:** adicione um método helper `findKnowledgeIndex` que retorna `(int, bool)`, e use ele aqui. Ou aceite a duplicação por enquanto e anota como dívida (faz sentido com a fase). Mas decida conscientemente.

---

## Bug menor #1: `LastSeenAt` propagado via fofoca pode regredir

Em `mergeGossipedKnowledge`:

```go
if knowledge.LastSeenAt.After(existingK.LastSeenAt) {
    // atualiza
}
```

Considere o cenário:
- Tomas vê Naila no mercado dia 1 hora 12 → entry com `LastSeenAt = dia1-12h`
- Tomas vê Naila no mercado dia 1 hora 13 → mesma entry, `LastSeenAt = dia1-13h`, `SeenCount=2`
- Tomas conta pro Ricardo dia 1 hora 14
- Ricardo recebe entry com `LastSeenAt = dia1-13h`, `LearnedAt = dia1-14h`
- Tomas conta pro Ricardo **de novo** dia 2 hora 10 (a entry de Tomas está com `LastSeenAt = dia1-13h` ainda — ele não viu mais a Naila no mercado)
- `knowledge.LastSeenAt (dia1-13h)` não é `After(existingK.LastSeenAt (dia1-13h))` → não faz nada

OK, isso está correto. Mas se Ricardo tivesse visto Naila pessoalmente dia 2 hora 9 → `LastSeenAt = dia2-9h` na entry dele. Tomas conta dia 2 hora 10 com `LastSeenAt = dia1-13h`. Não atualiza. **Correto** — Ricardo tem info mais nova.

Isso está bem. Só anotando pra você confirmar que o comportamento bate com o que quer.

**Pergunta de design real:** quando fofoca atualiza só `LastSeenAt`, o `LearnedAt` não muda. Está certo? Sim, no schema do refinamento `LearnedAt` é "quando este NPC soube pela primeira vez" — atualizar só na recepção inicial faz sentido. Confirmado.

---

## Bug menor #2: `pickRandomKnowledge` usa `rand` global sem seed

`rand.Perm(len(entries))` e `rand.Intn(...)` usam o gerador global. Em Go 1.20+ ele é auto-seeded com tempo, então não é o problema de "sempre mesma sequência". Mas:

1. Não é determinístico → testes ficam flaky se você quiser reproduzir
2. Para concorrência futura (vários ticks paralelos, ou seu admin injetando enquanto tick roda) o `rand` global tem mutex interno, mas é simples evitar

Por ora **deixa como está**. Quando for escrever testes reproduzíveis, troca por `rand.New(rand.NewSource(seed))` exposto via dependency injection. Tarefa de polish.

---

## Bug menor #3: `knowledge_config.go` ainda usa `err` solto em `return KnowledgeConfig{}, err`

Você trocou os `os.Exit(1)` por `return`, ótimo. Mas o erro retornado é a variável `err` que vem do `os.ReadFile` ou do `json.Unmarshal` — **ela é `nil` nesse ponto** porque foi consumida pelos retornos anteriores.

Exemplo:

```go
if config.GossipCooldownHours <= 0 {
    slog.Error(...)
    return KnowledgeConfig{}, err  // ← err é nil aqui!
}
```

Caller recebe `KnowledgeConfig{}` e `error == nil`. **Caller acha que deu certo e usa config zerada.** Servidor sobe com `gossipCooldownHours=0` e o sistema gossip vira flood.

**Fix:** retornar `fmt.Errorf(...)` como você já fez no `validTypes`:

```go
if config.GossipCooldownHours <= 0 {
    return KnowledgeConfig{}, fmt.Errorf("gossipCooldownHours inválido: %d", config.GossipCooldownHours)
}
```

Aplicar em todos os 5 lugares (`GossipCooldownHours`, `MaxKnowledgeBaseSize`, `GossipMinExchangePerEvent`, `GossipMaxExchangePerEvent`, e o loop de `expirationHours`).

E também: você não valida se `GossipMaxExchangePerEvent >= GossipMinExchangePerEvent`. Se o JSON vier com `min=5, max=2`, o `pickRandomKnowledge` força `maxCount = minCount` no defensivo, mas é melhor falhar na carga com erro claro.

---

## Bug menor #4: tickGossip não respeita o gate "1 troca por par por tick"

A documentação do refinamento (decisão 3.6 + seção 4.6) diz "troca rolada uma vez por par por tick (não duplicar)". Você fez isso via `processedPairs`. Bom.

Mas `cooldownDuration` em **horas de jogo** versus tick em **dev acelerado** (1 tick = 1h jogo). Cooldown=6 → fofoca de Tomas-Naila a cada 6 ticks. Em dev rodando rápido (24s reais = 1 dia jogo = 24 ticks = 4 fofocas potenciais por dia entre o mesmo par). É o comportamento desejado pra observar variedade.

**Não é bug. Está OK.** Só registro pra você prever no teste: cooldown e expiração rodam em horas de jogo. Em dev a 1h/s, você verá ~10 ticks/min reais. Para validar cooldown, basta deixar rodar ~6s reais entre encontros.

---

## Bug menor #5: arquivos `1_5-fofoca-knowledge-base.md` e `backlog.md` não foram alterados

O upload menciona esses dois arquivos como modificados, mas comparei com a versão que entreguei do refinamento e o conteúdo aparenta ser idêntico. O backlog também não tem nenhuma marcação dos itens já implementados.

**Sugestão:** marcar `[x]` nos itens entregues da 1.5 no backlog mantém honestidade:
- Struct Knowledge ✅
- KnowledgeBase + LastGossipedWith ✅
- knowledge_config.json ✅
- Auto-geração ✅
- Fofoca ✅
- Expiração (lazy ainda não — só sweep) ⚠️
- FIFO ❌
- Snapshot com KB ❌
- Comandos admin ❌
- Flag log NPCKnowledge ✅

---

## Resposta direta: pronto pra 4.7?

**Não. Faltam dois fixes antes:**

1. **Filtro `EntityId == npc.Id` em `eligibleKnowledgeForGossip`** (bug crítico #1) — sem isso a fofoca "trocou nada" liga cooldown falsamente.
2. **`fmt.Errorf` no `knowledge_config.go`** (bug menor #3) — config inválida sobe servidor com defaults zerados silenciosamente.

Ambos são pequenos (5-10 linhas cada).

O bug crítico #2 (duplo loop em `mergeGossipedKnowledge`) é otimização — pode adiar com nota.

Os menores #2 e #4 são para depois. O #5 é organização do backlog.

---

## Pergunta de design antes de seguir para 4.7

`GetActiveKnowledge` (4.7) é "lazy expiration nos getters". Mas o sweep do início do tick já remove tudo expirado. Pergunta:

**Em que momento haveria entry expirada que o sweep não pegou?**

Resposta: só entre `tickNpcKnowledge` (que faz o sweep) e o próximo tick. Como `admin_get_npc_knowledge` (4.10) lê do snapshot, e o snapshot é gerado **depois** do tick, a KB no snapshot já está limpa.

**Conclusão:** lazy expiration nos getters em runtime é redundante com o sweep, **a menos** que você imagine uso direto (não-snapshot) de `GetActiveKnowledge` — tipo dentro do mesmo tick, entre `tickNpcKnowledge` e `tickNpcBehavior`, ou no diálogo futuro do jogador.

Para a 1.5, sugestão pragmática:
- **Implementa um getter público `GetKnowledgeBase()` que retorna cópia da slice** (necessário para snapshot)
- **NÃO implementa filtragem lazy nesse getter** — sweep cobre, e adicionar filtragem aqui mascara bugs de sweep
- Se você quiser proteção extra, faz um `GetActiveKnowledgeForDialog(gameTime, config)` separado, quando o diálogo chegar

O 4.7 conforme refinamento original (filtrar expirados no getter usado pelo admin) ainda faz sentido como defesa em profundidade, mas é pequena. Posso ir por esse caminho se você preferir.

**Qual prefere?**
A. 4.7 conforme refinamento (lazy filter no getter)
B. Pular 4.7 e ir direto pra 4.8 (FIFO) + 4.9 (snapshot) + 4.10 (admin), com getter simples sem filtro
C. Outro caminho

Faz os 2 fixes acima e responde isso, aí seguimos.

---
