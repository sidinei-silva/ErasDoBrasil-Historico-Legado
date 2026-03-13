### Proposta de Estrutura de Dados (JSON Schema) para o Sistema de Missões
#### 1.0 Introdução: A Ponte da Alma para a Lógica
Este documento estabelece a proposta de arquitetura de dados para o sistema de missões de  *Eras do Brasil* . O objetivo estratégico é traduzir as ricas narrativas das missões, atualmente em formato de texto, para uma estrutura de dados JSON que seja robusta, escalável e diretamente consumível pelo motor do jogo. Em linha com a filosofia do projeto "Alma vs. Lógica", este schema representa a "Lógica" — a estrutura formal e quantificável que dará vida à "Alma" das missões descritas nos documentos de design. Ao formalizar gatilhos, etapas, condições e recompensas em um formato padronizado, criamos a ponte essencial entre o conceito narrativo e a implementação técnica, permitindo a construção de um banco de dados coeso e a automação de sistemas complexos de jogo. Este schema não é meramente uma especificação técnica; é o contrato fundamental que permitirá o trabalho paralelo entre as equipes de narrativa e engenharia, garantindo que o conteúdo possa ser produzido em escala enquanto minimiza a dívida técnica. A seguir, detalharemos os princípios que nortearam o design desta estrutura.
#### 2.0 Princípios Fundamentais do Schema Proposto
Uma arquitetura de dados bem-sucedida deve se basear em princípios sólidos para garantir a longevidade, a manutenibilidade e a capacidade de expansão do projeto. A estrutura proposta para as missões de  *Eras do Brasil*  foi concebida seguindo quatro pilares fundamentais, que asseguram sua adequação aos sistemas centrais do jogo e ao fluxo de trabalho da equipe.
1.  **Modularidade e Flexibilidade**  O schema foi desenhado para ser inerentemente modular, capaz de acomodar uma vasta gama de tipos de missões sem a necessidade de criar estruturas de dados distintas para cada caso. A combinação de gatilhos, etapas (steps) e verificações (checks) permite modelar desde uma missão de rastreamento baseada em proficiência, como a Indigena_01_O_Cacador_que_Nao_Voltou, até uma complexa trama política com múltiplos caminhos, como a Colonizador_04_A_Palavra_do_Rei_Nao_Ecoa_Aqui, que requer verificações de infiltração, rastreamento da rotina de NPCs (para encontrar a casa vazia do líder rebelde) e recompensas ramificadas com base no apoio do jogador à Coroa ou aos rebeldes. Essa flexibilidade é crucial para que os designers de missões possam inovar sem serem limitados por uma estrutura de dados rígida.
2.  **Integração com Sistemas Centrais**  A estrutura de dados das missões não existe em um vácuo; ela foi projetada para se conectar nativamente às mecânicas de "Mundo Vivo" que definem a experiência de  *Eras do Brasil* . A integração com o sistema de  **Ticks**  é fundamental, permitindo missões com urgência temporal, eventos que ocorrem em horários específicos e condições de falha baseadas no tempo. Da mesma forma, o schema se integra às  **rotinas de IA dos NPCs** , permitindo que gatilhos de missão dependam da localização ou do conhecimento de um personagem, e ao sistema de  **Proficiências de Vida** , transformando testes de habilidade em verificações lógicas dentro das etapas da missão. Essa integração profunda garante que as missões não sejam sobreposições estáticas, mas sim tecidas na malha de simulação do mundo, reagindo ao relógio central do jogo e aos comportamentos emergentes de seus habitantes.
3.  **Clareza e Legibilidade**  O schema deve servir como um contrato de dados claro e inequívoco entre os designers de missões e os engenheiros de sistemas. Ao utilizar nomes de campos intuitivos que mapeiam diretamente para conceitos no GDD, reduzimos a ambiguidade, aceleramos o pipeline de conteúdo e capacitamos a criação de ferramentas de autoria. Essa clareza garante que a intenção narrativa seja preservada do conceito ao código, prevenindo interpretações errôneas e custosas durante o desenvolvimento.
4.  **Escalabilidade**  O universo de  *Eras do Brasil*  está destinado a crescer, com a introdução de novas Eras, classes, facções e tipos de recompensa. A arquitetura proposta é escalável por design. O uso de  *arrays*  para gatilhos, etapas e recompensas, combinado com campos de type e parameters genéricos, permite a adição de novas lógicas no futuro sem exigir uma refatoração completa do banco de dados. Uma nova mecânica de jogo pode ser introduzida simplesmente adicionando um novo type de check ou reward, mantendo a integridade das missões já existentes.
Para demonstrar como esses princípios foram aplicados na prática, analisaremos a seguir uma missão específica que serviu como caso de estudo para a criação do schema.
#### 3.0 Análise do Caso de Estudo: A Missão "Indigena_01_O_Cacador_que_Nao_Voltou"
Esta seção apresenta a desconstrução analítica da missão Indigena_01_O_Cacador_que_Nao_Voltou. O objetivo é usar este exemplo prático para justificar a necessidade e a função de cada campo principal do schema de dados proposto. Ao decompor uma narrativa em seus componentes lógicos, podemos ver claramente como a estrutura JSON se torna uma representação fiel e funcional da experiência de jogo planejada.
*   **Identificadores Básicos**  O título da missão é "O Caçador que Não Voltou", servindo como a principal referência para o jogador na interface e no diário de missões.
*   **Gatilhos de Início (Triggers)**  A missão pode ser iniciada de duas maneiras distintas, demonstrando a necessidade de um sistema de gatilhos múltiplos e condicionais:
    1.  **Interação Passiva:**  Falar com Jaci, a mãe do caçador, após o meio-dia (Tick 50). Isso exige um gatilho do tipo NPC_INTERACTION com uma condição de tempo (min_tick).
    2.  **Gatilho Ativo via "Fofoca":**  Ouvir de um NPC com a tag "observador" sobre o desaparecimento de Iaguarê. Isso demanda um sistema de gatilhos capaz de consultar a knowledgeBase dinâmica dos NPCs, que é populada através do sistema de 'Fofoca' enquanto eles executam suas rotinas diárias.
*   **Estrutura em Etapas (Steps)**  A missão se desenrola em três etapas sequenciais, cada uma contendo "checks" que o jogador deve superar:
    1.  **Investigação:**  O jogador precisa obter informações de um guarda, o que requer um nível de afinidade mínimo (affinity > 10). Isso justifica um check do tipo DIALOGUE_CHOICE ou AFFINITY_CHECK.
    2.  **Rastro:**  O jogador deve seguir o rastro na floresta, o que exige um teste da proficiência de Rastreamento. A dificuldade (CD) desse teste muda com o tempo: é mais fácil antes do Tick 80 (CD 10) e mais difícil depois (CD 15), o que requer parâmetros condicionais dentro do PROFICIENCY_TEST.
    3.  **Encontro:**  A condição de vitória do combate final depende do tempo de chegada. Se o jogador chegar antes do Tick 100, luta ao lado de Iaguarê. Se chegar depois, Iaguarê está inconsciente, tornando a luta mais difícil e adicionando a tarefa de carregá-lo de volta.
*   **Condições de Falha (Fail Condition)**  O documento da missão especifica uma condição de falha implícita: se o jogador demorar mais de 120 Ticks, o rastro desaparece completamente. Isso se traduz diretamente em uma fail_condition do tipo TICK_LIMIT_EXCEEDED, que encerraria a missão com um resultado negativo.
*   **Recompensas (Rewards)**  Ao concluir a missão com sucesso, o jogador recebe três tipos distintos de recompensa, demonstrando a necessidade de um  *array*  de recompensas variadas:
    1.  **Bônus de Estatística:**  +1 permanente em testes de rastreamento (STAT_BONUS).
    2.  **Item Único:**  O Dente da Fera dos Sonhos (ITEM).
    3.  **Reputação:**  +20 de afinidade com a facção da Aldeia (REPUTATION).
Esta análise detalhada informa diretamente a estrutura do schema JSON que será apresentada na próxima seção, garantindo que cada campo tenha um propósito claro e validado por um caso de uso real.
#### 4.0 Estrutura Detalhada do Schema JSON
Esta seção apresenta a estrutura JSON proposta para os objetos de missão. Cada campo e subcampo é detalhado para fornecer uma compreensão clara de sua função e de como ele contribui para a modelagem das complexas narrativas de  *Eras do Brasil* .
##### 4.1 Estrutura Raiz do Objeto de Missão
A estrutura raiz contém os metadados essenciais que identificam e categorizam a missão.
```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "origin_tag": "string",
  "recommended_classes": ["string"],
  "mission_type": "string"
}

```
*  id: O identificador único e programático da missão (ex: indigena_01). Essencial para referências no código e no banco de dados.
*  title: O título da missão exibido na interface do usuário (UI) e no diário de missões (ex: "O Caçador que Não Voltou").
*  description: Um texto curto que resume o objetivo da missão para o jogador.
*  origin_tag: Uma tag que vincula a missão à sua origem cultural ou narrativa (ex: "Indigena", "Colonizador", "Folclorico"), útil para filtros e sistemas de reputação.
*  recommended_classes: Um  *array*  com sugestões de classes que se encaixam bem com a narrativa ou as mecânicas da missão, servindo como uma dica para o jogador.
*  mission_type: Uma categoria funcional para a missão (ex: "Rastreamento", "Investigacao", "Combate"), permitindo a organização e análise de conteúdo.
##### 4.2 Estrutura dos Gatilhos (triggers)
Esta seção define as condições que podem iniciar a missão.
```json
"triggers": [
  {
    "type": "string",
    "parameters": {}
  }
]

```
*  triggers é um  *array*  de objetos, permitindo que uma única missão tenha múltiplos pontos de entrada. O motor do jogo verifica continuamente esses gatilhos.
*  type: Define a lógica do gatilho (ex: TIME_CONDITION, NPC_INTERACTION, ENTER_AREA, NPC_GOSSIP).
*  parameters: Um objeto que contém os dados específicos para o type do gatilho. Por exemplo, para um NPC_INTERACTION, os parâmetros poderiam ser {"npc_id": "jaci", "min_tick": 50}. Para um tipo NPC_GOSSIP, os parâmetros seriam {"npc_tag": "observador", "gossip_key": "iaguare_missing"}.
##### 4.3 Estrutura das Etapas (steps)
As etapas representam a progressão sequencial da missão.
```json
"steps": [
  {
    "step_id": "integer",
    "objective": "string",
    "checks": [
      {
        "type": "string",
        "parameters": {}
      }
    ]
  }
]

```
*  steps é um  *array*  ordenado de objetos, onde cada objeto representa uma etapa da missão.
*  step_id: Um identificador numérico para a ordem da etapa.
*  objective: O texto do objetivo que será exibido na UI para guiar o jogador (ex: "Siga o rastro de Iaguarê pela floresta.").
*  checks: Um  *array*  de verificações que o jogador deve cumprir para completar a etapa. O campo type define a mecânica (ex: PROFICIENCY_TEST, COMBAT, ITEM_DELIVERY), e parameters contém os detalhes. Por exemplo, parameters poderia conter verificações simples como {"proficiency": "Rastreamento", "dc": 10}, ou lógicas condicionais mais complexas, como {"proficiency": "Rastreamento", "dc_if_tick_less_than": {"tick": 80, "dc": 10}, "dc_if_tick_greater_than": {"tick": 80, "dc": 15}}.
##### 4.4 Estrutura das Condições de Falha (fail_conditions)
Define as condições que, se atendidas, encerram a missão com falha.
```json
"fail_conditions": [
  {
    "type": "string",
    "parameters": {}
  }
]

```
*  fail_conditions é um  *array*  que permite definir múltiplas formas de falhar em uma missão.
*  type: Define a lógica da condição de falha (ex: TICK_LIMIT_EXCEEDED, NPC_DEATH, ITEM_LOST).
*  parameters: Contém os dados para a verificação, como {"tick_limit": 120} para um limite de tempo.
##### 4.5 Estrutura das Recompensas (rewards)
Especifica o que o jogador ganha ao completar a missão.
```json
"rewards": {
  "on_success": [
    {
      "type": "string",
      "parameters": {}
    }
  ]
}

```
*  rewards é um objeto que pode conter diferentes listas de recompensas para diferentes desfechos (ex: on_success, on_partial_success, on_failure). Essa estrutura é vital para missões como 'O Caçador que Não Voltou', onde chegar tarde resulta em um desfecho diferente e poderia acionar uma lista de recompensas on_partial_success.
*  Cada lista (como on_success) é um  *array*  de objetos de recompensa.
*  type: Define o tipo de recompensa (ex: ITEM, XP, REPUTATION, STAT_BONUS, CLASS_COIN).
*  parameters: Contém os detalhes da recompensa, como {"item_id": "dente_fera_sonhos", "quantity": 1} para um item, ou {"faction": "aldeia_indigena", "amount": 20} para reputação.
Com esta estrutura detalhada, podemos agora demonstrar sua aplicação prática no caso de estudo.
#### 5.0 Exemplo de Implementação: Indigena_01_O_Cacador_que_Nao_Voltou
Para demonstrar a eficácia e a clareza do schema proposto, a missão "O Caçador que Não Voltou", analisada anteriormente, será agora totalmente representada no formato JSON. Este exemplo prático ilustra como a complexidade narrativa e as mecânicas de jogo são capturadas de forma limpa e estruturada, prontas para serem interpretadas pelo motor do jogo.
**Guia para o JSON:**
*  A seção triggers modela as duas formas de iniciar a missão: falando com a mãe de Iaguarê após o meio-dia (Tick 50) ou através da knowledgeBase de um NPC observador, populada pelo sistema de 'Fofoca'.
*  Observe como as steps são sequenciais. O step_id: 2 (O Rastro) modela elegantemente a dificuldade dinâmica, utilizando os parâmetros dc_if_tick_less_than e dc_if_tick_greater_than para que o motor do jogo possa aplicar a CD correta com base no tick atual, sem a necessidade de lógica hard-coded.
*  A seção fail_conditions estabelece um requisito de urgência claro, definindo o limite de tempo (120 Ticks) para a conclusão bem-sucedida da missão.
*  A lista rewards demonstra a flexibilidade do schema para conceder múltiplos tipos de prêmios simultaneamente: um item único, um bônus de estatística permanente e um ganho de reputação com uma facção.
```json
{
  "id": "indigena_01",
  "title": "O Caçador que Não Voltou",
  "description": "Um jovem caçador, Iaguarê, não retornou da floresta. Sua mãe, Jaci, está preocupada. Encontre-o antes que a noite caia.",
  "origin_tag": "Indigena",
  "recommended_classes": ["Cacador_de_Feras", "Arqueiro_Selvagem"],
  "mission_type": "Rastreamento",
  "triggers": [
    {
      "type": "NPC_INTERACTION",
      "parameters": {
        "npc_id": "jaci",
        "min_tick": 50,
        "dialogue_branch": "start_mission_cacador"
      }
    },
    {
      "type": "NPC_GOSSIP",
      "parameters": {
        "npc_tag": "observador",
        "gossip_key": "iaguare_missing"
      }
    }
  ],
  "steps": [
    {
      "step_id": 1,
      "objective": "Investigue o desaparecimento de Iaguarê na vila.",
      "checks": [
        {
          "type": "DIALOGUE_CHOICE",
          "parameters": {
            "npc_id": "guarda_vila_norte",
            "required_affinity": 10,
            "success_flag": "found_trail_start"
          }
        }
      ]
    },
    {
      "step_id": 2,
      "objective": "Siga o rastro de Iaguarê pela floresta.",
      "checks": [
        {
          "type": "PROFICIENCY_TEST",
          "parameters": {
            "proficiency": "Rastreamento",
            "dc_if_tick_less_than": { "tick": 80, "dc": 10 },
            "dc_if_tick_greater_than": { "tick": 80, "dc": 15 },
            "success_flag": "found_iaguare"
          }
        }
      ]
    },
    {
      "step_id": 3,
      "objective": "Enfrente a criatura e salve Iaguarê.",
      "checks": [
        {
          "type": "COMBAT",
          "parameters": {
            "enemy_id": "devorador_sonhos",
            "victory_condition_a": { "max_tick": 100, "ally_npc": "iaguare_ferido" },
            "victory_condition_b": { "min_tick": 101, "objective_update": "carry_iaguare_back" }
          }
        }
      ]
    }
  ],
  "fail_conditions": [
    {
      "type": "TICK_LIMIT_EXCEEDED",
      "parameters": {
        "tick_limit": 120,
        "fail_message": "O rastro esfriou e a noite caiu. É tarde demais para encontrar Iaguarê."
      }
    }
  ],
  "rewards": {
    "on_success": [
      {
        "type": "STAT_BONUS",
        "parameters": {
          "stat": "rastreamento_test",
          "value": 1,
          "duration": "permanent"
        }
      },
      {
        "type": "ITEM",
        "parameters": {
          "item_id": "dente_fera_sonhos",
          "quantity": 1
        }
      },
      {
        "type": "REPUTATION",
        "parameters": {
          "faction_id": "aldeia_indigena",
          "amount": 20
        }
      }
    ]
  }
}

```
Como demonstrado, a estrutura proposta é plenamente capaz de capturar as nuances e a complexidade de uma missão dinâmica e integrada ao sistema de "Mundo Vivo", validando seu design.
#### 6.0 Conclusão e Próximos Passos
A adoção deste schema de dados para as missões é um passo fundamental na construção de uma base técnica sólida para  *Eras do Brasil* . Esta estrutura atende diretamente aos princípios de design estabelecidos: é  **modular**  para acomodar diversas narrativas, está profundamente  **integrada**  aos sistemas centrais de Ticks e IA, e é  **escalável**  para suportar o crescimento futuro do jogo. Ao criar uma linguagem comum entre o design narrativo e a implementação de sistemas, estamos estabelecendo um pipeline de produção eficiente e robusto.
Com a estrutura de missões definida, os próximos passos lógicos na arquitetura de dados do projeto, conforme o checklist de produção, são:
**Próximos Passos:**
1.  **Definir o Schema de Itens (JSON):**  Estruturar a Matriz 5x5 de Qualidade e Raridade para que possa ser interpretada pelo código, definindo atributos, durabilidade e efeitos.
2.  **Definir o Schema de Inimigos/NPCs (JSON):**  Modelar as estatísticas, a árvore de comportamento (behavior_tree), a base de conhecimento (knowledgeBase) e as tabelas de loot de todas as entidades do jogo.
3.  **Definir o Schema de Habilidades (JSON):**  Formalizar as fórmulas de dano, efeitos de status, custos de recurso e tempos de recarga de todas as habilidades de classe em um formato de dados estruturado.
Este schema de missões, portanto, torna-se a primeira de várias estruturas de dados críticas que formarão o sistema nervoso central do jogo, transformando a visão ambiciosa de  *Eras do Brasil*  em uma realidade digital escalável e dinâmica.
