# 🗺️ Ato 1 – A Primeira Ruptura (Versão Mundo Vivo & Integrada)

### 🪵 Título: "1497 – Sinais da Primeira Era"

> "Antes da chegada oficial, houve sussurros. E acima de tudo, houve algo que não podia esperar."

**Contexto Global:**
Estamos em 1497. Um ritual Folclórico fracassado causou o colapso parcial da Raiz do Mundo, abrindo portais temporais, mutando a fauna e a flora, e criando o Guardião da Fenda como resposta defensiva da Raiz. A tempestade resultante desviou a frota de Cabral para o Brasil. Colonizadores, tribos indígenas em conflito e Folclóricos divididos convergem para o epicentro da Ruptura. O jogador não é o único tentando resolver isso.

---

## ⏳ Mecânica Central: A Temporada do Ato 1

A Missão Principal não espera pelo jogador. Ela faz parte da **temporada ativa** do servidor, controlada pelo `StoryManager`. A passagem do tempo (relógio do jogo) altera a dificuldade, o ambiente e a narrativa.

### Fases da Temporada (State Machine)

- **Fase 1 — Tensão (`PRE_EVENT`):** Animais agem estranho. O céu muda de cor. NPCs comentam sobre presságios. Dificuldade: Normal.
- **Fase 2 — Instabilidade (`EVENT_ACTIVE`):** Magias falham ou explodem (CD +2). NPCs começam a fugir ou enlouquecer. Dificuldade: Difícil.
- **Fase 3 — Apogeu (`EVENT_ACTIVE` final):** Portais abrem aleatoriamente soltando monstros (Eventos de Combate Forçado). O Dano Espiritual ambiente causa 1 de dano por turno em áreas abertas. Dificuldade: Muito Difícil.
- **Legado (`POST_EVENT`):** A ruptura explode. A região muda visualmente (corrupção permanente). A missão muda de "Prevenir" para "Sobreviver e Conter". Placas com nomes dos participantes.

### Os Bandeirantes de Sangue (Facção NPC Antagonista)

Os **Bandeirantes de Sangue** são uma facção NPC ativa no mundo, controlada pelo `StoryManager` por temporada. Eles não são um rival de corrida — são uma **força antagonista com agenda própria**:

- Avançam pelo mapa conforme a temporada progride, controlados pelo servidor.
- Estabelecem postos, capturam NPCs e fortificam posições.
- Jogadores podem encontrá-los como inimigos de combate em diversos pontos do mapa.
- O progresso dos Bandeirantes afeta a dificuldade do Boss final e o estado do mundo.
- **Consequência:** Se os Bandeirantes dominarem uma região antes dos jogadores, o Boss final estará mais forte ("Ascendido") e a recompensa narrativa muda.

---

## 🎲 Estrutura da Campanha (Integração de Sistemas)

### Sessão 1 – *Sussurros na Floresta* (A Investigação)

**Objetivo:** Triangular a localização da Ruptura.

- **Mundo Vivo (Fofoca):** O local da ruptura não está marcado no mapa. O jogador deve interagir com a `knowledgeBase` dos NPCs.
    - *Aldeões:* "O gado não vai para o Norte."
    - *Caçadores:* "Vi luzes estranhas no Vale."
- **IA de NPC:** O único NPC que sabe o caminho exato (O Velho Pajé) segue uma rotina baseada no relógio do jogo. Ele não está na praça; ele está meditando na cachoeira (manhã) ou dormindo (noite). O jogador deve rastreá-lo.

### Sessão 2 – *Fronteira dos Mundos* (A Escolha)

**Objetivo:** Obter a "Chave Espiritual" para entrar no Epicentro.

- **Facções:** Três grupos bloqueiam o caminho. O jogador deve se aliar ou enganar um deles:
    1. **Indígenas:** Querem curar a ferida.
    2. **Colonizadores:** Querem extrair a energia.
    3. **Folclóricos (Fatalistas):** Querem usar o caos a seu favor. *(Os Restauradores podem ser encontrados como aliados em mini-campanhas.)*
- **Progressão da Temporada:** Se o jogador demorar muito (Fase 2 da temporada), as facções entram em guerra aberta, transformando o mapa em zona de combate.

### Sessão 3 – *A Corrida Final* (O Dungeon)

**Objetivo:** Atravessar a "Zona de Distorção".

- **Ambiente:** O terreno muda conforme a fase da temporada. Caminhos que existiam na Fase 1 agora são abismos na Fase 2.
- **Bandeirantes:** Patrulhas dos Bandeirantes podem emboscar jogadores. Se o jogador tiver **Explorador de Terras** ou **Arqueiro Selvagem**, pode detectar e contornar.

### Sessão 4 – *A Primeira Ruptura* (O Clímax)

**Objetivo:** Enfrentar o **Guardião da Fenda** — uma manifestação defensiva da Raiz do Mundo.

O Guardião da Fenda **não é um vilão**. Ele é uma resposta imunológica da própria Raiz, criado para selar a Ruptura a qualquer custo — inclusive eliminando quem se aproximar. Ele ataca os jogadores não por malícia, mas porque qualquer presença próxima à fenda é percebida como ameaça. Derrotá-lo (ou acalmá-lo) é necessário para acessar e estabilizar a Ruptura.

<!-- TODO: definir stats completos do Guardião da Fenda (PV, Defesa, ações de combate, loot) -->

- **Dificuldade Dinâmica:**
    - *Chegou cedo na temporada:* O Guardião está contido (Luta padrão).
    - *Chegou tarde (Fase 3+):* O Guardião absorveu a energia da ruptura. Ele é "Ascendido" (Ataques em área, Dano Espiritual massivo).

---

## 🔗 Sinergia: O Impacto das Mini-Campanhas

O jogo recompensa quem explorou o mundo. Ter completado as Mini-Campanhas (Sidequests) desbloqueia vantagens diretas no Ato 1.

| Missão Concluída (Sidequest) | Efeito no Ato 1 (Vantagem Tática/Narrativa) |
| :--- | :--- |
| **O Tambor que Silenciou o Céu** | **Uso de Item:** O jogador pode tocar o *Tambor* para atrasar a progressão da temporada por um período, dando mais tempo durante o clímax. |
| **Justiça das Mãos Sujas** | **Aliado:** O Capitão da Guarda (agora leal) envia patrulhas que limpam os inimigos comuns da Sessão 3, permitindo viagem rápida. |
| **A Canção que Não Dorme** | **Atalho:** A entidade do lago abre uma passagem submersa que leva direto ao Epicentro, ignorando as emboscadas dos Bandeirantes. |
| **O Ouro que Nunca Brilha** | **Conhecimento:** O Mentor Eremita ensina como desativar as defesas mágicas do Guardião da Fenda (Reduz a Defesa do Boss em -2). |
| **Os Filhos do Espinho e da Flor** | **Exército:** O clã aliado (Espinhos ou Flores) se junta à batalha da Sessão 2, garantindo vitória automática contra as facções rivais. |
| **O Sábio que Viu o Amanhã** | **Precognição:** O jogador sabe exatamente quando o Boss usará seu ataque especial, ganhando um turno de vantagem para defesa. |

---

## 🎁 Recompensas do Ato 1

A conclusão do Ato 1 marca a transição do personagem para o "Mid-Game".

1. **Moeda de Classe Universal (Ouro da Raiz):**
    - *Efeito*: Um fragmento de memória pura da Raiz. Ao ser consumido, ele invoca o conhecimento de mestres ancestrais diretamente na mente do personagem.
    - *Garantia:* Todos os jogadores que completarem a missão (vencedores ou sobreviventes) recebem este item. Ninguém fica travado.
    - *Mecânica*: Permite evoluir para o Tier 2 sem a necessidade de um Mentor ou Missão de Evolução. (Representa o amadurecimento do personagem pelo contato direto com a Ruptura).
2. **Desbloqueio da Troca de Origem (Espelho do Eco):**
    - O contato direto com a Ruptura amplia a conexão do personagem com a Raiz do Mundo. Ele ganha o item consumível **"Espelho do Eco"**, que permite visitar santuários para trocar de Origem (ex: acessar classes Folclóricas sendo Indígena). **Nota:** a troca de classe dentro da mesma origem já está disponível desde o início do jogo — o Espelho desbloqueia apenas a troca de *origem*.
3. **Acesso ao Mapa Aberto (Tier 2):**
    - Novas regiões (Sertão, Costa, Montanhas) são desbloqueadas no mapa de viagem.

---

### 🧩 Epílogo: O Estado do Mundo

O **Estado do Mundo** registra o resultado da temporada:

- **Vitória (Ruptura Fechada):** A floresta floresce com energia espiritual. A vila inicial prospera.
- **Sobrevivência (Ruptura Explodiu):** A floresta vira o "Bosque das Sombras". Monstros de Tier 2 aparecem lá. A vila inicial é evacuada.
