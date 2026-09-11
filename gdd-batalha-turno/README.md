# Eras do Brasil — GDD

> Game Design Document de um RPG de eco-fantasia ambientado em uma versão mística do Brasil colonial (1497), onde colonizadores, povos originários e seres folclóricos coexistem em ciclos de tempo, espiritualidade e memória.

## Sobre

Este repositório contém o **GDD (Game Design Document)**, lore, pesquisas e o site público do projeto **Eras do Brasil** — um MUD Moderno (MMORPG server-authoritative).

O **código do jogo** (servidor Go + cliente web) está em [eras-do-brasil-game](https://github.com/sidinei-silva/eras-do-brasil-game).

## Estrutura

```
├── gdd/                         # Game Design Document (A bíblia do jogo)
│   ├── 01_Livro_de_Regras/      # Mecânicas, combate, mundo vivo
│   ├── 02_Livro_de_Classes/     # 12 classes, tiers, herança
│   ├── 03_Enredo_e_Mundo/       # Ato 1, mini-campanhas, lore
│   ├── 04_Design_Visual/        # Referências visuais, UI/HUD
│   ├── 05_Livros_Auxiliares/    # Atlas do Eco (mapa)
│   ├── 06_Dados_e_Assets/       # Schemas JSON, dados iniciais
│   └── 99_Meta_e_Backlog/       # Roadmap e estratégia
├── research/                    # Pesquisas de mercado e diagnósticos
├── historico/                   # Sessões de trabalho anteriores
├── web/                         # Site público (erasdobrasil.com.br)
└── .github/workflows/           # Deploy do site via GitHub Pages
```

## Pilares de Design

- **Narrativa Profunda** — Fantasia eco-histórica com folclore brasileiro
- **Jogabilidade Tática** — Combate D20 por turnos, de estático a grid tático com posicionamento
- **Mundo Vivo** — NPCs com rotinas, facções que avançam, ciclo dia/noite, servidor persistente 24/7
- **Flexibilidade de Personagem** — Troca livre entre 12 classes de 3 origens via Dom da Revivência
- **MUD Moderno (Online)** — Servidor persistente, missões competitivas, inimigos evolutivos, zero instalação

## Inspirações

*Fallen London* · *Torn* · *Stoneshard* · *Solasta* · *Sea of Stars* · *Roadwarden* · *Kingdom of Loathing*

## Links

- **Código do Jogo:** [eras-do-brasil-game](https://github.com/sidinei-silva/eras-do-brasil-game)
- **Legado (Unity-era):** [ErasDoBrasil-Historico-Legado](https://github.com/sidinei-silva/ErasDoBrasil-Historico-Legado)
- **Site:** [erasdobrasil.com.br](https://erasdobrasil.com.br)
