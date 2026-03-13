### Relatório de Auditoria de Projeto: Eras do Brasil
#### 1.0 Introdução e Escopo da Auditoria
O propósito deste relatório é auditar o alinhamento de design do projeto  *Eras do Brasil*  para retificar inconsistências críticas. A análise confronta as decisões registradas no  **Histórico de Decisões**  (chats), o conteúdo documentado nos  **Livros Oficiais**  (GDDs) e o progresso reportado no  **Status do Projeto**  (Checklist). O objetivo desta auditoria é impor um alinhamento rigoroso entre os artefatos de design, estabelecer uma única fonte da verdade (SSoT) e mitigar os riscos que ameaçam o cronograma e a integridade do projeto.
#### 2.0 Pontos de Atenção: Conflitos Diretos entre Documentos
A existência de conflitos diretos em regras ou conceitos fundamentais  **inevitavelmente levará**  a retrabalho, desperdício de recursos e erosão da integridade do design. Essas divergências representam um risco estratégico inaceitável para a consistência do jogo, criando confusão para a equipe de desenvolvimento e prejudicando a experiência do jogador. Os conflitos detalhados abaixo não são incidentes isolados, mas sintomas de uma falha processual: a ausência de um documento mestre designado como a Fonte Única da Verdade (SSoT) e a falta de disciplina na atualização da documentação após deliberações de design.
##### 2.1 Conflito na Mecânica de Iniciativa
A auditoria identificou uma discrepância fundamental na regra que determina a ordem das ações em combate. As duas versões da regra utilizam atributos distintos, o que impacta diretamente o balanceamento e a estratégia dos jogadores.
| Fonte do Documento | Regra Definida |
| ------ | ------ |
| Histórico de Decisões (RPG Eras do Brasil_convertido.md) | Iniciativa: 1D20 + Destreza. |
| Livro de Regras | Iniciativa: Cada personagem rola 1D20 + Astúcia. |

**Avaliação de Impacto:**  A iniciativa é uma mecânica central no combate por turnos. A utilização de "Destreza" em uma fonte e "Astúcia" em outra cria uma ambiguidade crítica que impede o balanceamento preciso das classes e confunde os jogadores sobre quais atributos priorizar. É essencial unificar esta regra imediatamente.
##### 2.2 Conflito nos Atributos de Rolagem de Ataque
Observou-se uma divergência similar nos atributos que modificam as rolagens de ataque, refletindo uma evolução do design que não foi devidamente propagada para todos os documentos. A decisão inicial, registrada no histórico de decisões (RPG Eras do Brasil_convertido.md), menciona o uso de atributos genéricos de RPG, como DES para ataques à distância e INT ou SAB para magia.
Em contraste, o Livro de Regras oficial adota uma nomenclatura temática e específica do universo de  *Eras do Brasil* , utilizando atributos como Astúcia, Conhecimento ou Sabedoria Ancestral. Embora a transição para nomes temáticos seja uma decisão de design positiva que enriquece a imersão, a falha em atualizar a documentação cria uma fonte de conflito. Esta falta de atualização da documentação não se limita a conflitos diretos, mas se estende a lacunas críticas de conteúdo, onde decisões cruciais permanecem não implementadas, como detalhado a seguir.
#### 3.0 Lacunas de Conteúdo: Decisões Não Implementadas nos Livros Oficiais
Esta seção identifica conceitos e mecânicas cruciais que foram aprovados nos chats de decisão, mas que ainda não foram formalizados nos Livros Oficiais. Essas lacunas não representam apenas trabalho futuro, mas falhas na formalização de  **diferenciais competitivos e funcionalidades-chave**  prometidas no design inicial. A ausência de documentação técnica para estes sistemas inovadores coloca a própria identidade do projeto em risco.
##### 3.1 Ausência do Sistema Detalhado de IA de NPCs
No histórico de decisões (RPG Eras do Brasil_convertido.md), foi registrada a intenção de criar um sistema complexo de Inteligência Artificial (IA) para NPCs, com personalidade, rotinas diárias e conhecimento emergente, similar aos sistemas de  *Stardew Valley*  e  *Kingdom Come: Deliverance* . No entanto, a análise dos Livros Oficiais revela que, embora um capítulo para NPCs esteja previsto, não há nenhuma documentação que especifique o funcionamento desta arquitetura.
Esta não é a ausência de um mero capítulo; é a falha em documentar a arquitetura de um dos sistemas mais complexos e inovadores do projeto. Sem uma especificação formal para as rotinas, a rede de conhecimento e a memória de eventos, o desenvolvimento desta funcionalidade-chave está bloqueado, e o risco de uma implementação desalinhada com a visão original é altíssimo.
##### 3.2 Ausência de Mecânicas de Sobrevivência e Risco
Foram discutidas no histórico de decisões (RPG Eras do Brasil_convertido.md) diversas mecânicas de "risco e persistência" destinadas a reforçar o tom de sobrevivência do jogo. Contudo, as seguintes regras ainda não foram formalizadas no Livro de Regras:
*   **Full Loot:**  A mecânica onde o personagem perde seus itens ao ser derrotado, criando um ciclo de risco e recompensa.
*   **Inimigos que Evoluem:**  O sistema onde inimigos que derrotam um personagem ganham experiência (XP), tornando-se adversários mais perigosos no futuro.
A ausência da formalização dessas regras impacta diretamente a atmosfera de "sobrevivência" e o conceito de "mundo vivo" que são centrais para a proposta do jogo. Sem elas, o design falha em entregar o nível de desafio e consequência pretendido.
#### 4.0 Auditoria do Checklist: Análise de Status "Pronto" vs. "Ausente"
Um checklist de projeto preciso é uma ferramenta de gerenciamento indispensável para a alocação de recursos e a visibilidade do progresso. Esta seção audita o arquivo Checklist – Livro de Regras Eras do Brasil para validar se o status reportado de cada capítulo corresponde ao estado real do conteúdo nos Livros Oficiais.
##### 4.1 Itens com Status Incorreto
A análise cruzada revelou que o checklist está severamente desatualizado, reportando como parciais ou ausentes diversos capítulos que já se encontram em estado avançado ou concluído de produção.
| Capítulo | Status Reportado | Status Real | Justificativa da Discrepância |
| ------ | ------ | ------ | ------ |
| Sistema de Itens e Equipamentos | 🛠 Parcial | Próximo de ✅ Pronto | Checklist alega ausência de regras de durabilidade; no entanto, o Livro de Regras contém a seção 6.4 – Reparos, Manutenção e Durabilidade. |
| Sistema de Terrenos e Exploração | 🔜 Ausente | ✅ Pronto | Conteúdo marcado como Ausente está integralmente documentado no Livro de Regras sob o título "Capítulo 5 – Exploração e Mundo". |
| NPCs, Companions e Facções | 🔜 Ausente | 🛠 Parcial | O "Capítulo 8 – Mestres, Campanhas e Mundo Vivo" no Livro de Regras já detalha a estrutura de NPCs vivos, contradizendo o status de ausente. |
| Magias, Rituais e Espiritualidade | 🔜 Ausente | ✅ Pronto | Conteúdo marcado como Ausente está integralmente documentado no Livro de Regras sob o título "Capítulo 7 – Magia e Espiritualidade". |

A severa desatualização do checklist anula seu propósito como ferramenta de gerenciamento. Ele não reflete o progresso real, gerando um falso senso de atraso em áreas concluídas e mascarando as verdadeiras lacunas de conteúdo. A ferramenta, no seu estado atual, é uma fonte de desinformação que compromete a tomada de decisões estratégicas do projeto.
#### 5.0 Sumário de Ações Recomendadas
Com base nas descobertas desta auditoria, as seguintes ações corretivas e processuais devem ser executadas com prioridade máxima para restaurar a integridade e a governança do projeto:
1.  **Instituir Processo de Unificação de Regras:**  Designar formalmente o Livro de Regras como a única Fonte da Verdade (SSoT) para todas as mecânicas. Todas as deliberações futuras de design devem culminar na atualização imediata deste documento mestre.
2.  **Priorizar a Documentação de Sistemas-Chave:**  Alocar recursos imediatos para a especificação técnica dos sistemas de  **IA de NPCs**  e das  **mecânicas de risco**  (Full Loot, Inimigos Evolutivos). Estes devem ser tratados como requisitos de alta prioridade para a próxima milestone de desenvolvimento.
3.  **Realizar Auditoria Completa e Instituir Manutenção do Checklist:**  Executar uma revisão imediata de todos os itens do Checklist – Livro de Regras Eras do Brasil contra os GDDs. Implementar um processo de atualização semanal obrigatório para o gerente de projeto, garantindo que a ferramenta reflita o estado real da produção.
