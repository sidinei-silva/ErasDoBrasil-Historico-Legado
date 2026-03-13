### Relatório de Simulação de Combate: Conquistador (Tier 1) vs. Espírito Corrompido
#### 1. Introdução e Objetivos da Simulação
Este documento apresenta um relatório de balanceamento para o sistema de jogo  *Eras do Brasil* , focando na performance de um combatente em um cenário de confronto padrão. O objetivo desta simulação é avaliar o desempenho de um personagem Conquistador de Tier 1, equipado com seu conjunto inicial de armadura e arma, contra um inimigo arquetípico, o "Espírito Corrompido". A análise se concentrará em três eixos estratégicos cruciais para a experiência do jogador: a duração média do combate, o risco real de morte para o personagem e a utilidade tática das habilidades-chave da classe em um cenário de confronto direto (1 vs. 1). A seguir, apresentamos a configuração detalhada dos combatentes para estabelecer a base desta análise.
#### 2. Configuração dos Combatentes
Para garantir a integridade e a replicabilidade deste teste, é fundamental estabelecer uma base de dados clara e precisa para a simulação. Esta seção detalha todas as estatísticas, equipamentos e habilidades relevantes para cada participante, extraídos diretamente das regras oficiais do jogo, conforme documentado nos capítulos de Criação de Personagem e Sistema de Combate, bem como nas fichas de classe específicas.
##### 2.1. Combatente 1: Conquistador (Tier 1)
O Conquistador foi configurado com uma distribuição de atributos otimizada para sua função de  *main tank* , priorizando a  *sobrevivência efetiva (eHP)*  por meio do Vigor e a  *geração de ameaça (threat)*  por meio da Força Bruta e habilidades de controle.
| Atributo | Valor / Descrição | Fonte da Regra |
| ------ | ------ | ------ |
| **Pontos de Vida (PV)** | 18 | (14 base + 2 * Mod Vigor) |
| **Defesa** | 13 | (10 + 0 Mod Astúcia + 2 Armadura + 1 Passiva) |
| **Bônus de Ataque** | +1 | (Mod Força Bruta) |
| **Dano** | 1d6+1 | (Espada de Ferro + Mod Força Bruta) |
| **Redução de Dano** | 1 (físico corpo a corpo) | (Propriedade da Couraça) |
| **Iniciativa** | +0 | (Mod Astúcia) |
| **Arma Inicial** | Espada de Ferro Mal Forjada (Dano: 1d6, Qualidade: Muito Baixa) | Ficha da Classe |
| **Armadura Inicial** | Couraça de Couro com Reforço de Ferro (Defesa: +2, Pesada, Qualidade: Muito Baixa) | Ficha da Classe |
| **Habilidade Ativa** | **Provocação Tática:**  Força alvos a 2m a atacá-lo (CD 12 Sabedoria). Recarga: 3 turnos. | (CD 13 base - 1 Qualidade do Item) |
| **Habilidade Passiva** | **Postura Inabalável:**  Com armadura pesada, +1 de Defesa e imunidade a empurrões. | Ficha da Classe |

##### 2.2. Combatente 2: Espírito Corrompido
O Espírito Corrompido representa um adversário padrão que os jogadores encontrarão nas primeiras fases do jogo. Seus atributos são projetados para oferecer um desafio equilibrado, mas perigoso, para um personagem de Tier 1.
| Atributo | Valor / Descrição | Fonte da Regra |
| ------ | ------ | ------ |
| **Pontos de Vida (PV)** | 15 | Diretiva |
| **Defesa** | 12 | Diretiva |
| **Bônus de Ataque** | +3 | Diretiva |
| **Dano** | 1d6+1 | Diretiva |
| **Iniciativa** | +1 | (Mod Astúcia assumido) |

Com os perfis de combate estabelecidos, a simulação passo a passo do confronto pode ser iniciada.
#### 3. Simulação de Combate: Execução Passo a Passo
Esta seção narra três rodadas completas de combate, detalhando cada ação, rolagem de dados virtual e consequência em ordem de iniciativa. O objetivo é demonstrar o fluxo de uma batalha real dentro do sistema  *Eras do Brasil* , testando a interação entre as mecânicas de ataque, defesa, dano e habilidades especiais.
##### 3.1. Início do Combate: Rolagem de Iniciativa
Para determinar a ordem de ação, ambos os combatentes realizam um teste de Iniciativa (1d20 + modificador de Astúcia).
*   **Conquistador:**  Rolagem de 1d20+0 resulta em  **9** .
*   **Espírito Corrompido:**  Rolagem de 1d20+1 resulta em  **16** .
**Ordem Final:**  O Espírito Corrompido agirá primeiro em cada rodada, seguido pelo Conquistador.
##### 3.2. Rodada 1
**Turno do Espírito Corrompido:**  O Espírito avança e ataca o Conquistador com suas garras etéreas.
*   **Rolagem de Ataque:**  1d20+3 =  **15** .
*   **Resultado:**  Um  **acerto** , superando a Defesa 13 do Conquistador.
*   **Rolagem de Dano:**  1d6+1 =  **5** .
*   **Dano Final:**  A Redução de Dano da armadura do Conquistador (-1) absorve parte do impacto. O dano final é de  **4 pontos** .
*   **Status:**  Conquistador:  **14/18 PV** .
**Turno do Conquistador:**   **Ação:**  Para testar a principal ferramenta de controle de ameaça da classe, o Conquistador utiliza sua habilidade  **Provocação Tática** . Ele bate com a espada em sua couraça de ferro, o som metálico e o grito desafiador forçando o foco do Espírito.
*   **Teste de Resistência (Espírito):**  O Espírito deve passar em um teste de Sabedoria com  **CD 12** . A rolagem é 1d20 =  **8** .
*   **Resultado:**  O Espírito  **falha**  no teste e agora está sob o efeito da provocação, sendo obrigado a atacar o Conquistador em seu próximo turno. (Assumindo uma duração de 1 rodada para o efeito, conforme o padrão para habilidades de controle de Tier 1).
##### 3.3. Rodada 2
**Turno do Espírito Corrompido:**  Sob o efeito da provocação, a entidade é compelida a atacar o Conquistador novamente, ignorando outras possíveis ações táticas.
*   **Rolagem de Ataque:**  1d20+3 =  **7** .
*   **Resultado:**  O ataque  **erra** , falhando em alcançar a Defesa 13 do Conquistador.
**Turno do Conquistador:**  Com o inimigo focado, o Conquistador aproveita a oportunidade para contra-atacar com sua Espada de Ferro.
*   **Rolagem de Ataque:**  1d20+1 =  **19** .
*   **Resultado:**  Um  **acerto**  claro contra a Defesa 12 do Espírito.
*   **Rolagem de Dano:**  1d6+1 =  **6** .
*   **Status:**  Espírito Corrompido:  **9/15 PV** .
##### 3.4. Rodada 3
**Turno do Espírito Corrompido:**  Livre do efeito da provocação, o Espírito investe com fúria renovada. Ignorando a postura defensiva do Conquistador, o Espírito desfere um golpe com força sobrenatural.
*   **Rolagem de Ataque:**  1d20+3 =  **20 natural** .
*   **Resultado:**  Um  **Acerto Crítico** . Conforme as regras, o ataque acerta automaticamente e o dano é maximizado.
*   **Dano Crítico:**  O dado de dano (1d6) é maximizado para 6, somado ao bônus de +1, totalizando 7 de dano bruto.
*   **Dano Final:**  Após a Redução de Dano da armadura (-1), o dano final é de  **6 pontos** .
*   **Status:**  Conquistador:  **8/18 PV** . O personagem está com menos da metade de sua vida total.
**Turno do Conquistador:**  Abalado pelo golpe poderoso, o Conquistador tenta pressionar o ataque.
*   **Rolagem de Ataque:**  1d20+1 =  **11** .
*   **Resultado:**  O ataque  **erra por pouco** , não conseguindo superar a Defesa 12 do Espírito Corrompido.
Com o combate se estendendo e os recursos do Conquistador diminuindo, passamos à análise dos resultados observados.
#### 4. Análise e Conclusões Pós-Simulação
Com base na simulação detalhada, esta seção apresenta uma análise técnica para responder às questões centrais de balanceamento propostas no início deste relatório: a duração do combate, o risco para o jogador e a utilidade das habilidades da classe.
##### 4.1. Quantos turnos a luta duraria em média?
Considerando a troca de dano observada e as probabilidades de acerto, podemos extrapolar a duração média do confronto. O Conquistador possui 50% de chance de acertar (precisa de 11+ no d20), causando em média 4.5 de dano por acerto, o que resulta em um dano por rodada (DPR) de aproximadamente 2.25. O Espírito Corrompido tem 55% de chance de acertar (precisa de 10+ no d20), causando em média 3.5 de dano efetivo (após redução), resultando em um DPR de 1.92. Com base nesses valores, o Conquistador levaria cerca de 7 rodadas para derrotar o Espírito (15 PV / 2.25 DPR), enquanto o Espírito levaria aproximadamente 9 rodadas para vencer o Conquistador (18 PV / 1.92 DPR). Portanto, a luta duraria, em média, entre  **5 e 7 rodadas** , configurando um confronto equilibrado e com um desgaste significativo de recursos. Embora a análise de DPR favoreça o Conquistador, a simulação demonstrou que a alta variabilidade do dano do Espírito — especificamente via acertos críticos — pode subverter a média estatística, colocando o jogador em risco significativo e imediato, o que é desejável para um encontro "padrão".
##### 4.2. O Conquistador corre risco real de morte ou é fácil demais?
O Conquistador corre um  **risco real e significativo** . O acerto crítico sofrido na Rodada 3 é a prova mais clara de como a sorte pode virar o combate rapidamente, reduzindo os PV do personagem para menos da metade em um único golpe. Fatores como a habilidade passiva "Postura Inabalável" (+1 Defesa) e a redução de dano da Couraça Pesada são cruciais para sua sobrevivência. Sem esses bônus, sua Defesa seria 12 e ele sofreria mais dano por acerto, tornando a luta exponencialmente mais difícil. A simulação demonstra que, embora resiliente, o Conquistador não é invulnerável e precisa gerenciar bem suas ações para sobreviver. O nível de desafio está bem balanceado para um encontro solo de Tier 1.
##### 4.3. A habilidade "Provocação Tática" foi útil na simulação?
Em um combate 1 vs. 1, a utilidade primária de "Provocação Tática" — proteger aliados — é nula. No entanto, a habilidade demonstrou um valor tático secundário: o controle de ações do inimigo. Ao forçar o Espírito Corrompido a atacá-lo na Rodada 2, a habilidade impediu que ele utilizasse uma ação potencialmente mais perigosa (como uma habilidade especial, caso tivesse uma). Na simulação, a provocação resultou em um ataque forçado que errou, negando efetivamente o dano do inimigo naquela rodada. A simulação confirma que a habilidade funciona como projetado, mas também expõe a importância do sistema de Qualidade de Item. Com um equipamento de qualidade 'Excelente', a CD aumentaria para 15 (+2 bônus), tornando a habilidade significativamente mais confiável e reforçando o valor do crafting e do loot para a progressão da classe.
Com a análise concluída, as recomendações finais podem ser formuladas.
#### 5. Recomendações Finais
Com base nos resultados desta simulação, o Conquistador de Tier 1 demonstra estar bem calibrado para sua função de "tank", apresentando uma combinação robusta de defesa, resiliência e controle tático inicial. O confronto simulado foi desafiador, com risco real, mas justo, validando o balanceamento atual da classe para encontros solo.
**Recomenda-se que nenhum ajuste mecânico seja realizado neste momento.**  No entanto, sugerimos o monitoramento prioritário da classe nos seguintes cenários:
1.  **Combates contra múltiplos inimigos:**  Para avaliar a eficácia da "Provocação Tática" em sua função primária de controle de grupo.
2.  **Confrontos contra inimigos que utilizam dano mágico:**  Dado que um único acerto crítico na Rodada 3 reduziu o Conquistador a menos de 50% de seus PV, o monitoramento contra inimigos com dano mágico (que ignora a principal fonte de mitigação do Conquistador, sua RD de armadura) torna-se uma prioridade de teste para garantir que a classe não seja excessivamente vulnerável a esse tipo de dano.
A análise contínua nesses cenários garantirá que o Conquistador permaneça uma classe equilibrada e funcional em todas as etapas do jogo.
