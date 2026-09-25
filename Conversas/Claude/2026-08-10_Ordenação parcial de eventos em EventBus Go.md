## Sidinei:

Tenho um monólito em Go pra um MMORPG, usando goroutines + EventBus interno, com persistência RAM-first e SQLite como storage de fallback/snapshot. Meu problema: quando um evento de combate dispara múltiplos listeners (dano, XP, drop, achievements) de forma assíncrona, às vezes a ordem de aplicação importa (ex: morte precisa processar drop antes de resetar estado do NPC) mas não quero serializar tudo e perder o paralelismo. Que padrões de Go eu poderia usar pra garantir ordenação parcial só onde importa, sem virar um gargalo?

---

## Claude:

## Pontos fracos de cada abordagem primeiro, porque a escolha aqui é toda sobre trade-off:

**1. Actor-per-entity (mailbox pattern)**
Contras: precisa remapear seu EventBus atual pra rotear por chave (entity ID), não por tipo de evento; se um NPC vira hotspot (boss com muita interação), essa goroutine única vira gargalo local; overhead de gerenciar lifecycle de N goroutines (spawn/despawn com entidades entrando/saindo do mundo).

Ideia: cada NPC/entidade tem seu próprio `inbox chan Event`, consumido por uma única goroutine. Eventos pro mesmo NPC são sequenciais por construção (uma goroutine, uma instrução por vez); entidades diferentes processam em paralelo total. Ordem "drop antes de reset" fica garantida de graça, porque ambos rodam na mesma goroutine, sem lock nenhum.

```go
type EntityActor struct {
    inbox chan Event
}
func (a *EntityActor) run() {
    for ev := range a.inbox {
        a.handle(ev) // sequencial só dentro desta entidade
    }
}
```

**2. Tiers/fases com barreira (errgroup + WaitGroup)**
Contras: adiciona uma sincronização por evento (o barrier), então não é zero-custo; exige que você classifique antecipadamente cada listener em "crítico" vs "reativo", o que é trabalho de modelagem, não só código.

Ideia: listener ganha um campo `Priority`/`Phase`. O bus agrupa por fase e roda cada fase com `errgroup.Wait()` antes de liberar a próxima. Dentro da mesma fase, tudo roda concorrente. Custo de sincronização é proporcional ao número de fases (2-3), não ao número de listeners.

**3. Não usar o EventBus pra dependência causal — orquestrar diretamente**
Contras: quebra a uniformidade "tudo passa pelo bus", exige duas categorias de código (chamada direta vs evento publicado), pode ser visto como inconsistência arquitetural se a equipe crescer (mas você é solo, então isso pesa menos).

Ideia, que eu acho a mais direta pro seu caso: "drop antes de reset" não é um problema de ordenação de eventos, é uma dependência causal de domínio — modelar como pub-sub genérico é forçar a ferramenta errada. Trate `HandleDeath` como uma função/saga que chama `ResolveDrop()` depois `ResetNPCState()` sequencialmente (síncrono, dentro da própria goroutine do combate), e só *depois* disso publique `EntityDied{}` no EventBus para os listeners que são genuinamente independentes (XP, achievements, telemetria) — esses vão pra um worker pool sem ordem garantida nenhuma.

**4. Single-writer por agregado (princípio geral por trás de 1 e 3)**
O padrão comum: cada "dono" de estado (NPC, player) tem exatamente um consumidor sequencial daquele estado. Gargalo só aparece se você serializar entre agregados diferentes — o que você quer evitar é lock global no bus, não ordenação por chave.

**Onde normalmente mora o gargalo real:** se o seu EventBus atual usa um mutex/canal único pra despachar todos os eventos do jogo, a ordenação nem é o problema — é essa serialização acidental. Shardear por entity ID (opção 1) resolve os dois problemas ao mesmo tempo: ordenação onde importa e paralelismo real entre entidades que não interagem.

Faltam alguns dados que mudariam a escolha entre essas opções: quantas entidades simultâneas você espera por sessão de combate (poucas dezenas vs centenas), se listeners como "achievement" já tocam estado compartilhado entre players (o que criaria outra dependência causal escondida), e se seu EventBus já tem algum conceito de chave/roteamento ou é um pub-sub genérico por tipo de evento.

---
