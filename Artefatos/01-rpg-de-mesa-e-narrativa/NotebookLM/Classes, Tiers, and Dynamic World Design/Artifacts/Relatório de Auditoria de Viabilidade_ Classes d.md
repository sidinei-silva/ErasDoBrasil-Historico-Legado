### Relatório de Auditoria de Viabilidade: Classes de Suporte em Modo Solo (Ato 1)
##### 1.0 Introdução e Escopo da Análise
**1.1. Contexto Estratégico**
Este relatório apresenta uma auditoria de viabilidade focada nas classes de puro suporte — Xamã Curandeiro e Missionário — dentro do contexto da campanha do Ato 1 no modo Solo Offline ("Eco"). O objetivo central desta análise é identificar e avaliar potenciais riscos de  *softlock* , uma condição na qual um jogador pode ficar permanentemente preso devido à incapacidade de superar desafios de combate por falta de dano. A auditoria também avalia a eficácia dos sistemas de jogo existentes projetados para mitigar essa vulnerabilidade e, fundamentalmente, validar a robustez do nosso pilar de design de "Progressão Flexível".
**1.2. Metodologia**
A análise foi conduzida seguindo uma metodologia estruturada em quatro etapas principais:
*   **Análise de Capacidades de Combate:**  Uma avaliação detalhada das habilidades, atributos e equipamentos iniciais das classes de suporte para estabelecer uma linha de base de seu potencial de dano solo.
*   **Desconstrução dos Desafios da Campanha:**  Uma análise da "Corrida do Ato 1" e seus principais obstáculos (Relógio da Ruptura, combate forçado, chefe final) sob a perspectiva de um jogador com baixo potencial de dano.
*   **Avaliação dos Sistemas de Mitigação:**  Uma análise crítica dos sistemas de jogo projetados para auxiliar o jogador, como o sistema de Companheiros, a Herança de Habilidades e a sinergia com missões secundárias.
*   **Consolidação e Avaliação de Risco:**  A síntese dos achados para formular um diagnóstico claro sobre o risco de softlock e fornecer recomendações estratégicas para a equipe de desenvolvimento.
**1.3. Transição**
A seguir, apresentamos a análise detalhada das capacidades intrínsecas das classes de suporte em questão.
##### 2.0 Análise das Classes de Suporte Focadas
**2.1. Análise de Perfil de Jogo**
Para compreender a viabilidade de uma classe em um cenário solo, é fundamental analisar suas capacidades intrínsecas antes de considerar os sistemas de auxílio externos. Esta seção avalia o Xamã Curandeiro e o Missionário com base em seu design fundamental, focando em seu potencial de combate autônomo no início do jogo.
**2.2. Avaliação das Classes de Suporte**
| Eixo de Análise | Xamã Curandeiro | Missionário |
| ------ | ------ | ------ |
| **Estilo de Jogo Principal** | Suporte mágico e espiritual, com foco em cura, proteção e execução de rituais. Atua como um elo entre o mundo físico e o espiritual para harmonizar e restaurar. | Suporte mágico baseado em fé, com foco em cura, resistência espiritual e proteção contra forças malignas. Atua como um pilar moral e defensor espiritual do grupo. |
| **Habilidades Iniciais (Ativa e Passiva)** | **Ativa:**  Oferenda Curativa - Cura um aliado (1D6 + Sabedoria Ancestral). Não causa dano. <br>  **Passiva:**  Chamado dos Espíritos - Acelera rituais e concede vantagem contra maldições. Nenhuma contribuição para o dano. | **Ativa:**  Bênção da Salvação - Remove um efeito negativo ou concede +2 de Defesa contra ataques mágicos por 1 turno. Não causa dano. <br>  **Passiva:**  Fé Inabalável - Vantagem contra medo, influência espiritual negativa e corrupção. Nenhuma contribuição para o dano. |
| **Atributos Recomendados** | Sabedoria Ancestral e Conhecimento. Focados em potencializar magias espirituais, rituais e herborismo, sem investimento em atributos de dano físico (Força Bruta) ou de precisão (Astúcia). | Conhecimento e Presença. Focados no poder de magias de fé, interações sociais e resistência moral. Da mesma forma, não priorizam atributos de dano direto. |
| **Potencial de Dano Solo (Inicial)** | **Muito Baixo.**  A habilidade ativa é exclusivamente de cura. O dano depende unicamente de ataques básicos com armas de baixo poder (ex: Cajado Rachado de Cipó com dano 1D4). | **Muito Baixo.**  A habilidade ativa é puramente defensiva/utilitária. O potencial de dano é limitado a ataques básicos com armas de suporte (ex: Bastão de Fé de Madeira Escura com dano 1D4). |

**2.3. Síntese da Análise de Classes**
A análise comparativa revela que, em sua concepção fundamental, tanto o Xamã Curandeiro quanto o Missionário são desprovidos de ferramentas ofensivas eficazes para um cenário solo. Suas habilidades iniciais, distribuição de atributos e proficiências são estritamente voltadas para o suporte de um grupo. Consequentemente, ambas as classes apresentam um risco intrínseco significativo de baixo desempenho em combate, dependendo fortemente de fontes externas para causar o dano necessário para progredir.
**2.4. Transição**
Essa vulnerabilidade inerente é amplificada quando confrontada com os desafios específicos e a pressão temporal da campanha do Ato 1.
##### 3.0 Desconstrução dos Desafios da "Corrida do Ato 1"
**3.1. Análise dos Obstáculos**
Os desafios do Ato 1 não são apenas barreiras de combate, mas um teste contra o tempo. A mecânica do  **"Relógio da Ruptura"**  cria uma pressão constante que gera um  *feedback loop*  negativo para builds de baixo DPS. Para uma classe de baixo dano, combates que seriam triviais para um DPS podem se tornar longos e custosos, consumindo Ticks preciosos e aumentando exponencialmente a dificuldade da campanha.
**3.2. Análise dos Desafios por Sessão**
##### 3.2.1 Sessão 1 – Sussurros na Floresta
Esta fase inicial, focada em investigação e interação com NPCs, apresenta um risco  **baixo**  para as classes de suporte. A ausência de combate obrigatório permite que o jogador utilize suas habilidades sociais e de percepção sem ser penalizado pela falta de dano.
##### 3.2.2 Sessão 2 – Fronteira dos Mundos
O risco aumenta consideravelmente nesta sessão. O jogador deve negociar com facções para obter uma "Chave Espiritual". Se a diplomacia falhar ou se o Relógio da Ruptura avançar para a Fase 2, o mapa se transforma em uma zona de combate aberto. Para um personagem de suporte solo, enfrentar múltiplos inimigos sem uma fonte de dano confiável pode representar um obstáculo intransponível.
##### 3.2.3 Sessão 3 – A Corrida Final
O risco se intensifica com as emboscadas preparadas pelo grupo rival, "Os Bandeirantes de Sangue". O design da campanha explicitamente favorece classes como Explorador de Terras e Arqueiro Selvagem, que podem detectar e contornar esses confrontos. As classes de suporte, sem essas habilidades, seriam forçadas a lutar, consumindo mais tempo e recursos, o que acelera o avanço do Relógio da Ruptura.
##### 3.2.4 Sessão 4 – A Primeira Ruptura (Clímax)
Esta é a fase de maior risco de  *softlock* . O chefe final, "Guardião da Fenda", possui uma mecânica de  **Dificuldade Dinâmica** . Se o jogador chegar tarde (após o Tick 500), o chefe se torna  **"Ascendido"** , com ataques em área e dano massivo. Para um personagem de baixo dano, que naturalmente levará mais tempo para chegar a este ponto, enfrentar a versão fortalecida do chefe seria uma tarefa potencialmente impossível, resultando em um bloqueio de progressão.
**3.3. Conclusão Parcial**
A estrutura da "Corrida do Ato 1" cria uma espiral de dificuldade para as classes de suporte. A falta de dano leva a combates mais longos, que consomem mais Ticks do Relógio da Ruptura, o que, por sua vez, aumenta a dificuldade dos encontros e do chefe final. Sem a intervenção de sistemas de apoio, o risco de falha é extremamente alto.
**3.4. Transição**
Felizmente, a arquitetura do jogo inclui vários sistemas projetados especificamente para mitigar esses riscos e oferecer flexibilidade estratégica ao jogador.
##### 4.0 Avaliação dos Sistemas de Mitigação de Risco
**4.1. Análise dos Mecanismos de Suporte**
Esta seção representa o núcleo da auditoria, pois avalia se os sistemas de apoio ao jogador são robustos o suficiente para garantir a viabilidade das classes de suporte no modo solo. A análise conclui que as ferramentas disponíveis transformam o desafio de um  *hard check*  de DPS em um teste de conhecimento e engajamento estratégico do jogador com as mecânicas de flexibilidade do jogo.
**4.2. Análise Detalhada dos Sistemas**
1.  **Sistema de Companheiros/Mercenários (Capítulo 8)**  O sistema de companheiros é a solução mais direta para o déficit de dano. O jogador pode recrutar  **Mercenários**  ou  **Aliados de Facção**  para fornecer o poder de fogo necessário enquanto se concentra em seu papel de suporte. A eficácia deste sistema é altíssima, transformando o personagem de suporte no cérebro estratégico da dupla em vez de uma unidade de combate solitária. A principal recomendação associada é garantir que este sistema seja claramente introduzido e acessível desde o início do Ato 1.
2.  **Sistema de Herança de Habilidades (Alternância de Classes)**  Este é o fator de mitigação mais poderoso e flexível. O sistema permite que um jogador desbloqueie permanentemente qualquer classe para a qual complete os requisitos. A regra crucial é que  **apenas habilidades ativas são herdadas**  ao trocar de classe. Isso permite uma estratégia fundamental: um jogador pode iniciar como Missionário, juntar Moeda de Classe, desbloquear o Mosqueteiro, aprender a habilidade ativa Tiro Preparado (uma fonte de dano massivo), e então retornar à classe Missionário mantendo acesso a essa habilidade ofensiva. Este mecanismo dá ao jogador controle total para construir um personagem híbrido e autossuficiente.
3.  **Sinergia com Mini-Campanhas (Sidequests)**  As missões secundárias não são apenas conteúdo opcional; são vantagens táticas diretas que mitigam os principais pontos de pressão do Ato 1. A conclusão dessas missões pode:
    *   **Congelar o Relógio da Ruptura:**  A missão "O Tambor que Silenciou o Céu" concede um item que pausa o relógio por 20 Ticks, aliviando a pressão temporal.
    *   **Evitar Combate:**  A missão "A Canção que Não Dorme" desbloqueia um atalho que ignora completamente as emboscadas da Sessão 3.
    *   **Enfraquecer o Chefe Final:**  A missão "O Ouro que Nunca Brilha" ensina como reduzir a defesa do "Guardião da Fenda" em -2, tornando o combate final significativamente mais fácil.
4.  **Sistema de Qualidade de Itens**  Embora seja um fator de mitigação menor, o sistema de qualidade de itens oferece um caminho de progressão de poder. Itens de qualidade  **"Excelente"**  concedem um bônus de  **+2 na CD e +1 no Dano/Cura base da habilidade** . Isso significa que, mesmo sem habilidades de dano direto, um jogador pode focar em crafting ou loot para aprimorar o dano de seu ataque básico e a eficácia de suas habilidades de controle, fornecendo um aumento consistente em sua performance.
**4.3. Síntese de Eficácia**
A combinação desses quatro sistemas fornece uma rede de segurança robusta e multifacetada. A Herança de Habilidades oferece uma solução de "força bruta" para o problema de dano, enquanto os Companheiros fornecem uma alternativa mais direta. As sinergias de missões secundárias, por sua vez, permitem uma abordagem mais estratégica, onde o jogador pode contornar os desafios em vez de superá-los com dano. Juntos, eles garantem que um jogador atento e engajado tenha múltiplas rotas para o sucesso.
**4.4. Transição**
Com a análise das pressões e dos mecanismos de alívio concluída, podemos agora formular uma avaliação final do risco de softlock.
##### 5.0 Avaliação Final de Risco e Recomendações
**5.1. Diagnóstico do Risco de Softlock**
A análise consolidada demonstra que, embora as classes de puro suporte apresentem uma fragilidade inerente em cenários de combate solo, o design do jogo oferece mecanismos de alívio poderosos e diversificados. O risco de um jogador ficar permanentemente preso não advém de uma falha estrutural do sistema, mas sim da possibilidade de o jogador não estar ciente ou não se engajar com as ferramentas de mitigação disponíveis.
**5.2. Nível de Risco**
**Risco de Softlock: Baixo, condicionado à comunicação eficaz dos sistemas ao jogador.**
**5.3. Justificativa**
O risco é classificado como baixo porque as rotas de mitigação são multi-vetoriais: o Sistema de Companheiros oferece uma solução de poder direto, a Herança de Habilidades oferece uma solução de personalização e as Mini-Campanhas oferecem uma solução de anulação de desafio. Essa sobreposição garante que jogadores com diferentes estilos (tático, exploratório, de otimização) tenham saídas viáveis.
**5.4. Recomendações Estratégicas**
Para garantir que a experiência do jogador seja fluida e que os sistemas de mitigação cumpram seu propósito, as seguintes ações são recomendadas:
1.  **Garantir Acesso Antecipado aos Companheiros**  O sistema de Mercenários deve ser introduzido no início do Ato 1, talvez em uma das primeiras vilas ou acampamentos. Isso oferece a solução mais imediata e intuitiva para jogadores que escolheram uma classe de suporte e se sentem sobrecarregados pelo combate.
2.  **Comunicar o Sistema de Herança de Habilidades**  Implementar um tutorial contextual que é acionado na primeira vez que o jogador adquire uma Moeda de Classe, com um NPC Mestre de Classe explicando visualmente como a Herança de Habilidades ativas permite a criação de builds híbridas.
3.  **Balanceamento do Rival Offline**  Calibrar a progressão da IA do grupo rival "Os Bandeirantes de Sangue" para que seu avanço no Relógio da Ruptura seja, no máximo, 20% mais rápido que um jogador de suporte que se engaja com pelo menos uma mini-campanha. Isso cria pressão sem invalidar a exploração.
**5.5. Transição**
A implementação dessas recomendações fortalecerá a experiência de jogo para todas as classes, levando-nos à conclusão final deste relatório.
##### 6.0 Conclusão
Este relatório de auditoria conclui que as classes de suporte, Xamã Curandeiro e Missionário, são  **viáveis**  para completar a campanha "Corrida do Ato 1" no modo Solo Offline. Embora seu potencial de dano intrínseco seja extremamente baixo, o ecossistema de jogo oferece múltiplos sistemas de mitigação robustos — notadamente o sistema de Companheiros e a Herança de Habilidades — que capacitam o jogador a superar todos os desafios apresentados. Os achados confirmam a implementação bem-sucedida do nosso pilar de design de "Progressão Flexível". Com a implementação das recomendações para melhorar a comunicação desses sistemas, não há risco iminente de softlock estrutural, garantindo que todos os estilos de jogo possam ter uma experiência de progressão satisfatória.
