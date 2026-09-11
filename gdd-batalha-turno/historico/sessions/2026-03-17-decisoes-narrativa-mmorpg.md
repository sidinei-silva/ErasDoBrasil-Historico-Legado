# Sessão: Decisões de Narrativa e Mecânicas MMORPG

**Data:** 2026-03-17
**Branch:** `decisoes-narrativa-mmorpg-2026-03-17`
**Duração:** ~2 sessões (contexto estourou na primeira)

---

## Objetivo

Aplicar 16 decisões de design confirmadas ao GDD, cobrindo narrativa, mecânicas, escopo do MVP e arquitetura temporal. Todas as decisões foram tomadas previamente pelo game designer e documentadas em conversa anterior.

---

## 16 Decisões Aplicadas

| # | Decisão | ADR |
|---|---------|-----|
| 1 | Bandeirantes de Sangue como facção NPC (não jogável) | ADR-007 |
| 2 | Remoção do "Escolhido" / "Desperto" | ADR-007 |
| 3 | Missões competitivas (server-side, primeiro entrega = recompensa completa) | ADR-008 |
| 4 | Full Loot removido do MVP | ADR-009 |
| 5 | Votação simples para missões de história | ADR-008 |
| 6 | Evento finale de temporada (máquina de 3 estados) | ADR-008 |
| 7 | Ecos Instanciados (feature futura) | ADR-012 |
| 8 | Eco/Raiz reescritos (sem offline) | ADR-012 |
| 9 | Relógio da Ruptura absorvido pelas temporadas | ADR-008 |
| 10 | Tempo de temporada: 4-6 meses | ADR-008 |
| 11 | Inimigos Evolutivos no MVP (Normal → Veterano → Alfa → Lenda) | ADR-011 |
| 12 | Inimigos Evolutivos (expansão futura) | ADR-011 |
| 13 | Penalidade de morte: % XP + % durabilidade, sem drop de itens | ADR-010 |
| 14 | PvP removido do MVP | ADR-009 |
| 15 | Modo offline removido (100% online) | ADR-009 |
| 16 | Tick removido como mecânica visível ao jogador | ADR-012 |

---

## Arquivos Modificados

### Reescritas Completas (sessão 1)
- `gdd/03_Enredo_e_Mundo/00_Conceitos_Centrais_do_Mundo.md`
- `gdd/03_Enredo_e_Mundo/01_Ato_1_A_Primeira_Ruptura.md`
- `gdd/01_Livro_de_Regras/08_Mundo_Vivo_e_NPCs.md` (§8.1–§8.12)
- `gdd/Game_Pitch.md`
- `gdd/Project Plan.md`

### Seções Reescritas (sessão 1)
- `gdd/01_Livro_de_Regras/02_Mecanicas_Basicas.md` (§2.9)
- `gdd/01_Livro_de_Regras/05_Exploracao_e_Mundo.md` (§5.3)
- `gdd/06_Dados_e_Assets/01_Schemas_Estruturais.md` (campos de evolução)
- `gdd/06_Dados_e_Assets/03_Dados_Iniciais_Ato1.md` (Capitão Bandeirante)
- `gdd/05_Livros_Auxiliares/01_Atlas_do_Eco_Ato1.md`

### Substituição de "Tick" (sessão 2)
- `gdd/01_Livro_de_Regras/01_Introducao_e_Ambientacao.md`
- `gdd/01_Livro_de_Regras/04_Sistema_de_Combate.md`
- `gdd/01_Livro_de_Regras/06_Economia_Itens_e_Crafting.md`
- `gdd/01_Livro_de_Regras/07_Magia_e_Espiritualidade.md` (8 edições)
- `gdd/01_Livro_de_Regras/09_Apendices_e_Referencias.md`
- `gdd/04_Design_Visual/01_Estilo_Arte_e_Tecnica.md`
- `gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md`
- `gdd/04_Design_Visual/06_UI_Fase_2_Combate_Tatico.md`
- `gdd/03_Enredo_e_Mundo/04_Guia_Adaptacao_de_Missoes.md`
- `gdd/99_Meta_e_Backlog/03_Auditoria_GDD.md`
- `gdd/99_Meta_e_Backlog/01_Estrategia_de_Dados_e_Documentacao.md`
- `gdd/99_Meta_e_Backlog/02_Roadmap_Desenvolvimento.md`
- `gdd/99_Meta_e_Backlog/BACKLOG.md`
- 18 arquivos de mini-campanhas (Indígena, Colonizador, Folclórico)

### Substituição de "Desperto" (sessão 2)
- `gdd/01_Livro_de_Regras/03B_Progressao_e_Experiencia.md`
- `gdd/02_Livro_de_Classes/04_Troca_de_Origem.md`

### Metadados e Infra
- `README.md`
- `gdd/README.md`

### Novos Arquivos
- `gdd/decisions/ADR-007-narrativa-e-lore.md`
- `gdd/decisions/ADR-008-sistemas-competitivos-e-sazonais.md`
- `gdd/decisions/ADR-009-escopo-mvp.md`
- `gdd/decisions/ADR-010-penalidade-de-morte.md`
- `gdd/decisions/ADR-011-inimigos-evolutivos.md`
- `gdd/decisions/ADR-012-arquitetura-temporal-e-mundo.md`
- `historico/sessions/2026-03-17-decisoes-narrativa-mmorpg.md` (este arquivo)

---

## Regras Seguidas

- Texto criativo incerto marcado com `<!-- TODO -->`
- Tudo em português
- Arquivos em `historico/` e `research/` não foram alterados (registros históricos)
- Commits atômicos agrupados por tema
