# Backlog — GDD

> Tarefas de design, lore e documentação. Código em [`eras-do-brasil-game/backlog.md`](../../../eras-do-brasil-game/backlog.md).
>
> Cada tarefa tem um critério de aceite (AC) direto. Para trabalhar com IA: aponte a tarefa + os arquivos do GDD relevantes.

**Status:** 🔲 Pendente · 🟡 Em andamento · ✅ Concluído

---

## Furos de Lore
_Resolver antes de qualquer outra coisa — inconsistências que afetam múltiplos documentos._

- [x] **~~Causa da Ruptura de 1497~~** — Resolvido (Furo 2): Ritual Folclórico fracassado na Raiz do Mundo causou a Ruptura. Definido em `00_Conceitos_Centrais_do_Mundo.md` §2.1.

- [x] **~~Dom da Revivência — latente ou ativo no Ato 1?~~** — Resolvido (Furo 1): Troca de classe disponível desde o início; troca de origem requer Espelho do Eco (desbloqueado no fim do Ato 1). Ajustado em `01_Ato_1.md` e `03_Criacao_de_Personagem.md`.

- [x] **~~Motivação da Facção Folclórica no Ato 1~~** — Resolvido (Furo 3): Folclóricos divididos em Restauradores (querem fechar a Ruptura) e Fatalistas (querem usar o caos). Definido em `00_Conceitos_Centrais_do_Mundo.md`.

- [x] **~~Contradição de Nível para Tier 2/3~~** — Resolvido (Furo 6): Tabela XP em `03B_Progressao_e_Experiencia.md` alinhada com fonte de verdade (Tier 2 = Nível 5, Tier 3 = Nível 10).

- [x] **~~Mana vs Fadiga~~** — Resolvido (Furo 4): Mana removida. Sistema usa Fadiga Espiritual como limitador de magia (independente da Fadiga Física). Seção formal adicionada em `07_Magia_e_Espiritualidade.md`. Itens, dados JSON e atlas atualizados.

- [x] **~~Dano Espiritual e Exaustão Espiritual~~** — Resolvido (Furo 5): Dano Espiritual adicionado como tipo oficial em `04_Sistema_de_Combate.md` (resistência via Sabedoria Ancestral). "Exaustão Espiritual" padronizado para "Fadiga Espiritual".

- [x] **~~Escala de Ticks~~** — Resolvido: Tick removido como mecânica exposta ao jogador (ADR-007). Substituído por: tempo real (segundos/minutos), relógio do jogo (Manhã/Tarde/Noite/Madrugada), turnos (combate). 1 dia do jogo ≈ 2–4h reais.

- [x] **~~Guardião da Fenda — identidade, backstory e stats do boss final~~** — Resolvido (Furo 7): Guardião é manifestação defensiva da Raiz do Mundo (não é vilão). Identidade definida em `01_Ato_1.md` Sessão 4 e `03_Livro_de_Itens_e_Equipamentos.md`. Stats completos pendentes (TODO).

- [x] **~~Sanidade/Moral — definir ou remover do sistema~~** — Resolvido (Furo 8): Sistema de Sanidade removido. Substituído por teste de Resistência contra Medo (Presença CD 13) nas Ruínas Queimadas. Atualizado em Atlas e Game Pitch.

- [x] **~~Ecoera — definir ou remover conceito~~** — Resolvido (Furo 9): Conceito removido por não estar definido no lore canônico. Referência em mini-campanha substituída por "era futura alternativa através da Raiz do Mundo".

- [ ] **Mini-campanhas sem impacto sinérgico no Ato 1** — definir como elas alimentam a campanha principal
  AC: `03_Enredo_e_Mundo/03_Adaptacao_Digital_e_Campanhas.md` define como ≥3 mini-campanhas têm consequência na campanha principal

---

## Precisa para Fase 1 — Living World

- [ ] **Schemas JSON: NPC e Faction** — definições estruturais de NPC com agenda e facção com reputação
  AC: `06_Dados_e_Assets/01_Schemas_Estruturais.md` tem exemplos funcionais de NPC (agenda, estado) e Faction (id, reputação, comportamento)

- [ ] **NPC Agenda Data — Rotinas dos NPCs da Vila de São Tomé**
  AC: Arquivo de dados em `06_Dados_e_Assets/` com agenda completa de 3+ NPCs (bloco, ação e período do dia)

---

## Precisa para Fase 2 — Observer

- [ ] **Wireframes do Cliente Web** — HUD, Mapa de Nós, Tela de Cena, Combate
  AC: Arquivo em `04_Design_Visual/` com wireframes de baixa fidelidade das 4 telas principais do MUD web

- [ ] **Formato de Texto Narrativo para Tela de Cena** — como descrições de local e evento são exibidas
  AC: `04_Design_Visual/` documenta o formato (tamanho de bloco, estrutura, uso de variáveis como `[PLAYER_NAME]`)

---

## Precisa para Fase 2 — Observer (cont.)

- [ ] **Design do Tutorial / Onboarding** — o que ensinar e em que ordem para um MUD web
  AC: Documento em `04_Design_Visual/` ou `05_Livros_Auxiliares/` define os passos do onboarding (sistemas a apresentar, sequência, como fazer em texto sem UI gráfica)

---

## Precisa para Fase 3 — Player

- [ ] **Bestiário Ato 1** — inimigos, encontros e loot do Ato 1
  AC: Arquivo em `05_Livros_Auxiliares/` com entrada por inimigo: stats, loot, comportamento, localização e CD de encontro

- [ ] **Expandir Dados Iniciais Ato 1** — Enemy Stats, Itens e Localizações completos
  AC: `06_Dados_e_Assets/03_Dados_Iniciais_Ato1.md` tem dados para 8 blocos, 5+ inimigos e 15+ itens

- [ ] **Schemas JSON: Skill e Proficiency**
  AC: `06_Dados_e_Assets/01_Schemas_Estruturais.md` tem exemplos funcionais de Skill (ativa/passiva, custo, efeito) e Proficiency (tipo, XP, receita)

- [x] **~~Mecânica de Morte do Jogador~~** — Resolvido: Penalidade de morte definida (ADR-010). Perda de 10% XP (não perde nível) + 15% durabilidade. Sem drop de itens. Documentado em `08_Mundo_Vivo_e_NPCs.md` §8.12.

---

## Precisa para Fase 4 — Interaction

- [ ] **Livro de Proficiências de Vida** — coleta, produção e receitas
  AC: Arquivo em `05_Livros_Auxiliares/` com lista de proficiências, recursos, receitas de crafting e testes D20 associados

- [ ] **Livro de Diálogos e Narrativa** — guia de estilo de escrita para NPCs e cenas
  AC: Arquivo em `05_Livros_Auxiliares/` com tom/voz, regras de escrita de NPC e exemplos de bom/mau diálogo

- [ ] **Schema JSON para DialogueTree** — árvores de diálogo com condições e ramos
  AC: `06_Dados_e_Assets/01_Schemas_Estruturais.md` tem exemplo funcional de DialogueTree com condição, resposta e consequência

- [ ] **Schemas JSON: Quest, Gossip e Campaign**
  AC: `06_Dados_e_Assets/01_Schemas_Estruturais.md` tem exemplos funcionais dos 3 schemas com campos obrigatórios

- [ ] **Integração Quest ↔ Dialogue** — como aceitar missão via diálogo
  AC: `06_Dados_e_Assets/` documenta como um DialogueNode dispara ação de Quest (start, update, complete) com exemplo

- [ ] **Diálogos JSON dos NPCs da Vila de São Tomé** — primeiro hub jogável
  AC: Arquivo em `06_Dados_e_Assets/` com DialogueTree JSON de ≥3 NPCs (saudação, quest hook, fofoca)

- [ ] **Diálogos Completos — Mini-campanha "O Caçador que Não Voltou"**
  AC: Arquivo em `03_Enredo_e_Mundo/` com diálogos e texto narrativo completos (início, meio, fim, variações)

---

## Precisa para Fase 5 — D20 Full

- [ ] **Livro de Habilidades** — todas as habilidades Tier 1 das 12 classes consolidadas
  AC: Arquivo em `05_Livros_Auxiliares/` com tabela por habilidade: classe, ativa/passiva, custo, efeito, Tier de desbloqueio

- [ ] **Expandir Livro de Itens** — catálogo MVP Ato 1 completo
  AC: `05_Livros_Auxiliares/03_Livro_de_Itens_e_Equipamentos.md` tem todos os itens do Ato 1 (armas, armaduras, consumíveis, ferramentas, chave de quest)

- [ ] **Progressão de Tiers e Curvas de XP** — regras de avanço entre Tiers
  AC: `02_Livro_de_Classes/01_Tiers_e_Evolucao.md` tem tabela de XP por nível/tier com custo de Moedas de Classe para evolução

- [ ] **Herança de Habilidades — regras completas do Dom da Revivência**
  AC: `02_Livro_de_Classes/03_Heranca_de_Habilidades.md` documenta regras com exemplos de troca entre as 3 origens

- [ ] **Expandir Habilidades Tier 1 + Reaction Abilities**
  AC: Todas as 12 classes têm habilidades Tier 1 completas + 1 Reaction Ability cada no Livro de Classes

---

## Decisões MMORPG 2026-03-17
_Tarefas geradas pela sessão de decisões narrativas e mecânicas._

- [ ] **Schema JSON: Season e SeasonState** — definição estrutural de temporada com state machine
  AC: `06_Dados_e_Assets/01_Schemas_Estruturais.md` tem exemplo funcional de Season (id, fase, duração, consequências)

- [ ] **Schema JSON: CompetitiveQuest** — quest com múltiplos aceitantes e verificação server-side
  AC: `06_Dados_e_Assets/01_Schemas_Estruturais.md` tem exemplo funcional de CompetitiveQuest (publicação, aceite, timeout, recompensa)

- [ ] **Schema JSON: EnemyEvolution** — dados de evolução de inimigos (killCount, tier, migração)
  AC: `06_Dados_e_Assets/01_Schemas_Estruturais.md` tem exemplo funcional expandido com regras de progressão Normal→Veterano→Alfa→Lenda

- [ ] **Bestiário: Inimigos Evolutivos do Ato 1** — dados completos de inimigos com tiers evolutivos
  AC: `05_Livros_Auxiliares/` tem entrada por inimigo com stats base + stats por tier evolutivo + regras de migração

- [ ] **Balanceamento: Penalidade de Morte** — validar % XP e % durabilidade com curva de progressão
  AC: Documento em `99_Meta_e_Backlog/` com simulação de impacto da penalidade em diferentes níveis

- [ ] **Narrativa: Votação Simples** — definir UI e regras de votação para bifurcações narrativas
  AC: `08_Mundo_Vivo_e_NPCs.md` ou `04_Design_Visual/` documenta o fluxo de votação com mockup

---

## Decisões 2026-03-20 — Arquitetura do Mapa

- [x] **Arquitetura do Mapa — estrutura de camadas e regiões** — Resolvido: 3 camadas (Mapa-Múndi → Regional → Local), 5 regiões planejadas, zonas de nível da Mata Costeira definidas. Ver `01_Livro_de_Regras/05B_Arquitetura_do_Mapa.md`.

---

## Concluído
_Mover itens aqui quando prontos._
