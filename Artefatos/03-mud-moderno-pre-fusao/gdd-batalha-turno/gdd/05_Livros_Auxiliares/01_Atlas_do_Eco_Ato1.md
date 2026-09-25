# 🗺️ Atlas do Eco: A Mata Costeira (Ato 1)

> **Contexto:** A Mata Costeira é a Região 1 do mundo de *Eras do Brasil* (Temporada 1, Nível 1–5). Para a visão macro de todas as regiões, ver [Arquitetura do Mapa](../01_Livro_de_Regras/05B_Arquitetura_do_Mapa.md).

> *"A terra aqui não é muda. O chão lembra de quem pisou nele. O rio sabe quem se afogou. Navegar pela Mata Costeira não é apenas ler um mapa, é ler os humores de um organismo vivo."*
> — Diário de um Cartógrafo Desaparecido

Este livro detalha a geografia, as distâncias, os perigos ambientais e a estrutura de conexões da região do Ato 1. Ele serve como referência absoluta para a equipe narrativa e para o Motor do Jogo (cálculo de tempo de viagem e pathfinding).

---

## 1. O Mapa de Conexões (Topologia)

A região opera em um sistema de **Nós e Caminhos**. Embora a movimentação futura seja livre (Grid), a lógica de conexão segue este diagrama de fluxo.

```mermaid
graph TD
    %% Definição de Estilos
    classDef hub fill:#f9f,stroke:#333,stroke-width:4px;
    classDef danger fill:#f96,stroke:#333,stroke-width:2px;
    classDef water fill:#9cf,stroke:#333,stroke-width:2px;
    classDef forest fill:#9f9,stroke:#333,stroke-width:2px;
    classDef ruin fill:#ccc,stroke:#333,stroke-width:2px;

    %% Nós Principais
    Vila[🏠 Vila de São Tomé - HUB]:::hub
    Rio[🌊 Rio das Marés]:::water
    Mina[⛏️ A Mina de Ouro]:::danger
    Floresta[🌲 Floresta do Norte]:::forest
    Toca[🐺 Toca da Fera]:::forest
    Acampamento[⚔️ Acampamento Rival]:::danger
    Pico[🏔️ Pico da Neblina]:::ruin
    Ruinas[🔥 Ruínas Queimadas]:::ruin
    Ruptura[🌀 A RUPTURA - Final]:::danger

    %% Conexões e Custos (Ida)
    Vila -- "Estrada Velha (~10 min)" --> Rio
    Rio -- "Maré Baixa (~12 min)" --> Mina

    Vila -- "Mata Fechada (~25 min)" --> Floresta
    Floresta -- "Rastro (~12 min)" --> Toca
    Floresta -- "Trilha Oculta (~20 min)" --> Acampamento

    Floresta -- "Zona de Distorção (~50 min)" --> Ruptura

    Vila -- "Subida Íngreme (~45 min)" --> Pico

    Vila -- "Pântano (~40 min)" --> Ruinas
    
    %% Conexões Secretas (Atalhos)
    Rio -. "Túnel Submerso (Requer Item)" .-> Ruptura
```

---

## 1B. Tabela de Zonas — Nível e Papel

A Mata Costeira contém 9 zonas. A tabela abaixo resume o range de nível, mobs principais e papel de cada zona na experiência do jogador.

| Zona | Nível | Mobs Principais | Papel |
|------|-------|-----------------|-------|
| Vila de São Tomé | 0 (segura) | Nenhum | Hub, serviços, descanso |
| Rio das Marés | 1–2 | Jacarés, peixes agressivos | Recursos de água, ciclo de maré |
| Floresta do Norte | 1–3 | Lobos, espíritos menores | Exploração principal, madeira |
| Toca da Fera | 3–4 | Onça Pintada (mini-boss) | Desafio intermediário |
| Mina de Ouro | 2–4 | Bandeirantes hostis | Recursos minerais |
| Acampamento Bandeirante | 3–5 | Capitão Bandeirante (boss) | Combate de facção |
| Pico da Neblina | 3–5 | Espíritos ancestrais | Recursos raros, fadiga |
| Ruínas Queimadas | 4–5 | Espíritos corrompidos | Terror, dano espiritual |
| A Ruptura | 5 (boss) | Guardião da Fenda | Clímax da temporada |

> **Migração de mobs:** Mobs que atingem o cap de nível da zona migram para zonas de nível mais alto dentro da Mata Costeira. Ao atingir o cap da região (nível 5), migram para o Sertão Distorcido quando este for aberto (Temporada 2). Ver §8.10 do Cap. 8.

---

## 2. Regras de Terreno e Biomas

Cada zona possui modificadores globais que afetam tanto a **Exploração** (tempo de viagem) quanto o **Combate** (Buffs/Debuffs).

### 🏠 Zona Central: Vila de São Tomé
O último bastião de "normalidade".
* **Tipo de Terreno:** Urbano / Seguro.
* **Custo de Movimento:** Rápido (~5 min reais).
* **Regra de Descanso:** Descanso Longo aqui leva apenas ~10 min reais (bônus de conforto) e recupera 100% de Vida/Recursos.
* **Serviços:**
    * *Ferreiro:* Repara itens e vende armas básicas.
    * *Taverna:* Hub de "Fofoca" (Info sobre NPCs).
    * *Capela:* Remove maldições leves (Custo em Ouro).

### 🌲 Zona Norte: Floresta do Norte
Uma mata densa, antiga e vibrante, onde a luz do sol mal toca o chão.
* **Tipo de Terreno:** Mata Densa.
* **Custo de Movimento:** Moderado (~10 min reais).
* **Regra de Combate (Cobertura Natural):** Todos os personagens (aliados e inimigos) ganham +1 de Defesa contra ataques à distância se estiverem a mais de 5 metros do atacante.
* **Variável de Save (Procedural):**
    * A localização exata da *Toca da Fera* varia (Norte, Nordeste ou Noroeste da zona).

### 🌊 Zona Leste: Rio das Marés
Um rio largo que sofre influência de marés sobrenaturais.
* **Tipo de Terreno:** Água / Lama.
* **Custo de Movimento:** Rápido (Margem) / Impossível (Água Alta).
* **Ciclo da Maré (Acesso à Mina):**
    A maré opera em ciclos baseados no relógio do jogo. A Mina só é acessível na Maré Baixa.
    * **Manhã:** Baixa (Janela Inicial).
    * **Tarde:** Alta (Bloqueado).
    * **Noite:** Baixa (Segunda Chance).
    * **Madrugada:** Alta (Bloqueado).
    * **Nota:** Tentar entrar na Maré Alta exige teste de Natação (Vigor CD 18) e causa dano de afogamento.

### 🏔️ Zona Oeste: Pico da Neblina
Uma montanha sagrada envolta em nuvens que sussurram.
* **Tipo de Terreno:** Montanha / Vertical.
* **Custo de Movimento:** Longo (~15 min reais, Subida) / Rápido (~5 min, Descida).
* **Regra de Exaustão:** A cada período do dia passado aqui, o jogador deve fazer um teste de Vigor (CD 12) ou ganha 1 nível de Fadiga (–1 em todas as rolagens).
* **Regra de Combate (Ventos):** Ataques à distância têm Desvantagem. Empurrões jogam o alvo 2 metros a mais.

### 🔥 Zona Sul: Ruínas Queimadas
O local de um massacre antigo. O chão é cinza e o ar cheira a fumaça eterna.
* **Tipo de Terreno:** Terra Arrasada / Pântano.
* **Custo de Movimento:** Moderado (~10 min reais).
* **Regra de Terror:** Inimigos aqui são do tipo *Espiritual*. Personagens que falharem em um teste de **Resistência contra Medo (Presença CD 13)** sofrem alucinações (Textos falsos na interface ou sons de passos inexistentes).

---

## 3. A Rota dos Bandeirantes (Facção NPC Antagonista)

Os **Bandeirantes de Sangue** são uma facção NPC controlada pelo `StoryManager` por temporada. Eles não esperam pelo jogador — avançam pelo mapa conforme a temporada progride.

* **Ponto de Partida:** Acampamento Secreto (Zona Norte).
* **Objetivo:** Chegar à Ruptura (Epicentro).
* **Velocidade:** Avançam conforme a fase da temporada (ver [Ato 1](../03_Enredo_e_Mundo/01_Ato_1_A_Primeira_Ruptura.md)).
* **Checkpoints (Momentos de Tensão):**
    1.  **Fase 1 (PRE_EVENT):** Dominam a entrada da Floresta Norte. (Jogadores encontram patrulhas hostis lá).
    2.  **Fase 2 (EVENT_ACTIVE):** Estabelecem um posto avançado na "Fronteira da Distorção".
    3.  **Fase 3 (EVENT_ACTIVE final):** Iniciam o ritual de abertura forçada na Ruptura. (O Boss começa a ficar "Ascendido").

> **Interação:** Jogadores podem enfrentá-los em combate, sabotar seus postos ou tentar contorná-los (com classes como Explorador de Terras ou Arqueiro Selvagem). Sabotagem bem-sucedida atrasa o avanço dos Bandeirantes para a próxima fase.

---

## 4. Distribuição de Recursos (Loot Table Regional)

Para garantir que o "Completionista" tenha motivos para visitar tudo, os recursos são segregados por zona.

| Recurso | Onde Encontrar (Principal) | Uso Principal |
| :--- | :--- | :--- |
| **Madeira de Ferro** | Floresta do Norte | Crafting de Armas e Escudos Leves |
| **Erva-Lua** | Rio das Marés (Noite) | Poções de recuperação espiritual e Rituais |
| **Minério de Sangue** | Pico da Neblina (Cavernas) | Melhoria de Armas (Dano +1) |
| **Cinzas Espirituais** | Ruínas Queimadas | Itens Mágicos e Proteção contra Maldição |
| **Comida/Suprimentos** | Vila (Compra) ou Rio (Pesca) | Recuperação de PV em descanso |

---

## 5. Variáveis Procedurais (O "Tempero" do Save)

Embora o mapa seja fixo (A Vila é sempre no centro), o conteúdo dos nós varia a cada Save Game (`Seed`).

| Elemento | Variação Possível |
| :--- | :--- |
| **Baús de Tesouro** | Existem 10 locais possíveis para baús no mapa. Apenas 5 spawnarão no Save atual. |
| **Inimigos Especiais** | O "Lobo Alfa" pode estar na Floresta ou rondando o sopé do Pico. O jogador precisa rastrear. |
| **Rotina do Pajé** | *Save A:* Medita na Cachoeira (Manhã). *Save B:* Medita na Caverna (Manhã). |
| **Clima Inicial** | Pode começar com "Chuva" (Dificulta fogo, facilita furtividade) ou "Seca" (Risco de incêndio, movimento melhor). |