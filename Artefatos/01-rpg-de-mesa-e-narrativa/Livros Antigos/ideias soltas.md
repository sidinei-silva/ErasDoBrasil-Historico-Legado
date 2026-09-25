# Ideias Soltas - Sistema de Jogo

## 1. Sistema de Navegação em Quadrantes

Cada cenário do jogo é representado por um quadrante fixo. O jogador se move entre esses quadrantes com interações point-and-click. Cada transição entre quadrantes avança o tempo do jogo e pode gerar eventos no mundo.

## 2. Ambientes Variados por Quadrante

Cada quadrante pode conter elementos únicos como: estabelecimentos (lojas, tavernas), recursos naturais (plantas, minérios), NPCs, inimigos ou apenas espaço vazio. A composição do quadrante influencia nas interações possíveis e na estratégia do jogador.

## 3. Sistema de Tempo e Eventos

Toda ação do jogador, movimentação ou decisão avança o tempo. O mundo reage a esse tempo com eventos planejados, aleatórios ou consequência de escolhas passadas. Missões, encontros e ciclos de rotina são afetados por essa passagem de tempo.

## 4. Ações com Consequências

As escolhas do jogador (ou sua omissão) sempre geram reações no mundo, seja em NPCs, ambientes ou histórias. Um evento pode parecer simples mas desencadear consequências em cascata a médio ou longo prazo.

## 5. NPCs com Personalidade e Memória

Cada NPC terá:
- Nome e histórico pessoal.
- Log de eventos vividos ou testemunhados.
- Conhecimento acumulado sobre locais, pessoas e recursos.

Esse conhecimento influencia sua rotina, decisões e interações com o jogador ou com outros NPCs.

## 6. Rotinas Dinâmicas dos NPCs

NPCs terão rotinas diárias que podem envolver visitar locais (ex: taberna às 18h), mas com trajetos aleatórios. Isso torna encontros imprevisíveis, criando oportunidades e desafios únicos.

## 7. Evolução de Conhecimento e Relações dos NPCs

Ao cruzarem com outros NPCs ou passarem por certos locais com frequência, os NPCs:
- Aumentam conhecimento sobre pessoas, lugares e recursos.
- Desenvolvem interesses baseados nas preferências dos outros.
- Formam vínculos ou antipatias que impactam seus comportamentos futuros.

## 8. Sistema de Percepção e Visibilidade

NPCs podem observar ações do jogador mesmo estando em quadrantes vizinhos, dependendo da visibilidade do local e da percepção do jogador. O sistema é baseado em:
- Teste de percepção do jogador.
- Obstruções visuais do cenário (ex: iluminação, muros).
- Resultado: o jogador pode ser flagrado sem saber.

## 9. Mapa Explorável com Névoa de Guerra

O mapa do jogo exibe todos os quadrantes, mas apenas os já visitados ficam visíveis para o jogador. Isso estimula a exploração e o reconhecimento de terreno para estratégias futuras.

## 10. Sistema de Relações com NPCs

O jogador pode desenvolver vínculos com NPCs, desbloqueando:
- Informações sobre suas rotinas.
- Conhecimentos que o NPC tem sobre outros personagens ou locais.
- Possibilidades de ajuda, traição ou eventos únicos.

## 11. Obstruções no Cenário

Cada local terá um "nível de obstrução", que define o quanto ele bloqueia visão ou movimentação. Isso afeta percepção, furtividade e estratégia em interações ou combate.

## 12. Sistema de Combate com Turnos Parcialmente Sincronizados

- Cada batalha é por turnos.
- Cada turno consome metade do tempo de um quadrante.
- Assim, ações fora do combate (em outros quadrantes) continuam acontecendo em paralelo ao combate.

## 13. Ticks de Tempo (Online vs Offline)

**Modo Online**: O tempo flui em _ticks invisíveis_, que disparam eventos no mundo como movimentações de NPCs, surgimento de monstros ou mudanças no ambiente.

**Modo Offline**: Cada ação do jogador (mover, atacar, interagir) executa um tick. Isso garante sincronia e reatividade mesmo sem estar conectado.
