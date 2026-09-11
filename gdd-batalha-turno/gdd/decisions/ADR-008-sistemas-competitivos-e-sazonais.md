# ADR-008 — Sistemas Competitivos e Sazonais

**Status:** Aceito
**Data:** 2026-03-17
**Decisores:** Sidinei (game designer)

---

## Contexto

O jogo precisa de sistemas que mantenham o engajamento a longo prazo em um MMORPG. Missões puramente cooperativas podem se tornar repetitivas. O sistema de temporadas (seasons) precisa de um ritmo claro e eventos culminantes.

## Decisões

### D3 — Missões Competitivas
Algumas missões têm **resolução competitiva**: vários jogadores/grupos podem aceitar a mesma missão, mas o primeiro a entregar recebe a recompensa completa. Quem não conseguir a tempo recebe recompensa parcial ou a missão muda de estado. Verificação é server-side.

### D5 — Votação Simples para Missões de História
Decisões narrativas globais usam **votação simples** (maioria). Sem delegados, sem sistema complexo — cada jogador online vota, a maioria define o rumo da história da temporada.

### D6 — Evento Finale de Temporada (Máquina de 3 Estados)
Cada temporada culmina em um evento finale com 3 fases:
- `PRE_EVENT` → Preparação, acúmulo de recursos e narrativa
- `EVENT_ACTIVE` → O evento em si (boss, defesa, invasão)
- `POST_EVENT` → Consequências, recompensas, transição para próxima temporada

### D9 — Relógio da Ruptura Absorvido pelas Temporadas
O antigo "Relógio da Ruptura" (contador global de ameaça) foi absorvido pelo sistema de temporadas. A tensão narrativa é gerenciada pelo arco sazonal, não por um contador separado.

### D10 — Tempo de Temporada: 4-6 Meses
Cada temporada dura **4 a 6 meses reais**, permitindo arcos narrativos completos sem exaurir o conteúdo.

## Consequências

- Sistema de quests atualizado com flag `competitiva` e lógica de timeout.
- StoryManager gerencia o ciclo de estados do evento finale.
- Relógio da Ruptura removido como conceito separado.
- Roadmap alinhado a ciclos de 4-6 meses.
