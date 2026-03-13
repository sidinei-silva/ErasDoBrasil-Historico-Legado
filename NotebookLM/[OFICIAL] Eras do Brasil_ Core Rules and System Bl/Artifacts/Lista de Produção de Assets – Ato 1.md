### Lista de Produção de Assets – Ato 1
Equipe, este é o nosso guia mestre para a equipe de arte, detalhando todos os assets visuais necessários para a construção do Ato 1 de "Eras do Brasil". Este documento define o  *quê*  e, mais importante, o  *porquê*  por trás de cada sprite, ícone e cenário. A priorização (Alta, Média, Baixa) foi definida para um avanço focado nos marcos do protótipo jogável. Nossa meta é ter os elementos essenciais da experiência do jogador—movimentação, combate e interação com o núcleo do mundo—funcionando o mais rápido possível. Foquem nos assets de 'Alta' prioridade; eles são a espinha dorsal do Ato 1.
#### 1. Sprites de Personagens (Classes Tier 1)
Esta seção contém a lista completa dos 24 sprites de personagens jogáveis necessários para o Ato 1. Ela abrange as 12 classes iniciais, cada uma com seus dois estados fundamentais: Idle (parado) e Attack (ataque). As descrições visuais devem seguir a direção de arte de "Pixel Art moderna", capturando a essência narrativa e mecânica de cada classe, conforme definido na nossa lore e GDD.
| ID | Nome do Asset | Descrição Visual | Prioridade |
| ------ | ------ | ------ | ------ |
| CHAR_001 | Conquistador - Idle | Pixel art, postura firme com armadura pesada colonial e escudo. Paleta terrosa com detalhes metálicos. Seu design deve servir como um contraponto heroico ao do ENMY_001: Bandeirante de Sangue, que representa a versão corrompida e hostil da mesma cultura. | Alta |
| CHAR_002 | Conquistador - Attack | Animação de golpe com maça ou espada, movimento de corpo pesado e imponente. | Alta |
| CHAR_003 | Explorador de Terras - Idle | Postura alerta, segurando mapa ou adaga. Veste roupas de couro práticas, com bússola visível. | Alta |
| CHAR_004 | Explorador de Terras - Attack | Animação de ataque rápido com adaga ou espada curta, movimento ágil. | Alta |
| CHAR_005 | Mosqueteiro - Idle | Segurando um mosquete longo, postura de atirador. Veste capa e colete de pólvora. | Alta |
| CHAR_006 | Mosqueteiro - Attack | Animação de mira e disparo, com recuo e efeito de fumaça da pólvora. | Alta |
| CHAR_007 | Missionário - Idle | Postura serena, segurando um livro sagrado ou cruz. Veste mantos clericais. Paleta com brancos e dourados. | Alta |
| CHAR_008 | Missionário - Attack | Animação de canalização de bênção, com luz emanando das mãos ou do símbolo de fé. | Alta |
| CHAR_009 | Guerreiro Tribal - Idle | Postura de combate agressiva, com lança ou clava. Corpo com pinturas de guerra. Veste peles e couro. | Alta |
| CHAR_010 | Guerreiro Tribal - Attack | Animação de investida ou golpe poderoso com lança, expressando força bruta. | Alta |
| CHAR_011 | Caçador de Feras - Idle | Postura agachada, de rastreador. Veste couro flexível e carrega uma lança leve. | Alta |
| CHAR_012 | Caçador de Feras - Attack | Animação de arremesso de lança ou ataque rápido com adaga. | Alta |
| CHAR_013 | Arqueiro Selvagem - Idle | Postura furtiva com arco em punho. Veste peles e trajes de camuflagem na floresta. | Alta |
| CHAR_014 | Arqueiro Selvagem - Attack | Animação de puxar a corda do arco e disparar uma flecha. | Alta |
| CHAR_015 | Xamã Curandeiro - Idle | Postura ritualística, segurando um cajado de cipó ou talismã. Veste mantos com ervas e sementes. | Alta |
| CHAR_016 | Xamã Curandeiro - Attack | Animação de canalização de cura, com energia espiritual verde ou dourada. | Alta |
| CHAR_017 | Guardião Ancestral - Idle | Postura defensiva e imóvel. Corpo parece feito de casca de árvore e raízes. Carrega lança espiritual. | Alta |
| CHAR_018 | Guardião Ancestral - Attack | Animação de bloqueio ou golpe defensivo com lança, com efeito de escudo espiritual. | Alta |
| CHAR_019 | Lobo Lendário - Idle | Postura bestial, ágil. Híbrido de humano e lobo, com garras visíveis. | Alta |
| CHAR_020 | Lobo Lendário - Attack | Animação de avanço rápido e ataque com garras, deixando um rastro sombrio. | Alta |
| CHAR_021 | Ser Elemental - Idle | Flutuando levemente, com energia elemental circulando ao redor. O visual deve refletir a origem do personagem: um elemental folclórico pode ser caótico e natural (cipós, rochas brutas), enquanto um de origem colonizadora pode ter uma energia mais contida e alquímica (metal derretido, vapor controlado). | Alta |
| CHAR_022 | Ser Elemental - Attack | Animação de lançamento de uma rajada do elemento correspondente. | Alta |
| CHAR_023 | Encantador de Espíritos - Idle | Postura serena, talvez com um pequeno espírito flutuando próximo. Veste mantos com runas. | Alta |
| CHAR_024 | Encantador de Espíritos - Attack | Animação de invocação, com um selo mágico aparecendo no chão para chamar um espírito. | Alta |

*Nota de Produção: Todos os sprites de personagens Tier 1 são de 'Alta' prioridade, pois a mecânica do 'Dom da Revivência' permite que os jogadores troquem de classe livremente fora de combate. Precisamos do elenco completo para que esta mecânica central seja funcional no protótipo.*
Com os personagens definidos, o próximo passo é criar os ícones que representarão visualmente os sistemas, recursos e atributos que eles utilizam na interface.
#### 2. Ícones de UI (Interface do Usuário)
A clareza da interface do usuário (UI) é crucial para uma experiência de jogo intuitiva. Os ícones são a espinha dorsal dessa clareza, comunicando informações complexas de forma rápida e alinhada à nossa direção de arte eco-fantástica. Todos os ícones listados devem ser criados em pixel art no formato 32x32px, com simbologia tribal ou colonial, conforme o tema.
##### 2.1. Atributos
| ID | Nome do Asset | Descrição Visual | Prioridade |
| ------ | ------ | ------ | ------ |
| ICON_001 | Ícone de Vigor | Um coração estilizado com traços rústicos ou tribais. | Alta |
| ICON_002 | Ícone de Força Bruta | Um braço musculoso ou uma clava/martelo estilizado. | Alta |
| ICON_003 | Ícone de Astúcia | Uma máscara ou uma pena, simbolizando agilidade e sagacidade. | Alta |
| ICON_004 | Ícone de Sabedoria Ancestral | Um olho aberto com espirais ou um símbolo de raiz. | Alta |
| ICON_005 | Ícone de Conhecimento | Um livro aberto ou um pergaminho. | Alta |
| ICON_006 | Ícone de Presença | Uma face carismática ou uma chama, simbolizando influência. | Alta |

##### 2.2. Proficiências de Vida
| ID | Nome do Asset | Descrição Visual | Prioridade |
| ------ | ------ | ------ | ------ |
| ICON_007 | Ícone de Caça | Um rastro de pegada animal. | Média |
| ICON_008 | Ícone de Herborismo | Um ramo de folhas ou ervas. | Média |
| ICON_009 | Ícone de Mineração | Uma picareta cruzada com uma pedra. | Média |
| ICON_010 | Ícone de Alquimia | Um frasco borbulhando (caldeirão). | Média |
| ICON_011 | Ícone de Ferraria | Uma bigorna com um martelo. | Média |
| ICON_012 | Ícone de Rastreamento | Uma lupa sobre uma pegada. | Média |
| ICON_013 | Ícone de Arquearia | Um arco com uma flecha. | Média |
| ICON_014 | Ícone de Engenharia | Uma engrenagem ou uma ferramenta de medição. | Média |

##### 2.3. Recursos Coletáveis
| ID | Nome do Asset | Descrição Visual | Prioridade |
| ------ | ------ | ------ | ------ |
| ICON_015 | Ícone de Madeira de Ferro | Uma tora de madeira escura com brilho metálico. Encontrada na Floresta do Norte (TILE_002), deve parecer densa e resistente. | Alta |
| ICON_016 | Ícone de Erva-Lua | Uma erva com folhas que brilham com uma luz azul mística. Encontrada à noite na beira do Rio das Marés (TILE_005), seu brilho deve contrastar com a lama e a água escura do cenário. | Alta |
| ICON_017 | Ícone de Minério de Sangue | Uma pedra de minério vermelha e pulsante. Seu design deve ser consistente com os veios de minério que aparecerão no tileset TILE_003 (Caverna do Pico da Neblina). | Alta |
| ICON_018 | Ícone de Cinzas Espirituais | Um pequeno monte de cinzas com partículas roxas flutuando. Coletadas nas Ruínas Queimadas (TILE_004), o design deve ecoar a atmosfera de terror e a 'Regra de Terror' da zona. | Alta |
| ICON_019 | Ícone de Comida/Suprimentos | Um peixe assado ou um saco de grãos. | Média |

Esses personagens e ícones ganharão vida quando integrados aos cenários do jogo. A seção seguinte detalha os tilesets necessários para construir esses ambientes, a alma do nosso mundo.
#### 3. Tilesets e Cenários
Esta seção define os pacotes de tilesets para os ambientes exploráveis da Mata Costeira, o palco do Ato 1. As descrições devem guiar a criação de assets modulares que não apenas construam os mapas, mas também capturem a atmosfera única de cada bioma e reforcem suas mecânicas de jogo.
| ID | Nome do Asset | Descrição Visual | Contexto Narrativo / de Jogo | Prioridade |
| ------ | ------ | ------ | ------ | ------ |
| TILE_001 | Tileset: Vila de São Tomé | Urbano colonial rústico. Inclui tiles para casas de madeira e palha, chão de terra batida, uma capela simples, uma taverna e uma forja. Paleta terrosa. | O hub central e zona segura do Ato 1. Local de descanso, comércio e NPCs-chave. Deve transmitir uma sensação de segurança rústica, mas frágil. | Alta |
| TILE_002 | Tileset: Floresta do Norte | Mata densa e antiga. Inclui árvores altas que bloqueiam a luz, raízes expostas, vegetação rasteira, clareiras e trilhas de terra. Verdes profundos. | Principal fonte de Madeira de Ferro. A regra de 'Cobertura Natural' afeta o combate, então o ambiente deve ser visualmente denso, com muitas árvores e raízes para justificar a mecânica. | Alta |
| TILE_003 | Tileset: Caverna (Pico da Neblina) | Ambiente subterrâneo e rochoso no Pico da Neblina. Inclui paredes de caverna, estalactites, veios de Minério de Sangue pulsantes, poças d'água e passagens estreitas. | Principal fonte de Minério de Sangue. A exploração é dificultada pela 'Regra de Exaustão', exigindo que o ambiente pareça opressor, desgastante e com ar rarefeito. | Média |
| TILE_004 | Tileset: Ruínas Queimadas | O local de um massacre antigo. Terra arrasada e pantanosa. Inclui chão de cinzas, árvores carbonizadas e ruínas de cabanas. O ar deve parecer pesado, com cheiro de fumaça eterna. Atmosfera de terror com tons de cinza e roxo espiritual. | Zona governada pela 'Regra de Terror', causando alucinações no jogador. O design deve ser psicologicamente perturbador e é o habitat principal dos 'Espíritos Corrompidos'. | Média |
| TILE_005 | Tileset: Rio das Marés | Margem de rio com lama e areia. Inclui tiles de água (nível baixo e alto), pedras de rio e vegetação de mangue. | Local de coleta da Erva-Lua (à noite). A mecânica do 'Ciclo da Maré' é central aqui, então a diferença visual entre maré alta e baixa deve ser clara e impactante, comunicando acesso e perigo. | Média |

Ambientes imersivos precisam de desafios à altura. A próxima seção detalha os inimigos que habitarão essas terras, garantindo que a exploração seja sempre recompensadora e perigosa.
#### 4. Inimigos
Esta lista final detalha os adversários do Ato 1. Cada design deve ser uma aula de história visual instantânea para o jogador, comunicando a natureza da ameaça — o fanatismo organizado dos Bandeirantes, a agonia disforme dos Espíritos Corrompidos pela Raiz do Mundo, ou a fúria primitiva da fauna local. A clareza da ameaça é fundamental.
| ID | Nome do Asset | Descrição Visual | Contexto Narrativo / de Jogo | Prioridade |
| ------ | ------ | ------ | ------ | ------ |
| ENMY_001 | Inimigo: Bandeirante de Sangue | Humano, colonial. Armadura de couro e metal, carrega mosquete ou espada. Sua aparência deve ser determinada, implacável e organizada, refletindo sua disciplina militar. | A principal facção rival em uma 'corrida contra o tempo'. Eles não são bandidos aleatórios; são uma força expedicionária com um objetivo claro. Seu design deve comunicar eficiência e fanatismo. | Alta |
| ENMY_002 | Inimigo: Espírito Corrompido | Entidade etérea e flutuante, com forma humanoide distorcida. Brilha com uma luz roxa ou azul doentia, um eco visual da corrupção da Raiz do Mundo. | Encontrados principalmente nas Ruínas Queimadas (TILE_004), sua presença está ligada à 'Regra de Terror' da zona. O design deve evocar agonia e uma perda de identidade. | Alta |
| ENMY_003 | Inimigo: Onça | Um grande felino (jaguar). Pixel art detalhado, musculoso, com um padrão de manchas intimidador. Pode ter olhos brilhantes para indicar natureza mística. | Predador alfa da Floresta do Norte (TILE_002). Seu design deve comunicar a fúria primitiva da fauna local, intensificada pela instabilidade da Raiz do Mundo. | Média |
| ENMY_004 | Inimigo: Lobo Alfa | Um lobo maior e mais feroz que o comum, com cicatrizes e pelagem escura. Pode ter um brilho vermelho nos olhos. | Inimigo especial cuja localização varia a cada jogo (Floresta do Norte ou Pico da Neblina). Representa um desafio de rastreamento e um pico de dificuldade na exploração selvagem. | Média |
| ENMY_005 | Inimigo: Ghoul | Humanoide pálido e esquelético, com movimentos rápidos e erráticos, e garras afiadas. | Encontrado na cripta sob a capela da Vila de São Tomé durante a missão 'Onde Enterram os Segredos'. Seu design deve evocar um horror claustrofóbico e profano, adequado a um dungeon crawl apertado. | Baixa |
| ENMY_006 | Inimigo: Criatura Devoradora de Sonhos | Entidade sombria, de forma indefinida, talvez feita de sombras e névoa. Deve parecer surreal e perturbadora. | Entidade encontrada na missão 'O Caçador que Não Voltou'. Seu propósito é drenar a vitalidade de suas vítimas. O design deve ser surreal e etéreo, mais um pesadelo do que uma criatura física. | Baixa |

