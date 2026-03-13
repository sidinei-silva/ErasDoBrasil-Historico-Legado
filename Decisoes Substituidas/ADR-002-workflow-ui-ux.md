# ADR-002: Workflow de UI/UX — Wireframes, Prototipagem e Design de Interface

## Status

Substituído por [ADR-004](ADR-004-pivot-mmorpg-servidor-go.md)

> **Nota:** O projeto migrou de Unity/C# para servidor Go + cliente web. O workflow de UI/UX será redefinido para HTML/CSS/JS.

## Contexto

O GDD já possui documentação de design visual detalhada em `gdd/04_Design_Visual/`:
- Estilo visual geral, paleta e proporções
- UI/HUD e tipografia
- UI Fase 1 (Exploração e Combate Estático) — layouts detalhados
- UI Fase 2 (Grid Tático) — layouts detalhados
- Diretrizes técnicas de exportação

Porém, **não existe nenhuma etapa formal de UI/UX** no roadmap ou nas sprints:
- Nenhuma tarefa de criação de **wireframes**
- Nenhum momento previsto para **prototipagem de interface**
- Nenhuma validação de **usabilidade** antes de implementar as POCs de UI (Módulo F)
- As POCs de UI (28–32) foram planejadas para implementação direta, sem um passo de design intermediário

Isso cria um risco: implementar a UI diretamente a partir das specs escritas, sem uma etapa visual intermediária, pode resultar em retrabalho significativo quando os layouts não funcionarem na prática.

## Decisão

Incorporar um **workflow de UI/UX leve** ao roadmap existente, adicionando etapas de wireframe e prototipagem **antes das POCs de UI**, sem criar uma sprint nova nem atrasar o cronograma.

### Workflow Definido

```
Specs de Design (GDD)  →  Wireframes (Baixa Fidelidade)  →  Protótipo Navegável  →  POC Unity
─────────────────────────────────────────────────────────────────────────────────────────────────
gdd/04_Design_Visual/   →  docs/tech/wireframes/          →  Figma/Excalidraw      →  Scenes/POC/
(Já existem ✅)          (Sprint 4)                        (Sprint 6)               (Sprints 6-7)
```

### Etapas por Sprint

#### Sprint 4 — Wireframes Básicos (junto com Setup Unity)
- Criar wireframes de **baixa fidelidade** (esboços simples) para as 4 telas principais:
  1. **HUD Principal** — Barra superior com retrato, PV/XP, recursos, relógio
  2. **Mapa de Nós** — Layout do pergaminho com nós clicáveis
  3. **Tela de Cena (Split)** — Ilustração à esquerda + texto/ações à direita
  4. **Tela de Combate** — Sprites + hotbar + log de combate
- Ferramenta sugerida: **Excalidraw** (gratuito, versionável como `.excalidraw` ou exportar PNG)
- Armazenar em: `docs/tech/wireframes/`
- Base: Especificações de `gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md`

#### Sprint 6 — Protótipo e Validação (junto com POCs de UI)
- Antes de implementar as POCs de UI (28, 29, 30, 31, 32):
  1. Transformar wireframes em **protótipos navegáveis** (Figma, ou diretamente no Unity UI Toolkit)
  2. Validar o fluxo: Menu → Criação → Mapa → Cena → Combate → Inventário
  3. Testar legibilidade, hierarquia visual e feedback
- Saída: Wireframes atualizados com ajustes + protótipo funcional como base para as POCs

#### Sprint 7 — Validação Integrada (MVP)
- Durante o playtest (Tarefa 7.2), avaliar a UI como parte da experiência:
  - O jogador entende o HUD?
  - A navegação no mapa é intuitiva?
  - O combate tem feedback visual suficiente?
- Saída: Lista de ajustes de UI para iteração pós-MVP

### O Que NÃO Fazer Agora

- ❌ Design completo de UI para Fase 2 (Grid Tático) — isso é da Fase 4 (Beta)
- ❌ Design de telas de multiplayer — isso é da Fase 5 (Release)
- ❌ Pixel art final para UI — placeholders são suficientes até a Fase 3 (Alpha)
- ❌ Contratar/usar ferramentas pagas de design — manter leve e gratuito

### Relação com a Documentação Existente

| Documento Existente | Papel no Workflow |
|---|---|
| `gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md` | **Spec de referência** — descreve O QUE deve existir nas telas |
| `gdd/04_Design_Visual/06_UI_Fase_2_Combate_Tatico.md` | **Spec futura** — para quando o grid tático for implementado (Fase 4) |
| `gdd/04_Design_Visual/02_UI_HUD_e_Tipografia.md` | **Guia de estilo** — molduras, botões, fontes |
| `docs/tech/wireframes/` (NOVO) | **Wireframes** — tradução visual das specs para layouts concretos |
| `docs/tech/workflow-ui-ux.md` (NOVO) | **Processo** — como e quando trabalhar UI/UX |

## Consequências

**Positivas:**
- Reduz retrabalho nas POCs de UI (validar layout antes de implementar)
- Cria um artefato visual (wireframe) que facilita comunicação e revisão
- Integra UI/UX ao fluxo existente sem criar sprints extras
- A documentação existente do GDD serve como base sólida

**Negativas:**
- Adiciona tarefas às Sprints 4 e 6 (estimativa +0.5-1 dia por sprint)
- Wireframes de baixa fidelidade ainda podem divergir da implementação final
- Exige disciplina para atualizar wireframes quando as specs mudarem

## Alternativas Consideradas

- **Sprint dedicada de UI/UX antes das POCs:** Rejeitada — atrasa o cronograma e as POCs de lógica (Módulo A) não dependem de UI
- **Implementar UI direto sem wireframe:** Rejeitada — risco alto de retrabalho, especialmente para o layout split-screen do Roadwarden
- **Usar o Unity como ferramenta de prototipagem desde o início:** Parcialmente aceita — na Sprint 6, o protótipo pode ser feito diretamente no Unity UI Toolkit
