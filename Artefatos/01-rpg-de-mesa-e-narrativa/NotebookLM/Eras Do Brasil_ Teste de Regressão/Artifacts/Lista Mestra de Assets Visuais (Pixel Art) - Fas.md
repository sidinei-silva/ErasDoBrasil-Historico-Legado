### Lista Mestra de Assets Visuais (Pixel Art) - Fase 1
##### Introdução e Diretrizes Gerais
Este documento serve como a lista mestra de assets de cenário prioritários para a Fase 1 de produção do jogo  *Eras do Brasil* . O escopo aqui definido foi elaborado com base nos eventos narrativos do Ato 1 e nas 18 mini-campanhas que o compõem, focando em tilesets e backgrounds que são críticos para a progressão e imersão inicial do jogador. O objetivo principal é guiar a equipe de arte, garantindo que os cenários mais cruciais sejam produzidos primeiro, otimizando o fluxo de trabalho e alinhando a produção visual às necessidades do design de jogo. Conforme a direção de arte estabelecida, todos os assets devem seguir o estilo de "Pixel Art moderna" com um grid base de 32x32px para elementos interativos e ícones.

--------------------------------------------------------------------------------

##### 1. Bioma: Florestas e Matas
A floresta é o bioma central e mais recorrente do Ato 1, servindo como palco para a convergência de facções e o despertar da Primeira Ruptura. A versatilidade deste bioma é crucial; ele precisa ser capaz de representar tanto a natureza vibrante e cheia de vida quanto sua contraparte sombria, corrompida pela instabilidade da Raiz do Mundo. Esta corrupção deve se manifestar visualmente através de veias de energia roxa pulsando no solo, uma flora distorcida com espinhos antinaturais e uma paleta de cores dessaturada que contrasta com a vibração da floresta saudável. A criação de um tileset robusto para a floresta é a fundação visual da nossa primeira fase de desenvolvimento.
| Nome do Asset | Variação de Estado Requerida | Prioridade | Referência Narrativa/Mecânica |
| ------ | ------ | ------ | ------ |
| **Floresta Padrão (Tileset)** | Dia (luz solar filtrada pela copa das árvores), Noite (iluminação lunar, com áreas de escuridão total e outras banhadas por fachos de luz) | Alta | Asset base para a maioria dos eventos de exploração e mini-campanhas do Ato 1. |
| **Bosque das Sombras (Versão Corrompida)** | Noite, Atmosfera Opressora com névoa roxa e flora agressiva | Alta | Resultado visual se o jogador falhar em conter a Ruptura no final do Ato 1, transformando o bioma. |
| **Clareira Sagrada** | Dia, Noite, Vibração Mística (partículas de luz e runas sutis no chão) | Alta | Local para rituais e eventos de facção, como o despertar do Mentor em "O Tambor que Silenciou o Céu". |
| **Vale com Cachoeira** | Dia (Manhã), Noite | Alta | Ponto de encontro com o Velho Pajé, NPC chave para a localização do Epicentro da Ruptura no Ato 1. |
| **Trilha do Rio** | Dia, Noite | Baixa (Bloco de conexão, com menor densidade de eventos no Ato 1) | Rota de caravana usada na missão "O Tambor que Silenciou o Céu" e cenário para eventos de transição. |
| **Lago dos Espelhos** | Dia, Noite (Lua Alta com neblina) | Alta | Palco central da mini-campanha "A Canção que Não Dorme", onde a entidade se manifesta. |
| **Floresta dos "Espinhos"** | Corrompida, Agressiva (cipós com espinhos, solo árido) | Alta | Território de uma das facções espirituais da mini-campanha "Os Filhos do Espinho e da Flor". |
| **Floresta das "Flores"** | Simbiótica, Curativa (flores bioluminescentes, fauna pacífica) | Alta | Território da facção rival na mesma mini-campanha, "Os Filhos do Espinho e da Flor". |

Com a fundação da natureza selvagem definida, a próxima etapa é a construção dos hubs de civilização, que servirão como âncoras narrativas e visuais para o jogador.
##### 2. Bioma: Vilas e Assentamentos
As vilas e assentamentos são os principais hubs sociais e narrativos da Fase 1, onde o jogador encontrará missões, informações e as tensões culturais do mundo. A diretriz principal é diferenciar visualmente os assentamentos de origem Indígena e Colonial. Para os assentamentos coloniais, priorize linhas retas, madeira cortada, telhas e uma organização em grid, evocando ordem e domínio. Para as vilas indígenas, foque em estruturas orgânicas, materiais locais (palha, barro, cipó) e uma integração harmoniosa com a topografia, refletindo uma conexão com a terra.
| Nome do Asset | Variação de Estado Requerida | Prioridade | Referência Narrativa/Mecânica |
| ------ | ------ | ------ | ------ |
| **Vila Colonial Inicial (Tileset)** | Normal (Próspera), Evacuada/Corrompida | Alta | Hub principal para missões coloniais. A variação "Evacuada" ocorre se a Ruptura do Ato 1 explodir. |
| **Praça da Vila Colonial** | Dia (com corpo enforcado), Noite (com patrulhas) | Alta | Central para a mini-campanha "Justiça das Mãos Sujas". O corpo enforcado é o gatilho da missão. |
| **Porto de Santa Azeitona** | Dia, Noite | Baixa (Relevante para uma missão, mas não um hub principal na Fase 1) | Cenário da anomalia temporal da mini-campanha "Os Relógios do Porto Morto". |
| **Interior de Taverna Colonial** | Padrão (com NPCs e eventos de "Fofoca") | Alta | Local de encontro com NPCs para missões como "Onde Enterram os Segredos" e hub social para coleta de pistas. |
| **Vila Indígena (Tileset)** | Dia, Noite, Estado de Alerta (barricadas improvisadas, fogueiras de vigília, NPCs em postura defensiva) | Alta | Hub principal para missões indígenas. A variação "Estado de Alerta" é ativada na missão "Sombras na Aldeia da Lua Nova". |
| **Roça e Plantações** | Normal, Amaldiçoada (cinza/podre) | Baixa (Cenário de uma missão específica) | O estado "Amaldiçoada" é o gatilho visual para a mini-campanha "Sementes de Terra e Sangue". |
| **Forte Colonial** | Padrão | Baixa (Relevante na missão 'O Tambor que Silenciou o Céu', mas não um hub central na Fase 1) | Local de destino da caravana inimiga que o jogador precisa interceptar para recuperar o Tambor. |

Estes locais habitados contrastam diretamente com os espaços onde o tempo e a negligência reinaram, que agora detalharemos como os principais palcos de exploração e mistério.
##### 3. Bioma: Ruínas e Locais Sagrados
As ruínas são os palcos de mistérios, dungeons e revelações espirituais, onde o passado se manifesta de forma tangível. Esses cenários são os palcos para o  **Dom da Revivência** , onde ecos do passado e futuro se misturam. A arte deve facilitar essa imersão, com elementos que sugiram a sobreposição de eras, como arquitetura fantasmagórica ou flora de diferentes períodos históricos crescendo juntas.
| Nome do Asset | Variação de Estado Requerida | Prioridade | Referência Narrativa/Mecânica |
| ------ | ------ | ------ | ------ |
| **Ruínas da Aldeia Queimada** | Dia, Noite (com assombrações visíveis) | Alta | Palco da mini-campanha "Sombras Sobre a Aldeia Queimada", onde o jogador realiza um ritual de purificação. |
| **Fronteira dos Mundos (Entrada do Epicentro)** | Normal (tensão pré-conflito), Zona de Guerra (após Fase 2 do Relógio) | Alta | Palco da aliança ou conflito de facções na Sessão 2 do Ato 1. |
| **Cripta sob Capela** | Escura (requer tocha), Normal | Baixa (Dungeon opcional de uma mini-campanha) | Dungeon central da missão "Onde Enterram os Segredos", com segredos da Igreja local. |
| **Altar do Esquecimento** | Padrão (com chama fraca), Ativado (com memórias projetadas) | Baixa (Local de clímax de uma missão secundária) | Ponto final da peregrinação na mini-campanha "A Última Luz da Tribo Sem Nome". |

Das profundezas das ruínas esquecidas, a jornada continua para os ambientes mais extremos e isolados do mundo: as cavernas subterrâneas e os picos das montanhas.
##### 4. Bioma: Cavernas e Montanhas
Cavernas e montanhas representam ambientes de isolamento, provação e descoberta. Esses locais testam as habilidades de exploração do jogador e servem como covis para mentores eremitas, feras lendárias e segredos geológicos. A verticalidade e a claustrofobia devem ser elementos-chave na composição visual destes assets. Isso se traduz na necessidade de tilesets que suportem escalada visual (fendas, apoios de rocha), passagens estreitas que forcem uma visão de câmera mais próxima e grandes espaços abertos que revelem a vastidão geológica, conectando-se diretamente à energia da Raiz do Mundo.
| Nome do Asset | Variação de Estado Requerida | Prioridade | Referência Narrativa/Mecânica |
| ------ | ------ | ------ | ------ |
| **Mina de Ouro (Caverna)** | Entrada Submersa (Maré Alta), Entrada Acessível (Maré Baixa) | Alta | Principal local da mini-campanha "O Ouro que Nunca Brilha". A mecânica de maré é um puzzle de tempo baseado em Ticks. |
| **Toca da Fera (Caverna)** | Padrão | Baixa (Local de encontro de uma missão específica) | Local onde o caçador perdido é encontrado na mini-campanha "O Caçador que Não Voltou". |
| **Caverna do Sábio Eremita** | Padrão | Alta | Ponto de encontro com o Xamã eremita na mini-campanha "O Sábio que Viu o Amanhã". |
| **Montanha (Tileset de Escalada)** | Dia, Noite | Alta | Cenário da corrida contra o tempo para alcançar o topo na missão "O Sábio que Viu o Amanhã". |
| **Topo da Montanha (Pedra dos Ventos)** | Dia (com tempestade mágica controlada) | Alta | Arena do teste e local de encontro com o Mentor Elemental na missão "O Sopro dos Quatro Ventos". |

Após explorarmos os extremos físicos do mundo, devemos nos preparar para visualizar os locais onde a própria realidade se desfaz: as zonas de pura manifestação mística.
##### 5. Bioma: Zonas Místicas e de Ruptura
As Zonas Místicas são o ápice da temática eco-fantástica do jogo e o palco dos eventos mais importantes do Ato 1. Estes cenários representam a instabilidade crescente da Raiz do Mundo e devem ser visualmente impactantes. É aqui que a direção de arte pode explorar seu lado mais surreal, criando arenas de batalha e dungeons onde o tempo e o espaço colapsam. Isso deve suportar mecanicamente a  **Fase 3 (O Colapso)**  do Relógio da Ruptura, com portais se abrindo aleatoriamente e um terreno que muda dinamicamente, como descrito na estrutura do Ato 1.
| Nome do Asset | Variação de Estado Requerida | Prioridade | Referência Narrativa/Mecânica |
| ------ | ------ | ------ | ------ |
| **Zona de Distorção Temporal (Dungeon)** | Terreno Instável (caminhos mudam), Normal (antes do colapso) | Alta | Dungeon da Sessão 3 do Ato 1. O terreno muda conforme o progresso do Relógio da Ruptura. |
| **Epicentro da Ruptura (Arena do Boss)** | Fenda Contida, Fenda Explodida (Ascendida) | Alta | Arena do boss final do Ato 1. A variação "Explodida" corresponde ao estado "Ascendido" do boss se o jogador chegar após 500 Ticks. |

