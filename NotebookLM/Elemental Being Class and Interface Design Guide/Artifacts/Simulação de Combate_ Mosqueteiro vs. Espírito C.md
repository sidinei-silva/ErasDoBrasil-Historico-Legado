### Simulação de Combate: Mosqueteiro vs. Espírito Corrompido (Fase 1 Estático)
#### 1. Objetivo da Simulação
Este documento estabelece uma simulação de combate controlada para servir como teste de verificação da Fase 1 do sistema. O propósito é validar a sinergia entre a mecânica de combate estático e a funcionalidade de uma habilidade de classe central: o "Tiro Preparado" do Mosqueteiro. O objetivo principal é analisar se as regras de preparação e recarga, em conjunto com a interface de usuário (UI) baseada em texto, proporcionam uma experiência clara, tática e recompensadora para o jogador, conforme definido no Livro de Regras (04_Sistema_de_Combate.md) e nos documentos de UI (05_UI_Fase_1_Exploracao_e_Combate.md). Esta simulação também serve para validar empiricamente as conclusões do Relatório de Auditoria de Integração, que identificou a habilidade "Tiro Preparado" como um modelo de clareza mecânica para a digitalização.
#### 2. Configuração do Cenário
Para garantir a reprodutibilidade e a precisão desta análise, é fundamental definir claramente os perfis dos participantes do combate. A tabela a seguir detalha os atributos e habilidades do Mosqueteiro de Nível 1, extraídos diretamente da documentação de personagem, e os atributos de um Espírito Corrompido, um adversário plausível para este nível de desafio.
| Mosqueteiro (Nível 1) | Espírito Corrompido |
| ------ | ------ |
| **Origem:**  Colonizador | **Tipo:**  Entidade Mágica Hostil |
| **Atributos:**  Astúcia 4 (+1), Vigor 3 (+0) | **Atributos:**  Astúcia 3 (+0) |
| **PV:**  12 | **PV:**  15 |
| **Defesa Base:**  11 (10 + 1 de Astúcia) | **Defesa Base:**  10 (10 + 0 de Astúcia) |
| **Arma Equipada:**  Mosquete Enferrujado (Dano: 1D10) | **Ação Principal:**  Maldição Espiritual |
| **Habilidade Ativa:**  Tiro Preparado |  |
| **Habilidade Passiva:**  Mestre da Pólvora |  |

Com os combatentes devidamente configurados, a simulação pode ser iniciada para avaliar a dinâmica do confronto.
#### 3. Execução da Simulação - Rodada 1
A primeira rodada de combate é crucial para estabelecer a ordem de ação e iniciar as manobras táticas. Mesmo em um sistema de combate estático, a fase de iniciativa e as primeiras escolhas definem o ritmo do confronto e testam a clareza das ações do jogador e do inimigo.
##### 3.1. Fase de Iniciativa
A ordem de ação é determinada por um teste de Iniciativa, conforme as regras do Capítulo 4 do Livro de Regras. Cada combatente rola 1D20 e soma seu modificador de Astúcia.
*   **Simulação de Rolagem (Mosqueteiro):**  1D20 (resultado: 14) + 1 (Mod. Astúcia) =  **15**
*   **Simulação de Rolagem (Espírito Corrompido):**  1D20 (resultado: 8) + 0 (Mod. Astúcia) =  **8**
A ordem de turno final é:
1. Mosqueteiro
2. Espírito Corrompido
##### 3.2. Turno 1: Mosqueteiro
O Mosqueteiro age primeiro. Ele opta por utilizar sua Ação Principal para iniciar a habilidade  **"Tiro Preparado"** . Conforme a descrição da habilidade, esta ação consiste em mirar e preparar a arma, sacrificando a oportunidade de causar dano imediato em troca de um ataque mais poderoso no turno seguinte.
##### 3.3. Turno 2: Espírito Corrompido
O Espírito Corrompido utiliza sua Ação Principal para lançar uma  **"Maldição de Fraqueza"**  contra o Mosqueteiro, exigindo um teste de resistência de Vigor. O Mosqueteiro realiza o teste e obtém sucesso, resistindo ao efeito debilitante da maldição.
##### 3.4. Visualização na Interface (Fim da Rodada 1)
Ao final da rodada, o  **Log de Combate**  na interface do jogador apresentaria os eventos de forma clara e sequencial, conforme o modelo definido no documento de UI da Fase 1.
**--- Início da Rodada 1 ---**
*  Iniciativa: Mosqueteiro (15), Espírito Corrompido (8).
*   **Turno do Mosqueteiro:**  Você prepara seu mosquete, mirando cuidadosamente. (Ação: Tiro Preparado - 1/2)
*   **Turno do Espírito Corrompido:**  O Espírito Corrompido lança uma maldição! Você resiste ao efeito.  **--- Fim da Rodada 1 ---**
A primeira rodada termina com o Mosqueteiro em uma posição tática vantajosa, preparando o clímax de sua habilidade para a rodada seguinte.
#### 4. Execução da Simulação - Rodada 2
A segunda rodada é o ponto de validação da mecânica central em teste. Nela, o resultado da ação preparada pelo Mosqueteiro será demonstrado, testando o ciclo de recompensa da habilidade "Tiro Preparado".
##### 4.1. Turno 3: Mosqueteiro
Mantendo a ordem de iniciativa, o Mosqueteiro age primeiro e utiliza sua Ação Principal para concluir a habilidade  **"Tiro Preparado"** , disparando contra o Espírito Corrompido. Os seguintes bônus são aplicados:
*   **Bônus de Ataque:**  +2 na rolagem de ataque.
*   **Bônus de Dano:**  +3 no dano final.
**Teste de Ataque**
O Mosqueteiro rola 1D20 para o ataque e adiciona seus modificadores. O resultado é comparado com a Defesa Base (10) do Espírito Corrompido.
*   **Cálculo:**  1D20 (resultado: 20) + 1 (Mod. Astúcia) + 2 (Bônus de Habilidade) =  **23** .
*   **Resultado:**  O ataque  **acerta** . Uma rolagem natural de 20 no d20 resulta em um Acerto Crítico, conforme as regras de combate, o que maximiza o dano da arma.
**Cálculo de Dano**
Com o acerto confirmado, o dano é calculado. O dado da arma (1D10) é maximizado devido ao Acerto Crítico, e o bônus da habilidade é somado.
*   **Cálculo:**  10 (Dano máximo do Mosquete) + 3 (Bônus de Habilidade) =  **13 de dano** .
*   **Resultado:**  O Espírito Corrompido sofre 13 de dano, reduzindo seus PV de 15 para 2.
##### 4.2. Turno 4: Espírito Corrompido
Gravemente ferido, o Espírito Corrompido retalia com um ataque básico contra o Mosqueteiro, mas erra seu alvo.
##### 4.3. Visualização na Interface (Fim da Rodada 2)
O Log de Combate da Rodada 2 reflete o clímax da ação, comunicando claramente os bônus aplicados e o resultado devastador do ataque preparado.
**--- Início da Rodada 2 ---**
*   **Turno do Mosqueteiro:**  Você dispara o tiro preparado!
*   *Rolagem de Ataque: 20 (dado) + 1 (Astúcia) + 2 (Bônus de Habilidade) = 23. Acerto Crítico!*
*   *O Espírito Corrompido sofre 13 de dano! (10 do Mosquete + 3 de Bônus de Habilidade)*
*   **Turno do Espírito Corrompido:**  O Espírito ataca em retaliação, mas erra.  **--- Fim da Rodada 2 ---**
Adicionalmente, o jogador receberia feedback visual imediato: o número de dano "13" apareceria sobre o sprite do inimigo, e sua barra de vida diminuiria visivelmente, reforçando o impacto da ação.
#### 5. Análise e Conclusão
Esta seção final avalia os resultados da simulação para determinar se a mecânica do "Tiro Preparado" e a interface de combate da Fase 1 funcionaram de forma coesa e eficaz, cumprindo o objetivo inicial de proporcionar uma experiência tática e recompensadora.
##### 5.1. Verificação da Mecânica "Tiro Preparado"
A simulação confirma que a habilidade funciona conforme projetado. A mecânica de dois turnos cria um ciclo tático claro de  **risco vs. recompensa** . O jogador sacrifica a ação de um turno, tornando-se vulnerável, para garantir um ataque devastador no turno seguinte. No contexto do combate estático da Fase 1, onde o reposicionamento tático é abstrato, a decisão de sacrificar um turno para um ataque de alto impacto torna-se uma das escolhas estratégicas mais significativas do jogador, diferenciando o combate de uma simples troca de golpes. A performance da habilidade confirma as conclusões da auditoria de integração, validando-a como um pilar robusto para o kit do Mosqueteiro na Fase 1.
##### 5.2. Verificação da Interface de Texto
A interface textual, representada pelo Log de Combate, provou ser altamente eficaz. O log comunicou com sucesso todas as etapas da habilidade: a preparação no primeiro turno, o disparo no segundo e, crucialmente, a aplicação explícita dos bônus numéricos (+ 2 (Bônus de Habilidade)). Essa clareza matemática é essencial para que o jogador compreenda o valor de suas escolhas táticas e sinta a recompensa de ter planejado a jogada. A interface cumpre seu papel de traduzir as regras do sistema em um feedback compreensível e imediato.
##### 5.3. Veredito Final
A análise dos resultados da simulação leva a uma conclusão positiva e direta.
**Veredito: As regras da habilidade "Tiro Preparado" do Mosqueteiro e a UI de combate estático da Fase 1 estão bem integradas, proporcionando uma experiência de jogo funcional e taticamente clara.**
##### 5.4. Recomendações e Próximos Passos
**Recomendação:**  Dado o sucesso desta simulação, recomenda-se a criação de um cenário de teste semelhante para a habilidade "Investida Tribal" do Guerreiro Tribal, a fim de validar suas mecânicas de movimento abstrato e a aplicação de "vantagem" no combate estático.
**Ponto de Atenção:**  A simulação revelou que o valor do "Tiro Preparado" reside em sua capacidade de superar a defesa e causar dano significativo. Deve-se monitorar o design de inimigos da Fase 1 para garantir que os valores de PV e Defesa sejam calibrados para tornar a escolha de usar esta habilidade recompensadora, mas não trivial.
