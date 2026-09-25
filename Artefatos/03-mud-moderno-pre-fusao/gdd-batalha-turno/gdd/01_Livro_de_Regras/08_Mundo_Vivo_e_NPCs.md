# 🌍 Capítulo 8 – Mundo Vivo, NPCs e Servidor

Este capítulo é dedicado ao sistema de "Mundo Vivo", que é o **pilar central** do jogo. Ele detalha como o servidor simula o mundo, como os NPCs pensam, como o tempo afeta a simulação e como múltiplos jogadores coexistem no mesmo mundo persistente.

> **Nota sobre terminologia:** "Tick" neste documento refere-se ao ciclo interno do game loop no servidor (detalhe de implementação). Para o jogador, o tempo é medido em **tempo real** (segundos, minutos), pelo **relógio do jogo** (manhã, tarde, noite, madrugada) e por **turnos** (apenas em combate D20). 1 dia do jogo ≈ 2–4 horas reais.

---

## 8.1 – O Mundo Persistente

*Eras do Brasil* é um **mundo persistente online**. O servidor roda 24/7, simulando NPCs, economia, clima, facções e eventos — independentemente de haver jogadores conectados.

- **NPCs possuem rotinas, desejos, vínculos e conhecimento próprio.**
- **O mundo se move mesmo sem a presença dos jogadores.** Um novo jogador que entra pode encontrar o mundo em estado "Pós-Guerra", ouvindo apenas histórias sobre quem lutou na batalha.
- **Eventos acontecem em ciclos temporais do relógio do jogo, afetando regiões, recursos, mercados, facções e relações.**

Os três pilares do Mundo Vivo:
1.  **Simulação:** O servidor garante que o mundo viva e evolua continuamente.
2.  **Narrativa:** Eventos globais tecem histórias que emergem das ações coletivas dos jogadores.
3.  **Jogabilidade:** Desafios e recompensas se calibram dinamicamente pela economia e pela IA.

---

## 8.2 – Arquitetura do Tempo, Blocos e Ciclos

O mundo é construído sobre uma lógica de **Blocos de Cenário** (cap. 5.2) e regido por um **relógio do jogo** com ciclo dia/noite.

### O Relógio do Jogo
O servidor roda um game loop contínuo que avança o tempo do mundo independentemente das ações dos jogadores. O jogador experimenta o tempo de duas formas:

* **Tempo Real:** Durations de ações, prazos de quests e eventos são medidos em segundos/minutos reais.
* **Relógio do Jogo:** O mundo possui um ciclo dia/noite com 4 períodos — **Manhã, Tarde, Noite, Madrugada**. 1 dia do jogo ≈ 2–4 horas reais. NPCs seguem rotinas baseadas nesses períodos.

> **Nota técnica:** Internamente, o servidor processa o mundo em "ticks" (ciclos do game loop), mas esse detalhe não é exposto ao jogador. Toda comunicação usa tempo real ou o relógio do jogo.

```
// Game loop sequencial (detalhe interno)
GameLoop.ProcessarCiclo():
  TimeManager.AdvanceTime()
  NPCManager.AtualizarAgendas()
  QuestManager.VerificarPrazos()
  StoryManager.CheckScheduledEvents()
  PersistManager.SalvarDirty()
```

### Ciclos Temporais

- **Ciclos Diurnos:** Manhã → Tarde → Noite → Madrugada (4 períodos por dia do jogo).
- **Ciclos Semanais:** Feiras, rituais, migrações.
- **Ciclos Sazonais:** Estações que alteram recursos e clima.
- **Ciclos Espirituais:** Fases da lua, rupturas da Raiz.

A cada ciclo do servidor, o mundo atualiza:

- Movimentação de NPCs.
- Regeneração ou esgotamento de recursos.
- Ativação de eventos.
- Progresso de missões com prazo.
- Relações de facções e economia.

---

## 8.3 – O Sistema de IA de NPCs (Fusão de Modelos)

(Conteúdo fundido do original 8.3 e das novas regras de IA)

Os NPCs em *Eras do Brasil* são entidades vivas. O sistema é uma fusão de dois modelos: "Agendas" (rotinas fixas, como *Stardew Valley* ou *KCD*) e "Necessidades" (IA baseada em prioridades, como *Dwarf Fortress* ou *RimWorld*).

Cada NPC possui um `NPC_Data` com os seguintes componentes:

* **`Needs` (Necessidades):** Um conjunto de estatísticas que decaem periodicamente (ex: Fome, Sede, Energia/Sono, Social, Segurança).
* **`Traits` (Traços):** Modificadores passivos que afetam o decaimento das necessidades ou a tomada de decisão (ex: Gula, Preguiçoso, Ranzinza, Valente).
* **`Mood & Thoughts` (Humor e Memórias):** O Humor do NPC é o resultado direto de suas Necessidades não atendidas e de "Memórias" recentes (ex: "Comeu bem", "Foi insultado", "Amigo morreu").
* **`Agenda`:** A rotina de trabalho padrão do NPC baseada no relógio do jogo (ex: "Manhã — Ir para a Forja").

### O Fluxo de Decisão do NPC (Utility AI)

A cada ciclo do servidor, o cérebro de cada NPC roda o seguinte processo:

1.  **Fase 1 (Passivo):** Atualiza todas as `Needs` (Fome +1, Energia -1) e recalcula o `Humor` total.
2.  **Fase 2 (Decisão):** O NPC avalia todas as suas "Metas" (Trabalhar, Comer, Dormir, Socializar) e atribui uma prioridade a cada uma.
    * `Prioridade_Fome = npc.fome` (ex: 70)
    * `Prioridade_Trabalho = npc.agenda.GetPriority()` (ex: 50)
3.  **Fase 3 (Ação):** O NPC escolhe e executa a Ação que satisfaz a Meta de **maior prioridade**.
    * *Exemplo:* Se a `Prioridade_Fome` (70) for maior que a `Prioridade_Trabalho` (50), o Ferreiro "quebra" sua rotina de Agenda e decide ir à taverna para comer.

### Percepção Cognitiva (`knowledgeBase`)

Cada NPC possui uma "Base de Conhecimento" (`knowledgeBase`) onde armazena informações que *vê* durante suas rotinas:

* **Recursos:** Onde viu minérios ou ervas.
`{"type": "RECURSO", "id": "minerio_ferro_01", "location": "bloco_mina", "seenAt": "2024-01-15T10:30:00Z"}`
* **Monstros:** Onde viu perigos.
`{"type": "ENTIDADE", "id": "lobo_alfa", "location": "floresta_norte", "seenAt": "2024-01-15T08:00:00Z"}`
* **Rotinas:** Onde viu outros NPCs.
`{"type": "ROTINA_NPC", "id": "npc_guarda", "info": "Vai para a taverna ao meio-dia"}`
* As informações possuem um "prazo de validade" (baseado no timestamp) e são "esquecidas" após um tempo.

### Expiração e Esquecimento da Memória

O `NPCManager` varre periodicamente a `knowledgeBase` de cada NPC e **remove entradas expiradas**, garantindo que as informações sejam recentes e o mundo permaneça dinâmico.

* **Regra:** Uma entrada é removida quando `(currentTime - seenAt) > memoryLimit`.
* **Limite padrão sugerido:** ~2 dias de tempo do jogo.
* **Exceções:** Informações marcadas como "Importante" (ex: morte de um NPC, evento de ruptura) podem ter limite estendido ou ser permanentes.
* **Impacto:** Isso significa que um NPC não vai falar sobre um recurso que viu há 3 dias — a informação já expirou. O jogador precisa buscar fontes recentes.

### Relacionamentos (NPC <=> NPC) e "Fofoca"

NPCs rastreiam seu nível de amizade/inimizade com *outros NPCs* e com os jogadores.

Quando as rotinas de dois NPCs fazem com que eles se encontrem no mesmo bloco (ex: Ferreiro e Guarda na Taverna), o sistema de "Fofoca" é ativado, permitindo que troquem informações de sua `knowledgeBase`.

1.  Os NPCs trocam 1-2 itens de suas `knowledgeBase`.
2.  Eles atualizam seus `Relacionamentos` (ex: "Falar com o Ferreiro aumentou minha amizade com ele").

### Acesso do Jogador (Interação)

O jogador acessa essa rede de informação dinâmica ao conversar com o NPC. O que o NPC sabe (e se ele decide contar) depende de:

1.  **Afinidade:** O NPC gosta de você?
2.  **`knowledgeBase`:** O NPC *realmente viu* o que você está perguntando? (Ex: "Sim, eu vi minério de ferro na mina esta manhã.")
3.  **"Fofoca":** O NPC *ouviu falar* de outro NPC? (Ex: "Eu não vi, mas o Guarda me contou que viu lobos na floresta norte.").

---

## 8.4 – Facções, Influência e Progresso Global

(Conteúdo original do Cap 8.4 do `Livro de Regras.md`)

As **facções** representam grupos organizados que moldam a política, a espiritualidade, o comércio e os conflitos em *Eras do Brasil*. Cada facção possui **interesses, ideologias, territórios, NPCs afiliados e objetivos próprios**.

### 🏛️ O Que é uma Facção?
Uma facção é uma entidade social, cultural, espiritual, militar ou econômica composta por:
* NPCs organizados com funções, hierarquias e rotinas
* Crenças, objetivos e rivalidades
* Territórios ou áreas de influência
* Relações diplomáticas (amizade, rivalidade ou neutralidade)

### 🎯 Influência e Reputação com Facções
Cada jogador ou grupo possui uma **Reputação** com cada facção, que varia de:

| Nível de Reputação | Descrição                       | Efeito Prático                             |
|--------------------|----------------------------------|---------------------------------------------|
| 🟥 Inimigo          | Odiado, caçado, alvo            | NPCs atacam, bloqueiam acesso, emboscadas  |
| 🟧 Desfavorável     | Desconfiado, mal visto          | Preços mais altos, missões fechadas        |
| 🟨 Neutro           | Desconhecido ou irrelevante     | Acesso básico, sem benefícios ou punições  |
| 🟦 Respeitado       | Conhecido, prestigiado          | Descontos, acesso a missões ou rituais     |
| 🟩 Aliado           | Integrado, protegido, líder     | Acesso total a recursos, proteção e segredos |

As ações de um jogador podem **aumentar ou diminuir reputação** com uma ou mais facções ao mesmo tempo.

---

## 8.5 – Eventos Globais, Rumores e Ciclo do Mundo

(Conteúdo original do Cap 8.5 do `Livro de Regras.md`)

O mundo de *Eras do Brasil* não é estático. Ele pulsa, respira e reage a tudo que acontece.

### 🌪️ Eventos Globais
São acontecimentos que possuem **impacto coletivo e permanente (ou semi-permanente)** no mundo.

| Tipo de Evento        | Exemplos                                              |
|-----------------------|-------------------------------------------------------|
| Espirituais           | Ruptura de Véus, Enfraquecimento da Raiz, Eclipse Ancestral |
| Políticos/Sociais     | Queda de uma facção, fundação de uma vila, guerra civil |
| Ambientais            | Chegada de estação seca severa, praga mágica, floresta corrompida |

### 🌓 Ciclo do Mundo
O mundo de *Eras do Brasil* é regido por ciclos que afetam:
* Eventos espirituais
* Fauna e flora
* Presença de monstros
* Poder de magias, rituais e itens

---

## 8.6 – Companheiros e Personagens Secundários

(Conteúdo original do Cap 8.6 do `Livro de Regras.md`)

Os jogadores podem interagir com **companheiros, mercenários, aliados e personagens secundários**.

### 🤝 Companheiros e Seguidores
Jogadores podem recrutar **companheiros temporários ou permanentes**:

| Tipo             | Função                                  |
|------------------|-----------------------------------------|
| 🛡️ Mercenários    | Auxílio em combate, pagos por diária   |
| 🔥 Aliados de Facção | Suporte específico, bônus narrativos |
| 🧙 NPCs Rituais    | Ajudam em magias, rituais e cura       |
| 🐺 Criaturas      | Companheiros mágicos, animais ou espirituais |

#### 🎯 Regras Gerais para Companheiros
* **Ação em Combate:** Podem agir no combate, com ficha simplificada.
* **Requisitos:** Exigem pagamento, manutenção de afinidade ou cumprimento de missões.
* **Risco de Perda:** Podem ir embora se a afinidade cair muito ou se seus objetivos entrarem em conflito.

### ❤️ Sistema de Afinidade (Detalhado)
A "Afinidade" (relacionamento) que um NPC sente pelo jogador é uma mecânica central. Ela é modificada por ações diretas:

| Ação                                | Efeito na Afinidade |
|--------------------------------------|----------------------|
| Presentear com item valioso          | +2                   |
| Ajudar em missão                     | +1 a +3              |
| Faltar com compromisso               | –2                   |
| Ofender, mentir ou trair             | –3 ou mais           |
| Salvar em combate crítico            | +3                   |
| Pertencer à mesma facção             | +1 (Bônus passivo)   |

A afinidade gera:
* **Descontos** no comércio.
* **Acesso a informações exclusivas** (da `knowledgeBase` do NPC).
* **Ofertas de missões especiais**.
* **Apoio em combates ou rituais**.

### 🌳 Ciclo de Vida dos NPCs
NPCs não são eternos. Eles podem nascer, envelhecer e morrer (seja por eventos da história, ações do jogador ou causas naturais). A morte de um NPC importante é um **Evento Global** que pode gerar novas missões ou lacunas de poder.

---

## 8.7 – Arquitetura do Mundo Persistente (Online)

O game loop contínuo do servidor impulsiona todos os sistemas de simulação.

### StoryManager (O Calendário de Eventos do Mundo)

O `StoryManager` funciona como um "Calendário de Eventos do Mundo". A história principal, eventos sazonais e invasões de facções avançam com o relógio do jogo, não com o progresso de um jogador individual.

Um novo jogador que entra no servidor pode encontrar o mundo em um estado diferente do inicial — ouvindo apenas histórias sobre os jogadores que lutaram na batalha anterior.

**Branching de Timeline:**

```text
Dia 50 do jogo → Evento "Invasão" começa
  → NPCs em pânico, novos inimigos no mapa
  → Missão Mundial criada: "Derrote o Rei Goblin" (prazo: 7 dias reais)

Cenário A: Jogadores vencem no dia 3
  → StoryManager avança para "Era da Reconstrução"

Cenário B: Prazo expira sem resolução
  → StoryManager avança para "Era da Ocupação"
  → Mapa muda para todos
```

### Sistema de Missões Competitivas

Para se alinhar ao mundo persistente, as missões de NPCs seguem um modelo de **competição com verificação server-side**:

1. **Publicação:** Um NPC publica uma quest (ex: "Preciso de 10 Peles de Lobo").
2. **Múltiplos Aceites:** Vários jogadores podem aceitar a mesma missão.
3. **Progresso Verificado:** Todos os jogadores precisam completar o objetivo. O servidor verifica o progresso individualmente (anti-exploit).
4. **Primeiro a Entregar = Recompensa Total:** O primeiro jogador que retornar com os itens completos recebe a recompensa integral.
5. **Timeout de Entrega:** Após a primeira entrega, inicia-se um período de tempo (ex: 30 minutos reais) durante o qual outros jogadores que já completaram o objetivo podem entregar por **recompensa parcial** (ex: 50% do valor).
6. **Expiração:** Após o timeout, a missão expira. Jogadores que aceitaram mas não entregaram recebem "falha" no diário. O NPC informa: "O problema já foi resolvido."

> **Anti-exploit:** O servidor valida que o jogador realmente completou o objetivo (matou os mobs, coletou os itens, etc.) antes de aceitar a entrega. Não basta possuir os itens — o progresso da quest é rastreado server-side.

### Quadro de Missões (BountyManager) — Metas Coletivas

Sistema de contribuição comunitária onde jogadores contribuem individualmente para metas globais:

- Uma cidade precisa de 100 couros para construir uma muralha.
- Cada jogador contribui com até 10 couros.
- Ao atingir thresholds (25%, 50%, 75%, 100%), recompensas são liberadas para todos que contribuíram.
- Se o prazo expirar sem completar, a cidade sofre as consequências (invasão, escassez).

---

## 8.8 – Sistema de Temporadas e Eventos Globais

O mundo de *Eras do Brasil* é organizado em **temporadas** — arcos narrativos de longa duração (4-6 meses reais ou mais) que definem o estado do mundo, os eventos disponíveis e a progressão da história.

> **Nota:** O jogo é projeto de hobby do desenvolvedor. Cada temporada traz uma feature nova. Transparência com a comunidade sobre ritmo e escopo.

### State Machine de Evento de Temporada

Cada temporada segue uma state machine de 3 estados:

```text
PRE_EVENT (Tensão) → EVENT_ACTIVE (Apogeu) → POST_EVENT (Legado)
```

1. **`PRE_EVENT` — Tensão:** Sinais visuais no mundo, missões de preparação, NPCs comentam sobre o que está por vir. Duração: semanas reais.
2. **`EVENT_ACTIVE` — Apogeu:** O clímax da temporada. Jogadores contribuem coletivamente (kills, entregas de recursos, conclusão de missões). Resultado determinado por **threshold de contribuição coletiva** — sem simulação real-time de combate NPC vs NPC.
3. **`POST_EVENT` — Legado:** O mundo é transformado pela consequência (Vitória ou Derrota). NPCs contam o que aconteceu. Placas com nomes dos participantes são colocadas no mundo.

### Votação em Quests de História

Quests de história com escolhas narrativas usam **votação simples**: cada jogador vota com peso igual, vence a maioria. Balanceamento de peso por facção/guild é decisão futura.

### Decisão Coletiva

O desfecho é decidido pela ação (ou inação) da comunidade. Se os jogadores falharem em entregar suprimentos a tempo, a vila queima para todos na próxima temporada.

### Recompensas de Legado

- Jogadores recebem Títulos ("Veterano da Ruptura") que são reconhecidos por NPCs em futuras temporadas.
- Placas com nomes dos participantes são erguidas em locais relevantes.
- Estruturas construídas ou destruídas persistem no mundo.
- NPCs lembram e referenciam eventos passados em diálogos.

> **Feature futura (Temporada 3+):** *Ecos Instanciados* — jogadores que chegam depois de uma temporada poderão vivenciar conteúdo passado em modo instanciado (solo), com recompensas reduzidas. O servidor deve persistir estado de temporadas passadas desde o início para viabilizar isso.

---

## 8.9 – Sincronia de Tempo e Dinâmica Online

### Relógio do Jogo

O servidor roda um game loop contínuo:

- O **relógio do jogo** avança continuamente, mapeando tempo real para tempo do jogo (1 dia do jogo ≈ 2–4 horas reais).
- 4 períodos por dia: **Manhã → Tarde → Noite → Madrugada**.
- Isso garante que todos os jogadores conectados vejam o sol se pôr ou o Boss atacar ao mesmo tempo.
- NPCs seguem rotinas baseadas neste relógio.

### Turnos de Trabalho dos NPCs

Para evitar que NPCs "sumam" quando o jogador precisa deles, utilizamos **Turnos por Período**:

1. **Ciclo Dia/Noite:** O servidor roda um ciclo contínuo de 4 períodos.
2. **Turnos de NPC:**
    - **Manhã/Tarde:** O Mestre Ferreiro atende na Forja (Qualidade Alta).
    - **Noite:** O Mestre vai para a Taverna. O **Aprendiz** assume a Forja (Qualidade Normal, Estoque Reduzido).
    - **Resultado:** O serviço nunca fecha (evitando punição ao jogador casual), mas o mundo respira e os NPCs têm vida.

### Bolha de Combate

Quando um jogador entra em combate:

- O combate é resolvido em **turnos táticos D20** (Iniciativa), isolado do relógio do jogo.
- O mundo continua avançando ao redor — outros jogadores não são pausados.
- Ao final do combate, o tempo real decorrido é aplicado ao estado do jogador no mundo.

---

## 8.10 – Inimigos Evolutivos

> **ADR-009.** Substitui o antigo sistema de "Full Loot" (removido — ver ADR-010).

### Conceito

Inimigos no mundo de *Eras do Brasil* não são estáticos. Eles ganham experiência exclusivamente por **matar jogadores**, evoluindo em poder e categoria ao longo do tempo. Isso cria uma ecologia emergente onde a morte tem consequências narrativas e mecânicas.

### Regras (MVP)

1. **XP por Kill:** Quando um inimigo mata um jogador, ele ganha XP. A quantidade é fixa por tipo de inimigo.
2. **Nível e Categoria:** O nível do inimigo sobe com XP acumulado. A categoria é um label do range de nível:

| Categoria | Range de Nível | Comportamento |
|-----------|---------------|---------------|
| **Normal** | Nível mínimo do mapa | Comportamento padrão |
| **Veterano** | +25% do cap | Mais agressivo, loot melhor |
| **Alfa** | +50% do cap | Lidera grupos, habilidades especiais |
| **Lenda** | Cap do mapa | Nome único, evento de caça |

3. **Spawn e Nascimento:** Inimigos sempre nascem no nível mínimo do mapa onde spawnam (categoria Normal).
4. **Migração:** Ao atingir o cap de nível do mapa, o inimigo migra para a próxima região como Normal (reset de categoria, mantém XP). Um novo inimigo spawna na região original com cooldown.

> O fluxo de migração entre regiões segue o gradiente geográfico definido na [Arquitetura do Mapa](05B_Arquitetura_do_Mapa.md): Mata Costeira → Sertão Distorcido → Serra dos Ecos → Pantanal Vivo → Coração da Raiz.
5. **Cap de População:** Cada região tem um limite máximo de inimigos para evitar superpopulação.
6. **Cap de Endgame:** Nível máximo de um inimigo = nível máximo do jogador + margem pequena.
7. **Rate Limiting:** Um inimigo só ganha XP de morte de jogador a cada N minutos (anti-farming de XP de mob).
8. **Proteção de Quest:** Inimigos que são **target de uma quest ativa** de algum jogador NÃO evoluem nem migram enquanto a quest estiver ativa.

### Integração com Fofoca

Quando um inimigo evolui de categoria, o servidor dispara `OnMobEvolved`. NPCs que "presenciam" ou "ouvem sobre" o evento adicionam a informação à sua `knowledgeBase` e espalham via sistema de Fofoca:

- *"Cuidado com o lobo na Floresta Norte — dizem que já matou três aventureiros. Chamam ele de 'Sombra Cinzenta'."*

> **Feature futura (Temporada 2+):** Categoria separada de nível, quests emergentes de caça, Fofoca profunda, visual dinâmico por categoria. Ver ADR-009.

---

## 8.11 – Arquitetura do Motor (Managers)

O servidor é estruturado como um **game loop sequencial** que processa managers em ordem fixa a cada ciclo:

> **Arquitetura:** Ver [ADR-005](../../decisions/ADR-005-arquitetura-servidor-monolito-goroutines.md) no repositório do game para detalhes técnicos.

```text
GameLoop (goroutine principal — sequencial):
  WorldManager      — Atualiza terreno, clima, ciclo dia/noite
  NPCManager        — Atualiza agendas, needs, decisões de IA
  QuestManager      — Verifica prazos, missões competitivas, bounties
  StoryManager      — Calendário de eventos, temporadas, branching
  EconomyManager    — Preços, escassez, regeneração de recursos
  CombatManager     — Resolve combates em turno, aplica D20
  PersistManager    — Salva estado sujo (goroutine de I/O separada)

EventBus (goroutine separada — notificações assíncronas apenas):
  - Pub/Sub para notificações ao cliente, logging, métricas
  - NÃO coordena lógica entre managers

Conteúdo (dados do jogo, JSON):
  - NPCs e agendas
  - Items e receitas
  - Quests e objetivos
  - Skills e magias
  - Mapas e blocos de cenário

Cliente (interface):
  - HTML/CSS/JS via WebSocket
  - Renderiza texto e painéis de informação
  - Input do player (comandos de texto ou botões)
```

### EventBus (Notificações Assíncronas)

O EventBus é usado para **notificações assíncronas** — atualizar clientes, logging, métricas — e NÃO para coordenar lógica de jogo entre managers:

```text
// Quando player coleta item:
EventBus.Publish("OnItemCollected", { id: "item_minerio_ferro", qtd: 1 })

// Cliente recebe atualização de inventário
// Logger registra evento para analytics
// NPCs próximos adicionam à knowledgeBase (processado no próximo ciclo do NPCManager)
```

---

## 8.12 – Penalidade de Morte

> **ADR-010.** Full Loot foi removido do MVP. A penalidade de morte é baseada em XP e durabilidade.

### Morte PvE — Regras

Ao morrer em combate PvE, o jogador sofre:

1. **Perda de XP:** Perde **10% do XP do nível atual** (sugestão — valor de tuning). O jogador **nunca perde nível** — o XP é limitado ao mínimo do nível atual.
2. **Perda de Durabilidade:** Todos os equipamentos equipados perdem **15% de durabilidade máxima** (sugestão — valor de tuning). Itens com 0 de durabilidade ficam inutilizáveis até serem reparados.
3. **Sem Drop de Itens:** O jogador NÃO perde itens do inventário ao morrer.
4. **Itens de Quest Protegidos:** Itens vinculados a quests ativas não sofrem penalidade.

### Integração com Economia

A penalidade de durabilidade alimenta o loop econômico:

- Reparar itens exige **materiais de crafting + proficiência** (ver Cap. 6).
- Jogadores com proficiência em Ferraria ou Coureira podem oferecer serviços de reparo a outros.
- NPCs também oferecem reparo, mas a custo mais alto.

### Integração com Inimigos Evolutivos

Quando um jogador morre para um inimigo, o inimigo ganha XP (ver §8.10). Isso cria um ciclo onde mortes repetidas na mesma área geram inimigos progressivamente mais perigosos.

### Respawn

O jogador retorna ao último ponto de descanso seguro (vila, acampamento) com PV restaurados mas com as penalidades de XP e durabilidade aplicadas.

> **PvP:** Removido do escopo do MVP. Quando implementado (futuro), terá regras de penalidade próprias. Ver ADR-012.