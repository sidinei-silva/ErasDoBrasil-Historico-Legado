# ADR-009 — Escopo do MVP (Full Loot, PvP, Offline Removidos)

**Status:** Aceito
**Data:** 2026-03-17
**Decisores:** Sidinei (game designer)

---

## Contexto

O MVP precisa ser viável com escopo controlado. Três sistemas complexos foram identificados como arriscados para a primeira versão: Full Loot (drop de itens ao morrer), PvP entre jogadores, e modo offline. Cada um adiciona camadas de balanceamento, infraestrutura e design que podem comprometer o lançamento.

## Decisões

### D4 — Full Loot Removido do MVP
Jogadores **não perdem itens ao morrer** no MVP. A penalidade de morte é via XP e durabilidade (ver ADR-010). Full Loot pode ser reintroduzido em temporadas futuras como mecânica opcional de zonas de risco.

### D14 — PvP Removido do MVP
Não haverá combate entre jogadores no MVP. O foco é PvE cooperativo e competitivo (missões competitivas, não combate direto). PvP pode ser adicionado em fases futuras como arenas ou zonas específicas.

### D15 — Modo Offline Removido
O jogo é **100% online**. Não existe modo offline, não existe "Eco" como mundo offline. A Raiz é o único mundo persistente. Isso simplifica a arquitetura e garante que todos os jogadores compartilhem a mesma linha temporal.

## Consequências

- Sistema de inventário simplificado (sem lógica de drop on death).
- Sem necessidade de sistemas anti-grief de PvP no MVP.
- Arquitetura server-only (sem sync offline/online).
- "Eco" removido como conceito de mundo paralelo offline; redefinido como instância solo futura para conteúdo passado (ver ADR-012).
