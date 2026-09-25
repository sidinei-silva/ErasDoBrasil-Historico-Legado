# 🎮 Plano de Spin-offs — Jogos Menores para Aprendizado

> **⚠️ ARQUIVADO:** Este plano foi **descontinuado** após o [ADR-004 — Pivot MMORPG Servidor Go](../../vibe/decisions/ADR-004-pivot-mmorpg-servidor-go.md). O foco agora é 100% no servidor Go + cliente web. Spin-offs não fazem mais parte da estratégia.

**Data:** 2026-03-07
**Filosofia:** Usar a temática e sistemas do Eras do Brasil para criar jogos menores que:
1. Servem como **treino** de game dev, C#, Unity e pixel art
2. São **jogáveis** em si mesmos (potencial de publicação)
3. **Validam** mecânicas do jogo principal antes de integrá-las
4. Geram **conteúdo reutilizável** (assets, código, lore)

---

## Por que fazer Spin-offs?

| Benefício | Detalhe |
|-----------|---------|
| **Aprendizado incremental** | Aprende Unity/C# em escopo controlado (dias, não meses) |
| **Entregas rápidas** | Cada spin-off pode ser "terminado" em 2-4 semanas |
| **Motivação** | Ver algo publicável mantém o ânimo alto |
| **Validação de mecânicas** | Testa combate, progressão, ticks em contexto simplificado |
| **Portfólio** | Mostra capacidade de terminar projetos |
| **Reuso** | Código e assets migram para o jogo principal |
| **Exploração da IP** | Expande o universo Eras do Brasil em formatos diferentes |

---

## Spin-off 1: Card Game — "Duelos da Ruptura"

### Conceito
Card game de combate baseado no sistema D20 do Eras do Brasil. Jogador monta deck com cartas de habilidades das 12 classes e batalha contra NPCs ou outro jogador.

### O que Exercita
- **C# e Unity:** UI de cartas, drag-and-drop, efeitos visuais simples
- **Sistema de combate:** Valida D20, modificadores, vantagem/desvantagem
- **Balanceamento:** Testa poder relativo das classes num contexto simplificado
- **Pixel art:** Ilustrações simples de cartas (32×32 ou 64×64)

### Escopo Mínimo
- 3 decks pré-montados (1 por Origem: Colonizador, Indígena, Folclórico)
- 4 cartas por deck (ataque, defesa, habilidade especial, item)
- Combate por turnos contra IA simples
- Resolução por D20 + modificadores da carta
- Tela única (mesa de jogo)

### Tecnologia
- Unity 2D, UI Toolkit ou Canvas
- **Plataforma:** Web (WebGL) — fácil de compartilhar

### Tempo Estimado
- **v0.1 funcional:** ~12h (2 semanas a 6h/semana)
- **v0.2 polida:** +8h (mais 1 semana)

### Reuso para o Jogo Principal
- Motor de D20 (POC 02)
- Sistema de modificadores (POC 02)
- Dados de habilidades das classes (GDD Livro de Classes)

---

## Spin-off 2: Idle Game — "Ticks da Raiz"

### Conceito
Idle/incremental game baseado no sistema de Ticks do Eras do Brasil. O jogador "planta a Raiz do Mundo" e ela cresce automaticamente a cada Tick, gerando recursos, desbloqueando eras e enfrentando rupturas.

### O que Exercita
- **Sistema de Ticks:** Implementa e valida o relógio universal (POC 07)
- **Progressão:** Curvas de XP, scaling, tiers (POCs 04-05)
- **Economia:** Recursos, crafting simplificado (POCs 24-26)
- **UI:** Barras de progresso, números animados, feedback visual
- **Game feel:** Satisfação de clique, upgrades, milestones

### Escopo Mínimo
- Raiz cresce a cada Tick (auto + clique manual)
- 3 recursos: Energia, Essência, Fragmentos
- Upgrades: velocidade de Tick, multiplicadores, auto-coleta
- 5 eras para desbloquear (baseadas na linha eco-histórica do GDD)
- Evento de Ruptura a cada ciclo (mini-boss timer)

### Tecnologia
- Unity 2D ou **Web puro (HTML/CSS/JS)** — mais rápido de prototipar
- Pode evoluir para mobile depois

### Tempo Estimado
- **v0.1 funcional:** ~8h (HTML/JS) ou ~12h (Unity)
- **v0.2 com eras:** +8h

### Reuso para o Jogo Principal
- Lógica de Ticks (POC 07)
- Curvas de progressão (POC 04)
- Lore das eras (GDD Cap. 02 Eco-Histórica)

---

## Spin-off 3: Quiz/Trivia — "Saberes do Eco"

### Conceito
Jogo de quiz/trivia sobre a história do Brasil colonial e o lore do Eras do Brasil. Educativo e divertido, pode ser usado como ferramenta de divulgação do jogo.

### O que Exercita
- **Web dev:** HTML/CSS/JS (área de conforto — entrega rápida)
- **Roteiro/escrita:** Escrever perguntas força a pesquisar e consolidar o lore
- **Pixel art:** UI simples com temática visual do jogo
- **Marketing:** Pode ser publicado como "teaser" do universo

### Escopo Mínimo
- 50 perguntas (25 história real + 25 lore do jogo)
- 4 alternativas por pergunta
- Score + ranking local
- Tela de resultado com "ficha de Desperto" (baseada nas respostas)

### Tecnologia
- Web puro (já existe `web/` no repo)
- Pode virar PWA mobile

### Tempo Estimado
- **v0.1:** ~6h
- **v0.2 polida:** +4h

### Reuso para o Jogo Principal
- Pesquisa histórica valida o lore
- Banco de perguntas pode virar base de diálogos/riddles in-game

---

## Spin-off 4 (Futuro): Turn-Based Tactics — "Escaramuça"

### Conceito
Combate tático em grid isométrico, modo arena. 3v3 ou 5v5, classes do Eras do Brasil. Valida o combate avançado (POCs 21-23) sem o peso do mundo aberto.

### O que Exercita
- Grid isométrico + pathfinding A* (POCs 21-22)
- Combate posicional (cobertura, flanco, AoE)
- Pixel art em cenário isométrico
- Multiplayer local (preparação para P2P)

### Quando Começar
- **Depois** do MVP do Eras do Brasil (2027+)
- Requer que sistema de combate já esteja validado

---

## Ordem de Execução Recomendada

```
[Março 2026]     Spin-off 3: Quiz (Web) — mais rápido, usa área de conforto
[Maio-Jun 2026]  Spin-off 1: Card Game (Unity) — aprende Unity + valida D20
[Jul-Ago 2026]   Spin-off 2: Idle (Unity ou Web) — valida Ticks + progressão
[2027+]          Spin-off 4: Tactics — valida combate tático
```

> 💡 **Spin-offs rodam em paralelo com o desenvolvimento principal.** São o "escape" para quando uma POC travar ou para noites com menos energia.

---

## Organização no Repositório

```
spinoffs/
├── README.md              # Índice dos spin-offs + propósito
├── 01-quiz-saberes/       # Spin-off 3 (primeiro por ser mais rápido)
│   ├── README.md
│   └── ...
├── 02-card-game/          # Spin-off 1
│   ├── README.md
│   └── ...
├── 03-idle-ticks/         # Spin-off 2
│   ├── README.md
│   └── ...
└── 04-escaramuca/         # Spin-off 4 (futuro)
    └── README.md
```

---

*Documento vivo. Será atualizado conforme spin-offs progridem e novas ideias surgirem.*
