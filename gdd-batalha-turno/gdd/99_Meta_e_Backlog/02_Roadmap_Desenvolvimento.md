# 🗺️ Roadmap de Desenvolvimento — Eras do Brasil

> **Fonte de Verdade** para todas as fases, POCs e tarefas de desenvolvimento do projeto.
> Este documento consolida e substitui os antigos `02_Checklist`, `03_Roadmap_Tecnico` e `04_Roadmap_Detalhado`.

**Navegação rápida:**
- [Stack Tecnológica](#-stack-tecnológica)
- [Estrutura de Dados](#-estrutura-de-dados-data-driven)
- [Fase 0: POCs](#-fase-0-pocs--provas-de-conceito)
- [Fase 1: MVP](#-fase-1-mvp--o-despertar)
- [Fase 2: Pré-Alpha](#-fase-2-pré-alpha--o-mundo-vivo)
- [Fase 3: Alpha](#-fase-3-alpha--o-jogo-ganha-vida)
- [Fase 4: Beta](#-fase-4-beta--a-tática)
- [Fase 5: Release](#-fase-5-release--a-raiz-conecta)
- [Resumo de Progresso](#-resumo-de-progresso)

**Documentos relacionados:**
- [Project Plan](../Project%20Plan.md) — Visão geral, público-alvo e mecânicas
- [Game Pitch](../Game_Pitch.md) — Apresentação do jogo
- [Estratégia de Dados](01_Estrategia_de_Dados_e_Documentacao.md) — Filosofia "Alma vs. Lógica"
- [Schemas Estruturais](../06_Dados_e_Assets/01_Schemas_Estruturais.md) — Formato JSON de entidades
- [UI Fase 1](../04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md) — Referência de interface (exploração e combate estático)
- [UI Fase 2](../04_Design_Visual/06_UI_Fase_2_Combate_Tatico.md) — Referência de interface (grid tático)
- [Atlas do Eco](../05_Livros_Auxiliares/01_Atlas_do_Eco_Ato1.md) — Mapa do Ato 1

---

## 🖥️ Stack Tecnológica

| Componente | Tecnologia | Justificativa |
| :--- | :--- | :--- |
| **Servidor** | **Go 1.22+** | Goroutines nativas para game loop, IA de NPCs e múltiplas conexões simultâneas. Compilação estática, deploy simples. |
| **Cliente** | **HTML / CSS / JS (vanilla)** | Zero instalação — joga no navegador. Aproveita as skills web do dev. |
| **Comunicação** | **WebSocket (gorilla/websocket)** | Bidirecional e em tempo real. Mensagens em JSON. |
| **Dados** | **JSON (arquivos ou SQLite futuro)** | Templates imutáveis (definições de itens, classes, inimigos) + saves de jogadores. Sem banco externo na fase inicial. |
| **IA (Desenvolvimento)** | **GitHub Copilot (VS Code)** | IA centralizada para código, GDD e criatividade. Minimiza pulverização de contexto entre plataformas. |

---

## 📂 Estrutura de Dados (Data-Driven)

> Detalhes completos em [Estratégia de Dados](01_Estrategia_de_Dados_e_Documentacao.md) e [Schemas](../06_Dados_e_Assets/01_Schemas_Estruturais.md).

| Camada | Tecnologia | Propósito | Exemplo |
|---|---|---|---|
| **Template** | JSON (somente leitura) | Dados imutáveis do jogo | `espada_ferro.json` (Dano 1d6, descrição) |
| **Runtime** | Struct Go | Estado atual em memória | `ItemInstance{Durability, TemplateID}` |
| **Persistência** | JSON / SQLite | Save Game serializado | Apenas dados de runtime serializados |

---

## 🧪 Fase 0: Heartbeat — O Servidor Respira

> **Objetivo:** Provar que o servidor Go funciona. Game loop via goroutine, conexão WebSocket, cliente web básico.
> **Resultado:** Servidor rodando com `time.Ticker`. Cliente conecta via WebSocket e vê o relógio do jogo avançando na tela.

### Entregas

| # | Entrega | Critério de Aceite |
|---|---|---|
| 0.1 | Projeto Go inicial | `go run main.go` sobe um servidor HTTP na porta 8080 |
| 0.2 | Game loop (goroutine) | `time.Ticker` incrementa relógio do jogo a cada X segundos. Log no terminal. |
| 0.3 | WebSocket | Cliente HTML conecta via `ws://`. Servidor envia estado do relógio em JSON. |
| 0.4 | Cliente mínimo | Página HTML exibe relógio do jogo (período do dia) atualizado em tempo real. |

---

## 🛡️ Fase 1: Living World — O Mundo Existe

> **Objetivo:** Mundo com blocos, NPCs com rotina e ciclo dia/noite. O mundo "vive" mesmo sem jogador.
> **Resultado:** Servidor simula 3 blocos com 2 NPCs que seguem agenda por período do dia.

### Entregas

| # | Entrega | Critério de Aceite |
|---|---|---|
| 1.1 | Blocos e grafo | 3 blocos (Vila, Floresta, Ruínas) conectados. NPC pode mover entre eles. |
| 1.2 | NPCs com Agenda | Ferreiro: casa→forja→casa. Pajé: meditação→cachoeira→aldeia. Rotina guiada por período do dia. |
| 1.3 | Utility AI básica | NPC com necessidades (fome, cansaço). Ações priorizadas por utilidade. |
| 1.4 | Dia/Noite | Relógio do jogo com 4 períodos (Manhã→Tarde→Noite→Madrugada). NPC muda rotina por período. |
| 1.5 | Log de eventos | Servidor gera log: "Manhã: Ferreiro chegou na Forja", "Noite: Pajé dormiu". |

---

## 👁️ Fase 2: Observer — O Jogador Observa

> **Objetivo:** Cliente web mostra o estado do mundo em tempo real. O jogador "assiste" o mundo viver.
> **Resultado:** Interface web com mapa de nós, lista de NPCs por bloco e log de acontecimentos.

### Entregas

| # | Entrega | Critério de Aceite |
|---|---|---|
| 2.1 | Mapa de nós (HTML/CSS) | 3 blocos clicáveis. Mostra nome, tipo, NPCs presentes. |
| 2.2 | Feed de eventos | Log em tempo real: "Ferreiro está trabalhando", "Lobo apareceu na Floresta". |
| 2.3 | Inspeção de NPC | Clicar no NPC mostra nome, localização, necessidade dominante, última ação. |
| 2.4 | Relógio visual | Indicador de período do dia (Manhã/Tarde/Noite/Madrugada) + relógio do jogo. |

---

## 🎮 Fase 3: Player — O Jogador Age

> **Objetivo:** Criação de personagem, movimentação, inventário, D20, combate estático, save/load.
> **Resultado:** Loop jogável completo: criar → explorar → lutar → coletar → voltar → salvar.

### Escopo

| Sistema | Conteúdo |
|---|---|
| **Origens** | 1 (Indígena) |
| **Classes** | 1 (Guerreiro Tribal) |
| **Blocos** | 3 (Vila de São Tomé, Floresta do Norte, Ruínas Queimadas) |
| **Inimigos** | 2 (Lobo, Espírito Menor) |
| **Itens** | 5 iniciais (conforme [Dados Iniciais](../06_Dados_e_Assets/03_Dados_Iniciais_Ato1.md)) |
| **UI** | Interface web: HUD + Mapa de Nós + Combate (texto/log) + Inventário |
| **Save** | JSON no servidor |

### Core Loop
```
Criar Personagem → Explorar Bloco (tempo de viagem)
    → Encontrar Evento/Combate (D20 + Mods)
    → Coletar Loot/XP
    → Voltar à Vila (descansar, equipar)
    → Repetir
```

### Entregas

| # | Entrega | Critério de Aceite |
|---|---|---|
| 3.1 | Criação de personagem | Escolher Origem + Classe + Atributos (point-buy 27 pts). Personagem salvo. |
| 3.2 | Movimentação | Clicar em bloco adjacente → personagem move (consome tempo de viagem). |
| 3.3 | Motor D20 | Rolar D20 + modificadores vs CD. Acerto/Falha/Crítico corretos. |
| 3.4 | Combate estático | Iniciativa → Turnos → D20 vs Defesa → Dano → Loot. Log com matemática. |
| 3.5 | Inventário | Equipar/desequipar, peso/capacidade. |
| 3.6 | Save/Load | Salvar estado completo (HP, Loot, Posição). Recarregar corretamente. |

---

## ⚔️ Fase 4: Interaction — O Mundo Reage

> **Objetivo:** Diálogos, fofoca, facções, crafting, coleta e economia loop completo. O mundo ganha profundidade social e econômica.

### Entregas

| # | Entrega | Critério de Aceite |
|---|---|---|
| 4.1 | Sistema de Temporadas | State machine PRE_EVENT → EVENT_ACTIVE → POST_EVENT. Bandeirantes avançam por fase. Cenário muda conforme temporada. |
| 4.2 | NPCs e Diálogos | 3 NPCs com rotinas. Diálogos com condições. Fofoca (knowledgeBase). |
| 4.3 | Economia | Coleta de 3 recursos. Crafting de 2 receitas. Venda/compra com NPC. Matriz 5×5. |
| 4.4 | Classes expandidas | 3 Origens × 1 Classe cada = 3 classes jogáveis. Troca via Dom da Revivência + herança de ativa. |
| 4.5 | Conteúdo | 8 blocos do Ato 1 navegáveis. Eventos em cada bloco. 1 mini-campanha completa. |
| 4.6 | Facções e Reputação | Matar inimigo de facção X altera reputação. NPC muda comportamento. |
| 4.7 | Proficiências | Coleta + Produção. Testes D20 para crafting. XP de proficiência sobe. |

---

## ♟️ Fase 5: D20 Full — O Jogo Completo

> **Objetivo:** 12 classes, 3 Origens, Ato 1 completo, combate tático com grid.

### Entregas

| # | Entrega | Critério de Aceite |
|---|---|---|
| 5.1 | 12 classes Tier 1 | Todas jogáveis com habilidades ativas e passivas. Evolução para Tier 2 (4 classes). |
| 5.2 | Grid tático | Mapa 2D com posições. Alcance real (melee vs ranged). Cobertura. Flanco. |
| 5.3 | Habilidades espaciais | AoE, linha de visão, empurrão, terreno. |
| 5.4 | Ato 1 completo | Campanha "A Primeira Ruptura" jogável. Boss final. |
| 5.5 | 6+ mini-campanhas | Jogáveis e balanceadas com recompensa "2-1-3". |
| 5.6 | Balanceamento | Curva de XP. Economia. Dificuldade do Boss. |

---

## 🌿 Fase 6: Multiplayer — A Raiz Conecta

> **Objetivo:** Múltiplos jogadores simultâneos no mesmo servidor. Missões competitivas. Inimigos evolutivos. Eventos globais. A "Raiz" ganha vida.

### Entregas

| # | Entrega | Critério de Aceite |
|---|---|---|
| 6.1 | Autenticação | Login/registro. Personagem persistido no servidor. |
| 6.2 | Múltiplos jogadores | 2+ jogadores no mesmo mundo. Veem NPCs e uns aos outros. Chat in-game. |
| 6.3 | Penalidade de Morte | Morrer = perda de % XP (não perde nível) + % durabilidade nos equipamentos. Sem drop de itens. Ver ADR-010. |
| 6.4 | Trade server-authoritative | Troca entre jogadores validada pelo servidor. Atomicidade garantida. |
| 6.5 | Missões competitivas | Múltiplos aceitam, primeiro a completar vence. Expiração por tempo real. Ver ADR-011. |
| 6.6 | Eventos globais | StoryManager com Cenários A/B. BountyManager. Consequências permanentes. |
| 6.7 | Inimigos Evolutivos | Inimigos que derrotam jogadores ganham XP: Normal → Veterano → Alfa → Lenda. Ver ADR-009. |

---

## ✅ Resumo de Progresso

### Design & Regras (Concluído)
- [x] Livro de Regras completo (9 capítulos)
- [x] Livro de Classes (12 classes Tier 1 + sistema de Tiers)
- [x] Enredo e Mundo (Ato 1 + 18 mini-campanhas + linha eco-histórica)
- [x] Design Visual (estilo, paleta, tipografia, referências de UI)
- [x] Atlas do Eco Ato 1 (mapa de nós com distâncias)
- [x] Game Pitch e Project Plan
- [x] Schemas JSON (Classe, Item, Inimigo)

### Fábrica de Dados (Concluído)
- [x] Schemas estruturais definidos
- [x] Lista de assets (Art Bible)
- [x] Dados mockup iniciais (5 itens, 3 inimigos, 1 classe)

### Desenvolvimento (Em Andamento)
- [ ] Fase 0: Heartbeat (servidor Go + WebSocket + ciclo de tempo)
- [ ] Fase 1: Living World (blocos + NPCs + IA)
- [ ] Fase 2: Observer (cliente web observa mundo)
- [ ] Fase 3: Player (D20 + combate + inventário)
- [ ] Fase 4: Interaction (economia + diálogos + facções)
- [ ] Fase 5: D20 Full (12 classes + grid + Ato 1)
- [ ] Fase 6: Multiplayer (missões competitivas + inimigos evolutivos + eventos)

---

**Última atualização:** 2026-03-11
