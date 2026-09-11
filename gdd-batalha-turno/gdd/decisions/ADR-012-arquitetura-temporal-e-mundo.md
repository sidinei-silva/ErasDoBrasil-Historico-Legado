# ADR-012 — Arquitetura Temporal e Mundo (Tick, Eco/Raiz, Ecos Instanciados)

**Status:** Aceito
**Data:** 2026-03-17
**Decisores:** Sidinei (game designer)

---

## Contexto

O GDD original usava "Tick" como unidade de tempo visível ao jogador, "Eco" como mundo offline paralelo à "Raiz", e não tinha solução para jogadores que perdessem conteúdo sazonal. Essas três questões estão interligadas pela arquitetura temporal do jogo.

## Decisões

### D16 — Tick removido como mecânica visível ao jogador
"Tick" passa a ser **detalhe interno do game loop** (servidor). O jogador nunca vê "ticks". Em seu lugar:
- **Tempo real:** Segundos e minutos para durações curtas (crafting, cooldowns)
- **Relógio do Jogo:** Períodos do dia (Manhã, Tarde, Noite, Madrugada) para ritmo de jogo. 1 dia do jogo ≈ 2-4 horas reais
- **Turnos:** Unidade de tempo em combate

### D8 — Eco/Raiz Reescritos (sem offline)
- **Raiz:** Mundo persistente e único do servidor. Todos jogam na Raiz. É a linha do tempo mestra.
- **Eco:** Não é mais um mundo offline. Conceito reservado para instâncias solo futuras (ver D7).

### D7 — Ecos Instanciados (Futuro)
Em fases futuras, jogadores que chegarem após o fim de uma temporada poderão acessar **Ecos** — instâncias solo que reproduzem o conteúdo narrativo passado. Recompensas reduzidas comparadas à experiência ao vivo. Garante que nenhum jogador fique permanentemente excluído de conteúdo.

## Consequências

- Toda referência a "tick" como unidade visível ao jogador foi substituída por tempo real, relógio do jogo ou turnos.
- "Eco (Offline)" removido de toda documentação.
- Arquitetura simplificada: servidor único, sem sync offline.
- Glossário atualizado: "Tick" removido, "Relógio do Jogo" é o termo oficial.
- Ecos Instanciados marcados como feature futura no roadmap.
