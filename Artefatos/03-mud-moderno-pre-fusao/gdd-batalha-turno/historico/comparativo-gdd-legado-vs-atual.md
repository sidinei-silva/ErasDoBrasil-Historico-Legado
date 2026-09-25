# 🔍 Comparativo GDD: Legado vs Atual

**Data:** 2025-07-15  
**Objetivo:** Comparação exaustiva entre o repositório legado (`sidinei-silva/ErasDoBrasil-Historico-Legado`) e o GDD atual (`gdd/01_Livro_de_Regras/`), com foco em 5 áreas críticas para decisão de pivot.

**Fontes do Legado:**
- `Livros Antigos/Livro de Regras.md` (188KB, Cap. 1–7; Cap. 8 ausente)
- `Livros Antigos/ideias soltas.md` (conceitos brutos)
- `Livros Antigos/Checklist – Livro de Regras.md` (status: Cap. 6 Parcial, Cap. 7–8 Ausentes)
- `Chats Gemini/` — conversas 5, 7, 8, 9, 11 (a **verdadeira fonte** de decisões arquiteturais)
- `Conversas GPT/` — Setores de Missões, Enredo, Arte
- `Analise Notebook/` — Briefing Document, Project Plan, Relatório de Auditoria, Relatório de Evolução

**Fontes do Atual:**
- `gdd/01_Livro_de_Regras/` — Capítulos 01 a 09 (todos existentes e substanciais)

---

## 📌 Resumo Executivo

| Métrica | Legado | Atual |
|---------|--------|-------|
| Capítulos formalizados no Livro de Regras | 6 de 8 (Cap.7 parcial, Cap.8 ausente) | 9 de 9 (+ Cap.3B Progressão) |
| Magia e Espiritualidade (Cap.7) | Parcial (seções 7.1–7.4, sem taxonomia completa) | **Completo** (7.1–7.4 com classificação formal) |
| Mundo Vivo / NPCs (Cap.8) | **Ausente** do Livro de Regras formal | **Completo** (8.1–8.8, sistema formalizado) |
| Onde estão as decisões de NPC/Missões/Server? | Espalhadas em Chats Gemini (5, 8, 9) | Consolidadas no Cap.8 + Cap.9 |
| Decisões de arquitetura online/server | Detalhadas nos chats (Fastify/Redis/PG/Socket.io) | **Não especificadas** no GDD |
| StoryManager / Missões competitivas | Conceito rico nos chats | **Ausente** no GDD atual |
| Full Loot / Inimigos evolutivos | Discutido como "regra avançada opcional" | **Ausente** |

---

## 🔴 CATEGORIA 1: AUSENTE no GDD Atual (existia no legado)

Conceitos documentados no repositório legado que **não foram transportados** para o GDD atual.

---

### 1.1 — StoryManager (Calendário de Eventos do Mundo com Branching)

**Fonte Legada:** Gemini Conversations 5 (L719–740), 8 (L887–908), 9 (L719–740)

O legado define um `StoryManager` como um **calendário global de eventos por tick** que opera no servidor e ramifica a narrativa baseado nas ações dos jogadores:

```
Tick Global 10.000 → Evento "Invasão" começa
  → NPCs em pânico, novos inimigos no mapa
  → Missão Mundial criada: "Derrote o Rei Goblin" (prazo: Tick 15.000)

Cenário A: Jogadores vencem no Tick 12.500
  → Story.Event["Invasão"].CompletedBy = ["Player1", "Player2"]
  → StoryManager avança para "Era da Reconstrução"

Cenário B: Tick 15.000 chega sem resolução
  → Story.Event["Invasão"].CompletedBy = null
  → StoryManager avança para "Era da Ocupação Goblin"
```

**No GDD atual:** O Cap.8 menciona "Eventos Globais" (8.7) mas **não formaliza** o conceito de branching por linha do tempo nem a mecânica de Cenário A/B com estados persistentes divergentes.

**Impacto:** Sem o StoryManager, o mundo perde a capacidade de reagir coletivamente às ações dos jogadores. É o coração do "Mundo Vivo" no modo online.

---

### 1.2 — "Corrida pela Recompensa" (Missões Competitivas)

**Fonte Legada:** Gemini Conversations 5 (L774–816), 8 (L942–981), 9 (L774–816)

Sistema onde um NPC **anuncia um problema** (não "dá quest") e múltiplos jogadores podem aceitar:

```
Quest Data Structure:
{
  Quest_ID, Giver_NPC,
  State: "DISPONÍVEL" | "EM_ANDAMENTO" | "CONCLUÍDA" | "EXPIRADA",
  Accepted_By: [],
  Expires_On_Tick: 18000,
  Winner: null
}
```

- Player 1 aceita → `Accepted_By: ["Sidinei"]`
- Player 2 aceita depois → `Accepted_By: ["Sidinei", "Maria"]`
- Primeiro a completar ganha → `Winner: "Maria"`, outro recebe recompensa de consolação
- Se ninguém resolve antes do tick limite → Quest expira com consequências no mundo

**No GDD atual:** **Completamente ausente.** O POC `37-sistema-quests` existe na estrutura de pastas, mas não há design no Livro de Regras.

---

### 1.3 — "Quadro de Missões" / BountyManager (Metas Coletivas)

**Fonte Legada:** Gemini Conversations 5, 8 (seção 4)

Sistema server-side de contribuição comunitária:

```
Cidade_Precisa_De_Couro = {
  Total: 100,
  Atual: 0,
  MaxPorPlayer: 10
}
```

Jogadores contribuem individualmente para metas globais. Atinge thresholds → recompensas para todos que contribuíram.

**No GDD atual:** **Ausente.**

---

### 1.4 — Full Loot on Death (Loot Completo na Morte)

**Fontes Legadas:**
- Briefing Document (L68+): "death results in items dropped as loot, retrievable by players or NPCs"
- Project Plan: "optional hardcore mode"
- Setor de Arte: "Full loot na morte" como funcionalidade da POC digital
- Relatório de Auditoria: "NÃO formalizado no Livro de Regras" — confirmado como conceito apenas discutido
- Relatório de Evolução: listado como "regra avançada opcional para versão digital"

**No GDD atual:** **Nenhuma menção.** Nem como regra opcional, nem como nota futura.

**Impacto:** Full Loot era um pilar de alto risco do design. A ausência pode ser intencional (simplificação para MVP), mas precisa de decisão formal (ADR).

---

### 1.5 — Inimigos Evolutivos (Enemies that Gain XP)

**Fontes Legadas:**
- Briefing Document: "enemies that defeat a player gain XP, can reappear as powerful leaders"
- Relatório de Evolução: listado junto a Full Loot como regra avançada
- Nunca formalizado no Livro de Regras legado

**No GDD atual:** **Ausente.** Sem menção em nenhum capítulo.

---

### 1.6 — Arquitetura de Servidor (Stack Completa)

**Fonte Legada:** Gemini Conversations 9, 11

O legado detalha uma arquitetura completa:

| Componente | Tecnologia | Função |
|-----------|-----------|--------|
| Backend | **Fastify** (Node.js) | API, lógica server-side |
| Hot State | **Redis** | Ticks, posições de NPCs, estado volátil |
| Cold State | **PostgreSQL** | Saves de jogadores, histórico |
| Real-time | **Socket.io** | Eventos do mundo, broadcast |
| Short actions | **REST** | Equipar, inventário, ações rápidas |
| Frontend | **React + Zustand** | UI estilo Tibia (Canvas + painéis React) |
| Viewport | **Canvas / PixiJS** | Grid de navegação visual |

Modelo: **"Authoritative Shared Core"** — core de regras compartilhado, servidor é autoridade.

**No GDD atual:** Cap.9 menciona "Design Orientado a Dados" e a filosofia Motor vs Conteúdo, mas **não especifica nenhuma tecnologia, banco de dados ou protocolo de comunicação.** ADR-001 define Unity, mas não há spec de backend.

---

### 1.7 — Arquitetura "Comutável" (Offline vs. Online)

**Fonte Legada:** Gemini Conversations 5 (L995–1014), 8, 9

O conceito central é que `World.ProcessTick()` é **agnóstico à fonte de tick:**

```
// O "Motor" do Tick — reutilizável
World.ProcessTick():
  TimeManager.AdvanceTime(1)
  NPCManager.AtualizarAgendas()
  QuestManager.VerificarPrazos()
  StoryManager.CheckScheduledEvents()
  World.SaveState()

// Offline: player action → GameManager.ProcessTick() — location
// Online: setInterval(5000ms) → Server.ProcessTick() — global
// 100% reuso do core entre os dois modos
```

**Fases de desenvolvimento:**
1. **Fase 1-Off** → Validação offline (motor de regras puro)
2. **Fase 1-On** → Adicionar servidor
3. **Fase 2** → Economia e trocas
4. **Fase 3-Off** → Combate tático offline
5. **Fase 3-On** → Combate tático multiplayer

**No GDD atual:** Cap.8 menciona tick system e co-op, Cap.9 menciona Motor vs Conteúdo, mas **não formaliza a "comutabilidade"** nem as fases Off/On.

---

### 1.8 — Relógio da Ruptura (Rupture Clock)

**Fonte Legada:** Gemini chats; POC `10-relogio-ruptura` existe na estrutura do workspace

Um relógio global de ~500 ticks que governa transições de era e rupturas temporais. Quando o relógio completa um ciclo, eventos de ruptura disparam, alterando o mundo.

**No GDD atual:** **Não descrito** no Livro de Regras. O POC existe na estrutura de pastas, mas sem spec no GDD.

---

### 1.9 — QuestManager com EventBus (Arquitetura Event-Driven)

**Fonte Legada:** Gemini Conversations 5 (L508–523), 8 (L670–689), 9 (L475–523)

Arquitetura desacoplada via Pub/Sub:

```
// Quando player coleta item:
EventBus.Publish("OnItemCollected", { id: "item_minerio_ferro", qtd: 1 })

// QuestManager escuta e atualiza objetivos automaticamente
Quest_Template:
  QUEST_ID: "ferreiro_primeira_espada"
  Objetivos: [
    { Tipo: "COLETAR_ITEM", Alvo_ID: "item_minerio_ferro",
      Quantidade_Necessaria: 5, Quantidade_Atual: 0 }
  ]
```

Tipos de objetivo: `COLETAR_ITEM`, `FALAR_COM_NPC`, `MATAR_INIMIGO`

**No GDD atual:** **Ausente do Livro de Regras.** POC `37-sistema-quests` existe, mas o GDD não documenta a arquitetura de quests.

---

### 1.10 — Motor Reutilizável (Estrutura Completa de Managers)

**Fonte Legada:** Gemini Conversations 5 (L1179–1208), 9 (L1179–1208)

O legado define o "Motor" completo:

```
Motor (código reutilizável):
  TickManager
  NPCManager
  QuestManager
  InventoryManager
  CombatManager (baseado em turnos/ticks)
  EventBus

Conteúdo (dados específicos do jogo):
  JSON/ScriptableObjects definindo:
  - Todos os Items
  - Todos os NPCs e agendas
  - Todas as Missões e objetivos
  - Todas as Skills

Casca (cliente específico):
  UI, sprites, sons, input
```

**No GDD atual:** Cap.9 descreve a **filosofia** (Motor vs Conteúdo) com exemplo prático, mas **não lista os Managers** específicos nem define a interface de cada um.

---

## 🟡 CATEGORIA 2: COMPARTILHADO mas DIFERENTE

Conceitos que existem em ambos, mas com diferenças notáveis.

---

### 2.1 — Sistema de Economia / Itens / Crafting (Cap. 6)

| Aspecto | Legado | Atual |
|---------|--------|-------|
| Matriz 5x5 (Qualidade × Raridade) | ✅ Presente (Muito Baixa→Excelente × Comum→Lendário) | ✅ Presente (idêntica) |
| Bônus por qualidade | -1 / 0 / 0 / +1 / +2 | Mesmos valores |
| Efeitos de raridade | **Narrativos** (Lendário → "abre portas, forja alianças") | **Mecânicos** (Nível Recomendado + efeitos narrativos) |
| Fórmula de crafting | 1D20 + Attr + Prof, CD = 10 + raridade | Idêntica |
| Categorias de proficiência | Coleta, Refinamento, Produção | 🌿 Coleta, ⚙️ Refinamento, 🔨 Produção (+ emojis + subcategorias detalhadas) |
| Durabilidade | Tabela MB(3-5), B(6-8), M(9-12), A(13-16), E(17-20+) | Mesma tabela |
| Reparo campo / oficina | Campo CD12 (50%), Oficina CD10-16 (100%) | Idêntico |
| Fusão de itens | Mesmo tipo, CD14-18, sucesso absorve propriedade, Lendário não funde | Idêntico |
| Upgrade | Incremento qualidade, +1 bônus, Specialist/Master, CD=12+nível | Idêntico |

**Veredicto:** Sistemas **quase idênticos**. O atual é uma versão mais polida do legado com melhor formatação. A diferença mais relevante é que o atual adiciona "Nível Recomendado" como conceito formal e tem subcategorias mais detalhadas de proficiência.

---

### 2.2 — Sistema de NPC / IA / Mundo Vivo (Cap. 8)

| Aspecto | Legado (Chats Gemini) | Atual (Cap.8) |
|---------|----------------------|---------------|
| Modelo híbrido Agenda + Needs | ✅ (KCD/Stardew + DF/RimWorld) | ✅ (mesma referência) |
| Needs: Fome, Sede, Energia, Social, Segurança | ✅ com decay `npc.fome += 0.1` por tick | ✅ sem especificar taxa de decay |
| Traits | ✅ como modificador de personalidade | ✅ como modificador de personalidade |
| Mood & Memories | ✅ `"+5: Comeu refeição"`, `"Amigo morreu" (-40, 1 semana)` | ✅ com conceito de Thoughts/Humor, sem valores numéricos |
| OnTick 3 fases | ✅ Passive → Decision (Utility AI) → Action | ✅ Mesma estrutura 3 fases |
| knowledgeBase | ✅ com `type`, `id`, `block`, `ultimo_visto` | ✅ com mesma estrutura |
| Expiração de conhecimento | **5.000 ticks** | **500 ticks** (10× mais curta) |
| Fofoca/Gossip | ✅ 2 NPCs no mesmo bloco + social alto → troca de knowledge | ✅ Mesma mecânica |
| Facções/Reputação | Mencionado em `ideias soltas` | ✅ **5 tiers formais** (Inimigo → Aliado) |
| Percepção | ✅ Scan por bloco a cada tick | ✅ Mesma mecânica |

**Diferenças-chave:**
1. **Expiração de conhecimento:** 5000 ticks (legado) vs 500 ticks (atual). Redução de 10×. Pode ser intencional para forçar renovação mais rápida de informação.
2. **Formalização:** O legado tem mais exemplos concretos com valores numéricos (decay rates, humor scores). O atual é mais conceitual e abstrato.
3. **Facções:** O atual formaliza com 5 tiers; o legado apenas menciona.

---

### 2.3 — Sistema de Ticks

| Aspecto | Legado | Atual |
|---------|--------|-------|
| Tick como unidade de tempo | ✅ | ✅ |
| Tabela de custos | Movimento 1, combate 1, descanso 1-3 | Movimento 1-3, coleta 1, interação 1, combate 1/rodada, descanso 1-3 |
| Custo por terreno | Não formalizado | ✅ **Estrada(1), Floresta(2), Pântano/Montanha(3)** |
| Offline vs Online | ✅ Player-triggered vs server `setInterval` | Mencionado como Solo vs Co-op, sem detalhe Off/On |
| Tick Debt | ❌ | ✅ **Sistema formal de débito para async co-op** |
| Combat Bubble | ❌ | ✅ **1 rodada = 1 tick debt** |

**Diferença-chave:** O atual introduz **Tick Debt** e **Combat Bubble** como conceitos novos para resolver o multiplayer assíncrono, mas perde a distinção explícita offline/online do legado.

---

### 2.4 — Magia e Espiritualidade (Cap. 7)

| Aspecto | Legado (Cap.7, L2847–3224+) | Atual (Cap.7, 400+ linhas) |
|---------|---------------------------|--------------------------|
| Introdução / Filosofia | ✅ Magia como ato narrativo e mecânico | ✅ Mesma filosofia, mais expandida |
| Fontes de Magia | 4 fontes (Espiritual, Técnica, Elemental, Mental) | 4 fontes (Espiritual, Elemental, Mental, Ritualística) |
| Caminhos Espirituais | ❌ | ✅ **4 caminhos** (Guardião da Raiz, Condutor Elemental, Tecelão Mental, Ritualista Ancestral) |
| Classificação de tipos | ❌ Não formalizada | ✅ **5 tipos** (Ofensiva, Defensiva, Suporte, Manipulação, Ritualística) |
| Categorias de efeito | ❌ | ✅ **4 categorias** (Comum, Avançada, Ritualística, Épica) |
| Concentração | ✅ 1 magia por vez, teste Vigor CD10/metade dano | ✅ Idêntico |
| Contra-magia | ✅ Opcional, Reação + teste CD=10+nível | ✅ Idêntico |
| Energia / Fadiga | ✅ Itens rituais para rituais, épicas exigem suporte | ✅ Mesma tabela + **Fadiga Espiritual formal** (3 usos → Vigor CD12) |
| Recarga | ✅ Turnos / Ticks / Cenas | ✅ Idêntico |
| Áreas de efeito | ❌ | ✅ Descrição + grid futuro (Círculo/Linha/Cone) |
| Exemplos de magias | ❌ | ✅ **Tabela com 6 magias classificadas** |

**Veredicto:** O GDD atual é **significativamente mais completo** que o legado em Magia. Acrescenta taxonomia formal, Caminhos Espirituais, classificação por tipo/categoria, e exemplos concretos. O legado tinha a mecânica base (concentração, custos, contra-magia) mas sem a estrutura de classificação.

---

### 2.5 — Sistema de Combate (Cap. 4)

| Aspecto | Legado | Atual |
|---------|--------|-------|
| Turno-based | ✅ Iniciativa 1D20+Astúcia | ✅ Iniciativa 1D20+Astúcia |
| Fase 1 (estático) | Mencionado | ✅ **Formal** com tabela resumo |
| Fase 2 (grid tático) | Mencionado como futuro | ✅ **Formal** com expansão modular planejada |
| Ações em combate | Presentes | ✅ **6 tipos formalizados** com tabelas |
| Condições de status | Mencionadas | ✅ **9 condições** com efeitos mecânicos |
| Exemplo de combate | ✅ Com 4 participantes | ✅ Exemplos por tipo de ação |

**Veredicto:** O atual é muito mais detalhado e estruturado. O legado tinha o esqueleto funcional.

---

### 2.6 — Design Orientado a Dados (Motor vs Conteúdo)

| Aspecto | Legado (Chats Gemini) | Atual (Cap.9) |
|---------|----------------------|---------------|
| Filosofia Motor/Conteúdo | ✅ com lista de Managers | ✅ com exemplo prático (ferreiro.json) |
| Lista de Managers | `TickManager`, `NPCManager`, `QuestManager`, `InventoryManager`, `CombatManager`, `EventBus` | Não lista managers específicos |
| Exemplo multi-jogo | ❌ | ✅ `Eras do Brasil` vs `Neon Sprawl` (futuro Sci-Fi) |
| ScriptableObjects/Resources | ✅ Mencionado | ✅ Mencionado |

**Diferença-chave:** O legado é mais técnico (lista interfaces/managers), o atual é mais conceitual (filosofia + exemplo).

---

## 🟢 CATEGORIA 3: NOVO no GDD Atual (não existia no legado)

Conceitos que foram **criados ou formalizados pela primeira vez** no GDD atual.

---

### 3.1 — Tick Debt (Débito de Ticks)

**Local:** Cap. 8 (8.2–8.3)

Sistema formal para resolver multiplayer assíncrono:
- Quando um jogador entra em combate, acumula "Tick Debt"
- O mundo só avança quando todos os jogadores resolvem seus débitos
- Permite co-op sem forçar sincronização constante

**No legado:** Não existia. O legado resolvia com `setInterval` global no servidor.

---

### 3.2 — Anfitrião / Viajante (Roles de Co-op)

**Local:** Cap. 8

Papéis formais para multiplayer cooperativo:
- **Anfitrião:** Dono do "mundo", resolve os ticks do mundo
- **Viajante:** Visitante, age dentro do mundo do anfitrião

**No legado:** Não existia como conceito formal.

---

### 3.3 — Combat Bubble

**Local:** Cap. 8

Conceito de que o combate cria uma "bolha" temporal:
- 1 rodada de combate = 1 tick debt
- O mundo externo pausa para os combatentes
- Outros jogadores continuam explorando normalmente

**No legado:** Não existia.

---

### 3.4 — Custo de Terreno por Tipo

**Local:** Cap. 5

| Terreno | Custo em Ticks |
|---------|---------------|
| Estrada | 1 |
| Floresta | 2 |
| Pântano / Montanha | 3 |

**No legado:** Terrenos eram mencionados mas sem tabela formal de custos.

---

### 3.5 — Facções com 5 Tiers Formais

**Local:** Cap. 8 (8.6)

Reputação com 5 níveis: **Inimigo → Hostil → Neutro → Amigável → Aliado**

Com consequências mecânicas por nível (acesso a merchants, quests, diálogos).

**No legado:** Facções mencionadas em `ideias soltas` mas sem tiers ou mecânica.

---

### 3.6 — Sistema de Companheiros com Afinidade

**Local:** Cap. 8 (8.8)

NPCs podem se tornar companheiros permanentes baseados em:
- Nível de afinidade acumulado por interações
- Quests específicas completadas
- Alinhamento de valores/facção

**No legado:** `afinidade` mencionada como campo em interação com NPC, mas sem sistema de companheiros.

---

### 3.7 — Classificação Formal de Magia (Tipos + Categorias + Caminhos)

**Local:** Cap. 7 (7.2, 7.3)

Taxonomia completa:
- 4 Fontes × 4 Caminhos Espirituais × 5 Tipos Funcionais × 4 Categorias de Efeito
- Tabela de exemplos classificados

**No legado:** Fontes existiam, mas sem a camada de Caminhos, Tipos e Categorias.

---

### 3.8 — Fadiga Espiritual como Mecânica Formal

**Local:** Cap. 7 (7.4)

Após 3 usos consecutivos de magias avançadas → Teste de Vigor (CD 12) → falha causa Exaustão Espiritual.

**No legado:** Custos de magia existiam mas sem mecânica de fadiga progressiva.

---

### 3.9 — Condições de Status Formalizadas (9 tipos)

**Local:** Cap. 9 (9.3)

Lista completa: Envenenado, Derrubado, Atordoado, Assustado, Queimando, Congelado, Cego, Confuso, Vulnerável — cada um com efeito mecânico específico.

**No legado:** Condições mencionadas individualmente (ex: Atordoado em magia), mas sem lista consolidada.

---

### 3.10 — Fase 1 (Blocos) vs Fase 2 (Livre) como Arquitetura Dual Formal

**Local:** Cap. 4 (introdução) + Cap. 9 (9.5)

Planejamento explícito:
- **Fase 1:** Blocos de cenário + combate estático (JRPG / Sea of Stars)
- **Fase 2:** Movimentação livre + combate tático com grid isométrico (Stoneshard / Solasta)

Com apêndice dedicado (9.5) detalhando a transição.

**No legado:** Discutido nos chats como progressão natural, mas não formalizado no GDD.

---

## 🎯 Recomendações para Decisão de Pivot

### Decisões Urgentes (precisam de ADR)

| # | Decisão | Risco de Ignorar |
|---|---------|-----------------|
| 1 | **Full Loot on Death**: incluir como regra avançada opcional ou descartar? | Design perdido se não documentado |
| 2 | **StoryManager**: formalizar no GDD ou tratar como feature pós-MVP? | Perde o diferencial de "mundo reativo" no multiplayer |
| 3 | **Missões Competitivas ("Corrida pela Recompensa")**: incluir no design ou adiar? | Feature única do jogo, difícil de retrofitar |
| 4 | **Metas Coletivas ("Quadro de Missões")**: incluir? | Endgame comunitário depende disso |
| 5 | **Arquitetura de Servidor**: manter stack legada (Fastify/Redis/PG) ou pivotar para Unity backend? | Impacta todas as decisões Online |
| 6 | **Inimigos Evolutivos**: vale a complexidade? | Feature de nicho, pode ser cortada sem impacto |
| 7 | **Expiração de knowledge**: 500 ticks (atual) é intencional ou erro? | Muda radicalmente o feeling do mundo (memória curta vs longa) |

### Itens a Migrar (baixo risco, alto valor)

1. Documentar a **arquitetura "comutável"** (offline/online) — é elegante e já está provada conceitualmente
2. Formalizar o **Relógio da Ruptura** no GDD (já tem POC planejada)
3. Adicionar diagrama do **Motor de Ticks** (`ProcessTick()` com lista de Managers) no Cap. 9
4. Criar **Cap. 10 ou Apêndice B** para sistemas online (StoryManager, BountyManager, Competitive Quests)

---

## 📊 Mapa de Cobertura por Área de Foco

```
                          LEGADO    ATUAL    STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Economia/Items/Crafting  ██████   ██████   ✅ Paridade
2. Mundo Vivo/NPC AI/Ticks  ████░░   █████░   🟡 Atual mais formal, legado mais detalhado
3. Full Loot/Drop on Death  ██░░░░   ░░░░░░   🔴 Perdido
4. Server/Online Arch.      █████░   ░░░░░░   🔴 Perdido  
5. StoryManager/Missions    █████░   ░░░░░░   🔴 Perdido
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXTRAS:
6. Magia/Espiritualidade    ███░░░   ██████   🟢 Atual muito superior
7. Combate                  ██░░░░   █████░   🟢 Atual muito superior
8. Condições/Status         █░░░░░   █████░   🟢 Atual novo
9. Multiplayer Co-op        ░░░░░░   ████░░   🟢 Atual novo (Tick Debt)
```

---

**Conclusão:** O GDD atual é um documento **muito mais maduro e completo** que o legado para tudo que é mesa/single-player. Porém, **todo o design online/multiplayer competitivo** do legado (StoryManager, missões competitivas, metas coletivas, server arch) foi perdido na migração. Se o projeto pretende ter componente online, esses conceitos precisam ser resgatados e formalizados.
