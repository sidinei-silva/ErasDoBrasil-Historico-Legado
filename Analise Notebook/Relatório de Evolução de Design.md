# Relatório de Evolução de Design: Eras do Brasil

## 1.0 A Visão Estratégica: Da Concepção Digital ao Protótipo de Mesa

### 1.1 Introdução: O Propósito Deste Relatório

Este documento tem como objetivo traçar a jornada de tomada de decisão e a evolução do design do RPG "Eras do Brasil". Servindo como um registro histórico do projeto, o relatório documenta a transição de ideias conceituais para mecânicas de jogo consolidadas, detalhando as escolhas estratégicas que moldaram o sistema, a narrativa e a arquitetura do personagem. Da visão inicial de um mundo digital persistente à decisão de prototipar o sistema como um RPG de mesa, cada etapa foi crucial para definir a identidade do jogo. O documento culmina em um sumário conciso do estado final do projeto, refletindo o framework de regras e a estrutura narrativa estabelecidos.

### 1.2 A Decisão da Plataforma: A Evolução do Meio

A trajetória da plataforma de "Eras do Brasil" reflete uma abordagem pragmática e iterativa, focada na validação de mecânicas antes da alocação de recursos de desenvolvimento complexos.

1. **Estado Inicial: O Mundo Digital Persistente** A concepção original do projeto era um jogo digital com um mundo persistente. A infraestrutura tecnológica sugerida para esta visão incluía um frontend em **React**, um backend em **FastAPI** e um banco de dados **PostgreSQL**, visando controle total sobre as regras, persistência de dados e escalabilidade para futuras implementações, como um modo multiplayer.
2. **Ponto de Inflexão: O Pivô para o RPG de Mesa** Em um momento crucial, foi tomada a decisão estratégica de pivotar o desenvolvimento inicial para um RPG de mesa tradicional ("RPG de mesa mesmo"). Esta mudança representou um lance de mestre em gerenciamento de projeto, especialmente considerando o contexto de um único desenvolvedor sênior trabalhando sozinho. Em vez de um simples "teste de sistema", o pivô se tornou uma estratégia pragmática e de baixo custo para validar as mecânicas fundamentais e o _core loop_ da jogabilidade, mitigando os riscos de um desenvolvimento digital complexo antes de qualquer investimento significativo em código.
3. **Estado Final: O Plano Digital em Duas Fases** A experiência com o protótipo de mesa consolidou um plano de duas fases para a futura versão digital, utilizando o livro de regras como base sólida para ambos os estágios:
    - **Fase 1:** Um jogo com movimentação por **blocos de cenário conectados**, onde o jogador navega entre cenas fixas. O combate nesta fase é **estático por turnos**, no qual "os personagens ficam frente a frente e a pessoa só escolhe a ação", com posicionamento abstrato e foco na seleção de habilidades.
    - **Fase 2:** Uma evolução para um sistema mais complexo, com **movimentação livre por turnos** no mapa (no estilo de _Stoneshard_), onde cada passo consome tempo, e um combate **tático com grid** (inspirado em _Solasta_ ou _Wartales_), no qual posicionamento, alcance e terreno se tornam elementos estratégicos cruciais.

Dessa forma, a versão de mesa deixou de ser apenas um protótipo e se tornou a fundação canônica sobre a qual as duas fases da experiência digital serão construídas.

### 1.3 O Sistema de Tempo: A Introdução dos "Ticks"

Para unificar a progressão do tempo entre as diferentes plataformas e modos de jogo, foi introduzido o sistema de "ticks". Esta mecânica serve como a unidade fundamental de avanço do tempo no mundo, aplicável tanto à versão de mesa "guiada" quanto à versão digital. Os ticks funcionam de duas maneiras: no modo online, avançam em tempo real (a cada X segundos), enquanto no modo offline, o tempo avança a cada ação relevante executada pelo jogador (como mover-se entre blocos de cenário ou realizar uma ação em combate). Esse sistema é a espinha dorsal da simulação de um mundo vivo, influenciando desde as rotinas de NPCs até a duração de missões, e conecta diretamente as decisões do jogador à passagem do tempo.

--------------------------------------------------------------------------------

## 2.0 Mecânicas Fundamentais: A Construção do Sistema D20

### 2.1 Contexto e Análise da Seção

A definição das regras centrais é um pilar estratégico em qualquer RPG, pois dita a forma como os jogadores interagem com o mundo e como suas intenções se traduzem em resultados. Esta seção analisará a evolução do sistema de atributos e da mecânica de resolução de ações, componentes que formam a espinha dorsal de toda a jogabilidade de "Eras do Brasil", garantindo uma base coesa e funcional para todas as demais camadas do design.

### 2.2 Atributos: Da Concepção à Tematização

O processo de definição dos atributos do personagem evoluiu de um conceito genérico para um sistema temático que reflete a identidade do cenário.

1. **Estado Inicial:** A ideia original era utilizar um sistema D20 genérico, mas os atributos específicos que comporiam a ficha de personagem ainda não haviam sido definidos. A necessidade era clara, mas a identidade ainda era uma tela em branco.
2. **Evolução:** O desenvolvimento levou à criação de seis atributos finais com nomes temáticos, projetados para evocar a atmosfera do Brasil eco-fantástico e abranger as principais esferas de ação: física, mental, social e espiritual.

|   |   |
|---|---|
|Atributo Final|Função no Jogo|
|**Força Bruta**|Capacidade de causar dano físico, levantar peso e romper obstáculos.|
|**Astúcia**|Agilidade, furtividade, destreza manual e reflexos rápidos.|
|**Presença**|Carisma, persuasão, expressão emocional e liderança.|
|**Vigor**|Saúde, resistência física, fôlego e capacidade de suportar dano.|
|**Sabedoria Ancestral**|Conexão com o espiritual, intuição, percepção e vínculo com a natureza.|
|**Conhecimento**|Inteligência lógica, estudo, engenharia e magia. Ex: _Criar uma poção indígena → Conhecimento + Proficiência em Alquimia_.|

1. **Estado Final:** O sistema foi consolidado com uma mecânica de distribuição de **27 pontos**, que o jogador aloca livremente entre os seis atributos definidos, permitindo a customização do personagem desde sua criação.

### 2.3 Resolução de Ações: Do Básico às Variações Táticas

A evolução do sistema de resolução de ações partiu de uma base tradicional e expandiu-se para incorporar nuances táticas e narrativas, enriquecendo a experiência de jogo.

1. **Fundação:** A decisão central foi adotar a fórmula clássica de sistemas D20 para a resolução de testes: **1D20 + Modificador de Atributo + Proficiência (se aplicável)**. Esse resultado é comparado a uma Classe de Dificuldade (CD) para determinar o sucesso ou a falha da ação.
2. **Expansão:** Para adicionar profundidade e gerenciar situações mais complexas, três mecânicas complementares foram incorporadas ao sistema principal. Elas foram projetadas para enriquecer a jogabilidade sem adicionar complexidade desnecessária.
    - **Testes Opostos:** Utilizados em competições diretas entre dois personagens (jogadores ou NPCs). Ambos os lados rolam o dado e adicionam seus modificadores; o maior resultado vence.
    - **Sucesso Parcial/Consequência:** Implementado para criar resultados intermediários. Em vez de um resultado binário (sucesso/falha), um teste que fica próximo da CD pode resultar em um sucesso parcial, onde o objetivo é alcançado, mas com um custo ou consequência inesperada.
    - **Testes em Grupo:** Projetado para ações colaborativas, como erguer um portão pesado ou realizar um ritual coletivo. O sucesso é determinado pela maioria do grupo atingindo a CD, incentivando o trabalho em equipe.

Este conjunto de regras formou uma base robusta e flexível para todas as interações no jogo, desde o combate até a exploração e o diálogo.

--------------------------------------------------------------------------------

## 3.0 Arquitetura do Personagem: A Evolução dos Sistemas de Progressão e Identidade

### 3.1 Contexto e Análise da Seção

A criação de personagem e seus sistemas de progressão são o coração da experiência de um RPG, pois definem a identidade do jogador no mundo e seu caminho de evolução. Esta seção detalhará as decisões cruciais que moldaram a arquitetura do personagem em "Eras do Brasil", abrangendo a estrutura de Origens e Classes, os mecanismos de desbloqueio e herança de habilidades, e o sistema de proficiências não combativas.

### 3.2 Origens e Classes: Estruturando a Identidade

O sistema de identidade do personagem evoluiu para equilibrar arquétipos temáticos com flexibilidade mecânica, resultando em uma estrutura de Origens e Classes com múltiplos caminhos de progressão.

1. **Origens (Raças):** Foram definidas três origens finais, cada uma com um bônus mecânico distinto que reflete sua herança cultural e espiritual: **Colonizador, Indígena e Ser Folclórico**. Uma decisão narrativa importante foi a inclusão da "Mudança de Origem Narrativa". Através de um "evento mágico/espiritual", o personagem pode "experimentar temporariamente outra origem". Este é um mecanismo diegético que permite aos jogadores vivenciar diferentes perspectivas culturais e mecânicas de jogo sem criar um novo personagem, conectando-se diretamente ao tema central do jogo de histórias interligadas através da "Raiz do Mundo".
2. **Estrutura de Classes:** Para a primeira era do jogo, foi estabelecida uma estrutura de **4 classes iniciais (Tier 1) por origem**, totalizando 12 classes disponíveis no início do jogo. Essa decisão garante variedade desde o princípio e ancora cada classe em um contexto cultural específico.
3. **Evolução de Classes:** Para garantir uma progressão contínua e interessante, foi criado o sistema de **Tiers (níveis de especialização de 1 a 3)**. Esta solução foi explicitamente adotada para evitar que a evolução do jogador ficasse "presa em lançar mais era", permitindo que uma mesma classe se aprofunde e ganhe novas habilidades e identidade dentro de um mesmo período histórico.

### 3.3 Sistema de Progressão: A Influência de "Orna" e a Flexibilidade

O sistema de progressão foi fortemente inspirado na filosofia de jogos como "Orna", priorizando a continuidade e a flexibilidade sobre a punição por experimentar novos estilos de jogo.

1. **Princípio Fundamental:** A decisão basilar, inspirada no modelo de "Orna", foi que o jogador não deveria zerar sua progressão ao mudar de classe. A escolha por este modelo se deu por sua filosofia de empoderamento do jogador, que "recompensa o engajamento" contínuo e permite a "criação de builds híbridas" sem impor "punições rígidas" pela experimentação, incentivando a adaptação estratégica.
2. **Mecânica de Desbloqueio:** Para regular o acesso a novas classes ou Tiers, foi introduzida a **"Moeda de Classe"**. Este item raro funciona como uma chave que, combinada à necessidade de encontrar um NPC mestre específico e completar uma missão de desbloqueio, transforma a progressão em uma jornada com marcos narrativos e mecânicos.
3. **Herança de Habilidades:** A regra final sobre a herança de habilidades ao trocar de classe foi consolidada da seguinte forma:
    - **Habilidades ativas são mantidas** e podem ser utilizadas por qualquer classe que o personagem ative, permitindo combos estratégicos.
    - **Habilidades passivas e bônus de XP de proficiência são exclusivos da classe ativa**, reforçando a identidade e o benefício de se especializar em um arquétipo em um determinado momento.

### 3.4 Proficiências de Vida (Lifeskills): Separando Combate e Ofício

Para dar profundidade ao mundo e permitir que os personagens se desenvolvam além do combate, foi criado um sistema robusto de proficiências não combativas.

1. **Decisão Inicial:** As proficiências de vida (lifeskills) foram separadas em três categorias distintas para organizar a economia e as atividades do jogo: **Coleta** (obtenção de recursos), **Produção (Crafting)** (criação de itens) e **Refinamento/Complementares** (processamento de materiais e outras habilidades).
2. **Sistema de Evolução:** A progressão nas proficiências foi desenhada para ser uma mistura de prática e narrativa. O jogador ganha XP em uma proficiência ao utilizá-la com sucesso. No entanto, para subir de nível, o avanço é travado até que o personagem encontre um **NPC mestre naquela área e complete uma missão de desbloqueio**, integrando o desenvolvimento de habilidades ao mundo e seus personagens.
3. **Conexão com Classes:** Para criar sinergia entre o combate e os ofícios, foi estabelecido que a classe ativa do personagem concede um **bônus de XP** em proficiências de vida específicas. A categoria da proficiência beneficiada depende do Tier da classe: **Tier 1** afeta Coleta, **Tier 2** afeta Refinamento/Complementares, e **Tier 3** afeta Produção (Crafting).

--------------------------------------------------------------------------------

## 4.0 Sistema de Itens: Da Simplicidade à Matriz de Qualidade e Raridade

### 4.1 Contexto e Análise da Seção

Esta seção detalhará a evolução do sistema de equipamentos em "Eras do Brasil". O design transitou de uma abordagem simples e linear para um framework multifacetado que utiliza qualidade e raridade para criar profundidade, incentivar a progressão contínua e dar suporte a sistemas como o crafting e a exploração.

### 4.2 A Matriz 5x5: Qualidade x Raridade

A decisão de implementar uma matriz 5x5 representou uma mudança fundamental na filosofia de itemização do jogo, transitando de um modelo unidimensional para um sistema complexo que permite grande variação e um caminho de progressão claro.

1. **Ponto de Partida:** Inicialmente, os equipamentos eram definidos de forma simples, primariamente pela classe do personagem e pela era histórica em que eram obtidos. Essa abordagem limitava a variedade e a sensação de progresso.
2. **A Grande Virada:** A decisão transformadora foi a introdução de um sistema matricial 5x5, que combina dois eixos independentes:
    - **Qualidade (5 níveis):** Ruim, Normal, Boa, Excelente, Obra-prima.
    - **Raridade (5 níveis):** Comum, Incomum, Rara, Épica, Lendária.
3. **Impacto:** Essa matriz permitiu a criação de até **25 variações de um mesmo item base**. Isso gerou um sistema de "progressão natural" que desacopla a evolução de itens da simples busca por um equipamento de "próximo tier". Por exemplo, um jogador com uma "Lança Tribal" de qualidade _Ruim_ pode encontrar uma versão de qualidade _Boa_ do mesmo item, representando uma melhoria significativa. Isso torna os itens do início do jogo relevantes por mais tempo e cria um ciclo de loot e crafting mais granular e satisfatório, incentivando o jogador a buscar constantemente melhorias através de "crafting, loot ou melhoria".

### 4.3 Equipamentos Iniciais e Escolha do Jogador

As decisões sobre os equipamentos de início de jogo foram cuidadosamente calibradas para oferecer uma escolha tática inicial e estabelecer um ponto de partida claro para a progressão.

1. **Definição:** Foi estabelecida a regra de que cada classe inicial oferece **2 opções de arma e 2 opções de armadura** para o jogador escolher no momento da criação do personagem. Isso proporciona uma primeira decisão estratégica, permitindo que o jogador adapte seu kit inicial ao seu estilo de jogo preferido.
2. **Itens Utilitários/Culturais:** Além do equipamento de combate, cada classe inicial recebe um item utilitário com um "efeito mecânico simples". Esses itens reforçam a identidade cultural e funcional da classe, oferecendo uma pequena vantagem situacional.
3. **Qualidade Inicial:** Para criar um caminho de progressão evidente, foi definido que todos os itens iniciais são, por padrão, de qualidade **"Ruim"** e raridade **"Comum"**. Essa base modesta garante que os jogadores sintam o impacto de encontrar ou criar equipamentos melhores logo no início de sua jornada.

--------------------------------------------------------------------------------

## 5.0 Narrativa e Mundo: Da Adaptação do GDD à "Raiz do Mundo"

### 5.1 Contexto e Análise da Seção

O enredo é a alma de um RPG, fornecendo o contexto e a motivação para as ações dos jogadores. Esta seção documentará como a narrativa de "Eras do Brasil" foi adaptada do conceito original de um jogo digital para o formato de RPG de mesa, incorporando novos conceitos místicos que não apenas enriquecem o universo, mas também fornecem uma justificativa diegética para as mecânicas de jogo.

### 5.2 O Enredo Central: A "Raiz do Mundo"

A premissa narrativa do jogo evoluiu para integrar mecânicas de jogabilidade flexíveis, como viagens no tempo e campanhas modulares.

1. **Origem:** A base da história foi extraída do Documento de Design de Jogo (GDD) inicial, intitulado "1500 Caminhos do Brasil", que estabeleceu o cenário histórico-fantástico.
2. **Evolução para o RPG:** A adaptação para RPG de mesa introduziu o conceito da **"Raiz do Mundo"**, uma "essência mística" que conecta o tempo e o espaço no continente. Essa força sobrenatural foi o pilar narrativo que unificou vários conceitos mecânicos previamente díspares, servindo como a justificativa central para a principal mecânica do enredo: o **"Dom da Revivência"**. Este dom permite que os personagens dos jogadores acessem outras eras, vivenciando ecos de vidas passadas e futuros possíveis.
3. **Aplicação Mecânica:** Esses conceitos narrativos foram diretamente aplicados para justificar a estrutura de jogo. A capacidade de viajar entre eras abre a porta para "quick campaigns" (campanhas rápidas) e a inclusão de elementos inspirados em jogos _roguelite_, onde os jogadores podem explorar realidades alternativas ou ciclos de eventos, aumentando a rejogabilidade.

### 5.3 Estrutura de Campanhas: Ganchos e Mini-aventuras

Para suportar a narrativa central e oferecer conteúdo variado, foi criada uma estrutura de missões modulares e expansíveis.

1. **Criação das Mini-Campanhas:** Foi tomada a decisão de desenvolver missões paralelas e autocontidas, específicas para cada uma das três Origens (Colonizador, Indígena, Ser Folclórico). Essas mini-campanhas oferecem arcos de história focados que exploram os temas de cada cultura.
2. **Expansão com "Ganchos Maiores":** Para aumentar a longevidade e a profundidade do jogo, foram adicionados **"Ganchos Maiores de Campanha"** a cada mini-campanha. O propósito desses ganchos é transformar missões curtas em potenciais arcos narrativos longos, oferecendo ao mestre e aos jogadores a possibilidade de expandir uma aventura paralela em uma campanha completa.
3. **Padronização:** Visando o equilíbrio de conteúdo, foi decidido equalizar o número de mini-campanhas disponíveis para todas as origens, garantindo que jogadores de qualquer background tenham uma quantidade similar de histórias para explorar.

--------------------------------------------------------------------------------

## 6.0 Sumário Final: O Estado Atual do Jogo "Eras do Brasil"

A jornada de design de "Eras do Brasil" resultou em um sistema coeso e multifacetado, transitando de uma visão digital ambiciosa para um protótipo de mesa funcional que, por sua vez, informou um plano de desenvolvimento digital mais robusto e faseado. A seção a seguir serve como um "snapshot", um resumo consolidado de todas as principais mecânicas do jogo em seu estado final, conforme documentado ao longo deste relatório.

- **Sistema Central:** O jogo utiliza um sistema D20, com 6 atributos temáticos (Força Bruta, Astúcia, Presença, Vigor, Sabedoria Ancestral, Conhecimento). A resolução de ações é baseada na fórmula **1D20 + Modificadores**, complementada por mecânicas de testes opostos, sucesso parcial e testes em grupo.
- **Plataforma:** O foco de desenvolvimento atual é um **Livro de Regras para RPG de mesa**. Este livro serve como a base para uma futura adaptação digital planejada em duas fases: a primeira com movimentação por blocos de cenário e combate estático (Fase 1), e a segunda evoluindo para movimentação livre por turnos e combate tático em grid (Fase 2).
- **Criação de Personagem:** O processo envolve: escolher 1 de 3 Origens (Colonizador, Indígena, Ser Folclórico); escolher 1 de 12 classes iniciais (Tier 1); distribuir 27 pontos entre os 6 atributos; escolher 2 proficiências de vida iniciais no nível **Aprendiz (+1)**; e selecionar um kit inicial com 2 opções de arma e 2 de armadura.
- **Progressão:** A evolução de classes é estruturada em **Tiers (1 a 3)**. O desbloqueio de novas classes ou Tiers requer uma **"Moeda de Classe"**, encontrar um NPC específico e completar uma missão. Na troca de classes, **habilidades ativas são mantidas**, mas habilidades passivas e **bônus de XP de proficiência** são exclusivos da classe ativa.
- **Proficiências (Lifeskills):** Personagens ganham XP em proficiências através do uso. Para subir de nível, é necessário encontrar um mestre NPC e completar uma missão de desbloqueio. A classe ativa do personagem concede um bônus de XP em uma proficiência temática associada, dependendo do Tier da classe.
- **Itens:** O sistema de equipamentos é baseado em uma **matriz 5x5 de Qualidade x Raridade**, permitindo 25 variações para cada item base e garantindo uma progressão granular e contínua.
- **Narrativa:** O enredo é sustentado pelo conceito da **"Raiz do Mundo"**, que justifica a mecânica de viagem no tempo ("Dom da Revivência"). A estrutura de campanha é modular, consistindo em uma trama principal (Ato 1) e mini-campanhas paralelas por origem, cada uma com ganchos para expansão em arcos narrativos maiores.
- **Regras Avançadas (Opcionais):** Para a futura versão digital, foram definidas mecânicas opcionais, como **Durabilidade de item**, **Full Loot** (perda de itens ao morrer), **Fuga de batalha** e **Inimigos que ganham XP** ao derrotar o jogador, criando um mundo mais dinâmico e desafiador.