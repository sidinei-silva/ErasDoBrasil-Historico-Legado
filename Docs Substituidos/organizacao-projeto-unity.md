# 🏗️ Organização do Projeto Unity — POCs e Jogo Final

> **⚠️ ARQUIVADO:** Este documento foi **substituído** pelo [ADR-004 — Pivot MMORPG Servidor Go](../../vibe/decisions/ADR-004-pivot-mmorpg-servidor-go.md). O projeto migrou de Unity/C# para servidor Go + cliente web.
>
> **Decisão original:** [ADR-001](../../vibe/decisions/ADR-001-organizacao-projeto-unity.md) (status: Substituído)

---

## Visão Geral

O projeto "Eras do Brasil" usa **um único projeto Unity** para todas as 38 POCs e o jogo final. Não existem projetos separados. A separação é feita por **cenas** (sandboxes de teste) e **módulos de código** (namespaces C#).

```
POCs (Cenas isoladas)  ───►  MVP (Cena integrada)  ───►  Jogo Final (Cenas expandidas)
     mesmos scripts              mesmos scripts              mesmos scripts (refinados)
```

---

## Estrutura de Pastas Unity

```
ErasDoBrasil/                              ← Projeto Unity
├── Assets/
│   ├── Scripts/                           ← Código de produção (organizado por módulo)
│   │   ├── Core/                          ← Motor de regras, D20, atributos
│   │   │   ├── DiceRoller.cs
│   │   │   ├── AttributeSystem.cs
│   │   │   └── TierScaling.cs
│   │   ├── Data/                          ← ScriptableObjects, loaders
│   │   │   ├── ClasseSO.cs
│   │   │   ├── ItemSO.cs
│   │   │   └── JsonDataLoader.cs
│   │   ├── World/                         ← Ticks, navegação, eventos
│   │   │   ├── TickEngine.cs
│   │   │   ├── BlockNavigation.cs
│   │   │   └── WorldEventSystem.cs
│   │   ├── Combat/                        ← Combate, status, habilidades
│   │   │   ├── CombatManager.cs
│   │   │   ├── StatusCondition.cs
│   │   │   └── AbilitySystem.cs
│   │   ├── Economy/                       ← Inventário, crafting, comércio
│   │   │   ├── Inventory.cs
│   │   │   └── CraftingSystem.cs
│   │   ├── NPC/                           ← IA, rotinas, fofoca
│   │   │   ├── NPCRoutine.cs
│   │   │   └── UtilityAI.cs
│   │   ├── UI/                            ← HUD, menus, telas
│   │   │   ├── HUDController.cs
│   │   │   ├── NodeMapUI.cs
│   │   │   └── CombatUI.cs
│   │   ├── Persistence/                   ← Save/Load
│   │   │   └── SaveLoadManager.cs
│   │   ├── Network/                       ← P2P, sincronia
│   │   │   └── P2PManager.cs
│   │   └── Narrative/                     ← Quests, diálogos
│   │       ├── QuestSystem.cs
│   │       └── DialogueManager.cs
│   │
│   ├── Resources/
│   │   ├── ScriptableObjects/             ← Templates imutáveis
│   │   │   ├── Classes/
│   │   │   ├── Items/
│   │   │   └── Enemies/
│   │   └── JSON/                          ← Dados iniciais e saves
│   │
│   ├── Scenes/
│   │   ├── POC/                           ← 1 cena por POC (sandboxes de teste)
│   │   │   ├── POC01_FundacaoDados.unity
│   │   │   ├── POC02_MotorD20.unity
│   │   │   ├── POC03_AtributosCriacao.unity
│   │   │   └── ...
│   │   ├── MVP/                           ← Cenas do MVP integrado
│   │   │   └── MVP_Main.unity
│   │   └── Game/                          ← Cenas do jogo final (Fase 2+)
│   │
│   ├── Tests/
│   │   ├── EditMode/                      ← Testes unitários (sem cena)
│   │   │   ├── Core/
│   │   │   ├── Combat/
│   │   │   └── World/
│   │   └── PlayMode/                      ← Testes com cena
│   │
│   ├── Art/
│   │   ├── Placeholder/                   ← Retângulos coloridos, sprites teste
│   │   └── Final/                         ← Pixel art final (Fase 3+)
│   │
│   └── Prefabs/
│       ├── UI/
│       └── Characters/
│
├── Packages/
└── ProjectSettings/
```

---

## Mapeamento POC → Pasta de Script

| POC | Módulo | Pasta |
|-----|--------|-------|
| 01 — Fundação de Dados | A | `Scripts/Data/` |
| 02 — Motor D20 | A | `Scripts/Core/` |
| 03 — Atributos e Criação | A | `Scripts/Core/` |
| 04 — Tier Scaling | A | `Scripts/Core/` |
| 05 — Herança de Habilidades | A | `Scripts/Core/` |
| 06 — Matriz de Itens 5×5 | A | `Scripts/Data/` + `Scripts/Economy/` |
| 07 — Motor de Ticks | B | `Scripts/World/` |
| 08 — Navegação por Blocos | B | `Scripts/World/` |
| 09–11 — Eventos, Relógio, Clima | B | `Scripts/World/` |
| 12–16 — NPCs e IA | C | `Scripts/NPC/` |
| 17–23 — Combate | D | `Scripts/Combat/` |
| 24–27 — Economia | E | `Scripts/Economy/` |
| 28–32 — UI | F | `Scripts/UI/` |
| 33 — Save/Load | G | `Scripts/Persistence/` |
| 34–36 — Rede P2P | G | `Scripts/Network/` |
| 37–38 — Quests e Narrativa | H | `Scripts/Narrative/` |

---

## Namespaces C#

Cada módulo usa um namespace para evitar conflitos e manter organização:

```csharp
namespace ErasDoBrasil.Core { }       // Motor de regras, D20, atributos
namespace ErasDoBrasil.Data { }       // ScriptableObjects, loaders
namespace ErasDoBrasil.World { }      // Ticks, navegação, eventos
namespace ErasDoBrasil.Combat { }     // Combate, status, habilidades
namespace ErasDoBrasil.Economy { }    // Inventário, crafting
namespace ErasDoBrasil.NPC { }        // IA, rotinas, fofoca
namespace ErasDoBrasil.UI { }         // HUD, menus
namespace ErasDoBrasil.Persistence { } // Save/Load
namespace ErasDoBrasil.Network { }    // P2P
namespace ErasDoBrasil.Narrative { }  // Quests, diálogos
```

---

## FAQ

### As POCs ficam em pastas separadas do jogo?
**Não.** Os scripts ficam na mesma pasta de produção. O que é separado são as **cenas** (Scenes/POC/ vs Scenes/MVP/).

### E se uma POC ficar obsoleta?
A cena de POC pode ser deletada ou mantida como sandbox de debug. O código em `Scripts/` já faz parte do jogo.

### Como testar uma POC isoladamente?
Abra a cena em `Scenes/POC/POC_XX.unity`. Cada cena tem seus próprios GameObjects de teste que referenciam os scripts de produção.

### E os assets placeholder?
Ficam em `Art/Placeholder/`. Na Fase 3 (Alpha), são substituídos por pixel art final em `Art/Final/`. Scripts de UI referenciam sprites via SerializeField, facilitando a troca.

---

**Referências:**
- [ADR-001 — Organização do Projeto Unity](../../vibe/decisions/ADR-001-organizacao-projeto-unity.md)
- [POCs — Índice Mestre](../../pocs/README.md)
- [Sprint 4 — Setup Unity](../../docs/GUIA_RETOMADA.md)
