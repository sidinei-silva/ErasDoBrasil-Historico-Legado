# PoC — Albion Idle: Especificação do Tutorial

> **Escopo:** Esta PoC cobre exclusivamente o fluxo equivalente ao tutorial do Albion Online (The Lighthouse → The Cove → saída para o mundo). O objetivo é validar que o core loop funciona: zona define ação → ação gera recurso/fama → fama progride Destiny Board → progressão desbloqueia acesso a novo conteúdo.

---

## 1. Stack Técnica

| Camada | Tecnologia |
|---|---|
| Frontend | React + Vite + TypeScript + Zustand |
| Backend | Node.js + NestJS |
| ORM | TypeORM via `@nestjs/typeorm` |
| Banco de dados | SQLite (driver `better-sqlite3`) |
| Conteúdo estático | Arquivos JSON versionados no Git |
| Comunicação | HTTP REST (polling) |
| Hospedagem | Local / Railway/Render para testes externos |

**Por que TypeORM com NestJS:** o pacote `@nestjs/typeorm` é integração oficial — módulos, repositórios injetáveis e decorators seguem o mesmo estilo do NestJS. SQLite é configurado com `type: 'sqlite'` e um path de arquivo. Quando chegar a hora de migrar para PostgreSQL, é só trocar `type: 'postgres'` e adicionar as credenciais — as entidades e queries não mudam.

**O que não entra na PoC:** Redis, PostgreSQL, Docker, WebSocket, autenticação real (mock com user_id simples no header), animações, migrations automáticas (usar `synchronize: true` na PoC — desligar em produção).

**Fonte de dados do Albion:** repositório `broderickhyman/ao-bin-dumps` no GitHub contém dump dos arquivos do jogo em JSON/XML — usar como base para montar os JSONs de itens, armas, habilidades e mobs.

---

## 2. Estrutura de Dados Estáticos

```
/data
  /items
    weapons.json        # armas por tier e tipo
    armor.json          # armaduras por tier e slot
    tools.json          # ferramentas de coleta por tier
    consumables.json
  /mobs
    forest.json         # mobs da Floresta (T2)
    mountain.json       # mobs da Montanha (T2)
  /resources
    nodes.json          # nós de recurso por zona/bioma
  /zones
    zones.json          # zonas, bioma, tier, conexões, ações disponíveis
  /progression
    destiny_board.json  # árvore completa de nós do Destiny Board
    fame_per_action.json # fama por ação/tier
  /crafting
    recipes.json        # receitas por estação
  /skills
    abilities.json      # habilidades por arma, slot Q/W/E e cooldown
  /tutorial
    steps.json          # passos sequenciais do tutorial
```

**Regra:** banco só armazena estado dinâmico (inventário, progresso, posição). Definição de item, habilidade, zona é JSON — nunca vai pro banco. Os arquivos JSON são carregados em memória no boot do NestJS via módulo de configuração e ficam disponíveis como services injetáveis.

---

## 3. Zonas do Tutorial

A PoC replica a estrutura do tutorial original do Albion com adaptações para o modelo idle.

### Mapa do Tutorial

```
[O Farol] → [A Cova (Hub)] → [Floresta Esquecida] 
                           → [Forte da Montanha]
                           → [Saída — Cidade Iniciante]
```

### Tabela de Zonas

| Zona | Tipo | Tier | Recursos disponíveis | Mobs | Ações possíveis |
|---|---|---|---|---|---|
| O Farol | Introdução (linear) | 1 | Tronco Bruto, Pedra Bruta | Ladrões Hereges (T1) | Coletar, Matar |
| A Cova | Hub / Cidade Tutorial | — | — | — | Craftar, Refinar, Equipar, Viajar |
| Floresta Esquecida | Azul — Bioma Floresta | 2 | Troncos de Bétula, Couro Áspero | Raposas (recurso), Hereges (combate) | Coletar Madeira, Abater Animal, Matar Mob, Viajar |
| Forte da Montanha | Azul — Bioma Montanha | 2 | Minério de Cobre, Algodão | Hereges (combate) | Coletar Minério, Coletar Fibra, Matar Mob, Viajar |

**Princípio do sistema de zonas:** o player só vê e seleciona ações que existem na zona onde está. Não há menu global de "coletar qualquer coisa". As ações disponíveis são carregadas do `zones.json` com base na zona atual do player.

Exemplo de entrada em `zones.json`:
```json
{
  "id": "forgotten_woods",
  "name": "Floresta Esquecida",
  "type": "blue",
  "biome": "forest",
  "tier": 2,
  "connected_to": ["the_cove", "mountain_fort"],
  "available_actions": [
    {
      "type": "gather",
      "resource": "birch_log",
      "tool_required": "beginner_axe",
      "duration_ms": 4000,
      "fame_per_action": 15
    },
    {
      "type": "gather",
      "resource": "rugged_hide",
      "tool_required": "beginner_skinning_knife",
      "duration_ms": 5000,
      "fame_per_action": 12
    },
    { "type": "kill_mob", "mob_group": "heretic_scout", "fame_per_kill": 20 },
    { "type": "travel", "destinations": ["the_cove", "mountain_fort"] }
  ]
}
```

---

## 4. Fluxo do Tutorial (8 Passos)

Adaptação do Adventurer's Path do Albion para o modelo idle. Cada passo é uma entrada em `tutorial/steps.json` com condição de conclusão verificada pelo servidor.

| Passo | Zona | Ação | O que ensina |
|---|---|---|---|
| 1 | O Farol | Coletar 6 Troncos Brutos e 6 Pedras Brutas | Sistema de coleta, tempo fixo, fama |
| 2 | O Farol → A Cova | Viajar para A Cova | Sistema de viagem e tempo de deslocamento |
| 3 | A Cova | Craftar Machado e Picareta de Iniciante na Forja | Sistema de crafting, receitas, estações |
| 4 | A Cova → Floresta Esquecida | Viajar e coletar Troncos de Bétula e Couro Áspero | Zona define recurso disponível |
| 5 | Forte da Montanha | Coletar Minério de Cobre e Fibra de Algodão | Segundo bioma, segundo recurso |
| 6 | A Cova | Refinar recursos nas estações + Craftar equipamento T2 completo | Refinamento, cadeia de produção |
| 7 | A Cova | Equipar gear T2, configurar fila de habilidades | "You Are What You Wear", sistema de combate |
| 8 | Floresta Esquecida | Matar Hereges até atingir threshold de fama + ver Destiny Board | Auto-battler, progressão, Destiny Board |
| Saída | Forte da Montanha | Viajar para Cidade Iniciante | Gancho para o mundo pós-tutorial |

---

## 5. Inventário

O Albion usa dois limitadores simultâneos: **espaço (slots)** e **peso**. Ambos serão implementados na PoC.

- **Slots:** número máximo de tipos distintos de item. Itens iguais formam stack e ocupam 1 slot.
- **Peso:** cada item tem peso unitário. Stacks multiplicam o peso (ex: 50 troncos pesam mais do que 1 tronco). Peso máximo depende da bolsa equipada.

**Comportamento ao atingir limite:**
- Inventário cheio por peso ou slots → ação de coleta é interrompida no final do ciclo atual e servidor retorna status `inventory_full`.
- Player precisa esvaziar (ir à cidade, jogar fora) antes de retomar.

**Modelo de dados:**
```sql
-- Inventário do player
player_inventory (
  player_id,
  item_id,       -- referência ao JSON
  quantity,
  slot_index     -- posição visual opcional
)

-- Estado do player
player_state (
  player_id,
  current_zone_id,
  current_action,        -- JSON com tipo, alvo, started_at, duration_ms
  max_weight,
  max_slots,
  current_weight         -- calculado ou cached
)
```

---

## 6. Crafting

**Sem Focus na PoC.** Crafting é: consumir recursos → gerar item, sem variável de retorno premium.

**Regras:**
- Player deve estar em A Cova (ou zona com a estação correta).
- Cada receita especifica estação, recursos consumidos e item resultante.
- Crafting é instantâneo na PoC (sem tempo de craft) — pode ser adicionado depois como simples `duration_ms` na receita.

**Estações disponíveis no tutorial:**
- Forja Improvisada (Makeshift Forge) — armas e ferramentas T1
- Forja do Guerreiro (Warrior's Forge) — armaduras e armas de guerreiro T2
- Cabana do Caçador (Hunter's Lodge) — armaduras e armas de caçador T2
- Torre do Mago (Mage's Tower) — armaduras e armas de mago T2
- Fundição (Smelter), Curtume (Tanner), Serraria (Lumbermill), Tecelagem (Weaver) — refinamento

**Exemplo de receita em `crafting/recipes.json`:**
```json
{
  "id": "beginner_axe",
  "station": "makeshift_forge",
  "inputs": [
    { "item": "rough_log", "quantity": 3 },
    { "item": "rough_stone", "quantity": 3 }
  ],
  "output": { "item": "beginner_axe", "quantity": 1 }
}
```

---

## 7. Sistema de Combate (Auto-battler)

### 7.1 Fila de Habilidades (Skill Queue)

O player configura manualmente uma fila ordenada de habilidades. O combate executa essa fila em loop:

1. Verifica a habilidade na posição atual da fila.
2. Se disponível (cooldown zerado) → executa.
3. Se em cooldown → avança para a próxima na fila.
4. Se todas em cooldown → aguarda a mais próxima de ficar disponível.

O ataque básico (auto-attack) tem cooldown muito baixo (~1-1.5s, baseado no attack speed da arma) e é tratado como uma habilidade configurável na fila — pode ser posicionado em qualquer slot.

### 7.2 Estrutura de Habilidades por Arma

Fiel ao Albion: cada arma tem 3 slots de habilidade.

- **Slot Q:** player escolhe 1 entre as opções disponíveis para aquela arma.
- **Slot W:** player escolhe 1 entre as opções disponíveis para aquela arma.
- **Slot E:** fixo por arma (única opção).

Cada peça de armadura também contribui com habilidades nos slots de corpo, cabeça, botas — exatamente como no Albion.

### 7.3 Troca de Equipamento e Reconfiguração

Quando o player troca uma peça de equipamento:
- As habilidades daquela peça são removidas da fila.
- Os slots correspondentes ficam vazios (visualmente marcados como "não configurado").
- Player precisa ir manualmente ao loadout e configurar as habilidades do novo item.

Não há loadouts salvos por arma na PoC. É sempre reconfiguração manual.

### 7.4 Tempo Fixo e Resolução pelo Servidor

O servidor é autoritativo. Ao iniciar combate:

```
POST /actions/start
{ type: "kill_mob", zone: "forgotten_woods", mob_group: "heretic_scout" }

→ Resposta:
{ action_id: "abc123", started_at: "...", cycle_duration_ms: 4500 }
```

A cada ciclo o servidor calcula o resultado (dano, habilidades executadas, loot, fama). O cliente faz polling com `GET /actions/current` para receber o resultado quando o ciclo termina.

### 7.5 Modelo de dados de habilidade em `skills/abilities.json`

```json
{
  "weapon_id": "beginners_broadsword",
  "auto_attack": { "cooldown_ms": 1200, "damage_multiplier": 1.0 },
  "q_slot": {
    "options": [
      { "id": "heroic_strike", "cooldown_ms": 4000, "damage_multiplier": 2.5 },
      { "id": "heroic_cleave", "cooldown_ms": 5000, "damage_multiplier": 1.8, "aoe": true }
    ]
  },
  "w_slot": {
    "options": [
      { "id": "slowing_charge", "cooldown_ms": 8000, "effect": "slow" }
    ]
  },
  "e_slot": { "fixed": "knockback_charge", "cooldown_ms": 15000 }
}
```

---

## 8. Destiny Board

### 8.1 Estrutura de Branches

O Destiny Board tem 5 branches principais. Na PoC, apenas 3 são relevantes:

| Branch | Como avança | Relevância na PoC |
|---|---|---|
| **Aventureiro** | TODA fama do jogo contribui automaticamente | ✅ Central — passo 8 do tutorial |
| **Combate** | Fama de matar mobs, distribuída por peça de gear equipada | ✅ Tutorial passos 7-8 |
| **Coleta** | Fama de coletar recursos, por tipo de ferramenta/recurso | ✅ Tutorial passos 1-5 |
| Crafting | Fama de craftar itens | ⚠️ Presente mas secundário na PoC |
| Farming | Fama de fazendas e animais | ❌ Fora da PoC |

### 8.2 Regras de Distribuição de Fama

**Regra 1 — Adventurer recebe SEMPRE:**
Toda e qualquer fama gerada (combate, coleta, crafting, refinamento) é creditada simultaneamente ao nó do Aventureiro. Sem exceção. Isso também resolve o caso dos primeiros passos do tutorial (antes de ter gear): a fama vai para o Adventurer normalmente — é exatamente assim que funciona no Albion.

**Regra 2 — Combate: fama vai para a peça que mais contribuiu com dano:**
Quando um mob morre, o servidor verifica qual slot de equipamento foi responsável pela maior parte do dano. A fama é creditada ao nó daquela peça específica no board.
- Se o jogador matar um mob sem nenhum gear equipado → fama vai para Aventureiro mas **não é alocada a nenhum nó de combate**.

**Regra 3 — Coleta: fama vai para o nó da ferramenta/recurso utilizado:**
- Coletou madeira com Machado de Madeireiro → fama para o nó Woodcutter.
- Coletou minério com Picareta → fama para o nó Miner.
- Cada tipo de recurso tem seu próprio nó de gathering no board.

**Regra 4 — Crafting e Refinamento:**
- Refinou Troncos → fama para o nó Refiner (Wood).
- Craftou armadura de couro → fama para o nó Hunter's Lodge Crafter.

**Regra 5 — T4+ split de fama (fora da PoC, mas a estrutura deve suportar):**
A partir do Tier 4, o requisito de fama de cada nó é dividido:
- 20% da fama total → após esse threshold, o player pode gastar Learning Points para pular o restante.
- 80% restante → via fama normal ou Learning Points.

Na PoC (T1-T3 do tutorial), essa mecânica não aparece — os nós são desbloqueados apenas por fama acumulada.

### 8.3 Nós Relevantes na PoC (Tutorial T1→T3)

```
Adventurer Path (centro do board):
  Notice Adventurer → Trainee Adventurer → Journeyman Adventurer (9.000 fama)

Fighting Branch:
  Trainee Fighter → Journeyman Warrior  (path espada/machado)
                  → Journeyman Hunter   (path arco/adaga)
                  → Journeyman Mage     (path staffs)

Gathering Branch:
  Trainee Gatherer → Journeyman Woodcutter  (path madeira)
                   → Journeyman Miner       (path minério)
                   → Journeyman Skinner     (path couro)

Crafting Branch:
  Trainee Crafter → Journeyman Warrior's Forge Crafter  (480 fama)
                  → Journeyman Hunter's Lodge Crafter    (480 fama)
                  → Journeyman Mage's Tower Crafter      (480 fama)
```

A estrutura de dados é genérica — adicionar os outros 697 nós do board completo depois é só JSON, sem código novo.

### 8.4 Modelo de Dados

```sql
player_destiny_progress (
  player_id,
  node_id,         -- referência ao destiny_board.json
  fame_current,    -- fama acumulada neste nó
  unlocked_at      -- timestamp se já desbloqueado, null se em progresso
)
```

Na UI: carrega a árvore do JSON, faz merge com os dados do player. Nó sem linha no banco = bloqueado (cinza). Nó com `unlocked_at` preenchido = desbloqueado (cor). Nó com `fame_current > 0` mas sem `unlocked_at` = em progresso (barra de progresso).

### 8.5 Lógica de Crédito de Fama no Servidor

A cada ciclo concluído, o servidor executa:

```
1. Calcular fama_gerada com base na ação (tipo, tier, enchantment)
2. Sempre creditar em: nó Adventurer atual do player
3. Se ação = gather:  creditar também no nó do recurso coletado (woodcutter, miner, etc.)
4. Se ação = combat:  creditar também no nó da peça com maior contribuição de dano
5. Se ação = craft:   creditar também no nó da estação usada
6. Se ação = refine:  creditar também no nó de refining do recurso
7. Para cada nó creditado: se fame_current >= fame_required → desbloquear nó
```

Tabela de fama base para a PoC (T2-T3, sem enchantment, sem premium):

| Ação | Tier | Fama por unidade |
|---|---|---|
| Coletar recurso | T2 | 2 |
| Coletar recurso | T3 | 4 |
| Refinar recurso | T2 | 2 |
| Refinar recurso | T3 | 11 |
| Matar mob | T2 (zona azul) | ~15-30 |

---

## 9. Comunicação HTTP (PoC)

Polling simples. O servidor é sempre autoritativo — nunca aceita resultado calculado pelo cliente.

**Endpoints principais:**

```
POST /auth/mock              → cria sessão mock com user_id
GET  /player/state           → zona atual, inventário, peso, ação em andamento
POST /actions/start          → inicia ação (gather, kill, travel, craft)
GET  /actions/current        → resultado do ciclo atual se concluído
POST /actions/cancel         → cancela ação em andamento
GET  /zones/:id              → ações disponíveis na zona
GET  /destiny-board          → árvore + progresso do player
POST /equipment/equip        → equipa item
POST /equipment/skill-queue  → salva ordem da fila de habilidades
GET  /inventory              → inventário atual
POST /travel                 → inicia viagem para zona adjacente
```

**Ciclo de polling do cliente:**

```
1. POST /actions/start → recebe { action_id, cycle_duration_ms, started_at }
2. setTimeout(cycle_duration_ms) → GET /actions/current
3. Recebe resultado (drops, fama, novo ciclo ou interrupcao)
4. Se ação contínua (gather em loop) → servidor já reiniciou o ciclo
5. Se inventário cheio ou mob morto → servidor retorna status específico
```

---

## 10. PvP e Gank — Ideia Registrada (Fora do Escopo da PoC)

> ⚠️ Não implementar na PoC. Registrado aqui para não perder a ideia.

**Mecânica proposta:**

O player em modo "Gankar" entra em fila de matchmaking com prioridade por proximidade:

1. **Prioridade 1:** players ativamente em modo "Gankar" na mesma zona ou zonas adjacentes (mútuo — dois gankadores se encontram).
2. **Prioridade 2:** players no estado "Viajando" dentro das zonas selecionadas (máx. 2 adjacentes).
3. **Prioridade 3:** players realizando qualquer ação ativa na zona.
4. **Prioridade 4 (último recurso):** players em idle — incluindo possivelmente offline (a decidir).

**Set de defesa:** o player configura previamente um loadout de defesa diferente do de farm — podendo optar por um set ofensivo (bater de frente) ou de fuga (habilidades de escape: dash, slow, invulnerabilidade temporária). A mecânica de captura e fuga já foi esboçada anteriormente.

**Decisão pendente:** se players offline podem ser gankados ou se offline = imunidade automática.

---

## 11. O que fica fora da PoC

- Focus no crafting
- Economia entre jogadores (marketplace)
- Ilhas pessoais
- PvP e sistema de gank
- Zones amarelas/vermelhas/pretas
- Guilds e ZvZ
- Animações (cliente React puro, sem Godot)
- WebSocket (upgrade posterior)
- Autenticação real
- Destiny Board completo (apenas paths do tutorial)
