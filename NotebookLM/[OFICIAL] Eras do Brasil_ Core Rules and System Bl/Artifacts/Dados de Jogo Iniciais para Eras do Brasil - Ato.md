### Dados de Jogo Iniciais para Eras do Brasil - Ato 1
Este documento serve como a fonte de dados primária, no formato JSON, para a instanciação de entidades essenciais do jogo no Ato 1 de "Eras do Brasil". Estes dados foram rigorosamente projetados para serem consumidos diretamente pela engine do jogo, seguindo os schemas estruturais definidos na documentação técnica do projeto.
#### 1. Itens Iniciais Variados
Fornecer aos jogadores um conjunto inicial de itens variados é uma decisão estratégica crucial para a introdução ao mundo do jogo. A seleção de uma arma, uma armadura, uma ferramenta, um consumível e um recurso estabelece, desde o início da jornada, os ciclos de jogabilidade fundamentais: combate, defesa, coleta e aprimoramento. Essa abordagem equipa o jogador não apenas com ferramentas para sobreviver, mas também o imerge organicamente nas mecânicas centrais que definirão sua progressão.
##### 1.1. Arma: Espada de Ferro (Qualidade Média)
```json
{
  "idItem": "arma_espada_ferro_01",
  "nome": "Espada de Ferro",
  "tipo": "Arma",
  "subtipo": "Espada Longa",
  "descricao": "Uma espada de ferro padrão, confiável em combate. Um item comum entre os colonizadores.",
  "matriz": {
    "qualidade": "Média",
    "raridade": "Comum"
  },
  "valorBaseUC": 25,
  "propriedades": [
    {
      "tipo": "dano",
      "valor": "1d6",
      "tipoDano": "Corte"
    },
    {
      "tipo": "alcance",
      "valor": "1 metro"
    }
  ],
  "durabilidade": {
    "atual": 12,
    "maxima": 12
  },
  "idReceitaCrafting": "receita_ferraria_espada_ferro",
  "empilhavel": false,
  "maxPilha": 1
}

```
*Design Note: Esta espada serve como a linha de base para o combate corpo a corpo. Sua qualidade 'Média' e dano '1d6' são balanceados para serem eficazes contra os inimigos iniciais, mas sem ofuscar as recompensas do sistema de Ferraria.*
##### 1.2. Armadura: Colete de Couro (Qualidade Baixa)
```json
{
  "idItem": "armadura_colete_couro_01",
  "nome": "Colete de Couro",
  "tipo": "Armadura",
  "subtipo": "Leve",
  "descricao": "Um colete feito de couro endurecido, oferecendo proteção básica sem restringir o movimento.",
  "matriz": {
    "qualidade": "Baixa",
    "raridade": "Comum"
  },
  "valorBaseUC": 15,
  "propriedades": [
    {
      "tipo": "defesa",
      "valor": 1
    }
  ],
  "durabilidade": {
    "atual": 8,
    "maxima": 8
  },
  "idReceitaCrafting": "receita_coureira_colete_simples",
  "empilhavel": false,
  "maxPilha": 1
}

```
*Design Note: A qualidade 'Baixa' e o valor mínimo de defesa são intencionais. Este item serve como uma linha de base, criando um incentivo imediato e tangível para o jogador se engajar com a proficiência de 'Coureira' em busca de melhorias.*
##### 1.3. Ferramenta: Picareta de Mineração
```json
{
  "idItem": "ferramenta_picareta_01",
  "nome": "Picareta de Mineração",
  "tipo": "Ferramenta",
  "subtipo": "Mineração",
  "descricao": "Uma ferramenta robusta projetada para quebrar rochas e extrair minérios.",
  "matriz": {
    "qualidade": "Média",
    "raridade": "Comum"
  },
  "valorBaseUC": 10,
  "propriedades": [
    {
      "tipo": "bonusProficiencia",
      "proficiencia": "Mineração",
      "valor": 1
    }
  ],
  "durabilidade": {
    "atual": 12,
    "maxima": 12
  },
  "idReceitaCrafting": "receita_ferraria_picareta",
  "empilhavel": false,
  "maxPilha": 1
}

```
*Design Note: Introduz o ciclo de jogabilidade de coleta de recursos. O bônus de proficiência de +1 em 'Mineração' oferece um benefício imediato e tangível, incentivando o jogador a interagir com o sistema de Proficiências de Vida desde o início.*
##### 1.4. Consumível: Poção de Erva-Lua
```json
{
  "idItem": "consumivel_pocao_ervalua_01",
  "nome": "Poção de Erva-Lua",
  "tipo": "Consumível",
  "subtipo": "Poção",
  "descricao": "Uma poção que brilha suavemente, feita com Erva-Lua. Restaura a conexão espiritual.",
  "matriz": {
    "qualidade": "Média",
    "raridade": "Incomum"
  },
  "valorBaseUC": 30,
  "propriedades": [
    {
      "tipo": "efeito",
      "nome": "Restaura Mana",
      "valor": "2d4+2"
    },
    {
      "tipo": "uso",
      "valor": "Ação Principal"
    }
  ],
  "durabilidade": null,
  "idReceitaCrafting": "receita_alquimia_pocao_mana",
  "empilhavel": true,
  "maxPilha": 5
}

```
*Design Note: Este consumível estabelece a mecânica de gerenciamento de mana e a importância da 'Alquimia'. Sua raridade 'Incomum' e o vínculo com o recurso noturno 'Erva-Lua' ensinam ao jogador que a exploração contextual (hora do dia) é recompensada.*
##### 1.5. Recurso: Minério de Sangue
```json
{
  "idItem": "recurso_minerio_sangue_01",
  "nome": "Minério de Sangue",
  "tipo": "Recurso",
  "subtipo": "Minério",
  "descricao": "Um minério raro encontrado em veios profundos, que pulsa com uma tênue luz vermelha. Usado para aprimorar armas.",
  "matriz": {
    "qualidade": "N/A",
    "raridade": "Raro"
  },
  "valorBaseUC": 50,
  "propriedades": [
    {
      "tipo": "componenteCrafting",
      "uso": "Melhoria de Armas (Dano +1)"
    }
  ],
  "durabilidade": null,
  "idReceitaCrafting": null,
  "empilhavel": true,
  "maxPilha": 10
}

```
*Design Note: Como um recurso 'Raro' encontrado em uma zona específica e desafiadora (Pico da Neblina), este item introduz o ciclo central de exploração de risco vs. recompensa e impulsiona os jogadores a se engajarem com os sistemas de aprimoramento de armas precocemente.*
Com um inventário inicial estabelecido, torna-se essencial definir os adversários que os jogadores enfrentarão, testando a eficácia e a utilidade desses novos itens em cenários de risco e recompensa.
#### 2. Inimigos do Ato 1
A curva de dificuldade para o Ato 1 não é estática; ela é projetada para ser um sistema dinâmico que responde ao avanço do jogador. Os inimigos a seguir não são apenas obstáculos passivos, mas componentes de um ecossistema vivo. O Espírito Menor e a Onça Pintada representam as ameaças ambientais da Mata Costeira, testando as habilidades de combate fundamentais. O Capitão Bandeirante, no entanto, é o líder da facção rival "Bandeirantes de Sangue". Este grupo não espera pelo jogador; ele avança ativamente pelo mapa a cada  **"Tick"**  global, criando uma "Corrida contra a Sombra" para alcançar os objetivos da trama. Este design integra os encontros de combate diretamente à mecânica central de urgência do Ato 1.
##### 2.1. Inimigo Fácil: Espírito Menor
```json
{
  "idInimigo": "inimigo_espirito_menor_01",
  "nome": "Espírito Menor",
  "tipo": "Espiritual",
  "estatisticasBase": {
    "nivel": 1,
    "pv": 8,
    "defesa": 11,
    "atributos": {
      "vigor": 2,
      "forca": 1,
      "astucia": 3,
      "sabedoria": 4,
      "conhecimento": 2,
      "presenca": 3
    }
  },
  "acoesDeCombate": [
    {
      "nome": "Toque Gélido",
      "tipo": "Ataque",
      "dano": "1d4",
      "tipoDano": "Espiritual",
      "chanceDeUso": 1.0
    }
  ],
  "tabelaDeLoot": [
    {
      "idItem": "recurso_cinzas_espirituais_01",
      "quantidade": "1d2",
      "chanceDeDrop": 0.5
    }
  ],
  "xpRecompensa": 10
}

```
##### 2.2. Inimigo Médio: Onça Pintada
```json
{
  "idInimigo": "inimigo_onca_pintada_01",
  "nome": "Onça Pintada",
  "tipo": "Besta",
  "estatisticasBase": {
    "nivel": 2,
    "pv": 22,
    "defesa": 13,
    "atributos": {
      "vigor": 4,
      "forca": 4,
      "astucia": 5,
      "sabedoria": 3,
      "conhecimento": 1,
      "presenca": 4
    }
  },
  "acoesDeCombate": [
    {
      "nome": "Mordida",
      "tipo": "Ataque",
      "dano": "1d6+1",
      "tipoDano": "Perfurante",
      "chanceDeUso": 0.7
    },
    {
      "nome": "Bote Veloz",
      "tipo": "Habilidade",
      "dano": "1d8",
      "tipoDano": "Perfurante",
      "descricao": "A onça avança rapidamente. O alvo deve passar em um teste de Astúcia (CD 12) ou fica Derrubado.",
      "chanceDeUso": 0.3
    }
  ],
  "tabelaDeLoot": [
    {
      "idItem": "recurso_pele_onca_01",
      "quantidade": 1,
      "chanceDeDrop": 0.6
    },
    {
      "idItem": "recurso_presa_onca_01",
      "quantidade": "1d2",
      "chanceDeDrop": 0.3
    }
  ],
  "xpRecompensa": 25
}

```
##### 2.3. Chefe/Rival: Capitão Bandeirante
```json
{
  "idInimigo": "inimigo_capitao_bandeirante_01",
  "nome": "Capitão Bandeirante",
  "tipo": "Humanoide",
  "estatisticasBase": {
    "nivel": 3,
    "pv": 45,
    "defesa": 14,
    "atributos": {
      "vigor": 4,
      "forca": 4,
      "astucia": 4,
      "sabedoria": 3,
      "conhecimento": 3,
      "presenca": 5
    }
  },
  "acoesDeCombate": [
    {
      "nome": "Golpe de Espada",
      "tipo": "Ataque",
      "dano": "1d8+1",
      "tipoDano": "Corte",
      "chanceDeUso": 0.6
    },
    {
      "nome": "Tiro de Mosquete",
      "tipo": "Habilidade",
      "dano": "1d10+2",
      "tipoDano": "Perfurante",
      "descricao": "Requer 1 turno para recarregar após o uso.",
      "chanceDeUso": 0.2
    },
    {
      "nome": "Ordem de Batalha",
      "tipo": "Habilidade",
      "descricao": "Concede +1 de dano para todos os aliados Bandeirantes por 2 turnos.",
      "chanceDeUso": 0.2
    }
  ],
  "tabelaDeLoot": [
    {
      "idItem": "moeda_classe_colonizador_01",
      "quantidade": 1,
      "chanceDeDrop": 1.0
    },
    {
      "idItem": "arma_mosquete_enferrujado_01",
      "quantidade": 1,
      "chanceDeDrop": 0.25
    },
    {
      "idItem": "moeda_uc_pilha_media",
      "quantidade": "1d20+10",
      "chanceDeDrop": 1.0
    }
  ],
  "xpRecompensa": 75
}

```
Para enfrentar esses desafios, o jogador precisa de mais do que apenas itens; ele precisa de uma identidade, um conjunto de habilidades e um propósito tático. É aqui que as classes de personagem entram em jogo, definindo o estilo e a abordagem do jogador no mundo de Eras do Brasil.
#### 3. Classe Completa: Guerreiro Tribal
No ecossistema do jogo, a classe "Guerreiro Tribal" representa a linha de frente indomável da origem Indígena. Seu papel tático é o de um  **Tank ofensivo** , um protetor que não apenas absorve dano, mas o devolve com ferocidade, servindo como a muralha viva que protege o clã e o território. É importante notar que esta classe, como todas as outras, integra o sistema do  **"Dom da Revivência"** , permitindo que os jogadores desbloqueiem e alternem entre diferentes arquétipos para adaptar sua estratégia aos desafios do mundo.
```json
{
  "idClasse": "indigena_guerreiro_tribal_t1",
  "nome": "Guerreiro Tribal",
  "origem": "Indígena",
  "tier": 1,
  "descricaoNarrativa": "O Guerreiro Tribal é um defensor da terra, da floresta e do seu povo. Traz a força do clã em cada golpe e o espírito ancestral em cada movimento. Forjado nas lutas contra invasores e na proteção de sua comunidade, ele é símbolo de bravura, honra e respeito à ancestralidade.",
  "estiloDeJogo": "Tank ofensivo, agressivo e protetor da linha de frente",
  "atributosRecomendados": [
    "Vigor",
    "Força Bruta"
  ],
  "pvBase": 14,
  "pvPorNivel": 7,
  "proficienciaBonus": {
    "proficiencia": "Caça",
    "bonusXP": 1
  },
  "equipamentosPermitidos": {
    "armas": [
      "Lança",
      "Clava"
    ],
    "armaduras": [
      "Médias"
    ]
  },
  "habilidadesIniciais": [
    {
      "nome": "Investida Tribal",
      "tipo": "Ativa",
      "descricao": "Avança até 3 metros e realiza um ataque corpo a corpo com vantagem. Recarga: 2 turnos. Condição: Requer linha reta livre e arma corpo a corpo equipada."
    },
    {
      "nome": "Espírito do Clã",
      "tipo": "Passiva",
      "descricao": "Se estiver com menos de 50% dos PV, recebe +1 em ataques corpo a corpo. Condição: Ativa quando os PV estão abaixo da metade."
    }
  ]
}

```
Conclusão: Os blocos de dados JSON neste documento estão finalizados e prontos para integração pela engine. Todos os objetos foram validados contra os schemas estruturais definidos em 01_Schemas_Estruturais.md para garantir a integridade dos dados e a funcionalidade sistêmica. Estes artefatos constituem a base de conteúdo para a instanciação de entidades no Ato 1.
