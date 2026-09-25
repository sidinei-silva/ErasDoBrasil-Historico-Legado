### Estrutura de Dados (JSON Schemas) para o Jogo 'Eras do Brasil'
#### 1.0 Introdução: A Arquitetura Data-Driven
Este documento técnico estabelece a estrutura de dados fundamental para o jogo  *Eras do Brasil* . De acordo com a filosofia de desenvolvimento "Alma vs. Lógica" do projeto, este material foca exclusivamente na "Lógica", definindo os schemas JSON que servirão como a espinha dorsal para as entidades centrais do jogo na engine Unity. A adoção de uma arquitetura data-driven é crucial para garantir a modularidade, a escalabilidade e a facilidade de manutenção do projeto, permitindo que a equipe de design e narrativa popule o mundo do jogo de forma eficiente e consistente. A seguir, detalharemos a estrutura da primeira entidade central: a classe de personagem.

--------------------------------------------------------------------------------

#### 2.0 Schema: ClasseDePersonagem
A definição de um schema robusto para a ClasseDePersonagem é um passo estratégico fundamental. Esta estrutura de dados não apenas dita as capacidades mecânicas e o estilo de jogo do personagem, mas também serve como base para o balanceamento sistêmico, a criação de conteúdo futuro (como as evoluções de Tier 2 e 3) e a implementação de mecânicas complexas como a progressão de atributos e a herança de habilidades. Uma estrutura bem definida aqui garante que cada classe tenha uma identidade clara, tanto narrativa quanto funcional.
##### 2.1 Estrutura JSON para ClasseDePersonagem
*Nota: As seguintes estruturas de dados usam literais de string como*  *"integer"*  *e*  *"float"*  *para denotar o tipo de dado esperado para cada campo. Isso é para clareza descritiva; os arquivos JSON reais conterão valores numéricos ou de string brutos.*
```json
{
  "idClasse": "string", // Identificador único e programático, ex: "conquistador_t1"
  "nome": "string", // Nome exibido na interface do jogo, ex: "Conquistador"
  "origem": "string", // Referência à origem cultural: "Colonizador", "Indígena", "Ser Folclórico"
  "tier": "integer", // Nível de especialização da classe (1, 2, ou 3)
  "descricaoNarrativa": "string", // Texto de lore que contextualiza a classe no mundo
  "estiloDeJogo": "string", // Resumo do papel tático para a UI: "Tank", "DPS", "Suporte"
  "atributosRecomendados": ["string"], // Lista dos atributos principais, ex: ["Vigor", "ForcaBruta"]
  "pvBase": "integer", // Pontos de Vida base antes de modificadores de atributo
  "pvPorNivel": "integer", // Pontos de Vida ganhos a cada nível de personagem
  "proficienciaBonus": { // Define a "Proficiência de Vida" que recebe XP bônus
    "idProficiencia": "string", // ID da proficiência, ex: "mineracao"
    "categoria": "string" // Categoria da proficiência, ex: "Coleta", "Refinamento", "Produção"
  },
  "equipamentosPermitidos": { // Restrições de equipamento que definem a identidade da classe
    "armas": ["string"], // Tipos de armas permitidas, ex: ["Espada longa", "Maça"]
    "armaduras": ["string"] // Tipos de armaduras permitidas, ex: ["Pesadas", "Escudos"]
  },
  "habilidadesIniciais": [ // Lista de habilidades desbloqueadas no Tier 1
    {
      "idHabilidade": "string",
      "nome": "string",
      "tipo": "string", // "Ativa" ou "Passiva", crucial para a herança de habilidades
      "descricao": "string"
    }
  ]
}

```
##### 2.2 Análise dos Campos da Estrutura
| Chave | Análise de Propósito e Estrutura |
| ------ | ------ |
| idClasse | **Propósito:**  Define um identificador único e programático para a classe, essencial para referências em outras estruturas de dados (habilidades, itens, missões).  **Estrutura:**  string. |
| nome | **Propósito:**  Armazena o nome da classe exibido na UI. Este campo é utilizado no HUD do jogador, em logs de combate e na geração de diálogos de NPCs, exigindo considerações de localização.  **Estrutura:**  string. |
| origem | **Propósito:**  Vincula a classe a uma das três origens fundamentais (Colonizador, Indígena, Ser Folclórico), determinando o acesso inicial e temas narrativos.  **Estrutura:**  string. |
| tier | **Propósito:**  Representa o nível de especialização (Tier 1, 2 ou 3), controlando a progressão e o desbloqueio de habilidades avançadas.  **Estrutura:**  integer. |
| descricaoNarrativa | **Propósito:**  Contém o texto de lore que contextualiza o papel da classe no mundo, conforme detalhado no "Livro de Classes".  **Estrutura:**  string. |
| estiloDeJogo | **Propósito:**  Fornece um resumo tático para a UI, ajudando o jogador a entender o papel da classe (ex: "Tank", "DPS à distância").  **Estrutura:**  string. |
| atributosRecomendados | **Propósito:**  Lista os atributos principais que otimizam o desempenho da classe, guiando a distribuição de pontos do jogador.  **Estrutura:**  array de string. |
| pvBase e pvPorNivel | **Propósito:**  Define os Pontos de Vida iniciais e a progressão, sendo um fator chave para o balanceamento de classes tank vs. classes frágeis.  **Estrutura:**  integer. |
| proficienciaBonus | **Propósito:**  Identifica a "Proficiência de Vida" que recebe XP bônus. Este campo implementa diretamente a regra de "Bônus em Proficiências de Vida", criando um incentivo tangível para os jogadores alternarem de classe para otimizar suas sessões de crafting e coleta, fortalecendo assim o ciclo de jogabilidade principal entre combate e exploração.  **Estrutura:**  object. |
| equipamentosPermitidos | **Propósito:**  Define as restrições de equipamento, um pilar central para a identidade e balanceamento de cada classe.  **Estrutura:**  object contendo arrays de string. |
| habilidadesIniciais | **Propósito:**  Uma lista de objetos que define as habilidades iniciais. A distinção entre Ativa e Passiva é crucial para o sistema de "Herança de Habilidades", que permite que habilidades ativas sejam mantidas ao trocar de classe.  **Estrutura:**  array de objects. |

As classes definem quem o jogador é, mas sua eficácia é diretamente influenciada pelos equipamentos que utilizam. A estrutura a seguir detalha como esses itens são definidos.

--------------------------------------------------------------------------------

#### 3.0 Schema: Item
Uma estrutura de Item robusta é essencial para um RPG com foco em economia e crafting. O sistema 5x5 de Qualidade e Raridade precisa ser refletido diretamente no schema, pois impacta a mecânica de jogo de forma profunda. A qualidade de um item afeta diretamente a eficácia das habilidades de classe, enquanto a raridade pode desbloquear diálogos e eventos narrativos. Este schema garante que os itens sejam mais do que simples estatísticas, tornando-se elementos centrais no crafting, na economia dinâmica e no balanceamento geral.
##### 3.1 Estrutura JSON para Item
```json
{
  "idItem": "string", // Identificador único e programático, ex: "espada_ferro_mal_forjada"
  "nome": "string", // Nome do item exibido no jogo
  "tipo": "string", // Categoria geral para regras de sistema, ex: "Arma", "Armadura", "Consumível", "Ritual"
  "subtipo": "string", // Categoria específica para filtros e organização, ex: "Espada Longa", "Armadura Leve", "Poção"
  "matriz": { // Objeto que implementa o sistema 5x5 de classificação
    "qualidade": "string", // "Muito Baixa", "Baixa", "Média", "Alta", "Excelente"
    "raridade": "string" // "Comum", "Incomum", "Raro", "Épico", "Lendário"
  },
  "valorBaseUC": "integer", // Valor em Unidades Comerciais, antes de modificadores de economia regional
  "propriedades": [ // Array de efeitos mecânicos do item
    {
      "tipo": "string", // "Dano", "Defesa", "BonusAtributo", "EfeitoEspecial"
      "valor": "string", // Valor do efeito, ex: "1d6", "+2", "Vigor"
      "descricao": "string" // Descrição do efeito para a UI
    }
  ],
  "durabilidade": { // Rastreia o desgaste do item, conectando-se ao sistema de reparos
    "atual": "integer",
    "maxima": "integer"
  },
  "idReceitaCrafting": "string" // ID da receita necessária para criar este item, integrando-o ao sistema de Proficiências
}

```
##### 3.2 Análise dos Campos da Estrutura
| Chave | Análise de Propósito e Estrutura |
| ------ | ------ |
| idItem | **Propósito:**  Define um identificador único e programático para o item, usado em inventários, tabelas de loot e receitas.  **Estrutura:**  string. |
| nome | **Propósito:**  Armazena o nome do item exibido na UI, logs de crafting e diálogos de NPCs, exigindo considerações de localização.  **Estrutura:**  string. |
| tipo / subtipo | **Propósito:**  Classifica o item para regras de sistema (ex: o que pode ser equipado, o que pode ser consumido). tipo é geral, subtipo é específico.  **Estrutura:**  string. |
| matriz | **Propósito:**  Objeto central que implementa o sistema 5x5. A qualidade afeta bônus em habilidades e durabilidade, enquanto a raridade impacta valor e desbloqueios narrativos.  **Estrutura:**  object. |
| valorBaseUC | **Propósito:**  Define o valor em Unidades Comerciais, servindo como input para o sistema de economia regional, que pode aplicar modificadores baseados em escassez ou eventos, conforme descrito em 06_Economia_Itens_e_Crafting.md.  **Estrutura:**  integer. |
| propriedades | **Propósito:**  Um array flexível de objetos que descreve todos os efeitos mecânicos do item (dano, defesa, bônus, etc.), permitindo a criação de itens complexos e únicos.  **Estrutura:**  array de objects. |
| durabilidade | **Propósito:**  Objeto que rastreia o desgaste do item, conectando-se diretamente aos sistemas de reparo e manutenção.  **Estrutura:**  object. |
| idReceitaCrafting | **Propósito:**  Vincula o item a uma receita de crafting, integrando-o ao sistema de Proficiências de Vida.  **Estrutura:**  string. |

Com as estruturas de classes e itens definidas, o foco se volta para as entidades que o jogador enfrentará, cujos desafios e recompensas são moldados por esses mesmos sistemas.

--------------------------------------------------------------------------------

#### 4.0 Schema: Inimigo
A criação de um schema de Inimigo bem estruturado é vital não apenas para definir desafios de combate, mas também para alimentar o sistema de "Mundo Vivo". Esta estrutura permite que entidades hostis interajam com o ambiente, sigam rotinas programadas — como a facção rival "Bandeirantes de Sangue" — e forneçam recompensas coerentes através de tabelas de loot, integrando-as de forma orgânica à economia e ao ciclo de progressão do jogo.
##### 4.1 Estrutura JSON para Inimigo
```json
{
  "idInimigo": "string", // Identificador único, ex: "espirito_corrompido_floresta"
  "nome": "string", // Nome exibido no jogo
  "tipo": "string", // Categoria para sistemas de resistências/fraquezas, ex: "Espiritual", "Humanoide", "Fera"
  "estatisticasBase": {
    "pv": "integer",
    "defesa": "integer",
    "iniciativaMod": "integer", // Bônus ou penalidade na rolagem de iniciativa
    "atributos": { // Atributos que governam suas ações e resistências
      "vigor": "integer",
      "forcaBruta": "integer",
      "astucia": "integer",
      "sabedoriaAncestral": "integer",
      "conhecimento": "integer",
      "presenca": "integer"
    }
  },
  "acoesDeCombate": [ // Lista de ações disponíveis para a IA
    {
      "idAcao": "string",
      "nome": "string",
      "tipo": "string", // "Ataque", "Habilidade", "Debuff", "Defesa"
      "chanceDeUso": "float" // Probabilidade de escolher esta ação (0.0 a 1.0)
    }
  ],
  "tabelaDeLoot": [ // Define as recompensas em itens
    {
      "idItem": "string",
      "quantidade": "string", // Quantidade fixa ou em dado, ex: "1", "1d4"
      "chanceDeDrop": "float" // Probabilidade de dropar o item (0.0 a 1.0)
    }
  ],
  "xpRecompensa": "integer" // Quantidade de XP concedida ao derrotar
}

```
##### 4.2 Análise dos Campos da Estrutura
| Chave | Análise de Propósito e Estrutura |
| ------ | ------ |
| idInimigo | **Propósito:**  Identificador único para uso em eventos de combate, missões e tabelas de spawn de região.  **Estrutura:**  string. |
| nome | **Propósito:**  Nome do inimigo exibido na UI de combate e em logs, exigindo considerações de localização.  **Estrutura:**  string. |
| tipo | **Propósito:**  Define a categoria do inimigo, crucial para sistemas de dano elemental, resistências e fraquezas.  **Estrutura:**  string. |
| estatisticasBase | **Propósito:**  Agrupa todos os valores numéricos de combate (PV, Defesa, Atributos, etc.), centralizando os dados de balanceamento.  **Estrutura:**  object. |
| acoesDeCombate | **Propósito:**  Um array de ações possíveis, permitindo a criação de comportamentos de IA variados. O campo chanceDeUso permite ponderar a frequência de cada ação.  **Estrutura:**  array de objects. |
| tabelaDeLoot | **Propósito:**  Define as recompensas em itens. A estrutura suporta múltiplos drops com probabilidades individuais, alimentando o ciclo de exploração e crafting.  **Estrutura:**  array de objects. |
| xpRecompensa | **Propósito:**  Quantidade de experiência concedida, servindo como um pilar para a progressão do jogador.  **Estrutura:**  integer. |


--------------------------------------------------------------------------------

#### 5.0 Conclusão e Próximos Passos
Os schemas JSON apresentados neste documento — ClasseDePersonagem, Item e Inimigo — formam a base lógica e estrutural para as principais entidades de  *Eras do Brasil* . Ao definir rigorosamente esses contratos de dados, garantimos a consistência, a integração entre sistemas e a facilidade de implementação na engine Unity. Conforme delineado na "Estratégia de Dados e Documentação" do projeto, o próximo passo no pipeline de desenvolvimento é popular esses schemas com os dados específicos de cada classe, item e inimigo planejados para o Ato 1 da campanha, transformando a arquitetura lógica em conteúdo jogável.
