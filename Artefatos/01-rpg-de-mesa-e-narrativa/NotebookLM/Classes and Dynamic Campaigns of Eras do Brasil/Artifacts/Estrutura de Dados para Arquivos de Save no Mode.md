### Estrutura de Dados para Arquivos de Save no Modelo "Eco Compartilhado"
#### 1. Introdução: A Arquitetura de Save para um Mundo Persistente e Cooperativo
A arquitetura de salvamento de dados ( *save* ) é um pilar estratégico para o sucesso do modelo cooperativo "Eco Compartilhado" de  *Eras do Brasil* . Este modelo, onde um jogador Anfitrião (Host) é o dono do estado do mundo e um jogador Convidado (Client) traz seu próprio personagem para essa realidade, exige uma separação de dados rigorosa e bem definida. A integridade desta separação é fundamental para garantir a consistência narrativa do "Eco" (o mundo do Host), prevenir manipulação de dados e, acima de tudo, proporcionar uma experiência fluida e coerente para os jogadores, quer estejam em uma sessão solo ou cooperativa através da "Raiz do Mundo". Esta estrutura de dados não é apenas um requisito técnico; é a fundação que sustenta a fantasia de um Desperto viajando entre mundos únicos, cada um moldado pelas decisões de seu respectivo dono. Essa arquitetura é, portanto, guiada por um princípio único e inegociável: uma separação rígida entre o estado do mundo e o estado do personagem, garantindo tanto a integridade narrativa quanto a portabilidade do personagem.
#### 2. A Filosofia Central: O Host Salva o Mundo, o Client Salva o Personagem
O princípio fundamental da nossa arquitetura de save é uma divisão clara de responsabilidades: o arquivo de save do Host é a autoridade sobre o estado do mundo, enquanto o arquivo do Client é uma cápsula autocontida e portátil que define exclusivamente o seu personagem. Tudo o que pertence ao "Eco" — o progresso das missões, a localização e o conhecimento dos NPCs, a reputação com facções e as mudanças permanentes no ambiente — é registrado e preservado unicamente no save do Host. Em contrapartida, o Client salva apenas os dados que o definem como um "Viajante": seus atributos, seu inventário, sua experiência acumulada e suas habilidades desbloqueadas. Essa separação garante que um personagem possa entrar em diferentes "Ecos" sem corromper a narrativa local, levando consigo apenas seu progresso pessoal.
A tabela abaixo ilustra visualmente essa divisão de responsabilidades:
| Responsabilidade do Host (O Eco) | Responsabilidade do Client (O Viajante) |
| ------ | ------ |
| Estado e progresso das missões (Ato 1, etc.) | Atributos base (Vigor, Força Bruta, etc.) e status derivados (PV) |
| Estado dos NPCs (localização, knowledgeBase, afinidade) | Inventário, equipamentos e moedas (Loot) |
| Reputação com facções | Experiência (XP) e progresso de nível |
| Estado do ambiente (recursos, corrupção, etc.) | Classes desbloqueadas e seus Tiers |
| Contador de Ticks globais e eventos mundiais | Habilidades ativas herdadas |

Com esta filosofia estabelecida, podemos agora detalhar a estrutura de dados necessária para cada um desses arquivos.
#### 3. Detalhamento da Estrutura de Save do Host (O "Eco")
O arquivo de save do Host funciona como a "Fonte Única da Verdade" ( *Single Source of Truth* ) para o estado daquele universo de jogo específico. Sendo o "Âncora" do Eco, o Host é o único cujas decisões narrativas e ações de longo prazo moldam permanentemente a realidade. Esse controle centralizado é essencial para manter a coerência da história e a consistência do mundo, evitando paradoxos ou conflitos de dados que surgiriam se múltiplos jogadores pudessem sobrescrever o estado global. A seguir, detalhamos os componentes cruciais deste arquivo.
##### 3.1. Estado Global do Mundo e Ambiente
Estes dados definem o contexto físico e temporal em que toda a jogabilidade ocorre. Eles registram desde o avanço de mecânicas globais, como o "Relógio da Ruptura", até as mudanças permanentes no cenário, como a transformação de uma floresta no "Bosque das Sombras" após o clímax do Ato 1.
*  world_state.global_tick_counter: (Integer) Rastreia o avanço do "Relógio da Ruptura" e outros eventos globais que dependem da passagem de tempo.
*  world_state.current_era: (String) Identifica a era principal em que a campanha do Host se passa, como "1497_Primeira_Ruptura".
*  world_state.environment.[block_id].state: (String) Salva o estado de cada "bloco" do mapa (ex: "normal", "corrompido_pos_ruptura", "inundado"), refletindo as consequências de missões.
*  world_state.environment.[block_id].resources: (Array of Objects) Lista os recursos disponíveis em cada bloco e seu tempo de regeneração, atrelado ao contador de ticks.
##### 3.2. Progresso de Missões e Narrativa
Esta seção é o coração narrativo do save do Host. Como todas as decisões críticas da história são tomadas pelo Host, o estado de todas as missões, principais e secundárias, deve ser salvo exclusivamente por ele. Isso inclui o rastreamento de missões secundárias, como "Justiça das Mãos Sujas", que podem fornecer vantagens táticas ou aliados na campanha principal.
*  quests.main_story.act_1.status: (String) Registra o resultado da missão principal (ex: "in_progress", "completed_victory", "completed_survival").
*  quests.main_story.act_1.choices_made: (Array of Objects) Armazena decisões críticas que alteram o mundo, como alianças com facções ou o destino de NPCs chave.
*  quests.side_quests.[quest_id].status: (String) Rastreia o status de cada missão secundária (ex: "not_started", "in_progress", "completed").
*  quests.side_quests.[quest_id].current_stage: (Integer) Marca a etapa atual de missões com múltiplos objetivos.
*  quests.side_quests.[quest_id].outcome: (String) Registra o resultado final da missão, que pode se tornar um world_flag ou influenciar o comportamento de NPCs.
*  world_flags: (Array of Strings) Uma lista de gatilhos narrativos globais que foram ativados (ex: "capitao_da_guarda_leal", "ruptura_contida"), permitindo que o mundo reaja a eventos passados.
##### 3.3. Estado dos NPCs e Facções
Com base no sistema de "Mundo Vivo", é vital salvar o estado de cada NPC para manter a ilusão de um mundo autônomo. Salvar sua localização, conhecimento e relacionamentos é o que alimenta a IA dinâmica e os sistemas de "Fofoca", onde NPCs compartilham informações que viram ou ouviram.
*  npcs.[npc_id].current_location_block_id: (String) Armazena o bloco do mapa onde o NPC se encontra no momento do save, refletindo sua rotina diária.
*  npcs.[npc_id].knowledge_base: (Array of Objects) Salva as informações que o NPC viu ou ouviu (ex: {"event": "viu_luzes_estranhas", "tick_observed": 450}), formando a base para o sistema de "Fofoca". Este timestamp é crítico, pois permite que a informação se torne "obsoleta" ou menos confiável com o tempo, criando uma rede social mais dinâmica e verossímil.
*  npcs.[npc_id].affinity_towards_players: (Object) Mapeia o nível de afinidade do NPC com cada jogador (identificado por um ID único) que já visitou o Eco, influenciando diálogos e preços.
*  factions.[faction_id].reputation: (Integer) Armazena o nível de reputação do grupo de jogadores com cada facção do mundo.
A integridade do "Eco" do Host depende dessa estrutura de dados centralizada, que agora contrasta com a natureza portátil do arquivo do Client.
#### 4. Detalhamento da Estrutura de Save do Client (O "Viajante")
O arquivo de save do Client deve ser uma representação completa e independente de seu personagem. Ele é projetado para ser totalmente portátil, contendo todos os dados necessários para que o personagem possa existir e funcionar em qualquer "Eco" de um Host, sem depender de informações externas. Isso permite que um jogador progriga com seu personagem em campanhas com diferentes amigos, mantendo sua identidade, poder e espólios.
##### 4.1. Dados Fundamentais do Personagem
Estes são os dados que definem a identidade do personagem, estabelecidos durante sua criação e raramente alterados.
*  character.name: (String) O nome do personagem.
*  character.origin: (String) A origem escolhida: "Colonizador", "Indígena", ou "Ser Folclórico".
*  character.attributes: (Object) Contém os 6 atributos base (Vigor, Força Bruta, Astúcia, etc.) e seus valores atuais.
*  character.appearance: (Object) Campos dedicados à personalização visual.
*  character.narrative_flags: (Array of Strings) Registra o histórico e os laços pessoais definidos na criação, que podem ativar diálogos ou eventos únicos.
##### 4.2. Progresso e Habilidades
Aqui se concentra a evolução do personagem. Esta seção rastreia o crescimento, as capacidades e a flexibilidade tática adquirida ao longo de suas jornadas, incluindo o sistema de Tiers e a herança de habilidades ativas.
*  progression.level: (Integer) O nível geral do personagem.
*  progression.current_xp: (Integer) A quantidade atual de experiência acumulada.
*  progression.active_class_id: (String) A classe que está ativa no momento do save.
*  progression.unlocked_classes: (Array of Objects) Uma lista de todas as classes desbloqueadas, cada uma com seu class_id, tier, e class_xp individual, já que o progresso é por classe.
*  progression.unlocked_active_skills: (Array of Strings) O "pool" de habilidades ativas que foram herdadas de todas as classes já desbloqueadas e que podem ser usadas a qualquer momento.
*  progression.proficiencies: (Array of Objects) Lista as "Proficiências de Vida" do personagem com seu proficiency_id e level (Aprendiz, Competente, etc.).
##### 4.3. Inventário e Equipamentos
Com base na regra de "Ganhos Compartilhados", tudo o que o Client coleta em um Eco é seu para levar. Esta seção detalha cada item, sua qualidade, raridade e estado, conforme o sistema 5x5.
*  inventory.currency: (Integer) A quantidade de "Unidades Comerciais" (UC) que o personagem possui.
*  inventory.items: (Array of Objects) Uma lista de todos os itens na mochila. Cada objeto deve conter:
    *  item_id: (String) O identificador único do item.
    *  quantity: (Integer) A quantidade do item.
    *  quality: (String) A qualidade do item (ex: "Média", "Excelente").
    *  rarity: (String) A raridade do item (ex: "Comum", "Raro").
    *  current_durability: (Integer) A durabilidade atual do item. Um valor de -1 é convencionado para representar itens indestrutíveis.
*  equipped_items: (Object) Um mapeamento dos slots de equipamento (arma, armadura, etc.) para o ID único do item correspondente no inventário.
Com a estrutura de dados de Host e Client claramente definida, podemos responder de forma conclusiva à questão central sobre o estado das missões.
#### 5. Análise Direta: Salvando o Estado das Missões
Respondendo diretamente à questão fundamental:  **apenas o Host salva o estado das missões** . Essa é uma decisão arquitetural não negociável para a integridade do modelo "Eco Compartilhado". As missões, suas escolhas e suas consequências são elementos intrínsecos à história e ao estado do "Eco" de um Host. Se um Client pudesse salvar o progresso de uma missão (por exemplo, "Ato 1 Concluído"), ele poderia entrar no mundo de um novo Host que ainda nem começou o Ato 1 e criar um paradoxo narrativo insolúvel. Isso quebraria a consistência do mundo, anularia a agência do Host como "Âncora" da história e destruiria o pilar central do design cooperativo. O Client é um Viajante; ele participa e influencia os eventos, mas a  *memória*  desses eventos — a história do mundo — pertence exclusivamente ao Eco que ele visitou.
#### 6. Proposta de Estrutura JSON para os Arquivos de Save
Para materializar os conceitos discutidos, apresentamos a seguir exemplos de estruturas JSON para os arquivos de save do Host e do Client. Estes esquemas sintetizam todos os pontos abordados, oferecendo uma proposta tangível e coerente para a implementação.
##### 6.1. Exemplo de host_save.json
```
{
  "save_metadata": {
    "save_name": "Campanha do João",
    "play_time_seconds": 7200,
    "last_saved_timestamp": "2024-10-27T10:00:00Z"
  },
  "world_state": {
    "global_tick_counter": 512,
    "current_era": "1497_Primeira_Ruptura",
    "environment": {
      "floresta_sombria": {
        "state": "corrompido_pos_ruptura",
        "resources": [{"resource_id": "erva_sombria", "respawn_tick": 600}]
      }
    }
  },
  "quests": {
    "main_story": {
      "act_1": {"status": "completed_survival"}
    },
    "side_quests": {
      "justica_maos_sujas": {"status": "completed", "outcome": "capitao_exposto"}
    }
  },
  "npcs": {
    "paje_velho": {
      "current_location_block_id": "cachoeira_meditacao",
      "knowledge_base": [{"event": "viu_luzes_estranhas", "tick_observed": 450}],
      "affinity_towards_players": {"player_id_kaira": 25, "player_id_domingos": -10}
    }
  },
  "factions": {
    "aldeia_tupi": {"reputation": 50},
    "coroa_portuguesa": {"reputation": -20}
  }
}

```
##### 6.2. Exemplo de client_character.json
```
{
  "character": {
    "name": "Kaira",
    "origin": "Indígena",
    "attributes": {
      "vigor": 4,
      "forca_bruta": 3,
      "astucia": 6,
      "sabedoria_ancestral": 5,
      "conhecimento": 2,
      "presenca": 3
    }
  },
  "progression": {
    "level": 8,
    "current_xp": 1250,
    "active_class_id": "arqueiro_selvagem",
    "unlocked_classes": [
      {"class_id": "arqueiro_selvagem", "tier": 2, "class_xp": 800},
      {"class_id": "cacador_de_feras", "tier": 1, "class_xp": 300}
    ],
    "unlocked_active_skills": ["tiro_furtivo", "arremesso_rapido"],
    "proficiencies": [
      {"proficiency_id": "arquearia", "level": "competente"}
    ]
  },
  "inventory": {
    "currency": 150,
    "items": [
      {"item_id": "arco_longo", "quantity": 1, "quality": "Alta", "rarity": "Incomum", "current_durability": 14},
      {"item_id": "moca_de_classe", "quantity": 1, "quality": "Excelente", "rarity": "Épico", "current_durability": -1}
    ]
  },
  "equipped_items": {
    "main_hand": "arco_longo",
    "armor": "colete_pele_reforcado"
  }
}

```
#### 7. Conclusão: Garantindo a Integridade da Experiência
A separação de dados entre o Host (o mundo) e o Client (o personagem) é a fundação arquitetural que torna possível a experiência cooperativa robusta, flexível e narrativamente coerente de  *Eras do Brasil* . Ao atribuir a responsabilidade pelo estado do mundo exclusivamente ao Host e garantir que o personagem do Client seja uma entidade autocontida e portátil, criamos um sistema resiliente. Esta estrutura não apenas previne conflitos de dados e inconsistências na história, mas também capacita os jogadores a desfrutarem de jornadas únicas, seja sozinhos em seus próprios Ecos ou colaborativamente nos mundos de seus amigos, salvaguardando a integridade da jornada de cada jogador e de cada mundo.
