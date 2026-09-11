# 📝 Sessão — 2026-03-07: Reorganização Total do Projeto

**Duração:** ~2h
**Agente:** Copilot (modo padrão)
**Fase:** Diagnóstico + Reorganização

---

## Contexto

O desenvolvedor retornou ao projeto após período sem trabalhar nele. Sentindo-se perdido com a quantidade de material (tudo feito por IA) e sem clareza de próximos passos. Decidiu usar o Vibe Flow para reorganizar e ter um plano realista de execução.

## O que foi feito

### 1. Exploração Completa
- Lido: ROADMAP.md, project-status.md, backlog.md, GUIA_RETOMADA.md
- Lido: Todas as POCs (5 amostradas em detalhe), ADRs, Game Pitch, docs/tech
- Lido: Sessões anteriores (2026-02-11 e 2026-02-13)
- Lido: Issues locais (1.md, 2.md, conversa.md)
- Explorado: Repo legado (ErasDoBrasil-Historico-Legado) — estrutura e conteúdo mapeados
- Listadas: 62 issues abertas no GitHub

### 2. Diagnóstico
- Criado: `vibe/research/diagnostico-completo-projeto.md`
- Identificados 6 problemas principais:
  1. Escopo descontrolado (38 POCs, 62 issues)
  2. Desconexão design vs execução (GDD 100% vs código 0%)
  3. Conhecimento fragmentado (3 IAs, meses de trabalho)
  4. Tempo limitado vs ambição
  5. Gaps de habilidade (arte, roteiro)
  6. Organização de repositórios

### 3. Decisões
- **ADR-003:** Monorepo organizado (não multi-repo)
  - Justificativa: solo dev, IA precisa de contexto único, links internos funcionam
  - Pasta `game/` para Unity, `spinoffs/` para jogos menores

### 4. Documentos Criados
- `vibe/research/diagnostico-completo-projeto.md` — Diagnóstico 360°
- `vibe/decisions/ADR-003-estrategia-repositorios.md` — Estratégia de repos
- `docs/product/plano-desenvolvimento-realista.md` — Calendário Mar-Dez 2026
- `docs/product/plano-spinoffs-aprendizado.md` — 4 spin-offs planejados
- `docs/product/mvp-o-despertar-spec.md` — Spec formal do MVP  
- `docs/product/perfil-developer.md` — Skills e limitações
- `docs/tech/contexto-repo-legado.md` — Mapa do repo histórico
- `game/README.md` — Placeholder + estrutura planejada
- `spinoffs/README.md` — Índice dos spin-offs

### 5. Atualizações
- `vibe/project-status.md` — Atualizado com novos marcos e conquistas
- Criadas pastas: `game/`, `spinoffs/01-quiz-saberes/`, `02-card-game/`, `03-idle-ticks/`, `04-escaramuca/`

## Decisões Tomadas

| # | Decisão | Justificativa |
|---|---------|---------------|
| 1 | Manter monorepo | Solo dev, contexto de IA, links internos |
| 2 | MVP precisa de 12 POCs (não 38) | Cortar é mais importante que adicionar |
| 3 | Spin-offs como ferramenta de aprendizado | Treinar Unity/C# em escopo controlado |
| 4 | Quiz primeiro, card game segundo | Web é zona de conforto — primeiro win rápido |
| 5 | ~6h/semana é o teto realista | CLT + bebê, não forçar |

## Próximos Passos

1. **Resolver Sprint 0 (Lore)** — 8 furos de consistência do GDD (Issues #20-#31)
2. **Iniciar Spin-off 1 (Quiz)** — Web puro, 50 perguntas sobre lore e história
3. **Usar `@researcher` para validar** decisões de lore antes de implementar

## Insights para Futuros Agentes

- O desenvolvedor tem mais design documentado do que qualquer projeto indie típico — o gargalo é execução, não planejamento
- Manter sessões curtas (2h max) e focadas em 1 tarefa
- Sempre que possível, mostrar algo rodando na tela ao final da sessão
- As 62 issues do GitHub estão corretas e bem organizadas — são o backlog real
- O repo legado tem conversas valiosas mas não é source of truth

---

**Próxima sessão sugerida:** Sprint 0 — resolver furo #21 (Dom da Revivência) + furo #22 (Ruptura de 1497), usando `@researcher` para analisar opções.
