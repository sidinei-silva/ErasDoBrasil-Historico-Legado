# Eras do Brasil — Game Design Document (GDD)

> Fonte Única da Verdade (SSoT) do design de jogo. Todo o design, lore, regras e planejamento vivem aqui.

**Navegação rápida:** [Projeto](../README.md) · [Roadmap](../ROADMAP.md) · [🔴 Guia de Retomada](../docs/GUIA_RETOMADA.md) · [ADR-004](../vibe/decisions/ADR-004-pivot-mmorpg-servidor-go.md)

---

## 🌿 Visão Geral

*Eras do Brasil* é um **MUD Moderno** (servidor Go + cliente web) de **eco-fantasia** ambientado em uma versão mística do Brasil colonial (1497), onde **colonizadores, povos originários e entidades folclóricas** coexistem em um mundo persistente online interconectado por ciclos de tempo, espiritualidade e memória.

### Pilares do Design

* **A Raiz do Mundo** — Entidade espiritual que conecta todas as eras e memórias
* **O Dom da Revivência** — Troca livre de classes herdando habilidades ativas
* **Mundo Persistente Online** — Servidor Go 24/7, NPCs com rotinas, Utility AI, fofoca
* **Progressão Flexível** — 12 classes × 3 Tiers com builds híbridas
* **Itemização Profunda** — Matriz 5×5 de Qualidade × Raridade
* **Economia de Risco** — Missões competitivas, inimigos evolutivos, penalidade de morte (XP + durabilidade)

---

## 🧭 Estrutura do GDD

### 📕 [01 — Livro de Regras](01_Livro_de_Regras/)
As mecânicas centrais do jogo.

| Capítulo | Conteúdo |
|----------|----------|
| [01 — Introdução e Ambientação](01_Livro_de_Regras/01_Introducao_e_Ambientacao.md) | Premissa, tom, Dom da Revivência |
| [02 — Mecânicas Básicas](01_Livro_de_Regras/02_Mecanicas_Basicas.md) | Sistema D20, testes, vantagem/desvantagem |
| [03 — Criação de Personagem](01_Livro_de_Regras/03_Criacao_de_Personagem.md) | Atributos, point-buy (27 pts), origens |
| [03B — Progressão e Experiência](01_Livro_de_Regras/03B_Progressao_e_Experiencia.md) | **NOVO** Sistema de XP, níveis 1-15, ganhos por nível |
| [04 — Sistema de Combate](01_Livro_de_Regras/04_Sistema_de_Combate.md) | Iniciativa, turnos, ataques, dano |
| [05 — Exploração e Mundo](01_Livro_de_Regras/05_Exploracao_e_Mundo.md) | Ciclo dia/noite, navegação por blocos, tempo real |
| [05B — Arquitetura do Mapa](01_Livro_de_Regras/05B_Arquitetura_do_Mapa.md) | Camadas de navegação, regiões, zonas de nível, migração de mobs |
| [06 — Economia, Itens e Crafting](01_Livro_de_Regras/06_Economia_Itens_e_Crafting.md) | Matriz 5×5, proficiências, receitas |
| [07 — Magia e Espiritualidade](01_Livro_de_Regras/07_Magia_e_Espiritualidade.md) | Fontes de poder, fadiga mágica |
| [08 — Mundo Vivo e NPCs](01_Livro_de_Regras/08_Mundo_Vivo_e_NPCs.md) | Utility AI, rotinas, fofoca, facções |
| [09 — Apêndices e Referências](01_Livro_de_Regras/09_Apendices_e_Referencias.md) | Tabelas, glossário |

### 📗 [02 — Livro de Classes](02_Livro_de_Classes/)
Sistema de classes e progressão.

| Documento | Conteúdo |
|-----------|----------|
| [00 — Introdução ao Sistema](02_Livro_de_Classes/00_Sistema_de_Classes_Intro.md) | Visão geral do sistema |
| [01 — Tiers e Evolução](02_Livro_de_Classes/01_Tiers_e_Evolucao.md) | Tier 1→2→3, requisitos, Moeda de Classe, **pré-requisitos multi-class** |
| [02 — Alternância de Classes](02_Livro_de_Classes/02_Alternancia_de_Classes.md) | Dom da Revivência, troca de classe |
| [03 — Herança de Habilidades](02_Livro_de_Classes/03_Heranca_de_Habilidades.md) | Ativas herdadas, passivas não, **limite de slots por Tier** |
| [04 — Troca de Origem](02_Livro_de_Classes/04_Troca_de_Origem.md) | **NOVO** Espelho do Eco, mecânica de troca de origem |
| **Origem Colonizador** | [Conquistador](02_Livro_de_Classes/1_Origem_Colonizador/Conquistador.md) · [Explorador](02_Livro_de_Classes/1_Origem_Colonizador/Explorador_de_Terras.md) · [Missionário](02_Livro_de_Classes/1_Origem_Colonizador/Missionario.md) · [Mosqueteiro](02_Livro_de_Classes/1_Origem_Colonizador/Mosqueteiro.md) |
| **Origem Indígena** | [Guerreiro Tribal](02_Livro_de_Classes/2_Origem_Indigena/Guerreiro_Tribal.md) · [Caçador de Feras](02_Livro_de_Classes/2_Origem_Indigena/Caçador_de_Feras.md) · [Arqueiro Selvagem](02_Livro_de_Classes/2_Origem_Indigena/Arqueiro_Selvagem.md) · [Xamã Curandeiro](02_Livro_de_Classes/2_Origem_Indigena/Xama_Curandeiro.md) |
| **Origem Folclórica** | [Guardião Ancestral](02_Livro_de_Classes/3_Origem_Folclorica/Guardiao_Ancestral.md) · [Lobo Lendário](02_Livro_de_Classes/3_Origem_Folclorica/Lobo_Lendario.md) · [Ser Elemental](02_Livro_de_Classes/3_Origem_Folclorica/Ser_Elemental.md) · [Encantador de Espíritos](02_Livro_de_Classes/3_Origem_Folclorica/Encantador_de_Espiritos.md) |

### 📘 [03 — Enredo e Mundo](03_Enredo_e_Mundo/)
Narrativa, lore e campanhas.

| Documento | Conteúdo |
|-----------|----------|
| [00 — Conceitos Centrais](03_Enredo_e_Mundo/00_Conceitos_Centrais_do_Mundo.md) | Raiz do Mundo, eras, lore central |
| [01 — Ato 1: A Primeira Ruptura](03_Enredo_e_Mundo/01_Ato_1_A_Primeira_Ruptura.md) | Campanha principal |
| [02 — Linha Eco-Histórica](03_Enredo_e_Mundo/02_Linha_Eco-Historica_e_Rupturas.md) | Linha do tempo e rupturas |
| [03 — Adaptação Digital](03_Enredo_e_Mundo/03_Adaptacao_Digital_e_Campanhas.md) | Transição mesa → digital |
| [04 — Guia de Adaptação de Missões](03_Enredo_e_Mundo/04_Guia_Adaptacao_de_Missoes.md) | Como converter missões |
| **Mini-Campanhas** | [6× Indígena](03_Enredo_e_Mundo/1_MiniCampanhas_Indigena/) · [6× Colonizador](03_Enredo_e_Mundo/2_MiniCampanhas_Colonizador/) · [6× Folclórico](03_Enredo_e_Mundo/3_MiniCampanhas_Folclorico/) |

### 🎨 [04 — Design Visual](04_Design_Visual/)
Pixel art, paleta, UI/HUD.

| Documento | Conteúdo |
|-----------|----------|
| [01 — Estilo, Arte e Técnica](04_Design_Visual/01_Estilo_Arte_e_Tecnica.md) | Direção de arte, UI, ícones, tipografia, exportação |
| [05 — UI Fase 1 (Exploração/Combate)](04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md) | HUD, mapa de nós, cena split |
| [06 — UI Fase 2 (Combate Tático)](04_Design_Visual/06_UI_Fase_2_Combate_Tatico.md) | Grid isométrico, AoE, hotbar |

### 🗺️ [05 — Livros Auxiliares](05_Livros_Auxiliares/)

| Documento | Conteúdo |
|-----------|----------|
| [01 — Atlas do Eco (Ato 1)](05_Livros_Auxiliares/01_Atlas_do_Eco_Ato1.md) | Mapa de nós com distâncias e terrenos |
| [03 — Livro de Itens e Equipamentos](05_Livros_Auxiliares/03_Livro_de_Itens_e_Equipamentos.md) | Catálogo completo, Matriz 5×5, 15 itens MVP Ato 1, receitas de crafting |

### 💾 [06 — Dados e Assets](06_Dados_e_Assets/)

| Documento | Conteúdo |
|-----------|----------|
| [01 — Schemas Estruturais](06_Dados_e_Assets/01_Schemas_Estruturais.md) | JSON: ClasseDePersonagem, Item, Inimigo |
| [02 — Lista de Assets (Ato 1)](06_Dados_e_Assets/02_Lista_de_Assets_Ato1.md) | Art bible do Ato 1 |
| [03 — Dados Iniciais (Ato 1)](06_Dados_e_Assets/03_Dados_Iniciais_Ato1.md) | 5 itens, 3 inimigos, 1 classe mockup |

### 📋 [99 — Meta e Backlog](99_Meta_e_Backlog/)

| Documento | Conteúdo |
|-----------|----------|
| [01 — Estratégia de Dados](99_Meta_e_Backlog/01_Estrategia_de_Dados_e_Documentacao.md) | Filosofia "Alma vs. Lógica" |
| [02 — Roadmap de Desenvolvimento](99_Meta_e_Backlog/02_Roadmap_Desenvolvimento.md) | Fases (Heartbeat → Multiplayer), checklist |
| [03 — Auditoria do GDD](99_Meta_e_Backlog/03_Auditoria_GDD.md) | Resultado da auditoria de consistência (PR #1) |
| [BACKLOG](99_Meta_e_Backlog/BACKLOG.md) | Tarefas de design/lore pendentes por fase |

---

## 🔗 Links Externos

| Recurso | Descrição |
|---------|-----------|
| [README do Projeto](../README.md) | Visão geral do repositório |
| [Roadmap Público](../ROADMAP.md) | Status e progresso geral |
| [Game Pitch](Game_Pitch.md) | Documento de apresentação |
| [Project Plan](Project%20Plan.md) | Plano de projeto (MUD Moderno) |
| [ADR-004 — Pivot MMORPG](../vibe/decisions/ADR-004-pivot-mmorpg-servidor-go.md) | Decisão do pivot para servidor Go |
| [Guia de Retomada](../docs/GUIA_RETOMADA.md) | Ponto de partida para retomar o projeto |