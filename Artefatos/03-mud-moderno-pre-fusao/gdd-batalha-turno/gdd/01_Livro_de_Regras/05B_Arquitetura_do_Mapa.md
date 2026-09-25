# 🗺️ Capítulo 5B — Arquitetura do Mapa

> **Decisão aprovada em sessão de design (2026-03-20).** Este documento define a estrutura macro do mundo de *Eras do Brasil* — as camadas de navegação, as regiões planejadas e a lógica de escala por temporadas.
>
> **Relação com outros documentos:** O sistema de Blocos de Cenário (zonas) está detalhado no [Cap. 5 — Exploração e Mundo](05_Exploracao_e_Mundo.md). O detalhamento das zonas da Mata Costeira está no [Atlas do Eco — Ato 1](../05_Livros_Auxiliares/01_Atlas_do_Eco_Ato1.md). Migração de mobs entre regiões se integra com [Cap. 8 — Mundo Vivo §8.10](08_Mundo_Vivo_e_NPCs.md).

---

## 5B.1 — Sistema de Camadas

O mundo de *Eras do Brasil* é organizado em **3 níveis de navegação**, do macro ao micro. Cada camada representa um nível de detalhe diferente e é implementada em fases distintas do desenvolvimento.

---

### Camada 1 — Mapa-Múndi (Regiões)

Visão macro do Brasil de 1497 sob efeito da Ruptura.

- Cada região é uma **área geográfica grande** com bioma próprio, range de nível e conflito narrativo central.
- Cada temporada abre **1-2 regiões novas**, expandindo o mundo progressivamente.
- **Navegação:** o player vê a lista de regiões acessíveis com nível recomendado. Viagem entre regiões é longa (5–10 minutos reais).

**Exemplo no cliente MUD:**

```
Você está na Mata Costeira.
Regiões acessíveis: Sertão Distorcido (Nível 5-10, ~8 min viagem)
```

**Fase 2+ (cliente visual):** mapa do Brasil estilizado com pontos clicáveis por região.

---

### Camada 2 — Mapa Regional (Zonas)

Cada região contém **8–15 zonas** conectadas num grafo de nós.

- É o sistema de **Blocos de Cenário** já definido no Cap. 5.
- Cada zona tem: tipo de terreno, regras de combate, recursos, NPCs e mobs com range de nível.
- **Navegação:** grafo de nós. "Você está na Vila de São Tomé. Saídas: Floresta do Norte (~10 min), Rio das Marés (~5 min)."
- **Cliente visual (Fase 1):** mapa de nós estilo Slay the Spire (definido em [UI Fase 1](../04_Design_Visual/05_UI_Fase_1_Exploracao_e_Combate.md)).

---

### Camada 3 — Mapa Local (Sub-locais) — FUTURO (Temporada 2+)

Quando uma zona fica muito populosa, ela é expandida em **sub-locais** internos.

**Exemplo:** "Floresta do Norte" se divide em:

- Clareira Norte
- Trilha dos Cogumelos
- Arvoredo Antigo
- Margem do Riacho

Cada sub-local tem seus próprios mobs, recursos e NPCs, distribuindo players dentro da zona.

> **⚠️ NÃO implementar no MVP.** No MVP, cada zona é um nó único (sem sub-divisão interna).

<!-- TODO: Camada 3 será implementada na Temporada 2 quando zonas populosas precisarem de expansão -->

---

## 5B.2 — Mapa-Múndi: As 5 Regiões do Brasil

### Premissa Geográfica

A **Raiz do Mundo** está no centro do continente. O colapso causado pelo ritual Folclórico fracassado irradia do centro para fora. Quanto mais perto da Raiz = mais distorção = nível mais alto. Periferia = mais estável = nível mais baixo. Isso cria um **gradiente natural de dificuldade** que guia a progressão do jogador.

```
Litoral (Nível 1) ──────────────────────────────── Centro (Nível 20+)
[Mata Costeira] → [Sertão Distorcido] → [Serra dos Ecos] → [Pantanal Vivo] → [Coração da Raiz]
```

---

### Tabela de Regiões

| Região | Bioma Real | Nível | Zonas (est.) | Temporada | Conflito Central |
|--------|------------|-------|--------------|-----------|-----------------|
| Mata Costeira | Mata Atlântica / Litoral | 1–5 | 9 (existentes) | T1 | Ritual fracassado, Ruptura inicial, chegada de Cabral |
| Sertão Distorcido | Caatinga / Interior seco | 5–10 | 10–12 | T2 | Bandeirantes expandem, Ruptura se espalha, seca sobrenatural |
| Serra dos Ecos | Serra / Montanhas | 10–15 | 10–12 | T3 | Portais temporais, ecos de outras eras, facções disputam portais |
| Pantanal Vivo | Pantanal / Alagados | 15–20 | 10–12 | T4 | Vida descontrolada, base dos Fatalistas, terreno que se move |
| Coração da Raiz | Interior profundo | 20+ | A definir | T5+ | Endgame, arco final, todas as eras coexistem |

---

### Descrição das Regiões

#### Região 1 — Mata Costeira (Temporada 1)

Litoral onde Cabral chegou desviado pela tempestade da Ruptura. Floresta atlântica densa, vila colonial recém-fundada, conflitos iniciais entre as 3 origens. A fenda da Ruptura abriu aqui porque o ritual Folclórico aconteceu na costa, perto da concentração de Indígenas e Folclóricos. É a borda do colapso — distorção presente, mas ainda contida.

**Detalhamento completo:** [Atlas do Eco — Ato 1](../05_Livros_Auxiliares/01_Atlas_do_Eco_Ato1.md).

---

#### Região 2 — Sertão Distorcido (Temporada 2)

Interior seco, caatinga, mas distorcida pela Raiz — cactos que sangram, rios que fluem ao contrário, sol que queima azul. A Ruptura se espalha do litoral pro interior. Comunidades do sertão que existiam antes da Ruptura lidam com as consequências. Os Bandeirantes de Sangue expandem pra cá buscando recursos da Ruptura. Mobs que evoluíram na Mata Costeira migram pro Sertão.

- **Recursos únicos:** cristais de seca, raízes petrificadas, couro de criatura distorcida.
- **Mobs temáticos:** criaturas de caatinga distorcida, espíritos de seca, bandeirantes veteranos.

<!-- TODO: Detalhar zonas quando a Temporada 2 for planejada -->

---

#### Região 3 — Serra dos Ecos (Temporada 3)

Montanhas, cavernas profundas, altitude. A Raiz pulsa mais forte — ecos de outras eras vazam constantemente. Fragmentos de eras futuras aparecem (anacrônicos — objetos que não deveriam existir em 1497). É aqui que os Ecos Instanciados (ADR-012) fazem sentido: portais nas montanhas levam a instâncias de temporadas passadas. Facções disputam controle dos portais.

- **Recursos únicos:** minérios de era, fragmentos temporais, cristais de eco.
- **Mobs temáticos:** criaturas de outras eras, guardiões de portal, ecos corrompidos.

<!-- TODO: Detalhar zonas quando a Temporada 3 for planejada -->

---

#### Região 4 — Pantanal Vivo (Temporada 4)

Pantanal brasileiro transformado pela Raiz num organismo vivo — terreno se move, rios mudam de curso entre períodos do dia, ilhas aparecem e desaparecem. A Raiz gera vida descontrolada: criaturas impossíveis, fusões de fauna/flora/espíritos. A facção Folclórica "Fatalista" tem sua base aqui, usando o caos pra acumular poder.

- **Recursos únicos:** essências vivas, materiais mutantes, flora consciente.
- **Mobs temáticos:** fusões impossíveis, criaturas de lama viva, Fatalistas como antagonistas.

<!-- TODO: Detalhar zonas quando a Temporada 4 for planejada -->

---

#### Região 5 — Coração da Raiz (Temporada 5+, Endgame)

Centro do continente. Onde a Raiz do Mundo está fisicamente. Distorção máxima — todas as eras coexistem simultaneamente. Mobs endgame escalam sem cap fixo (apenas cap de nível máximo de player + margem). Conflito final: fechar a Ruptura definitivamente ou manter aberta para usar seu poder. É o arco final desta saga.

<!-- TODO: Região inteira a definir quando Temporada 5+ for planejada -->

---

## 5B.3 — Migração de Mobs entre Regiões

> Referência cruzada com [Cap. 8 — 8.10 (Inimigos Evolutivos)](08_Mundo_Vivo_e_NPCs.md).

O fluxo de migração segue o gradiente geográfico:

```
Mata Costeira (1-5) → Sertão Distorcido (5-10) → Serra dos Ecos (10-15) → Pantanal Vivo (15-20) → Coração da Raiz (20+)
```

**Regra de migração entre regiões:**

Quando um mob atinge o cap de nível da sua região, o sistema verifica se a próxima região está aberta (desbloqueada pela temporada):

- **Próxima região aberta:** o mob migra para lá como Normal (reset de categoria, mantém XP interno).
- **Próxima região ainda não aberta:** o mob permanece no cap como **"boss orgânico"** da região atual, tornando-se Lenda até a região abrir.

Isso garante que regiões sem expansão ainda produzam conteúdo emergente, e que a abertura de uma nova temporada provoque uma "onda de migração" narrativamente justificada.

---

## 5B.4 — Representação no Cliente

| Fase do Jogo | Mapa-Múndi | Mapa Regional | Mapa Local |
|--------------|-----------|--------------|-----------|
| Fase 2 (Observer) | N/A (1 região só) | Grafo de nós HTML/CSS (9 nós) | N/A |
| Fase 3 (Player MVP) | N/A (1 região só) | Grafo de nós interativo | N/A |
| Temporada 2+ | Lista de regiões ou mapa estilizado | Grafo de nós por região | Sub-locais (quando implementado) |

**No MUD textual (sempre disponível):**

```
[Mapa-Múndi]
Você está na região: Mata Costeira (Nível 1-5)
Regiões acessíveis: Sertão Distorcido (Nível 5-10, ~8 min viagem)

[Mapa Regional]
Você está em: Vila de São Tomé (Segura)
Saídas:
  → Floresta do Norte (Nível 1-3, ~10 min) - Mata Densa
  → Rio das Marés (Nível 1-2, ~5 min) - Água/Lama
  → Pico da Neblina (Nível 3-5, ~15 min) - Montanha
```
