# Dados de Jogo Iniciais para Eras do Brasil - Ato 1

Este documento serve como a fonte de dados primária, no formato JSON, para a instanciação de entidades essenciais do jogo no Ato 1 de "Eras do Brasil". Estes dados foram rigorosamente projetados para serem consumidos diretamente pela engine do jogo, seguindo os schemas estruturais definidos na documentação técnica do projeto.

## 1. Itens Iniciais Variados

Fornecer aos jogadores um conjunto inicial de itens variados é uma decisão estratégica crucial para a introdução ao mundo do jogo. A seleção de uma arma, uma armadura, uma ferramenta, um consumível e um recurso estabelece, desde o início da jornada, os ciclos de jogabilidade fundamentais: combate, defesa, coleta e aprimoramento. Essa abordagem equipa o jogador não apenas com ferramentas para sobreviver, mas também o imerge organicamente nas mecânicas centrais que definirão sua progressão.

### 1.1. Arma: Espada de Ferro (Qualidade Média)

```json
{
  "itemId": "arma_espada_ferro_01",
  "name": "Espada de Ferro",
  "type": "Arma",
  "subtype": "Espada Longa",
  "description": "Uma espada de ferro padrão, confiável em combate. Um item comum entre os colonizadores.",
  "matriz": {
    "qualidade": "Média",
    "raridade": "Comum"
  },
  "baseUcValue": 25,
  "properties": [
    {
      "type": "dano",
      "value": "1d6",
      "damageType": "Corte"
    },
    {
      "type": "alcance",
      "value": "1 metro"
    }
  ],
  "durability": {
    "atual": 12,
    "max": 12
  },
  "craftingRecipeId": "receita_ferraria_espada_ferro",
  "stackable": false,
  "maxStack": 1
}
```

_Design Note: Esta espada serve como a linha de base para o combate corpo a corpo. Sua qualidade 'Média' e dano '1d6' são balanceados para serem eficazes contra os inimigos iniciais, mas sem ofuscar as recompensas do sistema de Ferraria._

### 1.2. Armadura: Colete de Couro (Qualidade Baixa)

```json
{
  "itemId": "armadura_colete_couro_01",
  "name": "Colete de Couro",
  "type": "Armadura",
  "subtype": "Leve",
  "description": "Um colete feito de couro endurecido, oferecendo proteção básica sem restringir o movimento.",
  "matriz": {
    "qualidade": "Baixa",
    "raridade": "Comum"
  },
  "baseUcValue": 15,
  "properties": [
    {
      "type": "defesa",
      "value": 1
    }
  ],
  "durability": {
    "atual": 8,
    "max": 8
  },
  "craftingRecipeId": "receita_coureira_colete_simples",
  "stackable": false,
  "maxStack": 1
}
```

_Design Note: A qualidade 'Baixa' e o valor mínimo de defesa são intencionais. Este item serve como uma linha de base, criando um incentivo imediato e tangível para o jogador se engajar com a proficiência de 'Coureira' em busca de melhorias._

### 1.3. Ferramenta: Picareta de Mineração

```json
{
  "itemId": "ferramenta_picareta_01",
  "name": "Picareta de Mineração",
  "type": "Ferramenta",
  "subtype": "Mineração",
  "description": "Uma ferramenta robusta projetada para quebrar rochas e extrair minérios.",
  "matriz": {
    "qualidade": "Média",
    "raridade": "Comum"
  },
  "baseUcValue": 10,
  "properties": [
    {
      "type": "bonusProficiencia",
      "proficiency": "Mineração",
      "value": 1
    }
  ],
  "durability": {
    "atual": 12,
    "max": 12
  },
  "craftingRecipeId": "receita_ferraria_picareta",
  "stackable": false,
  "maxStack": 1
}
```

_Design Note: Introduz o ciclo de jogabilidade de coleta de recursos. O bônus de proficiência de +1 em 'Mineração' oferece um benefício imediato e tangível, incentivando o jogador a interagir com o sistema de Proficiências de Vida desde o início._

### 1.4. Consumível: Poção de Erva-Lua

```json
{
  "itemId": "consumivel_pocao_ervalua_01",
  "name": "Poção de Erva-Lua",
  "type": "Consumível",
  "subtype": "Poção",
  "description": "Uma poção que brilha suavemente, feita com Erva-Lua. Restaura a conexão espiritual.",
  "matriz": {
    "qualidade": "Média",
    "raridade": "Incomum"
  },
  "baseUcValue": 30,
  "properties": [
    {
      "type": "efeito",
      "name": "Reduz Fadiga Espiritual",
      "value": "1 nível"
    },
    {
      "type": "uso",
      "value": "Ação Principal"
    }
  ],
  "durability": null,
  "craftingRecipeId": "receita_alquimia_pocao_fadiga_espiritual",
  "stackable": true,
  "maxStack": 5
}
```

_Design Note: Este consumível estabelece a mecânica de gerenciamento de Fadiga Espiritual e a importância da 'Alquimia'. Sua raridade 'Incomum' e o vínculo com o recurso noturno 'Erva-Lua' ensinam ao jogador que a exploração contextual (hora do dia) é recompensada._

### 1.5. Recurso: Minério de Sangue

```json
{
  "itemId": "recurso_minerio_sangue_01",
  "name": "Minério de Sangue",
  "type": "Recurso",
  "subtype": "Minério",
  "description": "Um minério raro encontrado em veios profundos, que pulsa com uma tênue luz vermelha. Usado para aprimorar armas.",
  "matriz": {
    "qualidade": "N/A",
    "raridade": "Raro"
  },
  "baseUcValue": 50,
  "properties": [
    {
      "type": "componenteCrafting",
      "use": "Melhoria de Armas (Dano +1)"
    }
  ],
  "durability": null,
  "craftingRecipeId": null,
  "stackable": true,
  "maxStack": 10
}
```

_Design Note: Como um recurso 'Raro' encontrado em uma zona específica e desafiadora (Pico da Neblina), este item introduz o ciclo central de exploração de risco vs. recompensa e impulsiona os jogadores a se engajarem com os sistemas de aprimoramento de armas precocemente._

Com um inventário inicial estabelecido, torna-se essencial definir os adversários que os jogadores enfrentarão, testando a eficácia e a utilidade desses novos itens em cenários de risco e recompensa.

## 2. Inimigos do Ato 1

A curva de dificuldade para o Ato 1 não é estática; ela é projetada para ser um sistema dinâmico que responde ao avanço do jogador. Os inimigos a seguir não são apenas obstáculos passivos, mas componentes de um ecossistema vivo — e participam do sistema de **Inimigos Evolutivos** (ADR-009), onde inimigos que derrotam jogadores ganham XP e evoluem de Normal → Veterano → Alfa → Lenda. O Espírito Menor e a Onça Pintada representam as ameaças ambientais da Mata Costeira, testando as habilidades de combate fundamentais. O Capitão Bandeirante é o líder da facção NPC antagonista "Bandeirantes de Sangue" — uma facção controlada pelo `StoryManager` por temporada, que avança pelo mapa conforme a temporada progride, criando tensão e urgência na campanha principal.

### 2.1. Inimigo Fácil: Espírito Menor

```json
{
  "enemyId": "inimigo_espirito_menor_01",
  "name": "Espírito Menor",
  "type": "Espiritual",
  "baseStats": {
    "level": 1,
    "pv": 8,
    "defense": 11,
    "attributes": {
      "vigor": 2,
      "strength": 1,
      "cunning": 3,
      "wisdom": 4,
      "knowledge": 2,
      "presence": 3
    }
  },
  "combatActions": [
    {
      "name": "Toque Gélido",
      "type": "Ataque",
      "damage": "1d4",
      "damageType": "Espiritual",
      "usageChance": 1.0
    }
  ],
  "lootTable": [
    {
      "itemId": "recurso_cinzas_espirituais_01",
      "quantity": "1d2",
      "dropChance": 0.5
    }
  ],
  "xpReward": 10
}
```

### 2.2. Inimigo Médio: Onça Pintada

```json
{
  "enemyId": "inimigo_onca_pintada_01",
  "name": "Onça Pintada",
  "type": "Besta",
  "baseStats": {
    "level": 2,
    "pv": 22,
    "defense": 13,
    "attributes": {
      "vigor": 4,
      "strength": 4,
      "cunning": 5,
      "wisdom": 3,
      "knowledge": 1,
      "presence": 4
    }
  },
  "combatActions": [
    {
      "name": "Mordida",
      "type": "Ataque",
      "damage": "1d6+1",
      "damageType": "Perfurante",
      "usageChance": 0.7
    },
    {
      "name": "Bote Veloz",
      "type": "Habilidade",
      "damage": "1d8",
      "damageType": "Perfurante",
      "description": "A onça avança rapidamente. O alvo deve passar em um teste de Astúcia (CD 12) ou fica Derrubado.",
      "usageChance": 0.3
    }
  ],
  "lootTable": [
    {
      "itemId": "recurso_pele_onca_01",
      "quantity": 1,
      "dropChance": 0.6
    },
    {
      "itemId": "recurso_presa_onca_01",
      "quantity": "1d2",
      "dropChance": 0.3
    }
  ],
  "xpReward": 25
}
```

### 2.3. Chefe/Rival: Capitão Bandeirante

```json
{
  "enemyId": "inimigo_capitao_bandeirante_01",
  "name": "Capitão Bandeirante",
  "type": "Humanoide",
  "baseStats": {
    "level": 3,
    "pv": 45,
    "defense": 14,
    "attributes": {
      "vigor": 4,
      "strength": 4,
      "cunning": 4,
      "wisdom": 3,
      "knowledge": 3,
      "presence": 5
    }
  },
  "combatActions": [
    {
      "name": "Golpe de Espada",
      "type": "Ataque",
      "damage": "1d8+1",
      "damageType": "Corte",
      "usageChance": 0.6
    },
    {
      "name": "Tiro de Mosquete",
      "type": "Habilidade",
      "damage": "1d10+2",
      "damageType": "Perfurante",
      "description": "Requer 1 turno para recarregar após o uso.",
      "usageChance": 0.2
    },
    {
      "name": "Ordem de Batalha",
      "type": "Habilidade",
      "description": "Concede +1 de dano para todos os aliados Bandeirantes por 2 turnos.",
      "usageChance": 0.2
    }
  ],
  "lootTable": [
    {
      "itemId": "moeda_classe_colonizador_01",
      "quantity": 1,
      "dropChance": 1.0
    },
    {
      "itemId": "arma_mosquete_enferrujado_01",
      "quantity": 1,
      "dropChance": 0.25
    },
    {
      "itemId": "moeda_uc_pilha_media",
      "quantity": "1d20+10",
      "dropChance": 1.0
    }
  ],
  "xpReward": 75
}
```

Para enfrentar esses desafios, o jogador precisa de mais do que apenas itens; ele precisa de uma identidade, um conjunto de habilidades e um propósito tático. É aqui que as classes de personagem entram em jogo, definindo o estilo e a abordagem do jogador no mundo de Eras do Brasil.

## 3. Classe Completa: Guerreiro Tribal

No ecossistema do jogo, a classe "Guerreiro Tribal" representa a linha de frente indomável da origem Indígena. Seu papel tático é o de um **Tank ofensivo**, um protetor que não apenas absorve dano, mas o devolve com ferocidade, servindo como a muralha viva que protege o clã e o território. É importante notar que esta classe, como todas as outras, integra o sistema do **"Dom da Revivência"**, permitindo que os jogadores desbloqueiem e alternem entre diferentes arquétipos para adaptar sua estratégia aos desafios do mundo.

```json
{
  "classId": "indigena_guerreiro_tribal_t1",
  "name": "Guerreiro Tribal",
  "origin": "Indígena",
  "tier": 1,
  "narrativeDescription": "O Guerreiro Tribal é um defensor da terra, da floresta e do seu povo. Traz a força do clã em cada golpe e o espírito ancestral em cada movimento. Forjado nas lutas contra invasores e na proteção de sua comunidade, ele é símbolo de bravura, honra e respeito à ancestralidade.",
  "playstyle": "Tank ofensivo, agressivo e protetor da linha de frente",
  "recommendedAttributes": [
    "Vigor",
    "Força Bruta"
  ],
  "baseHp": 14,
  "hpPerLevel": 7,
  "proficiencyBonus": {
    "proficiency": "Caça",
    "bonusXp": 1
  },
  "allowedEquipment": {
    "weapons": [
      "Lança",
      "Clava"
    ],
    "armors": [
      "Médias"
    ]
  },
  "startingSkills": [
    {
      "name": "Investida Tribal",
      "type": "Ativa",
      "description": "Avança até 3 metros e realiza um ataque corpo a corpo com vantagem. Recarga: 2 turnos. Condição: Requer linha reta livre e arma corpo a corpo equipada."
    },
    {
      "name": "Espírito do Clã",
      "type": "Passiva",
      "description": "Se estiver com menos de 50% dos PV, recebe +1 em ataques corpo a corpo. Condição: Ativa quando os PV estão abaixo da metade."
    }
  ]
}
```

Conclusão: Os blocos de dados JSON neste documento estão finalizados e prontos para integração pela engine. Todos os objetos foram validados contra os schemas estruturais definidos em `01_Schemas_Estruturais.md` para garantir a integridade dos dados e a funcionalidade sistêmica. Estes artefatos constituem a base de conteúdo para a instanciação de entidades no Ato 1.