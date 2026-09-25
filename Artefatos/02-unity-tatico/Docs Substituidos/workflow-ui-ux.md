# 🎨 Workflow de UI/UX — Wireframes, Prototipagem e Design de Interface

> **⚠️ ARQUIVADO:** Este documento foi **substituído** pelo [ADR-004 — Pivot MMORPG Servidor Go](../../vibe/decisions/ADR-004-pivot-mmorpg-servidor-go.md). O workflow de UI/UX será redefinido para HTML/CSS/JS.
>
> **Decisão original:** [ADR-002](../../vibe/decisions/ADR-002-workflow-ui-ux.md) (status: Substituído)

---

## Visão Geral

O projeto já possui **especificações detalhadas de UI** no GDD (`gdd/04_Design_Visual/`), mas faltava um processo formal para traduzir essas specs em interfaces implementáveis. Este documento define **quando e como** fazer UI/UX ao longo das sprints.

```
Specs do GDD        →  Wireframes (Sprint 4)  →  Protótipo (Sprint 6)  →  POCs de UI (Sprint 6-7)
(o QUE existe)         (COMO vai ficar)           (COMO funciona)          (implementação)
```

---

## Documentação Existente de UI/UX

O GDD **já define** a direção visual e os layouts. Estes documentos são a **spec de referência** para wireframes e implementação:

| Documento | Conteúdo | Status |
|-----------|----------|--------|
| [Estilo Visual Geral](../../gdd/04_Design_Visual/01_Estilo_Visual_Geral.md) | Pixel art, paleta, proporções (32x32) | ✅ Completo |
| [UI, HUD e Tipografia](../../gdd/04_Design_Visual/02_UI_HUD_e_Tipografia.md) | Molduras, botões, barras, fontes | ✅ Completo |
| [UI Fase 1 — Exploração e Combate](../../gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md) | HUD, Mapa de Nós, Tela de Cena, Tela de Combate | ✅ Completo |
| [UI Fase 2 — Grid Tático](../../gdd/04_Design_Visual/06_UI_Fase_2_Combate_Tatico.md) | Grid, Trilha de Iniciativa, Preview de ação | ✅ Completo |
| [Assets, Ícones e Cenários](../../gdd/04_Design_Visual/03_Assets_Icones_e_Cenarios.md) | Lista de assets necessários | ✅ Completo |
| [Diretrizes Técnicas](../../gdd/04_Design_Visual/04_Diretrizes_Tecnicas_e_Exportacao.md) | Exportação, resolução, 9-slice | ✅ Completo |

> **O que faltava:** Um processo para transformar essas specs **em layouts visuais concretos** antes de implementar no Unity.

---

## Workflow por Sprint

### Sprint 4 — Wireframes de Baixa Fidelidade

**Quando:** Junto com o setup do projeto Unity (não bloqueia código).

**O que fazer:**
1. Criar wireframes simples (esboços) para as **4 telas principais** do MVP:
   - **HUD Principal** — Barra superior (retrato, PV/XP, recursos, relógio)
   - **Mapa de Nós** — Pergaminho com nós clicáveis conectados por trilhas
   - **Tela de Cena (Split)** — Ilustração esquerda + texto/botões direita
   - **Tela de Combate Estático** — Sprites inimigos + personagem + hotbar + log

2. Basear nos layouts descritos em [`05_UI_Fase_1_Exploracao_e_Combate.md`](../../gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md)

3. Salvar em `docs/tech/wireframes/`

**Ferramenta sugerida:** [Excalidraw](https://excalidraw.com/) (gratuito, exporta PNG/SVG, arquivos versionáveis no git)

**Saída:** 4 wireframes PNG + arquivos fonte

---

### Sprint 6 — Protótipo Navegável + POCs de UI

**Quando:** Antes de implementar as POCs de UI (28, 29, 30, 31, 32).

**O que fazer:**
1. Refinar wireframes com feedback das POCs de lógica (Sprints 4-5)
2. Criar **protótipo navegável** — pode ser:
   - Diretamente no **Unity UI Toolkit** (preferível — já é a implementação)
   - Ou no **Figma** (se quiser iterar mais rápido antes do Unity)
3. Validar o fluxo completo:
   ```
   Menu Inicial → Criação de Personagem → Mapa de Nós → Tela de Cena → Combate → Inventário → Save
   ```
4. Testar: legibilidade, hierarquia visual, feedback de ações, responsividade

**Saída:** Protótipo funcional + wireframes atualizados

---

### Sprint 7 — Validação Integrada (Playtest)

**Quando:** Durante o primeiro playtest do MVP (Tarefa 7.2).

**O que fazer:**
1. Avaliar a UI como parte da experiência jogável:
   - O jogador entende o HUD sem explicação?
   - A navegação no mapa é intuitiva?
   - O combate tem feedback visual suficiente?
   - Os botões de ação são claros?
2. Documentar problemas de usabilidade encontrados
3. Priorizar ajustes para iteração pós-MVP

**Saída:** Lista de ajustes de UI/UX para próximas iterações

---

## Telas do MVP (Fase 1)

Baseado nas specs do GDD, as telas que precisam de wireframe/implementação para o MVP são:

### 1. HUD Principal
- Barra superior com: Retrato + PV/XP | Recursos (Madeira, Pedra, Ervas) | Moeda | Relógio de Ticks
- Ref: [UI Fase 1 §1](../../gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md)

### 2. Mapa de Nós (Exploração)
- Pergaminho central com ícones: ? (inexplorado), Fogueira, Caveira, Cidade
- Linhas pontilhadas entre nós, animação de token ao mover
- Ref: [UI Fase 1 §2](../../gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md)

### 3. Tela de Cena (Split-Screen)
- Esquerda: Ilustração pixel art do local
- Direita: Título + texto descritivo + menu de ações (botões numerados)
- Ref: [UI Fase 1 §3](../../gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md)

### 4. Tela de Combate Estático
- Superior: Sprites de inimigos
- Inferior: Sprite do personagem
- Rodapé: Hotbar (ATACAR, HABILIDADE, ITEM, DEFENDER/FUGIR)
- Lateral: Log de combate com matemática
- Ref: [UI Fase 1 §4](../../gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md)

### 5. Inventário
- Grid de itens com tooltip (nome, stats, qualidade/raridade)
- Slots de equipamento (arma, armadura, acessório)
- Ref: POC 24

### 6. Criação de Personagem (Simplificada para MVP)
- Tela única: Origem (fixa: Indígena) → Classe (fixa: Guerreiro Tribal) → Point-buy de atributos → Confirmar
- Versão completa com múltiplas etapas é da Fase 2 (POC 32)

---

## Fases Futuras de UI/UX

| Fase | O que adicionar | Quando |
|------|----------------|--------|
| **Fase 2 (Pré-Alpha)** | Tela de criação completa, UI de diálogos, UI de crafting | Após MVP |
| **Fase 3 (Alpha)** | Pixel art final para todas as telas, animações de UI, estética marajoara | Após Pré-Alpha |
| **Fase 4 (Beta)** | Grid tático, trilha de iniciativa, preview de ação, cobertura visual | Após Alpha |
| **Fase 5 (Release)** | Telas de multiplayer (lobby, chat, trade), tutorial | Após Beta |

---

## Armazenamento de Artefatos

```
docs/tech/wireframes/
├── hud-principal.png              ← Wireframe do HUD
├── mapa-de-nos.png                ← Wireframe do mapa
├── tela-de-cena.png               ← Wireframe da cena split
├── tela-de-combate.png            ← Wireframe do combate
├── inventario.png                 ← Wireframe do inventário
└── criacao-personagem.png         ← Wireframe da criação
```

---

**Referências:**
- [ADR-002 — Workflow de UI/UX](../../vibe/decisions/ADR-002-workflow-ui-ux.md)
- [UI Fase 1 — Exploração e Combate](../../gdd/04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md)
- [UI Fase 2 — Grid Tático](../../gdd/04_Design_Visual/06_UI_Fase_2_Combate_Tatico.md)
- [UI, HUD e Tipografia](../../gdd/04_Design_Visual/02_UI_HUD_e_Tipografia.md)
