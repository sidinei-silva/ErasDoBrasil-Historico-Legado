# Sessão: Auditoria de Documentação

**Data:** 2026-03-07
**Tipo:** Auditoria e Limpeza de Documentação
**Objetivo:** Identificar e corrigir contradições, duplicações, arquivos desnecessários e lacunas na documentação

---

## Escopo da Auditoria

Todos os ~120 arquivos markdown do projeto foram analisados, cruzando informações entre:
- GDD (9 livros de regras + livros de classes + enredo + design visual + dados/assets + meta)
- Documentação de produto e técnica (`docs/`)
- Vibe Flow (`vibe/`)
- Roadmap e backlog (raiz + vibe/ + gdd/99_Meta_e_Backlog/)
- Arquivos auxiliares (issues/, ia-conversations/, scripts)

---

## Contradições Encontradas e Corrigidas

### 1. Fórmula de Defesa Base — Cap. 4 vs Cap. 2/9 ✅ CORRIGIDO

**Problema:** O cabeçalho da fórmula em `gdd/01_Livro_de_Regras/04_Sistema_de_Combate.md` (linha ~510) dizia `Defesa Base = 10 + Modificador de Astúcia`, omitindo o Bônus de Armadura. Cap. 2 e Cap. 9 apresentavam a fórmula completa com armadura.

**Correção:** Fórmula atualizada para `10 + Modificador de Astúcia + Bônus de Armadura (se houver)`. Tabela explicativa atualizada para consistência. Agora Cap. 2 = Cap. 4 = Cap. 9.

### 2. 11 Contradições de Lore (já rastreadas) — PENDENTE (Sprint 0)

As contradições de lore já estão rastreadas como Issues #21–#31 no GitHub e serão resolvidas no Sprint 0. Não são novas.

---

## Duplicações Encontradas e Consolidadas

### 1. ROADMAP.md + vibe/backlog.md + docs/GUIA_RETOMADA.md ✅ CONSOLIDADO

**Problema:** Os três documentos replicavam a mesma lista de 62 issues em 7 sprints, cada um com ~100% de sobreposição estrutural. Quando uma tarefa mudasse, seria necessário atualizar 3 documentos + GitHub.

**Correção:**
- **GUIA_RETOMADA.md** → Mantido como **fonte de verdade** (o mais detalhado, com contexto e instruções)
- **ROADMAP.md** → Simplificado para **índice resumido** com tabela de sprints e links para GUIA_RETOMADA
- **vibe/backlog.md** → Simplificado para **índice de referência rápida** com links para GitHub Project #10

### 2. Game_Pitch.md vs Project Plan.md ✅ CLARIFICADO

**Problema:** 30-40% de sobreposição em visão, mecânicas e roadmap. Ambos definem a visão do jogo mas para audiências diferentes.

**Correção:** Adicionada nota de propósito/audiência no topo de cada documento:
- **Game_Pitch** → Documento externo (investidores, publishers, comunidade)
- **Project Plan** → Documento interno (equipe de desenvolvimento)

A sobreposição é *esperada e saudável* — documentos diferentes para audiências diferentes.

---

## Arquivos Desnecessários Removidos

| Arquivo | Motivo | Status |
|---------|--------|--------|
| `issues/1.md` | Redundante com GitHub Issue #21 (Dom da Revivência) | ✅ Removido |
| `issues/2.md` | Redundante com GitHub Issue #22 (Causa da Ruptura) | ✅ Removido |
| `issues/conversa.md` | Conversa com Copilot que gerou as issues — contexto histórico, não mais necessário | ✅ Removido |
| `arquivos_temporarios/` | Pasta vazia | ✅ Removido |
| `gdd/copy-markdown-files.sh` | Script legacy para copiar .md para pasta flat | ✅ Removido |
| `gdd/git-diff.sh` | Script legacy para diffs | ✅ Removido |
| `gdd/git-history.sh` | Script legacy para histórico de arquivo | ✅ Removido |
| `ia-conversations/gemini/*.md` | 2 conversas Gemini que deveriam estar no repo legado (ErasDoBrasil-Historico-Legado) | ✅ Removido |

**Total: 8 arquivos + 3 pastas removidos**

---

## Atualizações em Cadeia

| Documento | O que foi atualizado |
|-----------|---------------------|
| `docs/GUIA_RETOMADA.md` | Referência da Defesa Base atualizada (Cap. 2 vs Cap. 4 vs Cap. 9); Livros Auxiliares: 2/7 (not 1/7) |
| `vibe/project-status.md` | Fase atual atualizada com menção à auditoria; nova conquista adicionada |
| `vibe/backlog.md` | Consolidado de ~170 linhas para ~50 linhas (índice de referência) |
| `ROADMAP.md` | Consolidado de ~230 linhas para ~90 linhas (índice resumido) |

---

## Documentação Faltante (Planejada)

Livros Auxiliares referenciados no GDD mas que ainda não existem:

| Livro | Sprint Planejado | Issue |
|-------|-----------------|-------|
| Livro de Habilidades | Sprint 1 | #33 |
| Livro de Proficiências de Vida | Sprint 1 | #35 |
| Bestiário Ato 1 | Sprint 1 | #36 |
| Livro de Magias e Rituais | Sprint 6+ (pós-MVP) | — |
| Livro de Receitas de Crafting | Fase 2 (pós-MVP) | — |

> **Nota:** Estes NÃO são bugs ou falhas — são deliverables planejados. O GDD referencia esses livros como "a serem criados".

### Links Wiki-style (`[[📘 ...]]`)

Existem 10 referências no formato wiki-style (Obsidian) nos capítulos 6 e 9 do GDD que não são links markdown válidos. Eles são referências futuras a livros que serão criados. Não foram convertidos agora porque a maioria dos destinos ainda não existe.

---

## Observações Adicionais

1. **Qualidade geral**: A documentação do projeto é excelente em profundidade e organização. A auditoria confirmou que a maioria dos documentos está bem conectada e consistente.

2. **Roadmap de Desenvolvimento** (`gdd/99_Meta_e_Backlog/02_Roadmap_Desenvolvimento.md`): Complementar ao ROADMAP.md sem duplicação — foco técnico com POCs detalhadas. Mantido sem alterações.

3. **Estratégia de Dados** (`gdd/99_Meta_e_Backlog/01_Estrategia_de_Dados_e_Documentacao.md`): Documento único e valioso que define a filosofia "Alma vs. Lógica". Sem problemas.

4. **ADRs** (`vibe/decisions/`): Todos bem formatados e completos. Sem problemas.

5. **Sessions** (`vibe/sessions/`): Logs históricos intactos e valiosos. Sem problemas.

---

**Resultado:** Projeto auditado e limpo. Pronto para Sprint 0 (Correções de Lore).
