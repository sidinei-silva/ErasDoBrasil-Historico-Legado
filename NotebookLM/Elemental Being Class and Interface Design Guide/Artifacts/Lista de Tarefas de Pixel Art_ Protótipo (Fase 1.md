### Lista de Tarefas de Pixel Art: Protótipo (Fase 1)
Este documento constitui a lista de tarefas oficial para a produção de assets de pixel art necessários para o protótipo da Fase 1 do jogo "Eras do Brasil", conforme definido nos documentos de design. A execução desta lista é fundamental para validar o loop de jogabilidade inicial e a identidade visual do projeto. Reitera-se que todos os ícones devem ser criados e exportados seguindo a grade base de 32x32px. A direção de arte geral deve seguir o estilo "Pixel Art moderna", com uma paleta de cores focada em tons terrosos, mas enriquecida por verdes profundos, azuis místicos e roxos espirituais. A atmosfera deve ser rústica, espiritual, mística e conectada à natureza e aos seus ciclos, tomando como principais referências visuais os jogos  *Sea of Stars*  e  *Wartales* .

--------------------------------------------------------------------------------

##### 1. Elementos de UI (Interface do Usuário)
A interface de usuário (UI) para a Fase 1 deve evocar a sensação tátil de um "jogo de tabuleiro digital" ou de um "RPG de Texto Visual". O objetivo não é a complexidade, mas a clareza imersiva. Os elementos a seguir formam a espinha dorsal da experiência do jogador, definindo a navegação por menus, a exploração por nós e o combate estático, que juntos devem criar uma primeira impressão coesa do nosso mundo.
###### 1.1. HUD Principal (Painel de Gestão Superior)
O HUD principal ficará fixo no topo da tela, fornecendo informações vitais de forma rápida e contextual.
*   **Moldura do Painel:**  Uma barra horizontal contínua com uma textura rica de madeira escura, com detalhes entalhados. Deve ser projetada utilizando uma metodologia 9-slice para permitir redimensionamento flexível sem distorção.
*   **Moldura do Retrato do Personagem:**  Um quadro ornamental, posicionado à esquerda, que abrigará o retrato do personagem ativo.
*   **Barras de Status:**  Designs únicos para a barra de Pontos de Vida (PV), em tons de vermelho, e a barra de Pontos de Experiência (XP), em azul/amarelo. Ambas devem possuir molduras que se integram à barra principal.
*   **Ícones de Recursos de Coleta:**  Ícones distintos e legíveis para Madeira, Pedra, Ervas e Couro.
*   **Ícone de Moeda:**  Um ícone para a Unidade Comercial (UC), que pode ser representado por uma peça de ouro ou um artefato simbólico de troca.
*   **Relógio de Ticks:**  Um ícone circular de sol/lua que transita visualmente para indicar a passagem do tempo e os ciclos de dia e noite.
###### 1.2. Tela de Exploração (Mapa de Nós)
A exploração na Fase 1 ocorre em um mapa de nós, onde cada ícone representa um "bloco" de cenário ou evento. A referência principal para a funcionalidade e o estilo visual deste mapa é  *Slay the Spire* .
*   **Nó de Local Inexplorado:**  Um ícone de interrogação (?) estilizado, que transmita mistério e oportunidade.
*   **Nó de Descanso:**  Ícone de uma fogueira acesa, simbolizando segurança e recuperação.
*   **Nó de Combate:**  Ícone de uma caveira, indicando um confronto inevitável.
*   **Nó de Povoado:**  Ícone de uma cidade, aldeia ou uma casa/oca para representar assentamentos.
*   **Fundo do Mapa:**  Uma textura de alta qualidade de pergaminho amarelado ou mapa antigo desenhado à mão, servindo de base para a disposição dos nós.
###### 1.3. Tela de Evento e Interação (Cena)
Ao chegar a um nó, a interface mudará para o Modo de Cena, que prioriza a imersão narrativa. A referência principal para este layout é  *Roadwarden* . O design deve apresentar uma tela dividida:
*   **Painel Esquerdo:**  Uma ilustração em pixel art de alta qualidade, detalhada e atmosférica, representando o cenário atual (ex: uma clareira, o interior de uma capela).
*   **Painel Direito:**  Uma área de texto sobre um fundo de pergaminho, contendo a descrição narrativa do evento e os botões de escolha do jogador.
###### 1.4. Tela de Combate Estático
É crucial notar que o combate na Fase 1 é estático e não utiliza um grid tático. A apresentação deve se assemelhar a JRPGs clássicos ou a jogos como  *Path of Adventure* , onde o foco está na seleção de ações a partir de um menu.
*   **Botões da Barra de Ações:**  Botões com aparência de madeira ou pedra para as ações principais: ATACAR, HABILIDADE, ITEM, e DEFENDER/FUGIR. Cada botão (a textura de fundo, não apenas o texto) deve ter três estados visuais distintos: parado (idle), ao passar o mouse (hover) e pressionado (pressed).
*   **Ícones de Status:**  Ícones simples e universalmente reconhecíveis para indicar condições como "Envenenado" e "Atordoado", a serem exibidos próximos aos sprites dos personagens afetados.
###### 1.5. Elementos Gerais e Estilo
Estes elementos devem ser aplicados de forma consistente em todas as janelas e painéis para garantir a coesão visual.
*   **Molduras de Janela:**  Molduras gerais para painéis e caixas de texto, seguindo o estilo de madeira rústica e decoradas com detalhes de cordas e penas.
*   **Fundo de Painéis:**  Uma textura de papel envelhecido ou pergaminho para ser usada como fundo em áreas de texto, garantindo boa legibilidade.
A criação destes elementos de interface permitirá a construção dos menus e inventários que serão preenchidos pelos ícones de itens a seguir.

--------------------------------------------------------------------------------

##### 2. Ícones de Itens Iniciais
Esta seção cataloga todos os equipamentos iniciais que necessitam de um ícone único de 32x32px para representação no inventário. Cada ícone deve refletir a origem cultural (Colonizador, Indígena, Ser Folclórico) e sua qualidade "Muito Baixa", conforme o "sistema 5x5 de Qualidade e Raridade". Isso significa que os itens devem ter um aspecto improvisado, rústico ou mal-acabado, comunicando visualmente que são o ponto de partida na jornada do jogador.
**Conquistador (Colonizador)**  Representando a força organizada dos exércitos coloniais, esta classe é a muralha viva que impõe ordem no caos do campo de batalha.
*   **Armas:**  Espada de Ferro Mal Forjada, Maça de Cabeça Rachada
*   **Armaduras:**  Couraça de Couro com Reforço de Ferro, Elmo de Couro com Cruz Colonial
*   **Item Utilitário:**  Medalhão de São Jorge
**Explorador de Terras (Colonizador)**  Este desbravador do novo mundo domina a leitura de mapas, terrenos perigosos e segredos ocultos.
*   **Armas:**  Espada Curta de Latão Colonial, Adaga de Bota Oculta
*   **Armaduras:**  Túnica de Couro Costurado, Casaco com Mapas Bordados
*   **Item Utilitário:**  Bússola de Madeira Marítima
**Mosqueteiro (Colonizador)**  Esta classe representa o avanço da pólvora e da engenharia bélica, especialista em causar dano à distância com precisão mortal.
*   **Armas:**  Mosquete Enferrujado de Carga Lenta, Pistola de Pólvora Improvisada
*   **Armaduras:**  Colete Almofadado com Alça de Pólvora, Capa de Tiro Colonial
*   **Item Utilitário:**  Estojinho de Pólvora Decorado
**Missionário (Colonizador)**  Personificação da fé institucional, atua como curandeiro, conselheiro e defensor espiritual do grupo.
*   **Armas:**  Bastão de Fé de Madeira Escura, Cruz de Madeira Rústica
*   **Armaduras:**  Veste Clerical Reforçada, Manto de Pregação de Linho Grosso
*   **Item Utilitário:**  Livro Sagrado de Bolso
**Guerreiro Tribal (Indígena)**  Um defensor da terra e de seu povo, que traz a força do clã em cada golpe e o espírito ancestral em cada movimento.
*   **Armas:**  Lança de Madeira Quebradiça, Clava de Madeira Crua
*   **Armaduras:**  Peitoral de Couro Enrijecido, Faixa Tribal de Ombro
*   **Item Utilitário:**  Tatuagem de Guerra (tinta espiritual simples)
**Caçador de Feras (Indígena)**  Moldado pela floresta, ele lê pegadas, sente o vento e ouve os sons da mata como se fossem palavras. É paciente, mortal e raramente visto antes de atacar.
*   **Armas:**  Lança de Osso Lascada, Adaga de Pedra Serrilhada
*   **Armaduras:**  Couro Flexível de Caçador, Faixa de Peles Amarradas
*   **Item Utilitário:**  Cinto de Presas e Pegadas
**Arqueiro Selvagem (Indígena)**  O mestre do arco silencioso e do movimento entre as árvores, um caçador nato que domina a paisagem natural como cobertura.
*   **Armas:**  Arco de Madeira Rústico, Zarabatana com Dardos Simples
*   **Armaduras:**  Proteção de Ombro em Couro Cru, Colete de Pele Costurada
*   **Item Utilitário:**  Medalhão de Presas Animais
**Xamã Curandeiro (Indígena)**  Canalizando espíritos, ervas sagradas e a sabedoria dos rituais, ele restaura, purifica e harmoniza, servindo como elo entre os mundos.
*   **Armas:**  Cajado Rachado de Cipó, Talismã de Ossos Espirituais
*   **Armaduras:**  Manto Cerimonial de Palha, Túnica de Ervas Trançadas
*   **Item Utilitário:**  Colar de Sementes Rituais
**Guardião Ancestral (Ser Folclórico)**  Um pilar de proteção que canaliza o poder dos ancestrais para defender seu grupo, lutando por equilíbrio e preservação.
*   **Armas:**  Lança Rústica de Raiz Encantada, Clava de Casca Espiritual
*   **Armaduras:**  Couraça de Fibra Espiritual, Faixa de Cipós Trançados
*   **Item Utilitário:**  Totem de Casca Consagrada
**Lobo Lendário (Ser Folclórico)**  Representando a fusão entre espírito e fera, este ser veloz e instintivo ataca com agilidade sobrenatural e desaparece entre os sussurros da floresta.
*   **Arma:**  Garras de Ossos Ancestrais
*   **Armaduras:**  Manto de Peles Totêmicas, Tecido de Farpas Espirituais
*   **Item Utilitário:**  Pingente de Dente Encantado
**Ser Elemental (Ser Folclórico)**  A manifestação viva de um dos grandes elementos, um ser de magia pura que canaliza a fúria da natureza em feitiços destrutivos.
*   **Armas:**  Cajado de Madeira Petrificada, Orbe Encantada de Barro Rúnico
*   **Armaduras:**  Veste Trançada com Fio de Fogo Frio, Túnica de Bruma Enfeitiçada
*   **Item Utilitário:**  Cristal de Canalização Bruta
**Encantador de Espíritos (Ser Folclórico)**  Um intermediário entre os planos, cuja essência vibra entre o mundo físico e o espiritual, invocando aliados etéreos e interpretando sussurros invisíveis.
*   **Armas:**  Máscara Espiritual do Canto-Ancestral, Amuleto de Madeira Cantada
*   **Armaduras:**  Veste de Linho Marcado, Manto de Runas Costuradas
*   **Item Utilitário:**  Fio de Contato Espiritual
Além dos objetos que os jogadores carregam, os próprios mundos que eles exploram também precisam ser visualmente representados para criar uma experiência imersiva.

--------------------------------------------------------------------------------

##### 3. Ilustrações de Cenário (Blocos de Exploração)
As ilustrações de cenário são assets visuais de alta prioridade, pois funcionarão como os fundos de alta qualidade que aparecerão no "Modo de Cena" do jogo. A função principal destas peças é estabelecer a atmosfera de cada local visitado e servir como o principal componente visual durante os eventos narrativos. A arte deve ser detalhada, rica em atmosfera e profundamente imersiva, transportando o jogador para o coração do nosso mundo eco-fantástico, um lugar onde o tempo é poroso.
###### 3.1. Ambientes Naturais
*   **Floresta (diurna e noturna):**  Representação da natureza selvagem e mística do Brasil.
*   **Clareira com elementos sagrados:**  Um local de poder, como uma árvore antiga ou um círculo de pedras, onde a energia da Raiz do Mundo é palpável.
*   **Caverna escura:**  Com variações que contam histórias: cristais luminescentes, cursos d'água subterrâneos ou selada por magia antiga.
*   **Pântano denso e úmido:**  Com névoa e vegetação exótica, transmitindo uma sensação de perigo e mistério.
*   **Região montanhosa/pedregosa:**  Com trilhas íngremes e vistas amplas, evocando solidão e desafio.
*   **Costa/Porto marítimo:**  Com embarcações coloniais rústicas, um ponto de encontro e conflito de culturas.
*   **Lago esquecido:**  Com uma atmosfera melancólica e misteriosa, guardando segredos submersos.
###### 3.2. Ambientes Construídos
*   **Aldeia Indígena e Vila Colonizadora:**  Não apenas assentamentos, mas "núcleos vivendo em tensão velada". A arquitetura e a atmosfera devem refletir essa coexistência frágil.
*   **Ruínas de uma Aldeia Queimada:**  Um cenário de desolação e vestígios de conflito. A arte deve transmitir o trauma e a perda gravados na paisagem.
*   **Ruínas de um Templo de Pedra:**  Um local antigo, coberto pela vegetação, que sussurra histórias de eras passadas.
*   **Interior de uma Capela Colonial:**  Um espaço de fé e ordem, com altar, bancos e iconografia religiosa, que pode esconder segredos.
*   **Cripta subterrânea sob a capela:**  Um lugar de túmulos e segredos ocultos, onde o sagrado e o profano se encontram.
###### 3.3. Ambientes Místicos e Sobrenaturais
*   **Sítio Místico:**  Um local com energia visível, como um círculo de pedras rúnicas ou uma fonte de luz espiritual, onde a barreira entre os mundos é fina.
*   **Dungeon Espiritual:**  O ponto máximo da ruptura temporal. Este cenário deve fundir visualmente elementos de diferentes eras para representar uma "fissura no tempo". A arte precisa mostrar essa fusão surreal, como uma arquitetura colonial entrelaçada com cipós ancestrais e anomalias temporais visíveis.
