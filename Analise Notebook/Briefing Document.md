# Briefing Document: Eras do Brasil RPG Project

## Executive Summary

This document synthesizes the core concepts, development strategy, and detailed mechanics of the "Eras do Brasil" project, a role-playing game set in a historical-fantastical version of Brazil. The project's central ambition is to create a rich, persistent world that begins as a tabletop RPG (TTRPG) for system validation and is designed to evolve into a sophisticated digital game.

The game's narrative is anchored by the mystical concepts of the **"Raiz do Mundo" (World Root)**, a spiritual field connecting different historical eras, and the **"Dom da Revivência" (Gift of Revival)**, an ability allowing characters to experience echoes of these eras. Players choose from three distinct origins: **Colonizador (Colonizer)**, **Indígena (Indigenous)**, and **Ser Folclórico (Folkloric Being)**.

Key mechanical innovations include a highly flexible class progression system inspired by the mobile RPG _Orna_, where classes are permanently unlocked and some abilities are inherited upon switching. Progression occurs through multi-tiered advancements within historical eras, avoiding a dependency on new content releases. The equipment system is equally deep, featuring a 5x5 matrix of Quality and Rarity that dictates item power and progression.

The development strategy is phased to manage complexity for a solo developer. The TTRPG serves as a live playtest. The initial digital version will feature exploration via connected scenes ("blocks") and a static, turn-based combat system. A subsequent phase will introduce free, point-and-click world movement and tactical, grid-based combat. This pragmatic approach prioritizes the development of complex AI, NPC routines, and a living world simulation before tackling more demanding visual and pathfinding challenges.

## 1. Core Project Vision and Development Strategy

The "Eras do Brasil" project is conceived with a dual-format approach, leveraging a tabletop RPG as a foundational framework for a future digital game. This strategy allows for iterative design, mechanical testing, and balance validation in a controlled environment before committing to digital development.

### 1.1. Tabletop RPG as a Foundation

The initial and primary focus is the creation of a comprehensive TTRPG rulebook. This tabletop version is not merely a precursor but a complete system designed to:

- **Validate Core Mechanics:** Test the D20-based action resolution, class progression, combat, and crafting systems with live players.
- **Refine Balance:** Adjust class abilities, item stats, and progression curves based on playtest feedback.
- **Establish a Guided Gameplay Style:** The TTRPG itself is designed to mirror the initial digital version's structure, using a "block-based" exploration model where the Game Master presents defined scenes and choices, rather than a completely open sandbox. This ensures the tabletop experience directly informs the digital design.

### 1.2. Phased Digital Adaptation

The transition to a digital format is planned in two distinct phases to manage development complexity for a solo creator.

- **Phase 1: Block-Based World & Static Combat**
    - **World Exploration:** The game world is structured as a series of interconnected, static scenes or "blocks." Players navigate by selecting directions (e.g., clicking on screen edges) to move from one block to another, similar to a point-and-click novel.
    - **Time System:** Each transition between blocks advances the in-game time by "ticks," triggering NPC routines, dynamic events, and mission timers.
    - **Combat System:** Combat is turn-based but "static," meaning it does not involve character movement on a tactical grid. The focus is on ability selection and turn order, akin to games like _Sea of Stars_ or classic JRPGs.
- **Phase 2: Free Movement & Tactical Combat**
    - **World Exploration:** The block-based system will evolve into free, point-and-click movement. Time will still advance via a "tick" system, similar to _Stoneshard_, where player actions and movement consume time, allowing the world to react dynamically.
    - **Combat System:** The static combat will be replaced by a tactical, grid-based system with character movement, range, line of sight, and attacks of opportunity, drawing inspiration from games like _Solasta_ and _Wartales_.

This phased approach allows the complex underlying systems (NPC AI, persistent world, event simulation) to be built and tested within the simpler Phase 1 framework before adding the technical overhead of advanced rendering, pathfinding, and collision detection required for Phase 2.

### 1.3. Recommended Technology Stack (Digital)

Several technology stacks have been proposed for the eventual digital implementation, depending on the chosen format:

|   |   |   |   |   |
|---|---|---|---|---|
|Format|Frontend|Backend|Database|Advantages|
|**Full Web Application**|React + TypeScript|FastAPI|AWS DocumentDB or PostgreSQL|Total control, scalability, future multiplayer potential.|
|**CLI Application (Prototype)**|N/A|Python|JSON file or SQLite|Simple and fast for validating rules before web development.|
|**Text Game Engine**|Twine|N/A|N/A|Rapid prototyping of narrative mechanics without extensive programming.|

## 2. Narrative Framework and World-Building

The game is set in a unique eco-fantastical Brazil where historical events are interwoven with folklore and magic. The core narrative engine revolves around time, memory, and spiritual connection.

### 2.1. Central Mystical Concepts

- **A Raiz do Mundo (The World Root):** This is a spiritual nexus that connects all eras of the continent's history. It is a living entity for Indigenous peoples, a divine creation for Missionaries, and a field of conscious stories for Folkloric Beings. Disruptions in the World Root, or "Rupturas," cause temporal anomalies and are central to the main plot.
- **O Dom da Revivência (The Gift of Revival):** Characters who possess this gift are "despertos" (awakened) and can perceive and interact with echoes of past and potential future eras. This provides the in-universe justification for the game's core mechanic of progressing through different historical periods.

### 2.2. Playable Origins (Races)

Character creation begins with the selection of one of three origins, each providing a unique mechanical bonus and narrative lens through which to experience the world.

- **Colonizador (Colonizer):** Represents European explorers, soldiers, and missionaries. They bring technology, organized religion, and a structured worldview.
- **Indígena (Indigenous):** Represents the native peoples of the land, deeply connected to its spiritual and natural forces.
- **Ser Folclórico (Folkloric Being):** Embodies the myths and legends of Brazil, acting as living stories with their own agendas.

A system for temporary, narrative-driven "origin changes" via magical events is also planned, allowing players to experience the world from a different cultural perspective for short campaigns.

### 2.3. Campaign Structure: Mini-Campaigns and Major Hooks

The narrative is designed to be modular and expandable. The game is structured around a main story (Ato 1), but is supplemented by numerous mini-campaigns tied to specific origins and classes. Each mini-campaign is self-contained but includes a **"Gancho Maior de Campanha" (Major Campaign Hook)**, a narrative thread that can be expanded into a longer, more complex story arc. This structure provides both short-term content and long-term replayability.

Examples of Mini-Campaigns:

- **Indígena:** "O Caçador que Não Voltou" (The Hunter Who Didn't Return)
- **Colonizador:** "Justiça das Mãos Sujas" (Justice of the Dirty Hands)
- **Ser Folclórico:** "Passos que não Deixam Pegadas" (Footsteps That Leave No Prints)

## 3. Core Gameplay Mechanics

The game is built on a D20 system but incorporates several unique mechanics designed to promote player engagement, build diversity, and a sense of continuous progression.

### 3.1. Character Creation and Attributes

- **Action Resolution:** The core mechanic is **1D20 + Attribute Modifier + Proficiency Bonus** against a Class de Dificuldade (CD) or an opposed roll.
- **Attributes:** The game uses six thematically named primary attributes:
    - **Vigor:** Health and physical resistance.
    - **Força Bruta (Brute Force):** Physical power and damage.
    - **Astúcia (Cunning):** Agility, reflexes, and stealth.
    - **Sabedoria Ancestral (Ancestral Wisdom):** Spiritual connection, intuition, and perception.
    - **Conhecimento (Knowledge):** Logic, technical skills, and magic.
    - **Presença (Presence):** Charisma, persuasion, and leadership.
- **Point-Buy System:** Players have **27 points** to distribute among these attributes.

### 3.2. Class and Progression System

This is a central feature, designed for flexibility and to reward long-term play. It draws heavy inspiration from the progression model of the RPG _Orna_.

- **Unlocking Classes:** A character starts with one of four initial classes available to their chosen origin (12 total initial classes). Other classes are unlocked permanently by spending a rare in-game currency, **"Moeda de Classe" (Class Coin)**, and completing a quest for a specific NPC master.
- **Non-Linear Progression:** Players are not locked into a single class path. Once unlocked, a player can switch between any of their available classes freely outside of combat. Progress in each class is saved individually.
- **Tiered Evolution:** Classes evolve through **Tiers** (e.g., Tier 1 to Tier 3) within the same historical era. This ensures that character progression is not solely dependent on the release of new eras, a key concern in the design philosophy: _"Não quero zerar a progressão toda vez que muda... Tenho medo de que, se for uma evolução por era, o jogador fique limitado."_ ("I don't want to reset progression every time it changes... I'm afraid that if it's one evolution per era, the player will be limited.")
- **Inherited Abilities:** When a player changes classes, they can retain a limited number of previously learned **active abilities**, allowing for the creation of unique hybrid builds. Passive abilities and class-specific bonuses are not inherited.

### 3.3. Proficiencies (Lifeskills)

The system features a robust set of non-combat skills inspired by MMORPGs, promoting diverse character roles beyond combat.

- **Categories:** Proficiencies are divided into three types:
    - **Coleta (Gathering):** e.g., Caça (Hunting), Mineração (Mining).
    - **Produção (Crafting):** e.g., Ferraria (Blacksmithing), Alquimia (Alchemy).
    - **Refinamento/Complementares (Refining/Complementary):** e.g., Tratamento de Couro (Leatherworking), Negociação (Negotiation).
- **Progression:** Lifeskills advance through an XP-per-use system. However, to level up, a character must find a master NPC and complete a specific mission, blending mechanical progression with narrative engagement.
- **Class Bonuses:** Each class provides a small XP bonus to a thematically linked lifeskill, but only while that class is active.

### 3.4. Equipment System

The itemization is designed to be a core pillar of player progression, featuring a detailed matrix system.

- **Quality and Rarity Matrix (5x5):** Every item has two independent properties: Quality (Ruim, Normal, Boa, Excelente, Obra-prima) and Raridade (Comum, Incomum, Rara, Épica, Lendária).
- **Combined Impact:** These two properties combine to determine an item's base stats, special effects, and its **Nível Recomendado (Recommended Level)**. A high-rarity item can have low quality, making it a powerful but flawed piece of gear, while a high-quality common item can be a reliable workhorse. This creates 25 possible variations for each base item.
- **Player Progression:** This system incentivizes players to continuously seek upgrades through crafting, looting, and trade, making item acquisition a central gameplay loop.

|   |   |   |   |   |   |
|---|---|---|---|---|---|
||Ruim|Normal|Boa|Excelente|Obra-prima|
|**Comum**|Lvl 1|Lvl 2|Lvl 3|Lvl 4|Lvl 5|
|**Incomum**|Lvl 2|Lvl 3|Lvl 4|Lvl 5|Lvl 6|
|**Rara**|Lvl 3|Lvl 4|Lvl 5|Lvl 6|Lvl 7|
|**Épica**|Lvl 4|Lvl 5|Lvl 6|Lvl 7|Lvl 8|
|**Lendária**|Lvl 5|Lvl 6|Lvl 7|Lvl 8|Lvl 9|

### 3.5. Advanced and Optional Systems

Several advanced mechanics are planned, primarily for the digital version, to create a more dynamic and high-stakes world.

- **Item Durability:** Equipment loses durability with use and can break if not repaired by a crafter.
- **Full Loot:** In certain modes or zones, a character's death results in their items being dropped as loot, which can be retrieved by other players or even NPCs.
- **Evolving Enemies:** Enemies that defeat a player character gain experience points. This can lead to emergent narratives where a common bandit that once defeated the player reappears later as a powerful gang leader.

## 4. Project Documentation and Organization

The development process is supported by a structured approach to documentation, managed within the Obsidian note-taking application and organized into distinct "Setores" (Sectors).

- **Modular Book Structure:** The game's rules and lore are being compiled into a series of interconnected, modular books rather than a single monolithic tome. This includes:
    - **Livro de Regras (Rulebook):** Contains the core mechanics, character creation framework, and general systems.
    - **Livro de Classes (Class Book):** Provides in-depth details for every class, including abilities, equipment, and evolution paths.
    - Future books are planned for Items, Magic, Proficiencies, and Monsters.
- **Sector-Based Organization:** The project workflow is divided into dedicated sectors, each managed in a separate context or chat, to maintain focus. These include:
    - 📖 Enredo e Narrativa (Plot and Narrative)
    - 📘 Livro de Regras e Sistema (Rulebook and System)
    - 🎨 Artes e Estilo Visual (Arts and Visual Style)
    - 🧩 Missões e Eventos (Quests and Events)

This organized methodology ensures that different facets of the complex project can be developed in parallel while maintaining coherence and a unified vision.