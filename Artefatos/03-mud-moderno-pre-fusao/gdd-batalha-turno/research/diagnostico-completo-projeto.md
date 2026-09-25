# 🔍 Diagnóstico Completo — Eras do Brasil

**Data:** 2026-03-07
**Objetivo:** Análise 360° do estado do projeto para fundamentar reorganização e plano de ação.

---

## 1. Raio-X do Projeto

### O que é o Eras do Brasil
RPG eco-fantástico baseado na história do Brasil colonial (1497), onde eras temporais coexistem por causa de uma "Ruptura" mística. Sistema D20 próprio, com combate por turnos (estático → tático), mundo vivo com sistema de Ticks, NPCs com rotinas e IA, 12 classes em 3 origens (Colonizador, Indígena, Folclórico), e cooperativo P2P.

### Cronologia do Desenvolvimento

| Período | Ferramenta | O que foi feito |
|---------|-----------|-----------------|
| ~2024 | GDD antigo (manual) | Conceito original, ideia de MMORPG, classes iniciais |
| ~2024-2025 | ChatGPT | Livro de Regras expandido, Livro de Classes, conversas de setores (Arte, Sistema, Enredo, Missões) |
| ~2025 | Gemini | Refinamento dos livros, expansão do enredo, mini-campanhas, design visual, análises NotebookLM |
| 2026-02 | GitHub Copilot | Auditoria GDD (PR #1), correções pré-backlog, 62 issues, ADRs, 38 POCs, website, sprint-planning |
| 2026-03 | GitHub Copilot + Vibe Flow | **Atual** — reorganização, plano de execução realista |

### Repositórios Existentes

| Repo | Descrição | Status |
|------|-----------|--------|
| `eras-do-brasil` | Projeto principal — GDD, POCs specs, docs, website | Ativo |
| `ErasDoBrasil-Historico-Legado` | Conversas GPT (3×), Gemini (20+), Livros Antigos, Análises NotebookLM | Arquivo morto (referência) |

---

## 2. Inventário do que Existe

### ✅ Completo e Sólido
- **GDD:** 9 capítulos do Livro de Regras + Capítulo 3B (Progressão/XP)
- **Classes:** 12 classes Tier 1 (4 por origem) com fichas completas
- **Sistemas:** Tiers, Herança de Habilidades, Troca de Origem, Multi-class
- **Enredo:** Ato 1 completo + 18 mini-campanhas tabeladas
- **Design Visual:** 6 documentos (estilo, UI Fase 1/2, assets, tipografia)
- **Schemas JSON:** ClasseDePersonagem, Item, Inimigo com dados iniciais
- **Pitch:** Game Pitch profissional (2000+ palavras)
- **Arquitetura:** ADR-001 (Unity único) + ADR-002 (Workflow UI/UX)
- **Planejamento:** 62 issues em 7 sprints, 9 epics, GitHub Project #10
- **POCs:** 38 POCs documentadas com READMEs detalhados (template consistente)
- **Histórico:** 2 sessões de trabalho documentadas

### ⚠️ Parcial
- **Livros Auxiliares:** 2/7 (Atlas do Eco + Catálogo de Itens). Faltam: Habilidades, Proficiências, Bestiário, Diálogos, Facções
- **Lore:** 8 furos/inconsistências identificados (Sprint 0 pendente)
- **docs/product/:** Vazio (apenas .gitkeep) — sem especificação formal de produto

### 🔴 Não Iniciado
- **Código:** 0/38 POCs implementadas. Projeto Unity não criado
- **Arte:** Nenhum asset produzido (definições visuais existem, mas sem execução)
- **Áudio:** Nenhuma definição além de placeholders futuros
- **Multiplayer:** Conceito definido, sem implementação
- **UI:** Wireframes planejados para Sprint 2, não começados

---

## 3. Diagnóstico dos Problemas

### 🔴 Problema 1: Escopo Descontrolado
**Sintoma:** 38 POCs, 62 issues, 10 fases de execução, 8 módulos de sistema.
**Causa:** Acúmulo de features desejadas de RPGs que o criador gostaria que existissem (sistema de fofoca, utility AI, clima/maré, grid tático, P2P).
**Impacto:** Paralisia por excesso — difícil saber "o que fazer agora".

### 🟡 Problema 2: Desconexão entre Design e Execução
**Sintoma:** GDD 100% completo, código 0%.
**Causa:** Meses de design assistido por IA sem validação prática (nenhuma POC rodou).
**Impacto:** Decisões de design que podem não funcionar na prática (ex: custo de Ticks, balanceamento de XP).

### 🟡 Problema 3: Conhecimento Fragmentado
**Sintoma:** "Não tenho 100% de conhecimento em como está".
**Causa:** GDD foi construído por 3 IAs diferentes ao longo de meses. Decisões estão espalhadas em conversas, issues, ADRs, sessões.
**Impacto:** Tempo perdido re-aprendendo o próprio projeto a cada retomada.

### 🟡 Problema 4: Tempo Limitado vs Ambição
**Sintoma:** CLT + bebê, 3 noites por semana.
**Causa:** Realidade de vida vs projeto de escopo AAA indie.
**Impacto:** Risco de burnout e abandono se não houver entregas tangíveis frequentes.

### 🟢 Problema 5: Gaps de Habilidade Identificados (mas gerenciáveis)
- **Arte:** Não sabe pixel art (tem curso, não fez)
- **Roteiro:** Dificuldade com estrutura narrativa e português
- **Game Dev:** Não conhece patterns específicos de jogos (mas é dev sênior)
- **C# / Unity:** Já usou (2017), precisa atualizar

### 🟢 Problema 6: Organização de Repositórios
**Sintoma:** Tudo no mesmo repo — GDD, POCs, site, conversas.
**Causa:** Facilitava contexto para IA, mas agora pesa.
**Decisão necessária:** Monorepo vs multi-repo (analisado na seção 5).

---

## 4. O que Funciona Bem

- **Documentação é excepcional:** Raros projetos indie têm esse nível de spec
- **Modularidade das POCs:** Cada POC é atômica, testável e progressiva
- **ADRs:** Decisões registradas com contexto e alternativas
- **Sprint-planning:** Issues bem organizadas com labels e sprints
- **Game Pitch:** Claro, convincente, diferenciado
- **Vibe Flow:** Acaba de ser adicionado, vai ajudar na organização

---

## 5. Análise: Monorepo vs Multi-Repo

### Opção A: Monorepo (como está hoje)

**Prós:**
- Contexto único para IA (importante para Copilot)
- Um só git clone para ter tudo
- Links internos entre docs funcionam
- Sem overhead de sincronização entre repos

**Contras:**
- Repo pesado (GDD + conversas + site + futuro código Unity)
- Histórico de git poluído (commits de docs misturados com código)
- Confuso para quem chega (o que é GDD? o que é código?)
- Unity `.meta` files vão poluir o repo

### Opção B: Multi-Repo com Link

**Prós:**
- Separação clara: GDD é GDD, código é código
- Unity repo limpo de documentação
- Cada repo tem CI/CD independente
- Git submodules ou links conectam

**Contras:**
- IA precisa de 2+ repos para contexto completo
- Manutenção de submodules é chateiro
- Links internos entre docs e código quebram

### 🎯 Recomendação: Monorepo Organizado (Opção A melhorada)

**Justificativa para seu caso:**
1. **Você é solo dev** — overhead de multi-repo não compensa
2. **IA é ferramenta primária** — contexto num repo só é vantagem enorme
3. **GDD referencia POCs e vice-versa** — isso funciona melhor no mesmo repo
4. **O repo histórico JÁ está separado** — conversas antigas não poluem
5. **Unity tem mecanismos** de `.gitignore` que resolvem o peso

**Ação:** Manter monorepo, mas reorganizar com fronteiras claras entre áreas. O projeto Unity fica dentro do repo principal em uma pasta dedicada.

---

## 6. Recomendações de Ação Imediata

### Prioridade 1: Definir MVP Mínimo Jogável
Antes de resolver 38 POCs, definir o loop mínimo que gera uma "coisa jogável":
- 1 personagem (Guerreiro Tribal, Origem Indígena)
- 1 mapa com 3 nós (Vila, Floresta, Ruínas)
- Combate básico (D20, HP, 3 habilidades)
- 1 quest simples (ir, matar, voltar)
- Save/Load básico

### Prioridade 2: Spin-offs como Treinamento
Usar a temática e sistemas do Eras do Brasil para fazer jogos menores:
- Card game (sistema de combate simplificado)
- Idle game (sistema de Ticks + progressão)
- Quiz/trivia (lore do Brasil colonial)

### Prioridade 3: Re-priorizar Sprints para Realidade
Com 3 noites/semana, sprints de "2-3 dias" viram 2-3 semanas.
Recalibrar expectativas e marcos.

---

*Este documento serve como base para as próximas decisões. Será complementado pela sessão de organização.*
