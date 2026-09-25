# ADR-001: Organização do Projeto Unity — Projeto Único para POCs e Jogo

## Status

Substituído por [ADR-004](ADR-004-pivot-mmorpg-servidor-go.md)

> **Nota:** O projeto migrou de Unity/C# para servidor Go + cliente web. Esta ADR não se aplica mais.

## Contexto

O projeto "Eras do Brasil" tem 38 POCs (Provas de Conceito) organizadas em 8 módulos e um jogo final que integra todas as mecânicas validadas. Ao iniciar a Sprint 4 (Setup Unity), surgiu a dúvida: **devemos usar um projeto Unity separado para cada POC ou um projeto único para tudo?**

Pontos a considerar:
- As POCs são progressivas — cada uma reutiliza código das anteriores
- O roadmap prevê integrar as POCs diretamente no MVP (Sprint 7)
- Manter múltiplos projetos Unity gera overhead de setup, duplicação de assets e dificuldade de integração
- O GDD já define uma estrutura de pastas clara para organizar o código por módulo

## Decisão

**Usar um único projeto Unity para POCs e jogo final**, com separação por **cenas e namespaces**, não por projetos.

### Estrutura Definida

```
ErasDoBrasil/                          ← Projeto Unity (raiz)
├── Assets/
│   ├── Scripts/
│   │   ├── Core/                      ← Motor de regras, D20, atributos (Módulo A)
│   │   ├── World/                     ← Ticks, navegação, eventos (Módulo B)
│   │   ├── NPC/                       ← IA, rotinas, fofoca (Módulo C)
│   │   ├── Combat/                    ← Combate, status, habilidades (Módulo D)
│   │   ├── Economy/                   ← Inventário, crafting, comércio (Módulo E)
│   │   ├── UI/                        ← HUD, menus, cenas (Módulo F)
│   │   ├── Persistence/               ← Save/Load (Módulo G)
│   │   ├── Network/                   ← P2P, sincronia (Módulo G)
│   │   └── Narrative/                 ← Quests, diálogos (Módulo H)
│   ├── Resources/
│   │   ├── ScriptableObjects/
│   │   └── JSON/
│   ├── Scenes/
│   │   ├── POC/                       ← Cenas isoladas de teste (1 por POC)
│   │   │   ├── POC01_FundacaoDados.unity
│   │   │   ├── POC02_MotorD20.unity
│   │   │   └── ...
│   │   ├── MVP/                       ← Cenas do MVP integrado
│   │   │   └── MVP_Main.unity
│   │   └── Game/                      ← Cenas do jogo final (fases posteriores)
│   ├── Tests/
│   │   ├── EditMode/                  ← Testes unitários (C# puro)
│   │   └── PlayMode/                  ← Testes de integração (com cena)
│   ├── Art/                           ← Sprites, animações, UI art
│   │   ├── Placeholder/              ← Assets temporários para POCs
│   │   └── Final/                    ← Assets finais (Fase 3+)
│   └── Prefabs/
├── Packages/
└── ProjectSettings/
```

### Regras de Organização

1. **Scripts são organizados por módulo funcional**, não por POC. O código da POC 01 fica em `Scripts/Core/`, da POC 07 em `Scripts/World/`, etc.
2. **Cada POC tem sua própria cena** em `Scenes/POC/`, servindo como sandbox de teste isolado.
3. **O código é escrito para produção desde o início** — não existe código "de POC" descartável. Cada script é pensado para ser reutilizado no MVP e nas fases seguintes.
4. **Namespaces C# seguem a estrutura de pastas**: `ErasDoBrasil.Core`, `ErasDoBrasil.Combat`, `ErasDoBrasil.World`, etc.
5. **Testes unitários acompanham o código** — cada POC deve ter testes em `Tests/EditMode/` validando a lógica.

### Como as POCs se Relacionam com o Jogo Final

```
POC (Validação)     →  MVP (Integração)     →  Jogo Final (Expansão)
─────────────────────────────────────────────────────────────────────
Scripts/Core/        →  Mesmo código          →  Mesmo código
Scenes/POC/POC01     →  Scenes/MVP/MVP_Main   →  Scenes/Game/
Assets placeholder   →  Assets placeholder    →  Assets finais
```

- **Fase POC:** Cada cena testa uma mecânica isolada. Scripts vão direto na pasta de produção.
- **Fase MVP:** A cena `MVP_Main` referencia os mesmos scripts, conectando-os em um fluxo jogável.
- **Fase Jogo Final:** Os scripts são refinados e expandidos. As cenas de POC continuam existindo como sandboxes de teste.

## Consequências

**Positivas:**
- Zero overhead de integração — o código já está onde precisa estar
- Reutilização natural — POCs constroem o jogo peça por peça
- Testes unitários acumulam cobertura progressiva
- Histórico de evolução de cada módulo no git

**Negativas:**
- Exige disciplina na organização de pastas desde o início
- Cenas de POC podem ficar "órfãs" com o tempo (mitigação: manter como sandboxes de debug)
- Conflitos de merge se duas POCs mexerem no mesmo sistema (mitigação: módulos isolados)

## Alternativas Consideradas

- **Projeto separado por POC:** Rejeitada — duplicação massiva, custo de integração alto, impossível reutilizar ScriptableObjects
- **Projeto de POCs separado do jogo final:** Rejeitada — requer migração manual de código, que é propensa a erros e perda de testes
