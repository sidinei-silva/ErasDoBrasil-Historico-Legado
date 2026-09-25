# Plano de Projeto: Eras do Brasil (MUD Moderno — Servidor Go)

> **Navegação:** [GDD](README.md) · [Game Pitch](Game_Pitch.md) · [Roadmap de Desenvolvimento](99_Meta_e_Backlog/02_Roadmap_Desenvolvimento.md) · [Projeto](../README.md)
>
> **Propósito:** Documento de estratégia **interna** — para a equipe de desenvolvimento. Define escopo técnico, arquitetura de sistemas e roadmap de fases.
> **Relação:** Para a apresentação externa do jogo (visão, narrativa, diferencial), veja o [Game Pitch](Game_Pitch.md).

## 1.0 Visão e Estratégia Geral

Este documento delineia a visão fundamental para 'Eras do Brasil', detalhando o conceito de alto nível, a missão central e a estratégia de entrada no mercado.

'Eras do Brasil' é um RPG de fantasia histórica ambientado em uma versão mística do Brasil. Nossa missão principal é criar uma experiência imersiva que entrelace magistralmente a história e o folclore brasileiros com uma jogabilidade inovadora e estrategicamente gratificante.

A estratégia de desenvolvimento é **incremental por fases**: construímos a complexidade em camadas, começando por um servidor Go com mundo persistente baseado em texto (MUD Moderno) e evoluindo para um cliente web rico. Cada fase entrega um valor jogável completo antes de avançar para a próxima.

## 2.0 Definição do Produto e Escopo

### 2.1. O Núcleo do Sistema (MVP)

Mecânicas fundamentais que guiam todas as fases:

- **Núcleo do Sistema:** Resolução de ações baseada em D20 contra uma Classe de Dificuldade (CD).
- **Pilares de Personagem:** Três Origens distintas: **Colonizador**, **Indígena** e **Ser Folclórico**.
- **Sistema de Classes:** Estrutura flexível com 12 classes iniciais, evoluindo através de três Tiers.

### 2.2. A Adaptação Digital (Modelo Servidor Persistente)

A visão é um mundo **100% online e persistente** (MUD Moderno) onde múltiplos jogadores coexistem.

- **Arquitetura Técnica:**
    - **Servidor Go:** Autoritativo. Game loop sequencial processa todos os managers por ciclo. IA de NPCs, estado do mundo, combate e economia. Toda a lógica de jogo reside no servidor.
    - **Cliente Web:** HTML/CSS/JS conectado via **WebSocket**. Renderiza a interface, envia comandos e recebe atualizações de estado em JSON.
- **Tempo do Jogo:**
    - **Relógio do Jogo:** Ciclo dia/noite com 4 períodos (Manhã, Tarde, Noite, Madrugada). 1 dia do jogo ≈ 2–4 horas reais.
    - **Tempo Real:** Prazos de quests, durations de ações e eventos medidos em segundos/minutos reais.
    - **Turnos:** Exclusivamente para combate D20.

> **Nota:** Não existe modo offline. O jogo é 100% online persistente. "Tick" é detalhe interno do game loop, não exposto ao jogador.

## 3.0 Público-Alvo e Posicionamento

- **Público Primário:** Jogadores experientes de RPG (mesa e digital) que buscam profundidade mecânica e narrativa. Jogadores de MUDs clássicos, fãs de *Fallen London*, *West of Loathing*, *Torn* e *Kingdom of Loathing*.
- **Posicionamento:** Preenche a lacuna de RPGs profundos com temática sul-americana (Eco-Fantasia), oferecendo um mundo persistente com inimigos evolutivos, missões competitivas, mundo vivo simulado por IA, e acesso zero-install via navegador.

## 4.0 Mecânicas Centrais de Gameplay

### 4.1. Progressão de Personagem

- **Tiers de Classe:** Evolução vertical (Tier 1-3).
- **A "Moeda de Classe":** Item raro necessário para desbloquear classes. Na Raiz (online), a obtenção é competitiva — Moedas existem em quantidade limitada e renovam com as temporadas.
- **Troca Estratégica:** Habilidades ativas desbloqueadas entram para um "pool" global do personagem.

### 4.2. Economia e Crafting

- **Proficiências:** Divisão entre **Coleta** e **Produção**.
- **Comércio Server-Authoritative:** Toda troca entre jogadores é validada pelo servidor. Em caso de desconexão, o servidor reverte a transação atomicamente. Itens dropados ficam no chão por um tempo antes de despawnarem.
- **Matriz de Itemização:** Poder definido por uma matriz 5×5 de Qualidade e Raridade.
- **Penalidade de Morte:** Morte PvE = perda de % XP (não perde nível) + % durabilidade nos equipamentos. Sem drop de itens. Reparo alimenta o loop econômico (crafting + materiais). Ver ADR-010.

### 4.3. Narrativa e Mundo

- **Raiz do Mundo:** A força mística que conecta as eras; no jogo, é a "master timeline" do servidor onde todos os jogadores coexistem.
- **Dom da Revivência:** Adaptação natural pela exposição à Raiz — não predestinação. Justificativa *in-game* para a troca de classes e acesso a diferentes períodos históricos.
- **StoryManager:** Sistema de narrativa ramificada no servidor que gera Cenários A/B com base em ações da comunidade.
- **Temporadas:** Arcos narrativos de 4-6 meses reais. Cada temporada traz uma feature nova. O jogo é hobby do desenvolvedor, com transparência à comunidade.

---

## 5.0 Roadmap de Desenvolvimento

> **Nota:** O roadmap detalhado está em [02_Roadmap_Desenvolvimento.md](99_Meta_e_Backlog/02_Roadmap_Desenvolvimento.md). Esta seção apresenta a visão estratégica das fases.

### Fase 0: Heartbeat — O Servidor Respira

- **Objetivo:** Provar que o servidor Go funciona. Game loop sequencial, goroutine, WebSocket.
- **Escopo:** Servidor Go com game loop. Cliente web conecta e vê o relógio do jogo avançando na tela.
- **Tech:** Go 1.22+ · `gorilla/websocket` · HTML/JS vanilla

### Fase 1: Living World — O Mundo Existe

- **Objetivo:** Mundo com blocos, NPCs com rotina e ciclo dia/noite.
- **Escopo:** 3 blocos (Vila, Floresta, Ruínas). 2 NPCs com Utility AI (agenda, necessidades). Ciclo dia/noite.

### Fase 2: Observer — O Jogador Observa

- **Objetivo:** Cliente web mostra o estado do mundo em tempo real.
- **Escopo:** Mapa de nós clicável. NPCs visíveis com status. Log de acontecimentos do mundo.

### Fase 3: Player — O Jogador Age

- **Objetivo:** Criação de personagem, movimentação, inventário, D20, combate estático.
- **Escopo:** 1 Origem (Indígena), 1 Classe (Guerreiro Tribal), combate por turnos, loot, save/load.

### Fase 4: Interaction — O Mundo Reage

- **Objetivo:** Diálogos, fofoca, facções, crafting, coleta, economy loop completo.
- **Escopo:** Proficiências, Matriz 5×5, comércio com NPCs, sistema de temporadas.

### Fase 5: D20 Full — O Jogo Completo

- **Objetivo:** 12 classes, 3 Origens, Ato 1 completo, grid tático.
- **Escopo:** Campanha "A Primeira Ruptura" jogável. 6+ mini-campanhas. Boss final.

### Fase 6: Multiplayer — A Raiz Conecta

- **Objetivo:** Múltiplos jogadores simultâneos. Missões competitivas. Inimigos evolutivos. Eventos globais.
- **Escopo:** Autenticação, persistência de saves no servidor, trade server-authoritative, StoryManager, penalidade de morte (XP + durabilidade).

> **PvP:** Removido do escopo do MVP. Será considerado em temporadas futuras. Ver ADR-012.

---

## 6.0 Sistemas Avançados e Visão Pós-Lançamento

- **Durabilidade e Reparo:** Equipamentos degradam com o uso (desgaste automático baseado no tempo de jogo).
- **Inimigos Evolutivos (MVP):** Inimigos que derrotam jogadores ganham XP, evoluindo de Normal → Veterano → Alfa → Lenda. Ver ADR-009.
- **Modo Hardcore (Opcional):** Morte permanente para o personagem.
- **Ecos Instanciados (Temporada 3+):** Jogadores que chegam após uma temporada podem vivenciar conteúdo passado em modo instanciado solo, com recompensas reduzidas.
