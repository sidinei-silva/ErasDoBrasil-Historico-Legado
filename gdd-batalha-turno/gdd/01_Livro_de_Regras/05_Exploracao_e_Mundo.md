# 🌍 Capítulo 5 – Exploração e Mundo

Explorar o mundo de *Eras do Brasil* vai muito além de mover-se de um lugar para outro — é viver em um universo reativo, cíclico e dinâmico, onde cada passo tem consequências.

Este capítulo apresenta o sistema de **exploração por blocos conectados**, o **ciclo de tempo do jogo**, a interação com **NPCs vivos e autônomos**, e os perigos e descobertas que aguardam os personagens fora do combate.

> 🔎 Enquanto o Capítulo 4 trata do combate, aqui focamos no **movimento estratégico e investigativo**, no **uso do tempo como fator de jogo** e na **descoberta do mundo como experiência central** da jornada.

O sistema de exploração foi projetado para:

- Permitir que NPCs se movam e evoluam junto ao jogador, seguindo **rotinas vivas**.
- Tornar cada ambiente significativo — com recursos, eventos, segredos e reações.
- Funcionar em um **mundo 100% online e persistente**, onde o tempo avança mesmo sem o jogador.

---

> A exploração é o que conecta as histórias, as batalhas e as decisões — e transforma o mundo conforme você o atravessa.

---
## 🌄 5.1 – Introdução à Exploração

A exploração em *Eras do Brasil* é o elo entre narrativa, descobertas e interação com o mundo vivo.
Mais do que apenas "se mover", explorar significa interagir com cenários, recursos, perigos, habitantes e eventos — tudo isso respeitando o ritmo do tempo no mundo e suas reações.

### 🗺️ Estrutura do Mundo: Camadas de Navegação

O mundo é organizado em 3 camadas de navegação:

1. **Mapa-Múndi (Regiões):** Áreas geográficas grandes do Brasil (Mata Costeira, Sertão, Serra, etc.). Cada temporada abre novas regiões.
2. **Mapa Regional (Zonas):** 8–15 zonas conectadas dentro de cada região. É o sistema de Blocos de Cenário descrito neste capítulo.
3. **Mapa Local (Sub-locais):** Expansão futura de zonas populosas em sub-áreas. Não disponível no MVP.

Para detalhes completos da estrutura de regiões e o mapa-múndi, ver [Arquitetura do Mapa](05B_Arquitetura_do_Mapa.md).

> Em um mundo onde as eras se entrelaçam, cada passo pode revelar um segredo ancestral, um evento espiritual ou uma nova ameaça.

---

### 🎲 Sistema de Blocos Conectados

A movimentação pelo mundo ocorre por meio de **blocos de cenário conectados** — como se fossem **peças de mapa entrelaçadas por caminhos**.

#### Conceitos:

- Cada bloco representa uma **região única**, como uma clareira, aldeia, ruína, montanha, vila ou templo.
- As conexões indicam para onde o jogador pode ir a partir do bloco atual.
- Ao escolher mudar de bloco, **eventos de transição** podem ocorrer: emboscadas, encontros com NPCs, descobertas, mudanças climáticas.

> ⚠️ O mestre ou sistema digital pode intercalar eventos randômicos ou narrativos sempre que um novo bloco for acessado.

---

### 📌 Modelo Digital

O jogo é **100% online** — o mundo existe no servidor e avança continuamente.

| Aspecto                    | Descrição                                        |
|----------------------------|--------------------------------------------------|
| Movimento entre blocos     | Feito por cliques ou setas direcionais           |
| Interação com NPCs e objetos| Baseado em menus, ações e caminhos              |
| Transição de cenário       | Visual e automatizada (com eventos)              |
| Passagem de tempo          | Contínua — o relógio do jogo avança mesmo sem o jogador |

---

### ⏱️ Tempo e Exploração

O tempo em *Eras do Brasil* avança continuamente no servidor, regido pelo **relógio do jogo** com 4 períodos — **Manhã, Tarde, Noite, Madrugada** (1 dia do jogo ≈ 2–4 horas reais).

- O relógio do jogo controla:
  - Rotinas e movimentação de NPCs
  - Efeitos persistentes e condições ambientais
  - Ciclo dia/noite, clima e eventos programados

> O tempo avança independentemente das ações do jogador. Cada ação de exploração (mover, interagir, coletar) consome **tempo real**, e o mundo reage de forma contínua.

---

### 🌐 Mundo Reativo e Persistente

Ao explorar, o mundo **não é estático**. Ele **reage às ações do jogador** e dos próprios NPCs, que também se movimentam, reagem e evoluem por conta própria.

- NPCs mudam de local ao longo do dia (rotinas)
- Eventos são ativados por condições específicas (ex: tempo, presença, relação com facções)
- Certos blocos podem se transformar ou desaparecer conforme o avanço da campanha

---

### 🧠 Objetivos da Exploração

Explorar significa:

- **Descobrir novos blocos e registrar no mapa**
- **Interagir com NPCs, obter informações e desbloquear eventos**
- **Coletar recursos únicos para crafting**
- **Evitar ou enfrentar perigos naturais ou mágicos**
- **Influenciar o mundo com suas escolhas e ações**

> A exploração é onde o mundo se revela, se dobra e se estende conforme o caminhar dos personagens.

---
## 🚶 5.2 – Movimentação e Distância Padronizada

A movimentação no mundo de *Eras do Brasil* é feita através de **blocos de exploração conectados**, regida pelo conceito universal de **Esforço de Viagem**.

O custo de deslocamento é calculado pela **Distância Narrativa**, não apenas pelo ato de clicar.

### 📏 A Regra da Distância Padrão
* **Unidade de Viagem** = Deslocamento significativo dentro de uma região (aprox. 15-30 minutos reais de caminhada ou travessia de um quadrante médio).

#### Aplicação nas Fases do Jogo:
* **Fase 1 (Blocos):** O custo é definido pela distância narrativa entre os nós.
    * *Praça → Taverna (Perto):* Rápido (~5 minutos reais).
    * *Vila → Floresta Profunda (Longe):* Longo (~15 minutos reais).
* **Fase 2 (Movimentação Livre):** O custo é acumulativo.
    * O jogador tem uma "Barra de Viagem".
    * Cada passo no grid enche a barra. Ao completar a distância padrão (ex: 10 passos), consome-se uma unidade de viagem.

---

### 🧭 Tipos de Movimento e Terreno

O jogador escolhe seu destino. O custo final em tempo depende do terreno:

| Terreno | Tempo de Viagem | Observação |
| :--- | :--- | :--- |
| **Estrada / Vila** | Rápido (~5 min reais) | Movimento normal e seguro. |
| **Floresta Densa** | Moderado (~10 min reais) | Terreno difícil, exige mais tempo. |
| **Pântano / Montanha** | Longo (~15 min reais) | Terreno muito difícil, exige esforço ou teste de Vigor. |

> Exemplo: Ir da Vila para a Caverna (Distância Longe + Terreno Montanha) pode levar ~20 minutos reais.

---

### 🔄 Passagem de Tempo e Eventos

O tempo avançado durante a movimentação é processado pelo mundo:
- **Eventos de Transição:** Podem ocorrer durante o trajeto (emboscadas, encontros).
- **Reação de NPCs:** Enquanto você viaja, os NPCs continuam suas rotinas normalmente.

---

### 🧭 Representação Visual

A movimentação é:

- **Guiada por cliques/setas**, escolhendo blocos conectados
- Com **animações e feedback visual** representando o deslocamento e o passar do tempo (Sol/Lua girando conforme o relógio do jogo avança).

---

### 📌 Regras Opcionais (RPG de Mesa)

O Mestre pode definir:

- **Limite de blocos por dia** de exploração
- **Rotas perigosas** com testes automáticos de perigo
- **Bloqueios temporários** causados por clima, eventos ou criaturas
- **Trilhas secretas**, que exigem rolagens ou conhecimento prévio

---

### 🧠 Exemplo Prático

O grupo está na "Encruzilhada dos Ventos". As opções visíveis no mapa são:

- Floresta das Visões (ao norte) - *Terreno Difícil*
- Ponte Quebrada (a oeste) - *Terreno Normal*

Eles decidem seguir para a Floresta das Visões.
* **Cálculo:** Distância Padrão × Terreno Difícil = ~10 minutos reais de viagem.

O relógio do jogo avança. Os NPCs da vila continuam suas rotinas enquanto o grupo viaja. O grupo chega ao destino.

---

> 📌 *Importante:* O sistema de movimentação por blocos é compatível com o sistema de eventos, coleta de recursos, encontros e tempo. Cada bloco é um ponto de decisão — e cada decisão, uma mudança no mundo.

---
## ⏳ 5.3 – Tempo Real e Ciclo Dia/Noite

O tempo em *Eras do Brasil* é contínuo e regido pelo **relógio do jogo**, que divide cada dia em 4 períodos: **Manhã, Tarde, Noite e Madrugada**. Um dia completo do jogo equivale a aproximadamente **2–4 horas reais**.

> 📖 **Referência Completa:** Para regras técnicas detalhadas sobre IA de NPCs, necessidades, rotinas, sistema de fofoca e arquitetura do tempo no servidor, consulte o [Capítulo 8 — Mundo Vivo, NPCs e Servidor](08_Mundo_Vivo_e_NPCs.md).

O tempo é medido de formas diferentes conforme o contexto:

| Contexto | Unidade de Tempo | Exemplo |
|----------|-----------------|---------|
| Combate | Turnos | "Efeito dura 3 turnos" |
| Habilidade fora de combate | Tempo real | "Dura 5 minutos" |
| Rotinas de NPC | Período do dia | "O Ferreiro trabalha de Manhã a Tarde" |
| Prazo de quest | Tempo real ou dias do jogo | "Entregue em 2 horas reais" |
| Regeneração de recursos | Tempo do jogo | "Renasce a cada Manhã" |

> **Nota técnica:** Internamente, o servidor processa o mundo em ciclos ("ticks"), mas esse detalhe não é exposto ao jogador. Ver [Capítulo 8](08_Mundo_Vivo_e_NPCs.md) para detalhes de implementação.

---

### 🧭 Custo de Tempo das Ações

| Ação                             | Tempo Aproximado | Observações |
|----------------------------------|------------------|-------------|
| Mover-se para outro bloco        | 5–15 min reais   | Depende da Distância e Terreno |
| Coletar recursos no bloco        | ~5 min reais     | Pode exigir teste ou proficiência |
| Interagir com NPC                | ~2 min reais     | Inclui conversas, compras, missões |
| Combate                          | Por turnos       | Tempo de combate é independente |
| Descansar                        | 5 min (curto) / 15 min (longo) | Restauração parcial ou total |
| Realizar ritual ou magia longa   | Variável         | Conforme descrição da magia |
| Estudar, treinar ou aprimorar    | Variável         | Definido pelo sistema |

---

### 🧠 NPCs e o Ciclo do Tempo

Os NPCs seguem **rotinas baseadas no período do dia**, não em ações discretas.

- Cada NPC possui uma **agenda diária** dividida por período:
  - **Manhã:** Acorda, vai ao mercado
  - **Tarde:** Trabalha na forja ou patrulha
  - **Noite:** Retorna para casa, descansa
  - **Madrugada:** Dorme (indisponível para interação)

NPCs ganham **conhecimento** sobre rotas, locais, monstros e outros NPCs com base nas interações que ocorrem ao longo do tempo.

---

### 🧠 Conhecimento e Interação entre NPCs

Quando dois NPCs se encontram:

- Gera-se +1 ponto de **conhecimento mútuo**.
- Se um deles possuir conhecimento prévio sobre locais, recursos ou monstros, o outro poderá **compartilhar ou absorver** essa informação com base em suas afinidades e papéis.

> Exemplo:
> Se o NPC A viu um monstro raro no bloco "Caverna Sagrada" e encontra o NPC B, o NPC B poderá começar a repassar essa informação ao jogador, caso tenha afinidade ou esteja disposto a negociar.

---

### 📌 Testes de Percepção

Se um jogador realiza uma ação ilícita ou sigilosa, e **há um NPC em um bloco adjacente**, o sistema pode exigir um:

- **Teste de Percepção (do NPC)** vs **Astúcia ou Furtividade (do jogador)**

Se o NPC for bem-sucedido:

- Ele **testemunha** a ação e pode espalhar a informação, reagir imediatamente ou gerar um evento futuro.

---

### 📅 Avanço Global e Mundo Persistente

- O tempo **avança continuamente** no servidor, 24/7. Não existe modo offline.
- Eventos ocorrem com base no relógio do jogo:
  - NPCs mudam de posição conforme o período do dia
  - Recursos se regeneram em ciclos (ex: "renasce a cada Manhã")
  - Locais entram em estado de alerta
  - Facções ou criaturas agem independentemente

> O **servidor** processa tudo automaticamente. O mundo não espera pelo jogador.

---

### 🔄 Resumo Visual – Sistema de Tempo

| Ação                            | Tempo          | Observações                     |
|---------------------------------|----------------|---------------------------------|
| Mover entre blocos              | 5–15 min reais | Variável por Terreno            |
| Interagir com NPC               | ~2 min reais   | Conversas, comércio, missões    |
| Combate                         | Por turnos     | Independente do relógio         |
| Descanso Curto / Longo          | 5 / 15 min     | Restaura PV e recargas          |
| Coleta / Craft / Ritual         | ~5 min+        | Depende da tarefa               |
| NPC age (rotina)                | Por período    | Manhã, Tarde, Noite, Madrugada |
| Evento Global                   | Por temporada  | Clima, fauna, facções, etc.     |

---

> ⚙️ O ciclo de tempo é o **motor** da simulação do mundo em *Eras do Brasil*. Ele conecta tempo, ação, rotina e consequência — criando um universo vivo e coerente.

---
## 🧑‍🤝‍🧑 5.4 – Interação com NPCs

NPCs (Personagens Não Jogáveis) são figuras fundamentais no mundo de *Eras do Brasil*. Eles não são apenas figurantes: possuem **rotinas próprias, memórias, opiniões, papéis sociais e níveis de conhecimento** sobre o mundo, monstros, recursos e outros personagens.

Este sistema cria uma experiência viva e reativa no mundo persistente online.

> 📖 **Referência Completa:** Para regras técnicas detalhadas sobre IA de NPCs (Utility AI), sistema de necessidades e traços, `knowledgeBase`, esquecimento de memória e sistema de fofoca, consulte o [Capítulo 8 — Mundo Vivo, NPCs e Servidor](08_Mundo_Vivo_e_NPCs.md), especialmente as seções 8.3 e 8.6.

---

### 🧠 Personalidade e Conhecimento

Cada NPC possui:

- **Personalidade base**: gentil, desconfiado, teimoso, fanático, pragmático, etc.
- **Conhecimento** (por tipo):
  - **Locais**: Blocos e ambientes que ele já visitou com frequência.
  - **Recursos**: Materiais ou fontes naturais que ele já viu/coletou.
  - **Monstros**: Criaturas com as quais já teve contato direto ou indireto.
  - **Outros NPCs**: Relações, rotas e características observadas em outros personagens.

Essas informações influenciam:

- As respostas que o NPC dá ao jogador.
- As dicas ou rumores compartilhados.
- As atitudes tomadas em eventos ou emergências.

> 🔄 O conhecimento do NPC **evolui continuamente** conforme ele se move, interage ou presencia algo.

---

### 🔁 Interações Básicas

O jogador pode realizar uma **ação de interação** com um NPC no mesmo bloco a qualquer momento.

A interação pode ser:

| Tipo de Interação     | Requer Teste? | Atributo Envolvido      |
|-----------------------|---------------|--------------------------|
| Conversar / Dialogar  | Opcional      | Presença (se necessário) |
| Trocar / Negociar     | Sim           | Presença ou Conhecimento |
| Pedir Informações     | Sim (caso difícil) | Presença, Astúcia       |
| Convencer / Intimidar | Sim           | Presença ou Vigor        |
| Ajudar / Curar        | Sim           | Atributo ou proficiência relacionada |
| Espionar / Enganar    | Sim           | Astúcia                  |

> O mestre (ou sistema digital) decide se o teste será necessário com base na atitude do NPC e no contexto da conversa.

---

### 🧭 Rotinas e Movimento de NPCs

NPCs se deslocam entre blocos conforme uma **rotina diária programada**, que pode incluir:

- Caminho entre sua moradia, trabalho, templo, mercado ou floresta.
- Interações com outros NPCs durante o percurso.
- Padrões fixos (ex: guarda que patrulha blocos) ou aleatórios com variação limitada.

> Em cada período do dia, o NPC executa as ações de sua rotina. Essa rotina **pode ser interrompida por eventos ou pelo jogador**, gerando consequências.

---

### 📡 Reações e Testemunhos

NPCs observam o mundo ao redor.

- Se o jogador cometer um **ato ilícito** (roubo, agressão, ritual proibido) e um NPC estiver em **bloco adjacente**, o mestre ou sistema pode aplicar um:

**Teste de Percepção do NPC**
**vs.**
**Teste de Astúcia ou Furtividade do jogador**

> Se o NPC perceber a ação:
> - Ele pode fugir, gritar, reportar ou confrontar.
> - A reputação do personagem pode ser afetada.
> - Pode gerar eventos no mundo (ex: emboscadas, multas, perseguições).

---

### 📚 Conhecimento Compartilhado

Quando dois NPCs se encontram durante suas rotas:

- Ganham **+1 ponto de conhecimento mútuo**.
- Podem trocar informações sobre:
  - **Locais**: “O novo vilarejo ao norte foi atacado.”
  - **Monstros**: “Vi pegadas do Lobo Lendário ontem.”
  - **Recursos**: “A mina está quase seca.”
  - **Rotina de outros NPCs**: “A curandeira vai sempre à floresta ao entardecer.”

Se o jogador **ganhar afinidade com um NPC**, ele poderá ter acesso a essas informações de forma mais confiável e útil.

---

### 🫂 Afinidade com NPCs

A relação entre jogador e NPC pode ser medida por **níveis de afinidade**:

| Nível de Afinidade | Efeito Possível                            |
|--------------------|--------------------------------------------|
| Neutro             | Respostas básicas, troca limitada          |
| Amigável           | Conversas abertas, início de laços         |
| Leal               | Compartilha segredos, ajuda sem cobrar     |
| Desconfiado        | Respostas evasivas, possível desvio         |
| Hostil             | Ignora, foge ou reage negativamente         |

> A afinidade pode subir ou cair conforme as ações do jogador, presentes, postura, alinhamento, ou rumores espalhados por outros NPCs.

---

### 🧪 Exemplo de Interação em Mesa

> *Jogador:* “Me aproximo do velho ferreiro e pergunto se ele já viu algo estranho na trilha ao norte.”
> *Mestre:* “Ele olha desconfiado. Faça um teste de Presença CD 13.”
> *Jogador:* (rola 1D20 + Presença) → 16
> *Mestre:* “Ele coça a barba e responde: ‘Vi pegadas grandes, mais de uma. Melhor você ir armado…’”

---

### 🎮 Exemplo na Versão Digital

- Jogador entra no bloco com a **Curandeira Naila**.
- Seleciona "Conversar".
- Naila tem afinidade Amigável com o jogador.
- Ela compartilha:
  > “Ontem, o Ermitão passou pela floresta. Parecia aflito. Se eu fosse você, o seguiria…”

---

> 🌿 A interação com NPCs em *Eras do Brasil* é viva, interconectada e repleta de possibilidades narrativas e táticas. Eles são fontes de informação, emoção e consequência.

---
## 🌾 5.5 – Ambientes e Recursos

O mundo de *Eras do Brasil* é formado por **blocos conectados**, que representam territórios, vilarejos, estradas, ruínas, biomas e locais místicos.
Cada bloco possui **propriedades ambientais, recursos naturais, obstáculos e eventos possíveis**, criando um ecossistema dinâmico e explorável.

---

### 🧱 Estrutura de Blocos

O mapa do jogo é composto por **blocos interligados**:

- Cada bloco representa um cenário individual: floresta, caverna, vila, ruína, estrada, etc.
- O jogador pode mover-se entre blocos vizinhos usando cliques ou setas direcionais.
- Os blocos podem:
  - Conter **recursos** para coleta
  - Abundar em **perigos ambientais**
  - Servir como **ponto de missão ou acampamento**

> 💡 O sistema define quais blocos estão acessíveis, ocultos ou com eventos pendentes.

---

### 🏞️ Tipos de Ambiente

Cada bloco pertence a um **tipo de ambiente**, que influencia:

- **Aparência visual**
- **Tipo de recurso disponível**
- **Perigos naturais ou monstros**
- **Dificuldade de travessia ou interação**

| Ambiente       | Características Comuns                                      |
|----------------|--------------------------------------------------------------|
| Floresta       | Herborismo, caça, madeira. Risco de emboscadas e espíritos.  |
| Montanha       | Minérios, pedra, visibilidade alta. Difícil locomoção.       |
| Pântano        | Fungos raros, venenos. Risco de doença e criaturas viscosas. |
| Vila / Cidade  | NPCs, lojas, missões, fofocas. Menos recursos naturais.      |
| Ruínas         | Itens mágicos, conhecimento antigo. Risco de armadilhas.     |
| Costeira       | Peixes, sal, raridades náuticas. Risco de tempestades.     |
| Caverna        | Recursos minerais, monstros. Requer luz para exploração.     |
| Sítio Místico  | Acontecimentos espirituais. Podem exigir testes de Presença. |

> ⚠️ Alguns ambientes podem ter **condições específicas** como névoa, fogo, escassez ou influência espiritual, modificando interações naquele bloco.

---

### 🌿 Recursos por Ambiente

Os recursos são classificados conforme o grupo de proficiências:

| Categoria     | Exemplos                  | Ambientes Comuns                        |
|---------------|---------------------------|------------------------------------------|
| 🌿 Coleta     | Ervas, peles, minérios    | Florestas, cavernas, campos, montanhas   |
| ⚙️ Refinamento| Argila, couro, carvão     | Pântanos, forjas, áreas industriais      |
| 🔨 Produção   | Madeira, metais, tecidos  | Vilas, ruínas, locais mágicos            |

> 🌱 A coleta de um recurso exige proficiência correspondente. Caso contrário, pode falhar ou gerar um item de qualidade inferior.

---

### 🔄 Regeneração e Raridade

Recursos possuem um **índice de raridade** e um **ciclo de regeneração** baseado no relógio do jogo:

| Tipo de Recurso       | Raridade | Regeneração            |
|------------------------|---------|------------------------|
| Madeira Comum          | Comum   | A cada período (~30 min reais) |
| Erva Curativa Menor    | Incomum | ~1 dia do jogo         |
| Minério Espiritual     | Raro    | ~2 dias do jogo        |
| Cristal Fragmentado    | Raro    | ~3 dias do jogo        |
| Flor do Eclipse        | Único   | Evento específico       |

> Alguns recursos são **limitados por era**, só podendo ser colhidos durante certos ciclos históricos ou eventos mágicos.

---

### 🧪 Testes para Coletar Recursos

A coleta pode requerer um **teste de atributo + proficiência**.

**Fórmula:**

`1D20 + Modificador de Atributo + Bônus de Proficiência`

- A CD é definida pela raridade do recurso e pelas condições do ambiente.
- Falhas podem gerar itens quebrados, ferimentos ou alertar inimigos.

#### Exemplo:

- Jogador tenta extrair **minério raro** em caverna escura.
- Proficiência: Mineração
- Teste: `1D20 + Conhecimento + Proficiência`
- CD: 15
- Resultado: 13 → **FALHA** → O personagem quebra a picareta e alerta um monstro próximo.

---

### 📌 Locais Especiais

Alguns blocos são considerados **locais únicos ou sagrados**, como:

- **Fontes de Energia Espiritual**
- **Altares antigos**
- **Campos de batalha esquecidos**
- **Passagens entre eras**

Esses locais exigem **permissão espiritual, presença de NPC-chave ou eventos globais** para serem acessados.

> 💠 Interações em locais especiais podem gerar:
> - Evolução de classe
> - Aprendizado de magias
> - Abertura de novas rotas ou realidades

---

> 🌿 A ambientação e os recursos em *Eras do Brasil* são ferramentas vivas, moldadas pelo cenário, pelo ciclo de tempo do mundo e pela interação dos personagens com o ambiente.

---
## 🎲 5.6 – Eventos Aleatórios e Roteirizados

Durante a exploração do mundo de *Eras do Brasil*, os jogadores poderão encontrar **eventos dinâmicos** que alteram a narrativa, criam oportunidades ou impõem desafios inesperados.
Esses eventos surgem como parte da **reação viva do mundo** às ações dos personagens, à passagem do tempo ou à movimentação dos NPCs e criaturas.

---

### 🔄 Tipos de Evento

Os eventos se dividem em duas grandes categorias:

| Tipo                  | Características                                                              |
|-----------------------|------------------------------------------------------------------------------|
| **Aleatórios** | Gerados por chance (rolagens, tabelas ou algoritmo digital)                  |
| **Roteirizados** | Criados intencionalmente pela equipe narrativa e gerenciados pelo servidor   |

> 📌 Eventos aleatórios podem ser transformados em eventos roteirizados caso evoluam com o envolvimento do jogador.

---

### 📜 Exemplos de Eventos Aleatórios

- Um **espírito faminto** aparece à noite pedindo ajuda.
- Um **enxame de insetos** devora todas as plantas do bloco atual.
- Um **NPC desconhecido** surge ferido e precisa de auxílio.
- Uma **chave ancestral** é encontrada enterrada sob um velho tronco.
- Um **ruído estranho** ecoa de uma direção ainda não explorada.

Esses eventos:

- Podem surgir ao entrar em um novo bloco.
- Podem ser acionados por tempo (ex: “a cada período em área selvagem”).
- Podem depender de atributos, proficiências ou decisões anteriores.

---

### 🧠 Lógica de Gatilhos (Digital)

No RPG digital, eventos são controlados por um sistema de **gatilhos** definidos por:

- Presença ou movimentação do jogador em um bloco
- Estado de NPCs (vivos, mortos, com conhecimento X)
- Nível de influência ou reputação
- Período do dia ou tempo acumulado
- Probabilidade ajustada por histórico ou classe do jogador

> 🔄 O sistema considera fatores como tempo de jogo, escolhas feitas e até classes desbloqueadas para personalizar a experiência.

---

### 🧩 Eventos Roteirizados

Esses são eventos **pré-planejados**, com impacto maior no enredo:

- Invasão de um vilarejo por inimigos
- Ritual espiritual que pode desequilibrar a região
- Aparecimento de um NPC chave de campanha
- Viagem entre eras (fragmentos colapsando)
- Missões principais e ganchos de novos atos

Eventos roteirizados possuem **três níveis de impacto** (baixo, médio, alto) e são ativados conforme decisões da comunidade.

---

### 🌐 Eventos Globais

No mundo persistente, eventos podem afetar **todos os jogadores conectados**, como:

- Chegada de uma nova facção
- Quebra de equilíbrio entre as Eras
- Espíritos corrompendo grandes áreas do mapa
- Recompensas únicas para os primeiros a completarem a missão

> Esses eventos possuem **ciclos próprios**, iniciando, progredindo e encerrando com base nas ações da comunidade.

---

### 🛠️ Como Interagir com Eventos

Os personagens podem:

- Testar atributos ou proficiências para mudar o curso de um evento.
- Ajudar ou impedir NPCs envolvidos.
- Utilizar equipamentos, magias ou habilidades específicas.
- **Ignorar** o evento (com possíveis consequências narrativas).

> 🎯 Muitos eventos têm mais de uma solução possível, permitindo abordagens diversas.

---

### 🧪 Testes Relacionados a Eventos

Para resolver eventos, o mestre (ou o sistema digital) pode solicitar testes variados:

| Situação                                | Tipo de Teste                      | Atributo Comum             |
|----------------------------------------|------------------------------------|----------------------------|
| Acalmar um espírito                     | Teste Social / Espiritual          | Presença ou Sabedoria      |
| Retirar um aliado de um incêndio       | Teste de Atributo com risco físico | Vigor ou Astúcia           |
| Reconhecer pistas de um mistério       | Teste de Percepção                 | Sabedoria Ancestral        |
| Sobreviver a um veneno ambiental       | Teste de Resistência               | Vigor                      |

---

> 🎭 Os eventos em *Eras do Brasil* não são meros obstáculos: são parte viva do mundo, capazes de alterar tramas, desbloquear rotas e transformar jogadores em lendas.

---
## 🧪 5.7 – Testes Fora de Combate

Nem todas as ações importantes em *Eras do Brasil* ocorrem em meio ao combate.
Durante a exploração, os jogadores enfrentarão decisões, obstáculos e oportunidades que exigem **testes fora de combate**, com foco em narrativa, proficiências e criatividade.

Esses testes são fundamentais para:

- Superar perigos ambientais
- Desvendar segredos do mundo
- Obter recursos, aliados ou rotas alternativas
- Interagir com NPCs de maneira significativa

---

### 🎲 Como funcionam os Testes

Testes fora de combate seguem a **mesma estrutura central de rolagem**:

**1D20 + Modificador de Atributo + Bônus de Proficiência (se aplicável)**

O resultado é comparado com uma **Classe de Dificuldade (CD)** definida pelo sistema.

---

### 🧠 Tipos de Testes Comuns

| Situação                                 | Tipo de Teste         | Atributo Base             |
|------------------------------------------|------------------------|---------------------------|
| Escalar uma ruína antiga                 | Teste de Atributo      | Vigor ou Astúcia          |
| Coletar ervas raras em floresta          | Teste com Proficiência | Sabedoria Ancestral       |
| Evitar armadilha natural (cipó, buraco)  | Teste de Reflexo       | Astúcia                   |
| Acalmar uma criatura agressiva           | Teste Social           | Presença                  |
| Traduzir inscrições espirituais          | Teste de Conhecimento  | Conhecimento              |
| Esquivar de queda de pedras              | Teste de Esquiva       | Astúcia                   |
| Curar um NPC fora de combate             | Proficiência / Atributo| Conhecimento ou Sabedoria |
| Localizar um caminho perdido             | Teste de Navegação     | Sabedoria ou Astúcia      |

> 🧩 O mestre pode permitir que proficiências complementares forneçam **vantagens** ou **redução da CD**, mesmo que não sejam obrigatórias.

---

### ⚖️ Sucesso, Falha e Sucesso Parcial

O resultado do teste pode ter três desfechos:

| Resultado na rolagem        | Efeito                                     |
|-----------------------------|---------------------------------------------|
| Igual ou superior à CD      | Sucesso: o personagem cumpre seu objetivo  |
| Inferior por até 3 pontos   | Sucesso Parcial: cumpre com consequências  |
| Inferior à CD               | Falha: não alcança o objetivo ou sofre penalidades |

> 🎭 O Sucesso Parcial é recomendado para dar fluidez à narrativa e evitar travamentos frustrantes.

---

### 🧭 Testes em Grupo

Quando mais de um personagem tenta a mesma ação (ex: levantar uma árvore caída, empurrar uma carroça), há três abordagens possíveis:

1. **Testes Individuais:** Cada um rola. Sucessos e falhas são avaliados separadamente.
2. **Liderança com Assistência:** Um lidera a ação, outros dão **ajuda** (concede vantagem na rolagem).
3. **Regra da Maioria:** Se mais da metade for bem-sucedida, o grupo como um todo obtém sucesso.

---

### 🎓 Testes com Proficiências de Vida

Proficiências de vida como **Mineração, Caça, Culinária, Ferraria** etc., são **extremamente relevantes** fora do combate.

- Permitem **rolagens otimizadas** (com bônus de +1 a +4).
- Podem desbloquear **opções exclusivas** de interação.
- Algumas ações só podem ser tentadas por personagens com a proficiência apropriada.

> 🔗 Veja o [[Livro de Proficiências]] para detalhes completos de cada uma.

---

### 🌿 Testes Narrativos

Alguns testes envolvem **impacto narrativo direto**, como:

- Convencer um grupo hostil a recuar
- Reconhecer um símbolo ancestral
- Resistir a uma tentação mágica

Esses testes são ideais para:

- Resolver conflitos sem combate
- Avançar missões secundárias
- Desencadear eventos ocultos

> O mestre pode adicionar **consequências narrativas** ricas mesmo em sucessos ou falhas, fortalecendo a imersão.

---

### 📌 Testes com Vantagem ou Desvantagem

Em algumas situações, o personagem pode receber:

- **Vantagem:** Rola 2D20 e escolhe o maior
- **Desvantagem:** Rola 2D20 e escolhe o menor

Causas típicas para isso:

- Ambiente favorável ou adverso
- Equipamento ou ferramenta especializada
- Condição de status ativa (Cego, Assustado, etc.)
- Ajudas de NPCs ou aliados

---

> ✅ Os testes fora de combate são onde o mundo se expande. Eles permitem que os personagens se destaquem fora do campo de batalha — como herboristas, diplomatas, ladinos, artífices ou exploradores.

---
## 🧭 5.8 – Conclusão e Transição para o Capítulo 6

A exploração em *Eras do Brasil* não é apenas um pano de fundo para os combates ou um intervalo entre missões.
Ela é o **tecido vivo** do mundo, onde decisões pequenas podem desencadear grandes eventos, encontros podem gerar vínculos duradouros, e cada desvio de caminho pode revelar um segredo esquecido pelas eras.

Com o sistema de blocos conectados, rotinas de NPCs, perigos naturais e testes narrativos, este capítulo provê as fundações para uma experiência **imersiva, estratégica e reativa** no mundo persistente online.

---

### 🔄 O que aprendemos neste capítulo:

- Como funciona a movimentação por blocos e rotas
- A importância do ciclo dia/noite e dos eventos do mundo
- Como os NPCs interagem com o tempo, o espaço e os jogadores
- A lógica de exploração de terrenos, recursos e perigos ambientais
- A estrutura de eventos aleatórios ou roteirizados
- A aplicação prática de testes fora de combate, proficiências e decisões narrativas

---

### 🔜 O que vem a seguir:

No próximo capítulo, **Capítulo 6 – Economia, Itens e Crafting**, abordaremos como o mundo de *Eras do Brasil* recompensa a exploração com:

- Recursos coletáveis
- Sistemas de criação de itens
- Qualidade e raridade dos equipamentos
- Comerciantes, reparos e economia do mundo persistente

Você entenderá como os frutos da exploração se convertem em **progresso, sobrevivência e personalização do personagem** — seja dominando a forja de um machado espiritual ou criando um ensopado raro que salva vidas em um ritual.

> ✍️ Prepare seus dados, sua mochila e sua ficha de proficiências — a jornada está apenas começando.

---