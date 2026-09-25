# Sessão: Revisão de Produto e MVP — Análise de Gaps

**Data:** 2026-03-07
**Agente:** @product-manager
**Objetivo:** Revisar se o planejamento existente está alinhado com a pesquisa de mercado. Identificar gaps e documentá-los — sem reescrever o que já funciona.

---

## Contexto da Sessão

Após a **pesquisa de mercado** (sessão anterior), o usuário pediu para:
> "Revisar se está tudo ok e documentar no vibe flow. Veja se tem algum gap do que já está planejado — tanto nos docs aqui dentro do projeto como em issues no GitHub."

### Fontes consultadas nesta sessão

| Fonte | Conteúdo |
|-------|---------|
| `docs/product/mvp-o-despertar-spec.md` | Escopo formal do MVP |
| `docs/product/plano-desenvolvimento-realista.md` | Calendário Mar-Dez 2026 |
| `docs/product/perfil-developer.md` | Capacidades e limitações do dev |
| `docs/product/plano-spinoffs-aprendizado.md` | Estratégia de aprendizado via jogos menores |
| `ROADMAP.md` | Estrutura de sprints e fases |
| `vibe/backlog.md` | Backlog com 62 issues |
| `vibe/research/2026-03-07-pesquisa-mercado.md` | Pesquisa de mercado (sessão anterior) |
| `gdd/Game_Pitch.md` | Documento de apresentação externa |
| **GitHub Issues #20–#81** | 62 issues ativos, todas consultadas via API |

---

## Veredicto Geral: O Planejamento Está Sólido ✅

**90% do planejamento existente está correto e bem estruturado.** Não há necessidade de refazer nada. O MVP é mínimo de verdade, o escalonamento de sprints é lógico e o plano de desenvolvimento respeita a realidade do desenvolvedor solo com ~6h/semana.

Os gaps identificados são **complementares** — não contradizem o que existe. São peças que faltam em áreas específicas (estratégia de go-to-market, decisões técnicas precoces).

---

## O Que Está SÓLIDO (sem gaps)

### ✅ Escopo do MVP "O Despertar"
- 1 Origem (Indígena), 1 Classe (Guerreiro Tribal Tier 1) — correto para validar o core loop
- 3 nós de mapa, combate estático D20, 3 inimigos, 1 quest hardcoded — minimal e jogável
- 12 POCs necessárias bem definidas (01, 02, 03, 06, 07, 08, 17, 18, 19, 24, 28, 33)
- **Co-op FORA do MVP** — decisão correta, dev solo não tem como entregar co-op P2P em MVP

### ✅ Estrutura de Sprints e Issues
- 62 issues bem escritas, com critérios de aceite claros
- Dependências entre POCs documentadas
- Epics de agrupamento para cada sprint

### ✅ Gaps de Narrativa (Rastreados)
- Issue #60 ("O Maior Gap do Projeto") já identifica: zero diálogos escritos, zero schema JSON para diálogos
- Totalmente reconhecido, no Sprint 1 como `critical`
- Não precisa de ação nova aqui

### ✅ Game Feel Infrastructure (Rastreado)
- Issue #71 ("Epic: Game Feel") lista tudo que falta: Tutorial, Main Menu, Audio, Acessibilidade, Localização
- Corretamente diferido para Sprint 6+ (pós-MVP faz sentido para um solo dev)
- Main Menu (#73) e Tutorial (#72) incluídos no Sprint 5 — adequado para apresentabilidade do MVP

### ✅ Plano de Spin-offs
- Card Game "Duelos da Ruptura" + Idle "Ticks da Raiz" = estratégia inteligente para aprender Unity/C#/pixel art
- Mitiga o risco de bloqueio técnico no projeto principal

### ✅ Decisões de Arquitetura
- ADR-001 (Organização Unity) e ADR-002 (Workflow UI/UX) documentados
- Stack Unity LTS + C# + NGO (para co-op futuro) = escolha sólida

---

## Gaps Identificados

### 🔴 GAP 1 — Estratégia de Lançamento no Steam / Early Access
**Severidade:** Alta | **Status:** Não existe nenhum issue ou doc

**O Problema:**
A pesquisa de mercado valida o modelo de Early Access (Wartales: 1M+ cópias; Divinity OS2: Metacritic 93-95 com EA). O projeto tem uma Fase 5 "Release" no roadmap, mas **não existe nenhuma definição** de:
- EA vs. lançamento completo?
- Quando abrir a página no Steam para acumular wishlists?
- Meta de wishlists antes de abrir EA?
- Faixa de preço target?

**Por que importa agora:**
Para o Wartales style, a página no Steam deveria ir ao ar ~6-12 meses antes do EA. Se o MVP "O Despertar" está previsto para Out/Nov 2026, a página no Steam deveria ir ao ar em ~Abr-Mai 2026 — **que é quando o dev estará no Sprint 2 (Unity foundation)**. Decidir isso sem pressa atual evita urgência depois.

**Ação sugerida:**
- Criar issue: `🚀 Definir Estratégia de Lançamento Steam / Early Access`
- Labels: `product`, `strategy`, `sprint-6+`
- Documentar em `docs/product/estrategia-lancamento.md` após decisão

---

### 🟡 GAP 2 — Estratégia de Comunicação do Co-op P2P
**Severidade:** Média | **Status:** Não rastreado

**O Problema:**
A pesquisa de mercado identifica o co-op P2P para 2 jogadores como **o maior diferencial inexplorado no gênero de tactical RPG**. O Game Pitch (`gdd/Game_Pitch.md`) já lista co-op como um dos 5 pilares inegociáveis:
> "Uma campanha que pode ser jogada 100% solo ou com um amigo em um modelo P2P"

Mas a spec do MVP tem co-op como "Muito cedo" e defere para Fase 5.

**O risco:**
Se o jogo for lançado no Steam sem a página comunicar claramente o roadmap de co-op, players que buscam co-op não vão wishlisted.

**O que não está documentado:**
- Como comunicar "co-op vem no futuro" de forma que gere antecipação, não decepção
- Quando no roadmap co-op deve ser apresentável (não necessariamente funcional, mas comunicado com data)
- Se há um milestone intermediário de validação técnica (ex.: uma mini POC de P2P no Sprint 6+ antes do release)

**Ação sugerida:**
- Criar issue: `📢 Definir Estratégia de Comunicação do Co-op P2P`
- Doc de 1 página em `vibe/scratchpad/coop-communication-strategy.md`

---

### 🟡 GAP 3 — Posicionamento da Cultura Brasileira (Marketing/Messaging)
**Severidade:** Média | **Status:** Implícito no GDD, não formalizado

**O Problema:**
A pesquisa de mercado afirma: **"zero concorrentes no gênero tactical RPG com cultura sul-americana/brasileira"** — este é o diferencial geográfico/cultural mais importante. O GDD e o Game Pitch descrevem bem a ambientação, mas não há um documento que defina:
- Como comunicar esse diferencial para um público internacional (EN)
- Quais elementos culturais são os "ganchos" para marketing (Ruptura como mecânica + metáfora histórica, por exemplo)
- O tom da comunicação: educativo? mítico? épico?

**Ação sugerida:**
- Adicionar seção "Posicionamento e Mensagem" ao `gdd/Game_Pitch.md` (ou criar `docs/product/positioning.md`)
- Pode ser feito como parte do processo de preparação da página Steam

---

### 🟢 GAP 4 — Decisão de Arquitetura i18n (Localização)
**Severidade:** Baixa-Média | **Status:** Issue #77 existe, mas mal posicionado

**O Problema:**
Issue #77 "Definir Estratégia de Localização (i18n)" está no Sprint 6+. O próprio issue afirma:
> "Fazer isso depois é 10x mais caro que fazer desde o início"

A decisão de **se** usar Unity Localization Package vs. JSON keys vs. texto direto — precisa ser tomada **antes de escrever os diálogos** (Sprint 1). Não precisa implementar i18n no MVP, mas o schema dos diálogos JSON (#62) deveria já estar preparado para suportar múltiplos idiomas.

**Ação sugerida:**
- Mover a **decisão** (ADR) do #77 para Sprint 1 ou Sprint 2
- A implementação continua em Sprint 6+
- Vincular decisão ao design dos schemas JSON de diálogo (#62)

---

## O Que NÃO É um Gap (confirmado)

| Item | Avaliação |
|------|-----------|
| Co-op fora do MVP | ✅ Correto — dev solo, 6h/semana, não é viável |
| Arte pixel art iniciante | ✅ Mitigado pelo plano de spin-offs |
| Narrativa/diálogos faltando | ✅ Rastreado como #60 (critical, Sprint 1) |
| Game Feel (audio, menus, etc.) | ✅ Rastreado como #71 (Sprint 6+, com Main Menu no Sprint 5) |
| Schemas JSON faltantes | ✅ Rastreado como #67/#68 (Sprint 2) |
| Fases pós-MVP muito vagas | ✅ Intencional — sprint 6+ é icebox para o futuro |

---

## Recomendações de Ação (Priorizadas)

### Imediato (antes de começar Sprint 0)
1. **Criar issue** para estratégia de lançamento Steam/EA (GAP 1)
2. **Mover a parte de decisão** do issue #77 de Sprint 6+ para Sprint 2

### Curto prazo (durante Sprint 1)
3. **Adicionar nota** no Game Pitch ou criar primeiro rascunho de positioning co-op (GAP 2)
4. **Garantir** que schema JSON de diálogos (#62) já prevê campo de idioma multi-lingua

### Médio prazo (Sprint 4-5, antes do playtest)
5. **Definir** estratégia de lançamento Steam/EA (GAP 1 — com data alvo Apr-May 2026 para página ir ao ar, se o MVP está previsto Out/Nov 2026)

---

## Issues para Criar (sugestão)

```
🚀 Definir Estratégia de Lançamento Steam / Early Access
  Sprint: sprint-6+
  Labels: product, strategy
  Conteúdo: EA ou full release? quando abrir Steam? meta de wishlists? pricing?

📢 Definir Estratégia de Comunicação do Co-op P2P
  Sprint: sprint-6+
  Labels: product, strategy, narrative
  Conteúdo: como comunicar "co-op vem no futuro" no Steam e redes sociais?
```

---

## Status Atual do Planejamento (atualizado)

| Área | Status | Notas |
|------|--------|-------|
| Visão de Produto | ✅ Sólida | GDD + Game Pitch bem definidos |
| MVP "O Despertar" | ✅ Sólido | Minimal, realista, rastreado |
| Sprint 0-5 (Backlog) | ✅ Sólido | 62 issues bem definidas |
| Plano de Desenvolvimento | ✅ Sólido | Mar-Dez 2026, realista |
| Go-to-Market / Steam | 🔴 Faltando | GAP 1 — sem issue, sem doc |
| Comunicação do Co-op | 🟡 Incompleto | GAP 2 — implícito, não formalizado |
| Posicionamento Cultural | 🟡 Incompleto | GAP 3 — existe no GDD, falta messaging |
| Decisão i18n | 🟡 Atrasado | GAP 4 — issue #77 mal posicionado no tempo |

---

## Decisão do Usuário (2026-03-07)

> "Acredito que esses gaps apontados não são relevantes para agora — vou deixar eles para depois."

**Todos os 4 gaps foram identificados, avaliados e conscientemente adiados.** O foco atual é a execução: Sprint 0 → POCs → MVP "O Despertar".

Os gaps ficam registrados aqui para consulta futura quando chegar a fase de go-to-market (pré-Steam / pré-release).

## Próximo Passo

**→ Iniciar Sprint 0** — Correções de Lore (issues #20–#31).
