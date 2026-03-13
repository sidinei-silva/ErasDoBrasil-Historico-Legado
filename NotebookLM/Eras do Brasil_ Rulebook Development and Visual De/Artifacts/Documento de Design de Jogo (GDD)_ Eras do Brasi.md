### Documento de Design de Jogo (GDD): Eras do Brasil
#### 1.0 Visão Geral e Pilares Fundamentais do Jogo
##### 1.1 Introdução Estratégica
"Eras do Brasil" é um RPG de eco-fantasia que mergulha na rica tapeçaria da história, mitologia e espiritualidade do Brasil. O conceito fundamental do jogo reside em uma premissa única: diferentes eras da história e do mito não são lineares, mas coexistem e se entrelaçam em um plano místico. Esta realidade fragmentada permite que personagens — sejam eles colonizadores, indígenas ou seres folclóricos — acessem ecos de outras vidas e ciclos, moldando não apenas seus próprios destinos, mas o fluxo do tempo em si. Esta seção define os pilares de design inegociáveis que sustentam toda a experiência de jogo, servindo como a fundação conceitual sobre a qual todos os sistemas e narrativas são construídos.
##### 1.2 O Conceito Central: A Raiz do Mundo e o Dom da Revivência
Dois conceitos fundamentais governam o universo de "Eras do Brasil", justificando tanto a sua narrativa quanto as suas mecânicas centrais.
*   **A Raiz do Mundo:**  No coração espiritual do continente, existe uma entidade mística que conecta todas as eras, culturas e memórias. Para os indígenas, é um ser vivo; para os missionários, uma criação divina; para os seres folclóricos, o campo onde as histórias ganham consciência. A fragmentação desta raiz é o catalisador para o cenário do jogo, causando a sobreposição de diferentes ciclos temporais e a quebra do equilíbrio entre os mundos físico e espiritual.
*   **O Dom da Revivência:**  Como consequência da ruptura da Raiz do Mundo, certos indivíduos despertam com uma habilidade mística: a capacidade de acessar memórias, ecos e habilidades de vidas que nunca viveram — ou que talvez tenham vivido em outros ciclos. Este dom justifica narrativamente a flexibilidade do sistema de jogo, permitindo que os jogadores alternem entre classes e origens através de eventos como visões, rituais ou pactos, herdando habilidades e expandindo seu potencial de forma dinâmica.
##### 1.3 Os Três Pilares do Design
A filosofia de design de "Eras do Brasil" é sustentada por três pilares interconectados que guiam a experiência do jogador em todos os níveis.
*   **Mundo Vivo e Reativo:**  O universo do jogo não é um cenário estático que aguarda o jogador. Ele se move de forma independente, regido por um sistema de "ticks" que avança o tempo. NPCs possuem rotinas diárias, memórias de eventos e conhecimento que evolui. Eventos ocorrem em ciclos, facções disputam territórios e o mundo reage não apenas às ações do jogador, mas também à sua omissão, criando um ecossistema dinâmico e persistente.
*   **Narrativa Fragmentada e Pessoal:**  A história é contada através da coexistência de Eras, permitindo que os jogadores explorem conflitos e mistérios de diferentes períodos históricos e místicos simultaneamente. Em vez de um caminho linear, a narrativa se desdobra através de arcos principais, mini-campanhas de origem e eventos que respondem às escolhas do jogador, permitindo que cada um molde seu próprio caminho e legado através das eras.
*   **Flexibilidade Sistêmica Profunda:**  O sistema de jogo é construído para permitir uma personalização estratégica profunda. Os jogadores não estão presos a uma única classe ou origem. A mecânica do "Dom da Revivência" permite alternar entre classes desbloqueadas fora de combate, herdando habilidades ativas e adaptando o papel do personagem aos desafios específicos de cada missão, combate ou interação social.
Com esta visão conceitual estabelecida, a execução do projeto seguirá uma abordagem faseada, garantindo que cada um desses pilares seja implementado e validado de forma incremental e coesa.
#### 2.0 Estrutura de Desenvolvimento em Fases
##### 2.1 Introdução Estratégica
A complexidade de um mundo vivo e reativo exige uma abordagem de desenvolvimento estratégica e incremental. Por isso, "Eras do Brasil" será construído em fases, permitindo que os sistemas centrais de regras, narrativa e interação sejam testados e validados de forma controlada. Essa metodologia garante que a profundidade do projeto seja alcançada sem sobrecarregar a produção, ao mesmo tempo em que entrega experiências de jogo distintas e completas em cada etapa, construindo uma base sólida para a visão final.
##### 2.2 Fase 1: RPG de Mesa Digital
A primeira fase do projeto se manifestará como um RPG de mesa com forte suporte digital. Esta etapa servirá como a fundação para todas as regras, sistemas e narrativas do universo "Eras do Brasil". O  *Livro de Regras*  será a fonte da verdade, detalhando a criação de personagens, mecânicas de resolução de ações, combate por turnos e os sistemas de exploração. Embora a experiência seja a de um RPG de mesa clássico, jogado com um Mestre e dados, ela será otimizada para plataformas digitais, validando o núcleo da jogabilidade antes da transição para um jogo totalmente automatizado.
##### 2.3 Fase 2: A Transição para o Jogo Digital
A segunda fase expandirá a base do RPG de mesa para um jogo digital completo, evoluindo em duas etapas planejadas para garantir uma transição suave e tecnicamente viável.
###### 2.3.1 Etapa 2.1 - Exploração em Blocos e Combate Estático
A primeira versão do jogo digital manterá uma estrutura de exploração baseada em quadrantes ou "blocos". O jogador navegará pelo mundo através de interações  *point-and-click* , movendo-se entre cenas fixas que representam diferentes locais. O combate permanecerá por turnos, mas será estático, sem movimentação tática em grid. As ações serão resolvidas com base nas escolhas do jogador (atacar, usar habilidade, defender), focando na estratégia de uso de recursos e habilidades em vez de posicionamento.
###### 2.3.2 Etapa 2.2 - Exploração Livre e Combate Tático
Na etapa final, a jogabilidade evoluirá para um sistema mais complexo e imersivo. A exploração por blocos dará lugar à movimentação livre do personagem, enquanto o combate se transformará em um sistema tático isométrico baseado em grid. Esta evolução se inspirará em referências como  *Solasta*  e  *Stoneshard* , onde o posicionamento, cobertura, alcance e ataques de oportunidade se tornam elementos centrais da estratégia. Esta fase representa a visão completa e madura da experiência de jogo digital.
As fases de desenvolvimento estão intrinsecamente ligadas aos sistemas de jogo detalhados que as sustentarão, desde a resolução de uma simples rolagem de dados até a simulação de um mundo complexo.
#### 3.0 Sistemas de Jogo Fundamentais
##### 3.1 Introdução Estratégica
Os sistemas de jogo são o motor que impulsiona a visão de "Eras do Brasil", traduzindo os pilares de design em mecânicas tangíveis e interativas. Esta seção detalhará as regras centrais que governam a experiência do jogador, desde a resolução de ações básicas até a complexa simulação de um mundo vivo. Estas mecânicas foram projetadas para serem modulares e escaláveis, aplicando-se de forma consistente em todas as fases de desenvolvimento, do RPG de mesa à versão digital final.
##### 3.2 Mecânicas Centrais de Resolução
A resolução de todas as ações com resultado incerto é governada por um sistema unificado, detalhado na tabela abaixo.
| Mecânica | Descrição |
| ------ | ------ |
| **Testes de Atributo** | Ações são resolvidas com a fórmula: 1D20 + Modificador de Atributo + Bônus de Proficiência (se aplicável). |
| **Modificadores de Atributo** | Cada atributo (valor de 1 a 6) fornece um modificador de -2 a +3, que é somado à rolagem do dado. |
| **Classe de Dificuldade (CD)** | Um número-alvo que a rolagem do teste deve igualar ou superar para que a ação seja bem-sucedida. |
| **Rolagens Críticas** | Um  **20 natural**  no dado é um Sucesso Crítico (sucesso excepcional com bônus). Um  **1 natural**  é uma Falha Crítica (erro grave com consequências negativas). |

##### 3.3 Criação e Progressão de Personagem
O sistema de personagem é projetado para máxima flexibilidade e profundidade estratégica, refletindo o conceito do "Dom da Revivência".
*   **Origens:**  Existem três origens jogáveis que definem as raízes culturais e espirituais do personagem:  **Colonizador** ,  **Indígena**  e  **Ser Folclórico** . A origem determina o acesso a classes iniciais e influencia reações de NPCs.
*   **Classes:**  Cada origem oferece acesso a quatro classes iniciais (Tier 1). As classes evoluem através de Tiers (1 a 3), aprofundando sua especialização. Todas as classes iniciais são visíveis desde o início para permitir o planejamento estratégico de longo prazo.
*   **Alternância e Herança:**  Refletindo o Dom da Revivência, os jogadores podem alternar entre quaisquer classes já desbloqueadas quando estão fora de combate. Ao fazer isso, eles mantêm acesso às  **habilidades ativas**  das classes anteriores, permitindo combinações táticas únicas.
*   **Proficiências de Vida:**  Além das habilidades de combate, os personagens desenvolvem proficiências em três áreas:  **Coleta**  (ex: Caça, Mineração),  **Refinamento**  (ex: Coureira, Fundição) e  **Produção**  (ex: Alquimia, Ferraria).
##### 3.4 Sistema de Combate Evolutivo
O combate é tático e por turnos, projetado para evoluir junto com as fases de desenvolvimento do jogo.
*   **Estrutura de Turnos:**  O combate é organizado em rodadas, com a ordem de ação determinada pela  **Iniciativa**  (1D20 + Modificador de Astúcia). Em seu turno, um personagem pode realizar uma ação principal, como  **Ataque** ,  **Habilidade** ,  **Magia**  ou  **Defesa** .
*   **Evolução do Sistema:**  O sistema transitará de um  **combate estático**  (Fase 1), focado em escolhas de ação sem movimento, para um  **combate tático em grid isométrico**  (Fase 2.2), inspirado em jogos como  *Solasta* , onde posicionamento, cobertura e alcance são cruciais.
*   **Turnos Parcialmente Sincronizados:**  Uma mecânica única onde o tempo do mundo continua a passar fora do combate. Cada turno de batalha consome  **metade do tempo de um quadrante**  de exploração, o que significa que NPCs em outros locais continuam suas rotinas e eventos podem progredir em paralelo, mesmo enquanto os jogadores estão em combate.
##### 3.5 Exploração e Mundo Vivo
A exploração é o coração da experiência, impulsionada por sistemas que criam um mundo dinâmico e reativo.
*   **Navegação por Quadrantes:**  Na Fase 1 e 2.1, a movimentação ocorre através de um sistema  *point-and-click*  entre blocos ou quadrantes fixos. O mapa se revela à medida que novas áreas são visitadas, utilizando uma mecânica de  **Névoa de Guerra**  que incentiva a exploração.
*   **Sistema de Ticks e Tempo:**  Cada ação significativa, como mover-se entre quadrantes, avança o tempo do jogo através de "ticks". No modo  **Online** , o tempo flui continuamente em ticks invisíveis. No modo  **Offline** , cada ação do jogador executa um tick. Esses ticks disparam eventos, a movimentação de NPCs e a regeneração de recursos.
*   **Eventos e Consequências:**  O mundo reage dinamicamente às ações do jogador — ou à sua inércia. As escolhas geram consequências em cascata que podem afectar NPCs, ambientes e o desenrolar da história a curto e longo prazo.
##### 3.6 Interação Social e NPCs Dinâmicos
Os NPCs são mais do que meros provedores de missões; são entidades autônomas que habitam o mundo.
*   **Personalidade e Memória:**  Cada NPC possui um histórico e um log de eventos que testemunhou. Seu conhecimento sobre o mundo, outros personagens e recursos influencia suas decisões e diálogos.
*   **Rotinas Dinâmicas:**  Os NPCs seguem rotinas diárias (ex: visitar a taverna às 18h), mas com trajetos parcialmente aleatórios, tornando os encontros orgânicos e imprevisíveis.
*   **Evolução de Conhecimento:**  NPCs aprendem sobre o mundo ao interagirem entre si ou ao explorarem novos locais, desenvolvendo relações e compartilhando informações que o jogador pode descobrir.
*   **Sistema de Percepção:**  NPCs podem observar as ações do jogador à distância, com base em um  **teste de percepção**  que considera obstruções no cenário que bloqueiam visão e movimento. Isso permite que um jogador seja flagrado sem seu conhecimento, gerando consequências futuras.
A combinação de rotinas dinâmicas, conhecimento evolutivo e um sistema de percepção reativo resulta em um mundo que se sente genuinamente vivo e imprevisível, e não apenas uma coleção de sistemas avançados.
##### 3.7 Economia e Criação de Itens (Crafting)
O sistema de itens é robusto e integrado à exploração e progressão, baseado em uma matriz de Qualidade e Raridade.
*   **Matriz 5x5 de Qualidade x Raridade:**  Cada item é classificado por sua condição física (Qualidade) e seu valor místico ou histórico (Raridade), criando uma vasta gama de equipamentos.
|  | ⚪ Comum | 🟤 Incomum | 🔷 Raro | 🟣 Épico | 🟡 Lendário |
| ------ | ------ | ------ | ------ | ------ | ------ |
| ⚠️  **Muito Baixa** | Arma quebrada de madeira | Ferramenta improvisada tribal | Medalha rachada de herói antigo | Cajado corrompido | Espada lendária partida |
| 🟠  **Baixa** | Espada de ferro mal forjada | Poção mal misturada | Túnica surrada de ordem secreta | Tambor ritual danificado | Colar de alma fragmentada |
| 🟡  **Média** | Couraça de couro comum | Poção de cura básica | Amuleto espiritual de floresta | Pederneira encantada | Diário de um herói perdido |
| 🟢  **Alta** | Espada bem equilibrada | Kit de ferramentas refinado | Arco cerimonial indígena | Instrumento mágico de mestre | Máscara do espírito antigo |
| 🔵  **Excelente** | Espada rúnica de mestre ferreiro | Elixir perfeito | Relíquia de guerra antiga | Cocar de ancestral lendário | Orbe da Primeira Era |

*   **Pilares da Economia:**  A economia do jogo se apoia em quatro pilares:  **Coleta**  de recursos no mundo,  **Crafting**  de novos itens usando proficiências,  **Comércio**  com NPCs e outros jogadores, e  **Recompensas**  obtidas em missões.
*   **Regras Adicionais:**  Os itens possuem regras de  **durabilidade** , exigindo  **reparos**  e manutenção. Além disso, é possível realizar a  **fusão de itens**  para transferir propriedades especiais.
Com a estrutura mecânica detalhada, podemos agora explorar o conteúdo narrativo e de mundo que dá alma a estes sistemas.
#### 4.0 Conteúdo Narrativo e de Mundo
##### 4.1 Introdução Estratégica
O conteúdo narrativo é a alma de "Eras do Brasil". O enredo, as missões e a construção de mundo não são um pano de fundo estático, mas um sistema interativo que respira e evolui. Ele é projetado para reagir às mecânicas de jogo e ser moldado pelas escolhas do jogador, transformando cada campanha em uma história única e pessoal, tecida nos fios do tempo e da memória.
##### 4.2 Enredo Principal: Ato 1 – A Primeira Ruptura
O Ato 1, intitulado  *A Primeira Ruptura* , se passa em 1497 e cobre o arco narrativo "Sinais da Primeira Era", estabelecendo os principais conflitos e mistérios do universo do jogo.
*   **Contexto:**  A história se passa em  **1497** , três anos antes da chegada documentada de Pedro Álvares Cabral. Um grupo clandestino de exploradores portugueses se aproxima da costa, enquanto tribos indígenas relatam sinais espirituais e entidades folclóricas despertam, sentindo a iminência de uma mudança que ameaça o equilíbrio de todas as Eras.
*   **Estrutura:**  O Ato 1 é estruturado em cinco sessões de jogo, projetadas para introduzir o mundo, os conflitos e as mecânicas centrais de forma orgânica.
| Sessão | Título | Duração Média | Objetivos |
| ------ | ------ | ------ | ------ |
| 1 | **Sussurros na Floresta** | 2h–3h | Introduzir os três povos, o mistério de um caçador desaparecido, símbolos estranhos e a descoberta de um artefato místico, o "Fragmento de Eco". |
| 2 | **Fronteira dos Mundos** | 2h–3h | Forçar o encontro do grupo através de um evento sobrenatural com o espírito "Aquele que Sonha as Eras", que lhes apresenta a primeira grande escolha entre três caminhos: explorar ruínas, ajudar colonos ou realizar um ritual. |
| 3 | **Rituais e Profecias** | 3h | Durante um ritual conjunto, um jogador experimenta uma  *Quick Campaign* , vivenciando outra origem/classe, introduzindo o Dom da Revivência como mecânica jogável. |
| 4 | **A Missão de Sangue e Terra** | 3h–4h | Aprofundar o conflito entre as origens através de uma disputa por um artefato recém-descoberto, forçando dilemas morais e combate direto. |
| 5 | **A Primeira Ruptura** | 3h+ | Levar ao clímax místico, onde o artefato se quebra, abrindo um "dungeon espiritual" que mistura eras e revela a ameaça principal e a capacidade de acessar outros ciclos. |

##### 4.3 Mini-Campanhas Paralelas por Origem
Para aprofundar a experiência e a rejogabilidade, cada origem (Indígena, Colonizador e Ser Folclórico) possui arcos narrativos paralelos e modulares, que exploram seus conflitos e mitologias específicas.
###### Origem: Indígena
*   **O Caçador que Não Voltou**
    *   **Resumo:**  O grupo deve seguir os rastros de um caçador desaparecido que partiu em busca de uma criatura lendária devoradora de sonhos.
    *   **Gancho Maior de Campanha:**  A criatura é, na verdade, um espírito guardião corrompido, e a missão se torna o início de uma jornada para restaurar o equilíbrio espiritual da floresta.
*   **Sombras Sobre a Aldeia Queimada**
    *   **Resumo:**  Espíritos atormentados assombram as ruínas de uma aldeia queimada por colonizadores, e o personagem deve decidir entre purificar o local ou usar o sofrimento como fonte de poder.
    *   **Gancho Maior de Campanha:**  A aldeia fazia parte de um antigo selo protetor, agora fragmentado, levando a uma campanha para restaurar ou romper completamente o selo.
*   **O Tambor que Silenciou o Céu**
    *   **Resumo:**  Um tambor cerimonial quebrado silenciou os rituais de uma tribo, e o personagem deve libertar um espírito da música para restaurá-lo.
    *   **Gancho Maior de Campanha:**  O tambor é um de quatro instrumentos lendários que mantêm a sincronia entre os planos, iniciando uma busca para reunir o conjunto completo.
###### Origem: Colonizador
*   **Justiça das Mãos Sujas**
    *   **Resumo:**  Investigar a morte misteriosa dos acusadores de um homem enforcado sem julgamento, decidindo se a justiça será feita ou reescrita.
    *   **Gancho Maior de Campanha:**  A execução foi um ritual de uma irmandade oculta que acredita em sacrifícios públicos para manter a ordem, levando o jogador a desmantelar, infiltrar-se ou usar o culto para seus fins.
*   **O Ouro que Nunca Brilha**
    *   **Resumo:**  Um mapa aponta para uma jazida de ouro em terras sagradas, forçando uma escolha entre ganância e respeito aos pactos espirituais.
    *   **Gancho Maior de Campanha:**  O ouro é um selo mágico para conter uma entidade antiga, e o mapa é uma armadilha para atrair sacrifícios, revelando um plano continental.
*   **Fé que Ilumina ou Queima**
    *   **Resumo:**  Interpretar um "milagre" ocorrido em território sagrado, cuja natureza é disputada entre colonos e indígenas.
    *   **Gancho Maior de Campanha:**  O milagre foi uma interferência do futuro, fragmentos de linhas temporais coexistindo, permitindo que o jogador aprenda a navegar entre realidades ou forçar uma única versão.
###### Origem: Ser Folclórico
*   **A Canção que Não Dorme**
    *   **Resumo:**  Uma melodia ancestral ecoa de um lago, criada por um ser encantado preso entre planos que exige uma resolução para seu tormento.
    *   **Gancho Maior de Campanha:**  Libertar a entidade exige encontrar as "notas perdidas" da canção, espalhadas em sonhos e locais de poder pelo mundo.
*   **Passos que não Deixam Pegadas**
    *   **Resumo:**  Caçar ou se tornar o Caçador Sem Sombra, uma entidade que personifica a perda e o instinto predatório.
    *   **Gancho Maior de Campanha:**  O Caçador é um guardião amnésico dos caminhos místicos que agora ataca todos que se aproximam da Raiz do Mundo, oferecendo a escolha de restaurá-lo ou herdar seu legado.
*   **O Sopro dos Quatro Ventos**
    *   **Resumo:**  Passar por quatro testes elementais — físico, mágico, espiritual e moral — para provar seu valor ou ser partido entre mundos.
    *   **Gancho Maior de Campanha:**  Os quatro ventos são entidades primordiais desgarradas, e o personagem pode se tornar um mediador elemental para reuni-los ou tomar seu lugar como o quinto elemento: o da vontade.
##### 4.4 Linha do Tempo Eco-Histórica
A história de "Eras do Brasil" não é linear, mas marcada por distorções que bifurcam eventos reais, criando oportunidades narrativas únicas.
| Ano Estimado | Evento (Eco-Histórico) | Ruptura / Anomalia | Oportunidades Narrativas |
| ------ | ------ | ------ | ------ |
| **1497** | Expedição secreta portuguesa chega ao Brasil. | Um artefato desperta na floresta, abrindo a primeira fissura entre eras. | Campanha principal, introdução ao Dom da Revivência e encontros com seres de outras épocas. |
| **1530** | Início das capitanias hereditárias. | Uma linhagem de nobres firma um pacto com entidades folclóricas para manter poder sobre a terra. | Campanhas de espionagem, rituais de herança e o conceito de "capitanias místicas". |
| **1584** | Missões jesuíticas se espalham. | Uma ordem secreta da Igreja descobre a Raiz do Mundo e tenta selá-la com "ritos de silêncio absoluto". | Aventuras em ruínas de missões jesuíticas e a busca por segredos espirituais apagados. |
| **1612** | Invasão francesa no Maranhão. | Um eclipse total ativa um elo místico entre os encantados e as forças lunares europeias. | Campanhas sobre noites que nunca terminam e disputas entre entidades místicas de diferentes culturas. |

Este universo narrativo, rico e multifacetado, exige uma identidade visual que consiga capturar sua essência rústica, mística e profundamente brasileira.
#### 5.0 Direção de Arte e Apresentação Visual
##### 5.1 Introdução Estratégica
A direção de arte de "Eras do Brasil" não é um elemento meramente cosmético, mas uma ferramenta fundamental para comunicar a atmosfera rústica, mística e espiritual do jogo. Ela deve evocar a sensação de um passado redescoberto, onde a natureza e o sobrenatural estão intrinsecamente conectados. Esta seção serve como um guia visual unificado para garantir a consistência estética em todas as fases do projeto, desde os ícones de interface até a arte de cenário e combate.
##### 5.2 Estilo Visual e Referências
A identidade visual do jogo é definida por uma combinação de pixel art moderna e influências culturais brasileiras, resumida na tabela abaixo.
| Elemento Visual | Definição |
| ------ | ------ |
| **Estilo Gráfico** | Pixel Art moderna, com atenção aos detalhes e iluminação atmosférica. |
| **Paleta Principal** | Tons terrosos, madeira, palha, dourado envelhecido, verdes profundos e toques de azuis e roxos místicos. |
| **Atmosfera** | Rústica, espiritual, conectada à natureza e aos ciclos de tempo e vida. |
| **Referências Visuais** | *Sea of Stars* ,  *Wartales* ,  *Solasta*  (para o combate), arte brasileira artesanal e indígena. |

##### 5.3 Design de UI, HUD e Ícones
A interface do usuário (UI) deve ser funcional e imersiva, reforçando a identidade visual do jogo.
*   **UI e HUD:**  Os componentes da interface, como janelas e barras de status, utilizarão molduras com textura de madeira, detalhes em cordas e entalhes tribais. O HUD será contextual, aparecendo apenas quando necessário para não poluir a tela e maximizar a imersão no cenário.
*   **Ícones:**  Todos os ícones de atributos, proficiências e status serão em pixel art de 32x32px com fundo transparente. A simbologia será clara e inspirada em elementos tribais e naturais. Por exemplo: um coração para Vigor, uma máscara para Astúcia, e ícones temáticos para as Proficiências de Vida (folhas para Coleta, ferramentas para Refinamento, bigornas para Produção).
##### 5.4 Tipografia e Arte de Cenário
O texto e os ambientes são elementos cruciais para a apresentação e legibilidade da experiência.
*   **Tipografia:**  As fontes devem garantir excelente legibilidade e suporte completo ao Português do Brasil (PT-BR). As fontes avaliadas incluem  **Londrina Solid**  para títulos,  **TinyUnicode**  para textos menores e  **Press Start 2P**  como uma opção estilizada.
*   **Arte de Cenário e Blocos:**  Os ambientes serão construídos como "cenas conectadas", onde cada bloco é uma ilustração detalhada em pixel art. Elementos interativos como NPCs e recursos serão sprites sobrepostos a esses fundos, criando uma sensação de profundidade e vida.
*   **Combate:**  A arena de combate adotará um estilo tático isométrico, com um grid em perspectiva. Os tiles do cenário serão coloridos para indicar visualmente o alcance de movimento (azul) e de ataque (vermelho), garantindo clareza estratégica durante as batalhas.
A seguir, um apêndice detalhado servirá como recurso de consulta rápida sobre as classes de personagem que dão vida a este mundo.
#### 6.0 Apêndice: Detalhamento das Classes de Personagem (Tier 1)
##### 6.1 Introdução Estratégica
Esta seção funciona como um apêndice de referência rápida para todas as classes iniciais (Tier 1) disponíveis no jogo. Cada classe está intrinsecamente ligada à sua origem e oferece um estilo de jogo único, com habilidades e papéis distintos que são fundamentais tanto para a estratégia de combate quanto para a narrativa. Este guia serve para auxiliar jogadores e desenvolvedores a compreender rapidamente o núcleo funcional de cada arquétipo.
##### 6.2 Classes de Origem: Colonizador
###### Conquistador
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | Tank clássico focado em provocação, resistência e proteção de aliados na linha de frente. |
| **Atributos Recomendados** | Vigor, Força Bruta |
| **Habilidade Ativa Inicial** | **Provocação Tática:**  Inimigos próximos devem focar seus ataques no Conquistador. |
| **Habilidade Passiva Inicial** | **Postura Inabalável:**  Com armadura pesada, ganha +1 de Defesa e imunidade a empurrões. |

###### Explorador de Terras
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | Suporte tático, especialista em exploração, navegação e uso de armadilhas. |
| **Atributos Recomendados** | Astúcia, Sabedoria Ancestral |
| **Habilidade Ativa Inicial** | **Reconhecimento Rápido:**  Concede a todos os aliados bônus em Iniciativa e Percepção. |
| **Habilidade Passiva Inicial** | **Cartografia Prática:**  Nunca se perde em áreas já visitadas e ganha bônus em testes de Navegação. |

###### Mosqueteiro
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | Atirador de elite com alto dano à distância, focado em controle de campo e disparos explosivos. |
| **Atributos Recomendados** | Astúcia, Conhecimento |
| **Habilidade Ativa Inicial** | **Tiro Preparado:**  Gasta um turno para mirar e, no turno seguinte, dispara com bônus massivo de dano e acerto. |
| **Habilidade Passiva Inicial** | **Mestre da Pólvora:**  Ignora a primeira penalidade de recarga por combate e prepara armas mais rápido. |

###### Missionário
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | Suporte mágico focado em cura, bênçãos de proteção e resistência espiritual. |
| **Atributos Recomendados** | Conhecimento, Presença |
| **Habilidade Ativa Inicial** | **Bênção da Salvação:**  Remove um efeito negativo de um aliado ou concede defesa contra ataques mágicos. |
| **Habilidade Passiva Inicial** | **Fé Inabalável:**  Vantagem em testes contra medo e influências espirituais negativas. |

##### 6.3 Classes de Origem: Indígena
###### Guerreiro Tribal
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | Tank ofensivo e agressivo que protege a linha de frente com investidas e alta resistência física. |
| **Atributos Recomendados** | Vigor, Força Bruta |
| **Habilidade Ativa Inicial** | **Investida Tribal:**  Avança rapidamente e realiza um ataque corpo a corpo com vantagem. |
| **Habilidade Passiva Inicial** | **Espírito do Clã:**  Recebe bônus em ataques corpo a corpo quando está com menos de 50% dos PV. |

###### Caçador de Feras
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | DPS móvel e rastreador, mestre do ambiente selvagem, com foco em ataques de precisão. |
| **Atributos Recomendados** | Astúcia, Sabedoria Ancestral |
| **Habilidade Ativa Inicial** | **Arremesso Rápido:**  Realiza um ataque à distância com uma arma de arremesso com bônus de acerto. |
| **Habilidade Passiva Inicial** | **Rastreio Natural:**  Bônus em testes de Percepção e Sobrevivência em ambientes selvagens. |

###### Arqueiro Selvagem
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | DPS furtivo à distância, especialista em emboscadas e mobilidade em terrenos naturais. |
| **Atributos Recomendados** | Astúcia, Vigor |
| **Habilidade Ativa Inicial** | **Tiro Furtivo:**  Causa dano adicional se o alvo ainda não agiu no combate. |
| **Habilidade Passiva Inicial** | **Passos Silenciosos:**  Ignora penalidades de terreno difícil e ganha bônus em Furtividade em ambientes naturais. |

###### Xamã Curandeiro
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | Suporte mágico e espiritual, focado em cura, purificação de maldições e realização de rituais. |
| **Atributos Recomendados** | Sabedoria Ancestral, Conhecimento |
| **Habilidade Ativa Inicial** | **Oferenda Curativa:**  Cura um aliado a curta distância. |
| **Habilidade Passiva Inicial** | **Chamado dos Espíritos:**  Realiza rituais em metade do tempo e tem vantagem contra maldições. |

##### 6.4 Classes de Origem: Ser Folclórico
###### Guardião Ancestral
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | Tank espiritual que defende o grupo com escudos mágicos e alta resistência a entidades sobrenaturais. |
| **Atributos Recomendados** | Vigor, Sabedoria Ancestral |
| **Habilidade Ativa Inicial** | **Escudo Espiritual:**  Concede bônus de Defesa a um aliado por um turno. |
| **Habilidade Passiva Inicial** | **Aura Protetora:**  Ganha bônus de Defesa contra ataques corpo a corpo e imunidade a empurrões. |

###### Lobo Lendário
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | DPS híbrido, ágil e rápido, que combina ataques físicos e espirituais com alta mobilidade e detecção. |
| **Atributos Recomendados** | Astúcia, Presença |
| **Habilidade Ativa Inicial** | **Investida Sombria:**  Move-se rapidamente em linha reta, ignorando terreno, e causa dano adicional se atingir um inimigo. |
| **Habilidade Passiva Inicial** | **Faro de Alma Viva:**  Detecta presenças mágicas, espirituais ou animais próximas e é imune a emboscadas. |

###### Ser Elemental
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | Mago elemental ofensivo que controla as forças da natureza para causar dano em área e aplicar efeitos de controle. |
| **Atributos Recomendados** | Conhecimento, Sabedoria Ancestral |
| **Habilidade Ativa Inicial** | **Rajada Elemental:**  Causa dano mágico e aplica um efeito elemental leve (queimar, empurrar, etc.). |
| **Habilidade Passiva Inicial** | **Vínculo Elemental:**  Ganha resistência (meio dano) contra um tipo de elemento escolhido na criação. |

###### Encantador de Espíritos
| Característica | Descrição |
| ------ | ------ |
| **Estilo de Jogo** | Suporte mágico e invocador que interage com o mundo espiritual para distrair, controlar ou fortalecer aliados. |
| **Atributos Recomendados** | Presença, Conhecimento |
| **Habilidade Ativa Inicial** | **Invocação Menor:**  Invoca um espírito auxiliar temporário que pode atacar ou distrair inimigos. |
| **Habilidade Passiva Inicial** | **Canal Espiritual:**  Detecta presenças sobrenaturais e ganha bônus em interações com o plano espiritual. |

