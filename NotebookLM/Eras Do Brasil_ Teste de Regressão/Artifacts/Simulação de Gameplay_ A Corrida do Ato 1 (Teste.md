### Simulação de Gameplay: A Corrida do Ato 1 (Teste de Estresse)
#### 1.0 Introdução à Simulação
Este relatório documenta um teste de estresse simulado, projetado para validar a reatividade do sistema  **Mundo Vivo**  sob condições de progressão lenta do jogador. O cenário acompanha um  **Guerreiro Tribal de Nível 1**  durante a missão  **"A Primeira Ruptura"** . O objetivo é avaliar como as mecânicas centrais reagem a um estilo de jogo investigativo, onde a exploração e o diálogo são priorizados sobre a velocidade. As mecânicas observadas foram: o  **Relógio da Ruptura** , um contador global de 500 Ticks que dita o estado do mundo; as fases de colapso ambiental, que se intensificam à medida que a  **Raiz do Mundo**  se torna instável; e a "corrida" contra o grupo rival de NPCs, os  **Bandeirantes de Sangue** . A simulação a seguir demonstra como essas mecânicas interagem dinamicamente para criar consequências narrativas e de gameplay significativas, moldadas diretamente pelo atraso do jogador.

--------------------------------------------------------------------------------

#### 2.0 Sessão 1: A Investigação - Sussurros na Floresta
##### 2.1 Início da Jornada e Primeiros Sinais (Ticks 0-50)
A simulação inicia com o  **Guerreiro Tribal**  chegando à região da floresta. Os primeiros sinais da  **Fase 1**  do  **Relógio da Ruptura**  já são evidentes: o céu exibe uma coloração roxa-espiritual, um sintoma visual de que a  **Raiz do Mundo**  está se tornando instável na região, e os animais demonstram um comportamento agitado, fugindo de uma ameaça invisível. Fiel ao seu perfil investigativo, o jogador opta por não seguir os rastros imediatamente. Em vez disso, ele dedica tempo para interagir com os aldeões locais. Cada conversa consome Ticks, mas revela fragmentos de informação da base de conhecimento dos NPCs. Pistas vagas, como  *"O gado não vai para o Norte"* , começam a formar um mosaico de possibilidades, mas sem apontar uma direção clara. Esta fase inicial de investigação consome um total de  **50 Ticks** .
##### 2.2 O Avanço do Rival e a Busca pelo Pajé (Ticks 51-120)
Com 50 Ticks já consumidos pelo jogador, o sistema registra que os  **Bandeirantes de Sangue**  completaram a primeira etapa de sua jornada, ganhando uma vantagem inicial. O jogador, agora ciente de que precisa de um guia, inicia a busca pelo  **Velho Pajé** , o único NPC que conhece o caminho exato para a anomalia. A simulação testa a rotina de IA do Pajé: o jogador o procura na praça da vila, mas ele não está lá. Conforme sua agenda, durante a manhã ele se encontra meditando na cachoeira. O jogador é forçado a rastreá-lo, consumindo mais tempo. A eventual localização e a conversa com o Pajé consomem  **70 Ticks adicionais** .  *Esta sequência valida com sucesso a rotina de IA do NPC conforme especificado no documento*  *01_Ato_1*  *. O atraso do jogador é uma consequência direta e orgânica de um mundo que opera em seu próprio cronograma, não um evento roteirizado.*
Ao final desta fase, o resumo do progresso é o seguinte:
*   **Total de Ticks do Jogador:**  120
*   **Progresso do Rival:**  2 etapas concluídas. Posição estimada: Significativamente à frente.
*   **Estado do Mundo:**   **Fase 1** , aproximando-se do ponto de virada para a instabilidade.
Com a localização da Ruptura finalmente descoberta, o jogador avança para a próxima fase da jornada, sem saber que o tempo já se tornou seu maior inimigo.

--------------------------------------------------------------------------------

#### 3.0 Sessão 2: A Fronteira dos Mundos - A Escolha em Meio ao Caos
##### 3.1 A Transição para a Instabilidade (Ticks 121-210)
O jogador inicia a viagem em direção à área das facções. A jornada consome Ticks preciosos. No meio do caminho, um momento crucial é acionado: o  **Relógio da Ruptura**  ultrapassa o  **Tick 201** . Imediatamente, o mundo mergulha na  **Fase 2: Instabilidade** . O impacto é sistêmico e imediato. O jogador testemunha magias falhando com maior frequência (CD +2), NPCs antes pacíficos agora agem de forma errática, e o cenário se torna visivelmente mais sombrio. Ao chegar à fronteira, a consequência mais grave do atraso se revela: as três facções —  **Indígenas** ,  **Colonizadores**  e  **Folclóricos**  — que antes poderiam ser negociadas, agora estão em guerra aberta. O mapa se transformou em uma zona de combate, e a oportunidade de uma resolução pacífica foi permanentemente perdida.
##### 3.2 Navegando pela Zona de Guerra (Ticks 211-280)
Para obter a  **Chave Espiritual** , item necessário para adentrar o epicentro da Ruptura, o jogador é forçado a fazer uma escolha tática em meio ao conflito. Sendo um  **Guerreiro Tribal** , a aliança natural é com a facção  **Indígena** . Ele se junta à batalha, utilizando sua habilidade  **Investida Tribal**  para romper a linha de frente inimiga. O confronto, a coordenação com os aliados e a obtenção da chave consomem um número significativo de Ticks.
Ao final desta sessão, o status da simulação é atualizado:
*   **Total de Ticks do Jogador:**  280
*   **Progresso do Rival:**  5 etapas concluídas. Posição estimada:  **Zona de Distorção** .
*   **Estado do Mundo:**  Firmemente na  **Fase 2** . O ambiente é hostil e a magia é instável.
Com a chave em mãos, o jogador agora enfrenta uma corrida desesperada pela  **Zona de Distorção** , um lugar que, assim como o resto do mundo, foi irrevogavelmente alterado pelo tempo.

--------------------------------------------------------------------------------

#### 4.0 Sessão 3: A Corrida Final - O Colapso Iminente
##### 4.1 Atravessando a Zona de Distorção (Ticks 281-410)
Esta fase da jornada, um dungeon natural que leva ao epicentro da Ruptura, é onde o atraso do jogador se manifesta de forma mais punitiva. A  **Fase 2**  do Relógio alterou drasticamente o terreno: caminhos que antes eram seguros agora são abismos, forçando o jogador a encontrar rotas alternativas. É neste ambiente que os  **Bandeirantes de Sangue**  prepararam uma emboscada. Sem as habilidades de detecção de um  **Explorador de Terras**  ou  **Arqueiro Selvagem** , o  **Guerreiro Tribal**  é pego de surpresa.  *A falha em detectar a emboscada destaca o papel crítico das habilidades de classe, demonstrando uma implementação bem-sucedida de contramedidas estratégicas baseadas em classe na fase de exploração. Conforme o design da classe*  *Guerreiro Tribal*  *, seus atributos recomendados são*  ***Vigor***  *e*  ***Força Bruta***  *. A ausência de*  ***Astúcia***  *ou*  ***Sabedoria Ancestral***  *elevadas o torna mecanicamente vulnerável a armadilhas que exigem percepção, validando a interdependência entre a build do personagem e os desafios ambientais. A eficácia da emboscada sugere que a composição do grupo rival 'Bandeirantes de Sangue' inclui um NPC com a classe*  ***Explorador de Terras***  *ou*  ***Arqueiro Selvagem***  *, cujo kit de habilidades é projetado para tal tática.*  O combate subsequente é custoso em tempo. Durante a luta, o Relógio ultrapassa o  **Tick 401** , e o mundo entra na  **Fase 3: O Colapso** .
##### 4.2 Sobrevivendo ao Colapso (Ticks 411-490)
A transição para a  **Fase 3**  transforma a jornada em um pesadelo. Portais dimensionais começam a se abrir aleatoriamente, forçando combates contra monstros. Pior ainda, o  **Dano Espiritual**  ambiente começa a surtir efeito: em áreas abertas, o personagem sofre 1 de dano por turno, um dreno constante que esgota seus recursos e um sinal de que a própria  **Raiz do Mundo**  está se desfazendo e expondo a realidade a energias brutas. A narrativa transmite desespero, com o  **Guerreiro Tribal**  lutando não apenas contra inimigos, mas contra a própria desintegração da realidade.
O status final antes do clímax reflete a situação crítica:
*   **Total de Ticks do Jogador:**  490
*   **Progresso do Rival:**  9 etapas concluídas. Posição estimada: Câmara do chefe final.
*   **Estado do Mundo:**  Em pleno colapso da  **Fase 3** , a um passo da catástrofe total.
Exausto e atrasado, o jogador finalmente chega à câmara do chefe, apenas para encontrar um cenário que ele não poderia prever.

--------------------------------------------------------------------------------

#### 5.0 Sessão 4: O Clímax - A Primeira Ruptura
##### 5.1 O Cenário no Epicentro (Tick 490)
Ao entrar na câmara, o  **Guerreiro Tribal**  se depara com uma cena caótica. Os  **Bandeirantes de Sangue**  já estão no local, travando uma batalha feroz contra o  **Guardião da Fenda** . A rivalidade se desfaz diante da ameaça iminente; um pacto silencioso é formado pela sobrevivência. Sem hesitar, o jogador entra na luta, que já está em andamento.
##### 5.2 O Mundo Quebrado (Pós-Tick 500)
A aliança chega tarde demais. O relógio atinge o  **Tick 500** . A Ruptura explode. O objetivo da missão muda de "Prevenir" para "Sobreviver e Conter". O impacto no combate é devastador: o  **Guardião da Fenda**  absorve a energia e ascende, transformando-se no  **Guardião da Fenda Ascendido** . Conforme a regra de dificuldade dinâmica, o chefe agora possui ataques em área e seu dano é massivamente ampliado. A luta se torna uma batalha desesperada.
##### 5.3 O Confronto Final
Os momentos finais são uma demonstração de resiliência. O  **Guerreiro Tribal**  e os  **Bandeirantes de Sangue** , agora aliados, lutam juntos contra o chefe fortalecido. Quando a vida do jogador cai abaixo de 50%, sua habilidade passiva  **Espírito do Clã**  é ativada, concedendo-lhe +1 em ataques corpo a corpo. A luta é longa e custosa, drenando todos os recursos. No final, eles alcançam uma vitória de Pirro, derrotando o guardião, mas falhando em sua missão principal. O mundo ao redor foi permanentemente alterado.

--------------------------------------------------------------------------------

#### 6.0 Conclusão e Análise do Teste de Estresse
##### 6.1 Avaliação dos Resultados
A simulação de um jogador lento resultou em um desfecho coerente com as regras do sistema de  **Mundo Vivo** .
*   **Missão Principal:**   **Fracasso** . O jogador não conseguiu impedir a ruptura antes do limite de 500 Ticks.
*   **Vencedor da Corrida:**   **Os Bandeirantes de Sangue** . O grupo rival de NPCs chegou primeiro a todos os objetivos principais.
*   **Estado Final do Mundo:**  A floresta se transformou no  **Bosque das Sombras** , uma zona de alto nível, e a vila inicial foi evacuada. O jogador recebe o título de  **Sobrevivente** .
##### 6.2 Análise do Sistema de Mundo Vivo
A simulação valida inequivocamente que as escolhas do jogador geram consequências sistêmicas. A abordagem investigativa não foi meramente uma escolha de ritmo, mas uma variável de entrada que alterou diretamente o estado do mundo, os objetivos da missão e os resultados narrativos, provando a robustez do motor de  **Mundo Vivo** .
A sinergia entre o avanço do Rival e as mudanças de fase do  **Relógio da Ruptura**  funcionou conforme o planejado, criando uma experiência dinâmica que é simultaneamente punitiva e coerente. A simulação provou que o mundo não espera pelo herói; ele avança e se transforma independentemente das ações do jogador, forçando-o a se adaptar ou arcar com as consequências. O teste de estresse foi, portanto, bem-sucedido em provar a reatividade e as consequências geradas pelo sistema de tempo global.
