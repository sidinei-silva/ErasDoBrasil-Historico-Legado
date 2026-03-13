### Análise de Balanceamento de Combate: O Encontro com a Onça-Pintada Espiritual
##### 1. Introdução e Metodologia da Análise
Este documento constitui um relatório de design de balanceamento para o jogo  *Eras do Brasil* , focado na experiência de combate fundamental. O objetivo desta análise é simular um encontro de combate padrão em dois cenários distintos — um jogador solo e uma dupla de jogadores — para avaliar a escalabilidade da dificuldade. A metodologia busca garantir que a experiência cooperativa, um dos pilares do design do jogo, permaneça desafiadora e taticamente interessante, evitando que a adição de um segundo jogador torne os encontros triviais. Para assegurar a consistência e a replicabilidade dos resultados, apresentamos a seguir os parâmetros detalhados utilizados em ambas as simulações.
##### 2. Parâmetros da Simulação de Combate
A definição de parâmetros claros é crucial para uma simulação de balanceamento consistente e replicável. Esta seção detalhará as fichas de combate dos personagens jogadores (Tier 1) e do inimigo prototipado, bem como as regras de combate fundamentais que foram aplicadas. Todas as informações e mecânicas são baseadas nos documentos oficiais de regras do  *Eras do Brasil* , garantindo que a análise reflita com fidelidade o sistema de jogo proposto.
###### 2.1. Fichas dos Personagens Jogadores (Tier 1)
As fichas a seguir foram construídas com base nas classes de Tier 1, assumindo uma distribuição de atributos focada nas recomendações de cada arquétipo para otimizar o desempenho em combate.
###### Guerreiro Tribal
| Parâmetro | Guerreiro Tribal (Tier 1) |
| ------ | ------ |
| **Pontos de Vida (PV)** | 18 |
| **Defesa** | 11 |
| **Atributo de Ataque** | Força Bruta (+2) |
| **Rolagem de Ataque** | 1D20 + 2 |
| **Arma** | Lança de Madeira Quebradiça (1D6 Dano de Perfuração) |
| **Armadura** | Peitoral de Couro Enrijecido (Reduz em 1 o dano de ataques corpo a corpo) |
| **Habilidade Ativa** | Investida Tribal: Avança até 3 metros e realiza um ataque corpo a corpo com vantagem (Recarga: 2 turnos) |
| **Habilidade Passiva** | Espírito do Clã: +1 em ataques corpo a corpo se PV < 50% |

###### Arqueiro Selvagem
| Parâmetro | Arqueiro Selvagem (Tier 1) |
| ------ | ------ |
| **Pontos de Vida (PV)** | 14 |
| **Defesa** | 13 |
| **Atributo de Ataque** | Astúcia (+2) |
| **Rolagem de Ataque** | 1D20 + 2 |
| **Arma** | Arco de Madeira Rústico (1D6 Dano de Perfuração) |
| **Armadura** | Proteção de Ombro em Couro Cru (+1 de Defesa) |
| **Habilidade Ativa** | Tiro Furtivo: +2 de dano se o alvo não agiu no combate (Recarga: 1 turno) |
| **Habilidade Passiva** | Passos Silenciosos: Ignora penalidades de terreno difícil e recebe +2 em testes de Furtividade em ambientes naturais |

###### 2.2. Ficha do Inimigo (Protótipo)
**Nota:**  Como o bestiário oficial está em desenvolvimento, esta ficha foi prototipada seguindo as diretrizes de um "Inimigo Médio" de Tier 1, para servir como base para esta análise de balanceamento.
| Parâmetro | Onça-Pintada Espiritual |
| ------ | ------ |
| **Classificação** | Inimigo Médio (Tier 1) |
| **Pontos de Vida (PV)** | 25 |
| **Defesa** | 12 |
| **Ações** | 1 por turno |
| **Ataque Principal** | Garras Espectrais (1D20 + 3 vs. Defesa) |
| **Dano** | 1D6 + 2 de Dano Espiritual |
| **Habilidade Especial** | Bote Espiritual: Ataque com 1D8+2 de dano. Atingido deve passar em teste de Vigor (CD 12) ou fica  **Derrubado** . (Recarga: 2 turnos) |

###### 2.3. Regras de Combate Aplicadas
As simulações a seguir aderiram estritamente às regras de combate descritas no "Capítulo 4 – Sistema de Combate", com os seguintes pontos sendo fundamentais para a análise:
*   **Iniciativa:**  Calculada com 1D20 + Modificador de Astúcia para determinar a ordem de ação.
*   **Estrutura de Turno:**  Cada participante realiza uma  **Ação Principal**  em seu turno.
*   **Resolução de Ataque:**  Um ataque acerta se a rolagem de 1D20 + Modificador de Ataque igualar ou superar a Defesa do alvo.
*   **Acerto Crítico:**  Um 20 natural no dado resulta em um acerto automático com o dano máximo da arma/habilidade.
*   **Falha Crítica:**  Um 1 natural no dado resulta em uma falha automática, e o atacante fica  **Vulnerável**  (o próximo ataque contra ele recebe +2 de bônus) até seu próximo turno.
*   **Condição**  **Derrubado**  **:**  Concede vantagem para ataques corpo a corpo contra o alvo. Levantar-se consome a Ação Principal do personagem.
Com estes parâmetros estabelecidos, a análise prossegue para o primeiro cenário de combate simulado.
##### 3. Simulação e Análise: Cenário A (Lobo Solitário)
Este cenário estabelece a linha de base de dificuldade para um jogador solo, opondo um Guerreiro Tribal a uma Onça-Pintada Espiritual. O objetivo é avaliar a capacidade de sobrevivência do jogador e o dano médio por rodada (DPR) contra um inimigo padrão de seu nível, determinando se o encontro é desafiador, mas superável.
A simulação a seguir descreve um fluxo de combate provável, baseado em médias estatísticas de dano e acerto.
**Simulação: 1 Guerreiro Tribal vs. 1 Onça-Pintada Espiritual**
*   **Turno 1:**  O Guerreiro inicia o combate com sua Investida Tribal, garantindo vantagem no ataque e uma alta probabilidade de acerto. Ele causa dano médio (aprox. 4 pontos). Em resposta, a Onça ataca com suas Garras Espectrais. Com um bônus de +3 contra a Defesa 11 do Guerreiro, a chance de acerto é alta (65%). Supondo um acerto, ela causa dano médio (aprox. 6 pontos), reduzido para 5 pela armadura do Guerreiro.
*   **Turno 2:**  O Guerreiro ataca novamente, desta vez sem vantagem, tendo uma chance moderada de acertar a Defesa 12 da Onça. Supondo um acerto, ele causa mais 4 pontos de dano. A Onça, por sua vez, utiliza seu Bote Espiritual. O ataque, mais forte, acerta e causa dano elevado (aprox. 7 pontos). Este é o momento decisivo do combate: o Guerreiro deve passar em um teste de Vigor (CD 12).
    *   **Análise do Teste:**  Assumindo que o Guerreiro seguiu as recomendações e possui Vigor 5 (modificador +2), ele precisa rolar um 10 ou mais no D20. Isso representa uma chance de sucesso de 55%. O resultado deste teste, essencialmente um "lançar de moeda", define o rumo da luta.
*   **Turno 3 (Se o Guerreiro falhar no teste):**  Estando Derrubado, ele é forçado a usar sua Ação Principal para se levantar. Seus PV estão abaixo de 50%, ativando sua passiva Espírito do Clã (+1 no ataque), mas ele não pode atacar neste turno. A Onça ataca novamente, agora com vantagem, resultando em um acerto quase garantido que provavelmente derrotará o Guerreiro.
*   **Turno 3 (Se o Guerreiro passar no teste):**  Ele permanece de pé e pode atacar. Com Espírito do Clã ativo, ele causa dano aumentado (aprox. 5 pontos). A luta continua, mas o Guerreiro está com PVs críticos e a Onça ainda representa uma ameaça letal.
**Conclusão do Cenário A:**  O encontro solo é  **altamente desafiador e perigoso** . A vitória do Guerreiro depende criticamente do sucesso no teste de resistência contra o Bote Espiritual. A simulação indica que uma derrota é um resultado muito provável, ocorrendo em aproximadamente  **4 a 5 turnos** . Isso estabelece uma linha de base de alta dificuldade, onde a sobrevivência exige gestão tática das habilidades e um momento crucial de sorte.
##### 4. Simulação e Análise: Cenário B (A Dupla)
Este cenário testa o impacto da adição de um segundo jogador (um Arqueiro Selvagem), focando em como a "economia de ações" — duas ações de jogadores contra uma do inimigo — altera o ritmo e a dificuldade do combate. O objetivo é verificar se o desafio se mantém ou se torna excessivamente fácil para a dupla.
**Simulação: 1 Guerreiro Tribal + 1 Arqueiro Selvagem vs. 1 Onça-Pintada Espiritual**
*   **Turno 1:**  O Arqueiro, com sua Astúcia elevada, provavelmente age primeiro. Ele utiliza seu Tiro Furtivo, causando dano aumentado (aprox. 6 pontos), pois a Onça ainda não agiu. Em seguida, o Guerreiro usa sua Investida Tribal para um ataque com vantagem (aprox. 4 pontos de dano). A Onça já sofreu cerca de 40% de seu total de vida antes mesmo de seu primeiro turno. Ela responde atacando o Guerreiro, a ameaça mais próxima, causando dano padrão (aprox. 5 pontos, após redução).
*   **Turno 2:**  O Arqueiro dispara novamente (dano normal, aprox. 4 pontos). O Guerreiro também ataca (aprox. 4 pontos). O dano combinado da dupla por rodada é substancialmente alto. A Onça, já ferida, usa seu Bote Espiritual, focando novamente no Guerreiro. Mesmo que o ataque acerte e o Guerreiro seja Derrubado, a ameaça da Onça é drasticamente reduzida.
*   **Turno 3:**  Com a Onça já com PVs críticos, o Arqueiro pode usar seu Tiro Furtivo novamente (sua recarga é de apenas 1 turno), finalizando o inimigo antes que ele tenha a chance de capitalizar sobre o Guerreiro Derrubado.
**Conclusão do Cenário B:**  A adição de um segundo jogador  **reduz drasticamente a dificuldade**  do encontro. A economia de ações favorável à dupla e o aumento massivo no dano por rodada neutralizam a ameaça da Onça de forma muito eficiente. A vitória é quase certa e ocorre em aproximadamente  **3 turnos** . O encontro, que era perigoso para um jogador, torna-se trivial para dois.
##### 5. Conclusões e Recomendações de Balanceamento
A análise comparativa dos cenários A e B confirma uma hipótese central do design de jogos cooperativos: a dificuldade não escala linearmente com o número de jogadores. O aumento da economia de ações e do potencial de dano do grupo supera em muito as capacidades de um inimigo projetado para um confronto solo, tornando a experiência cooperativa significativamente menos desafiadora. Para preservar a tensão tática em ambos os modos de jogo, são necessários ajustes dinâmicos.
###### 5.1. Comparativo de Duração e Dificuldade
| Cenário | Nº Estimado de Turnos | Análise da Dificuldade |
| ------ | ------ | ------ |
| **A (Solo)** | 4–5 Turnos (Derrota Provável) | **Alta.**  O encontro é perigoso e depende de um teste de resistência crucial para a sobrevivência. Funciona bem como um desafio solo de alto risco. |
| **B (Dupla)** | 3 Turnos (Vitória) | **Trivial.**  A superioridade em ações (2 vs. 1) e o alto dano por rodada do grupo neutralizam a ameaça rapidamente, removendo quase toda a tensão do combate. |

###### 5.2. Sugestão de Regra de "Ajuste Dinâmico"
Com base na conclusão de que o encontro se torna muito fácil para a dupla, é recomendável implementar uma regra simples de "Ajuste Dinâmico" que o Mestre (ou o sistema digital) possa aplicar automaticamente quando houver mais de um jogador enfrentando um inimigo "solo" projetado como desafio individual.
###### Recomendação: Aumentar os Pontos de Vida do Inimigo
*   **Regra Sugerida:**  Para cada jogador adicional no grupo após o primeiro, aumente os Pontos de Vida (PV) totais do inimigo "solo" em  **75%** .
    *   *Exemplo:*  A Onça-Pintada Espiritual, com 25 PV, passaria a ter  **44 PV**  (25 + 19) ao enfrentar uma dupla.
*   **Análise do Impacto:**  Esta é a solução mais simples e direta. Ela não aumenta a letalidade do inimigo (seu potencial de dano por turno permanece o mesmo), mas prolonga o combate, forçando a dupla a gerenciar seus recursos e recargas de habilidades por mais tempo. O encontro se torna mais uma prova de resistência e consistência tática do que uma corrida de dano, preservando o desafio sem alterar a complexidade mecânica fundamental do inimigo.
*   **Nota para o Mestre:**  Para um desafio ainda maior e mais complexo, uma alternativa seria adicionar um segundo inimigo mais fraco em vez de aumentar os PV do principal. Essa abordagem altera drasticamente a economia de ações (2 vs. 2), exigindo que os jogadores dividam o foco e tomem decisões táticas mais complexas sobre prioridade de alvos.
