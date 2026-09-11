# ADR-011 — Inimigos Evolutivos

**Status:** Aceito
**Data:** 2026-03-17
**Decisores:** Sidinei (game designer)

---

## Contexto

Inimigos estáticos tornam a exploração previsível. O mundo vivo precisa que até os monstros respondam ao estado do jogo.

## Decisões

### D11 — Inimigos Evolutivos no MVP
Inimigos possuem um sistema de evolução baseado em **sobrevivência**:

| Tier | Nome | Condição |
|------|------|----------|
| 0 | Normal | Spawn padrão |
| 1 | Veterano | Sobrevive a múltiplos encontros ou mata jogadores |
| 2 | Alfa | Lidera grupo, stats elevados |
| 3 | Lenda | Raro, nomeado, recompensas únicas |

No MVP, a evolução é baseada em `killCount` (quantos jogadores o inimigo derrotou) e tempo de sobrevivência.

### D12 — Inimigos Evolutivos (Futuro)
Em fases futuras, o sistema expande para incluir:
- Migração entre zonas
- Adaptação a táticas dos jogadores (resistência a dano frequente)
- Formação de hordas e territórios
- Inimigos Lenda como world bosses emergentes

## Consequências

- Schema de Inimigo atualizado com campos: `evolucao: { tier, killCount, originMapId }`.
- Dados iniciais do Ato 1 incluem exemplos de inimigos com campo de evolução.
- O InimigosManager precisa de lógica de promoção de tier.
- Cria momentos emergentes (jogadores caçando um Lobo Lenda específico).
