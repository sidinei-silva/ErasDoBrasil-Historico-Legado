# Linha do Tempo — Desenvolvimento do Eras do Brasil

> Reconstrução cronológica de como o projeto nasceu e evoluiu, a partir dos chats
> originais com o ChatGPT e da conversa de WhatsApp que deu o pontapé inicial. Serve
> de mapa para não se perder na história do desenvolvimento e como índice de
> navegação para os documentos-fonte.
>
> **Status:** cobre as conversas do ChatGPT em [`Conversas/GPT/`](Conversas/GPT/), a
> conversa de WhatsApp em [`Conversas/WhatsApp/`](Conversas/WhatsApp/), as conversas
> do Gemini em [`Conversas/Gemini/`](Conversas/Gemini/), as sessões do Claude em
> [`Conversas/Claude/`](Conversas/Claude/), os logs de sessão do Copilot arquivados em
> [`Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/`](Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/) e uma checagem direta
> dos repositórios de código ativos (`eras-do-brasil-gdd`, `eras-do-brasil`, fora deste
> repositório). As conversas do ChatGPT cobrem até 24/09/2026 (dois exports: o antigo,
> até 2025, e um de 26/08 a 25/09/2026). Ainda falta mapear
> `Artefatos/01-rpg-de-mesa-e-narrativa/NotebookLM/` na cronologia (ver
> [Pendências](#pendências) no fim).

## Origem: cinco fases, separadas por hiatos

O projeto não começou como "Eras do Brasil", e nem começou no ChatGPT. Começou como
uma piada de WhatsApp — **"Bora fazer um game?"** — em julho de 2023, virou
**"1500 Caminhos do Brasil"**, um RPG de turno digital sobre a história do Brasil,
passou por uma fase de RPG de mesa de mundo persistente em 2025 (ChatGPT e Gemini),
foi implementado em Unity com o Copilot no início de 2026, e em 11/03/2026 o Copilot
pivota o projeto para código de verdade — um MMORPG textual em Go, que o Claude assume
três dias depois. Nessa fase técnica, o projeto quase morre pausado enquanto um
spin-off idle ("A Escória"/"Outlander") nasce, cresce sozinho, e acaba **absorvendo**
o Eras do Brasil: a arquitetura do spin-off e o mundo/lore do Eras se fundem em um
único jogo, ainda chamado "Eras do Brasil", mas tecnicamente construído como A Escória
— e é esse jogo que continua em desenvolvimento ativo hoje, no repositório
`eras-do-brasil` (fora deste repositório de histórico).

## Cronologia

| # | Data | Fonte | Resumo | Arquivo |
|---|------|------|--------|---------|
| 1 | 2023-07-02 | WhatsApp — conversa com Guilherme Bambam | **Origem real do projeto.** Sidinei chama Guilherme para "fazer um game", cola o resultado de uma conversa anterior no ChatGPT já com o conceito **"1500 Caminhos do Brasil"** (RPG de turno inspirado em Pillars of Eternity/Wartales/Baldur's Gate) e conta que a ideia veio de uma reportagem sobre a independência da Bahia. Conversa continua até 2023-07-04 discutindo sistema de companheiros (estilo Solasta/Baldur's Gate) e classes. | [2023-07-02_Conversa WhatsApp Guilherme Bambam_transcrita.md](Conversas/WhatsApp/2023-07-02_Conversa%20WhatsApp%20Guilherme%20Bambam_transcrita.md) |
| 2 | 2023-07-01 | História do Brasil (ChatGPT) | Primeiro chat registrado no ChatGPT: pedido de uma linha do tempo da história do Brasil. Revisitado em **2025-04-17**, quando Sidinei pediu um "backup nostálgico" — um documento de canvas confirmando que o nome original do jogo era **"1500 Caminhos do Brasil"** e detalhando os atos/classes da ideia original (ver seção [Achado](#achado-o-nome-original-era-1500-caminhos-do-brasil) abaixo). | [2023-07-01_Historia do Brasil_convertido.md](Conversas/GPT/2023-07-01_Historia%20do%20Brasil_convertido.md) |
| 3 | 2023-07-07 | [OFICIAL] RPG História do Brasil (ChatGPT) | Pedido mais estruturado: linha do tempo completa da colonização à proclamação da República, com personagens e eventos. Primeira vez que o chat é marcado como "oficial". | [2023-07-07_OFICIAL RPG Historia do Brasil_convertido.md](Conversas/GPT/2023-07-07_OFICIAL%20RPG%20Historia%20do%20Brasil_convertido.md) |
| — | *(hiato de ~19 meses)* | | | |
| 4 | 2025-02-23 | RPG de Mesa Persistente (ChatGPT) | Retomada da ideia, agora como RPG de mesa de mundo persistente (inspirado em MMORPGs), não mais RPG de turno digital. | [2025-02-23_RPG de Mesa Persistente_convertido.md](Conversas/GPT/2025-02-23_RPG%20de%20Mesa%20Persistente_convertido.md) |
| 5 | 2025-03-19 | RPG Eras do Brasil (ChatGPT) | O nome **"Eras do Brasil"** aparece. Consolidação do conceito: classes/subclasses baseadas em figuras históricas e folclóricas, crafting, economia, evolução do cenário por escolhas dos jogadores, sistema em D20. Chat gigante (a base de lore mais extensa). | [2025-03-19_RPG Eras do Brasil_convertido.md](Conversas/GPT/2025-03-19_RPG%20Eras%20do%20Brasil_convertido.md) |
| 6 | 2025-04-13 | Setores para Desenvolvimento Eras (ChatGPT) | Decisão de criar um "projeto" no ChatGPT e dividir o desenvolvimento em setores (um chat por setor: arte, marketing, regras, NPCs, enredo, inimigos, cenários/mapas, itens, missões, recursos). | [2025-04-13_Setores para Desenvolvimento Eras_convertido.md](Conversas/GPT/2025-04-13_Setores%20para%20Desenvolvimento%20Eras_convertido.md) |
| 7 | 2025-04-14 | Setor de Arte (ChatGPT) | Abertura do setor de arte e design visual (pixel art). | [2025-04-14_Setor de Arte_convertido.md](Conversas/GPT/2025-04-14_Setor%20de%20Arte_convertido.md) |
| 8 | 2025-04-17 | Setor Enredo Narrativa (ChatGPT) | Abertura do setor de narrativa (RPG de mesa + futura versão digital). | [2025-04-17_Setor Enredo Narrativa_convertido.md](Conversas/GPT/2025-04-17_Setor%20Enredo%20Narrativa_convertido.md) |
| 9 | 2025-04-17 | Setor Livro de Regras e Sistema (ChatGPT) | Abertura do setor responsável pelo livro de regras/sistema. | [2025-04-17_Setor Livro de Regras e Sistema_convertido.md](Conversas/GPT/2025-04-17_Setor%20Livro%20de%20Regras%20e%20Sistema_convertido.md) |
| 10 | 2025-04-17 | Setor Missões e Eventos (ChatGPT) | Abertura do setor de missões e eventos. | [2025-04-17_Setor Missões e Eventos_convertido.md](Conversas/GPT/2025-04-17_Setor%20Missões%20e%20Eventos_convertido.md) |
| 11 | 2025-07-13 | Documentação Eras do Brasil (ChatGPT) | Pedido de um template de documentação/linha do tempo das decisões do projeto, para depois poder limpar a memória do ChatGPT. **Este documento é a continuação direta dessa ideia.** | [2025-07-13_Documentacao Eras do Brasil_convertido.md](Conversas/GPT/2025-07-13_Documentacao%20Eras%20do%20Brasil_convertido.md) |
| 12 | 2025-08-08 | Plano de Execução Detalhado (ChatGPT) | Pedido de um plano de execução em várias etapas para uma tarefa grande (a preparar/detalhar). | [2025-08-08_Plano de Execucao Detalhado_convertido.md](Conversas/GPT/2025-08-08_Plano%20de%20Execucao%20Detalhado_convertido.md) |
| — | *(hiato de ~3 meses; migração de setores do ChatGPT para o Gemini)* | | | |
| 13 | 2025-11-07 | Eras do Brasil, desenvolvimento do game (Gemini) | Retomada no **Gemini**: recapitulação completa do sistema (Origens, Classes por Tier, atributos, Ticks, facções, as 3 fases digital+mesa) e definição de ferramental — discussão de editores (Notion→Obsidian→alternativa com nuvem) e da stack técnica (pub/sub de eventos por tick para NPCs vivos). | [2025-11-07_Eras do Brasil, desenvolvimento do game.md](Conversas/Gemini/2025-11-07_Eras%20do%20Brasil%2C%20desenvolvimento%20do%20game.md) |
| 14 | 2026-01-30 | Música para RPG de Fantasia Brasileira (Gemini) | Direção musical do jogo: trilha inspirada em Celtic/Nordic/Skyrim adaptada à fantasia brasileira, com sugestões de ferramentas de geração (Suno/Udio) e estrutura de letra ligada às 12 classes e ao "Relógio da Ruptura". | [2026-01-30_Música para RPG de Fantasia Brasileira.md](Conversas/Gemini/2026-01-30_M%C3%BAsica%20para%20RPG%20de%20Fantasia%20Brasileira.md) |
| 15 | 2026-02-06 | Stack e Arquitetura para Jogo Web RPG (Gemini) | Decisão de stack técnica para a versão web (Node.js vs Flutter/Dart), arquitetura pensada para co-op e "Shared Core", no estilo Tibia/Ragnarok com layout de janelas ao redor do cenário central. | [2026-02-06_Stack e Arquitetura para Jogo Web RPG.md](Conversas/Gemini/2026-02-06_Stack%20e%20Arquitetura%20para%20Jogo%20Web%20RPG.md) |
| 16 | 2026-02-14 | Ficou muito bom isso. (Gemini) | Validação de UI: comparação de duas opções de interface (baseadas nos docs `05_UI_Fase_1_Exploracao_e_Combate.md` e `02_UI_HUD_e_Tipografia.md`), definição do layout "sanduíche" para os modos de Exploração e Combate. | [2026-02-14_Ficou muito bom isso..md](Conversas/Gemini/2026-02-14_Ficou%20muito%20bom%20isso..md) |
| 17 | 2026-02-18 | Justificando o Conflito no Jogo (Gemini) | Resolução de um buraco narrativo: por que os inimigos atacam o herói. Define a motivação central — "lutamos pela Sincronia" — ligando o conflito ao Game Pitch, aos Conceitos Centrais e ao Ato 1. | [2026-02-18_Justificando o Conflito no Jogo.md](Conversas/Gemini/2026-02-18_Justificando%20o%20Conflito%20no%20Jogo.md) |
| 18 | 2026-02-11 | Sprints 1 e 2 concluídas (Copilot, `gdd-batalha-turno`) | Ainda era Unity: sistema de XP/progressão, troca de origem via Espelho do Eco, pré-requisitos multi-classe. Projeto tinha 38 POCs planejadas e 62 issues abertas. | [historico/sessions/2026-02-11_sprints-1-2.md](Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/sessions/2026-02-11_sprints-1-2.md) |
| 19 | 2026-02-13 | Decisões Unity e workflow UI/UX (Copilot, `gdd-batalha-turno`) | **ADR-001** (projeto Unity único, código de produção desde o início) e **ADR-002** (wireframes dentro das sprints). Últimas decisões formais da era Unity antes do pivô. | [historico/sessions/2026-02-13_decisoes-unity-uiux.md](Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/sessions/2026-02-13_decisoes-unity-uiux.md) |
| 20 | 2026-03-07 | Auditoria, reorganização total e revisão de MVP (Copilot) | Três sessões no mesmo dia: auditoria de ~120 arquivos do GDD (corrige contradições, remove duplicações); diagnóstico de 6 problemas do projeto (escopo descontrolado, GDD 100%/código 0%, conhecimento fragmentado em 3 IAs) com **ADR-003** (monorepo) e plano de 4 spin-offs de aprendizado; revisão de produto confirma 90% do planejamento sólido e identifica 4 gaps (Steam/EA, comunicação de co-op, posicionamento cultural, i18n) que Sidinei **decide conscientemente adiar**. | [Conversas/Copilot/2026-03-07_sessão_copilot_organização_e_desenvolvimento.md](Conversas/Copilot/2026-03-07_sess%C3%A3o_copilot_organiza%C3%A7%C3%A3o_e_desenvolvimento.md) |
| 21 | 2026-03-11 | **O pivô — MUD Moderno (Copilot, `gdd-batalha-turno`)** | **Esta é a sessão do pivô de verdade**, não a de 14/03 com o Claude. Frustração com "3 anos de documentação sem nenhuma linha de código" leva ao abandono do Unity Co-op P2P e adoção do **MUD Moderno**: servidor Go (goroutines, WebSocket), cliente web, server-authoritative. **ADR-004** formaliza a decisão; ~30 arquivos reescritos/arquivados, incluindo Game Pitch, Project Plan e Roadmap. | [historico/sessions/2026-03-11-pivot-mmorpg-servidor-go.md](Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/sessions/2026-03-11-pivot-mmorpg-servidor-go.md) |
| 22 | 2026-03-13 | Reestruturação física e migração para WSL (Copilot) | Remove `pocs/`/`spinoffs/`, cria `game/server/`+`game/textClient/`, planeja comandos admin (RCON-like). Sessão termina com um "bota-fora" completo — handover documental para continuar no WSL sem perder contexto, preparando a virada para o Claude Code. | [historico/sessions/2026-03-13-bota-fora-sessao-completa.md](Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/sessions/2026-03-13-bota-fora-sessao-completa.md) |
| 23 | 2026-03-14 | Análise de conversas com IA (Claude) | **Retomada no WSL, já com o pivô decidido 3 dias antes.** Claude assume o handover do Copilot: workflow fixado em 3 repos (gdd/game/legado) e num Claude Project como "Game Designer sênior crítico". | [2026-03-14_Análise de conversas com IA.md](Conversas/Claude/2026-03-14_An%C3%A1lise%20de%20conversas%20com%20IA.md) |
| 24 | 2026-03-15 | Go para desenvolvimento de game server (Claude) | Go confirmado (2ª vez) e correção de um erro grave nos ADRs: troca de managers paralelos via EventBus por um **game loop sequencial** (World→NPC→Combat→Story→Economy→Persist) — decisão que rege toda a arquitetura técnica dali em diante. | [2026-03-15_Go para desenvolvimento de game server.md](Conversas/Claude/2026-03-15_Go%20para%20desenvolvimento%20de%20game%20server.md) |
| 25 | 2026-03-17 | Narrativa dinâmica e temporadas no mmorpg (Claude + Copilot) | Nasce a tese central do jogo: **"o mundo não espera por herói"** — sem escolhido, reputação emergente por quests competitivas, temporadas que fecham a história permanentemente. 16 decisões aplicadas ao GDD via **ADR-007 a ADR-012** (mesmo dia, sessão espelhada no `gdd-batalha-turno`). | [2026-03-17_Narrativa dinâmica e temporadas no mmorpg.md](Conversas/Claude/2026-03-17_Narrativa%20din%C3%A2mica%20e%20temporadas%20no%20mmorpg.md) · [sessão GDD](Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/sessions/2026-03-17-decisoes-narrativa-mmorpg.md) |
| 26 | 2026-03-19 | Furos de lore (Copilot, `gdd-batalha-turno`) | 9 furos de consistência resolvidos: causa da Ruptura de 1497 (ritual folclórico fracassado), Mana substituída por **Fadiga Espiritual**, Guardião da Fenda redefinido como protetor (não vilão), Dano Espiritual como tipo oficial. | [historico/sessions/2026-03-19-furos-de-lore.md](Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/sessions/2026-03-19-furos-de-lore.md) |
| 27 | 2026-03-20 | Arquitetura do Mapa e Regiões (Copilot, `gdd-batalha-turno`) | Mapa hierárquico em 3 camadas (Mapa-Múndi → Zonas → Sub-locais, estes adiados). 5 regiões com gradiente de nível: Mata Costeira (1–5) → Sertão Distorcido → Serra dos Ecos → Pantanal Vivo → Coração da Raiz (20+). Só a Mata Costeira é detalhada para o MVP. | [historico/sessions/2026-03-20-arquitetura-mapa.md](Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/sessions/2026-03-20-arquitetura-mapa.md) |
| 28 | 2026-04-18 | Estrutura de pastas para projeto de game (Claude) | Sessão-maratona: **ADR-007** [do repositório de código, numeração própria] fecha a arquitetura (flat por domínio, cada manager dono do próprio estado, sem "GameState" central) e nasce o formato "Refinamento N.N" usado em todos os chats técnicos seguintes. Recusa deliberada de TDD-com-IA para o núcleo de simulação. | [2026-04-18_Estrutura de pastas para projeto de game.md](Conversas/Claude/2026-04-18_Estrutura%20de%20pastas%20para%20projeto%20de%20game.md) |
| 29 | 2026-04-29 | Conceito de jogo idle com gestão de personagens (Claude) | **Primeira menção da ideia de um jogo idle** (estilo Evil Hunter Tycoon/Melvor Idle). Sidinei decide guardar a ideia e manter o foco no Eras do Brasil — ainda não é o pivô. | [2026-04-29_Conceito de jogo idle com gestão de personagens.md](Conversas/Claude/2026-04-29_Conceito%20de%20jogo%20idle%20com%20gest%C3%A3o%20de%20personagens.md) |
| 30 | 2026-05-23 | Decisões técnicas para Eras do Brasil (Claude) | Claude identifica um padrão: a dúvida "devo trocar de linguagem" já voltou **5 vezes em 2 meses** — sintoma de cansaço/sobrecarga, não decisão técnica. Primeiro sinal explícito de fadiga com o projeto, via diários de desenvolvimento anexados. | [2026-05-23_Decisões técnicas para Eras do Brasil.md](Conversas/Claude/2026-05-23_Decis%C3%B5es%20t%C3%A9cnicas%20para%20Eras%20do%20Brasil.md) |
| 31 | 2026-05-26 | Eras do Brasil como action RPG idle (Claude) | Sidinei propõe fundir o Eras com elementos idle/ARPG; Claude aponta 8 contradições com o GDD vigente e recusa a mistura, pedindo para escolher entre 3 fantasias de gênero — pergunta que migra para um projeto separado. | [2026-05-26_Eras do Brasil como action RPG idle.md](Conversas/Claude/2026-05-26_Eras%20do%20Brasil%20como%20action%20RPG%20idle.md) |
| 32 | 2026-05-31 | Adaptação idle MMORPG do Albion Online (Claude) | Nasce **"Albion Idle"**, um spin-off separado do Eras do Brasil, e nasce a fantasia alternativa **"Deuses-Armas"** para vesti-lo — Sidinei evita usar a lore do Eras num spin-off menor, com medo de "esfriar" o projeto principal. Ver [evolução do nome](#evolução-do-nome-do-jogo-idle-albion-idle--deuses-armas--a-escória--outlander) abaixo. | [2026-05-31_Adaptação idle MMORPG do Albion Online.md](Conversas/Claude/2026-05-31_Adapta%C3%A7%C3%A3o%20idle%20MMORPG%20do%20Albion%20Online.md) |
| — | *(hiato de ~3 semanas — sessão "Chat 0 — Calibração" de 2026-06-19, onde "Deuses-Armas" virou "A Escória"/"Outlander", não foi capturada no export do Claude — ver [Pendências](#pendências))* | | | |
| 33 | 2026-06-23 | Próximo passo desenvolvimento do jogo Outlander (Claude) | **A decisão "qual projeto continuar".** O spin-off já se chama **A Escória** (codinome de repositório "Outlander"). Claude recomenda Outlander sobre Eras do Brasil — não por ser melhor IP, mas por ser viável solo (Eras exigiria "sistemas de estúdio de 30 pessoas": NPCs com fofoca/rotina/necessidades). **Eras do Brasil é congelado, não abandonado** — guarda-se a tese "o mundo não espera por herói" para reaproveitar depois. | [2026-06-23_Próximo passo desenvolvimento do jogo Outlander.md](Conversas/Claude/2026-06-23_Pr%C3%B3ximo%20passo%20desenvolvimento%20do%20jogo%20Outlander.md) |
| — | *(julho: poucos registros; em agosto o desenvolvimento corre em **dois trilhos paralelos** — ChatGPT e Claude — ver [O lado ChatGPT](#o-lado-chatgpt-26082409) abaixo)* | | | |
| 34 | 2026-08-26 | Atual - Arquitetura Go do servidor (ChatGPT) | Abre o **chat-tronco técnico da Escória**, que fica aberto até 24/09 (113 trocas, ramificado 2 vezes). A arquitetura que vira oficial — `Network → Command → Game Loop (dono único do estado) → GameState → Events → HTTP/WS/Postgres` — **já nasce na primeira resposta**. Todo o código de conta, login, personagem e entrada no mundo é implementado nele. | [2026-08-26_Atual - Arquitetura Go do servidor_convertido.md](Conversas/GPT/2026-08-26_Atual%20-%20Arquitetura%20Go%20do%20servidor_convertido.md) |
| 35 | 2026-08-27 | Iniciar Arena Server (ChatGPT) | Experimento descartável do "Game Dev Lab" (repo próprio) para aprender game server em Go. Parou no domínio em memória, sem chegar ao game loop — o Claude o cortou em 29/08. | [2026-08-27_Iniciar Arena Server_convertido.md](Conversas/GPT/2026-08-27_Iniciar%20Arena%20Server_convertido.md) |
| 36 | 2026-08-28 | Com eras e escoria · Projeto RPG Solo com LLM (ChatGPT) | **O ChatGPT compara três projetos** (A Escória, Eras do Brasil e um terceiro, RPG solo com LLM). Melhor jogo: Escória; universo mais diferenciado: Eras; e *"se o objetivo for fazer UM jogo e realmente terminá-lo → A Escória… Eras do Brasil eu deixaria como projeto de longo prazo"*. Veredito: *"Não mesclar os jogos em um só. Sim, mesclar conceitos."* — um dia antes do Claude chegar à mesma conclusão. | [2026-08-28_Com eras e escoria· Projeto RPG Solo com LLM_convertido.md](Conversas/GPT/2026-08-28_Com%20eras%20e%20escoria%C2%B7%20Projeto%20RPG%20Solo%20com%20LLM_convertido.md) · [branch](Conversas/GPT/2026-08-28_Branch%20%C2%B7%20Com%20eras%20e%20escoria%C2%B7%20Projeto%20RPG%20Solo%20com%20LLM_convertido.md) |
| 37 | 2026-08-31 | Organização de projetos pessoais e uso de IA (Claude) | Decisão reafirmada pela 2ª vez: **"Escória primeiro, Eras congelado — não mescle: a soma é um jogo maior que os dois, e mata os dois."** | [2026-08-31_Organização de projetos pessoais e uso de IA.md](Conversas/Claude/2026-08-31_Organiza%C3%A7%C3%A3o%20de%20projetos%20pessoais%20e%20uso%20de%20IA.md) |
| 38 | 2026-09-03 | Mockup de interface (ChatGPT) | Primeira direção de arte da Escória: **2D cartum chibi vetorial** (não pixel art), fechado em 05/09 como **isométrico 3/4 estilizado**. Nasce a cena de chegada do tutorial: *"Mais um. Anda. A maré não traz quem ela não pode usar."* | [2026-09-03_Mockup de interface_convertido.md](Conversas/GPT/2026-09-03_Mockup%20de%20interface_convertido.md) |
| 39 | 2026-09-06 | Revisão da lore e motivações do jogo (Claude) | **A fusão.** Sete dias depois de reafirmar "não mesclar", Claude reverte o próprio veredito: *"o esqueleto da Escória, o mundo do Eras"* — A Escória nunca teve mundo próprio, e importar o do Eras custa quase zero em código. *"A Escória é o Eras com o número de série lixado."* No mesmo dia, o ChatGPT também conclui que WebSocket não é necessário na PoC idle. | [2026-09-06_Revisão da lore e motivações do jogo.md](Conversas/Claude/2026-09-06_Revis%C3%A3o%20da%20lore%20e%20motiva%C3%A7%C3%B5es%20do%20jogo.md) · [ChatGPT: HTTP/WS](Conversas/GPT/2026-09-06_Arquitetura%20HTTP%20WebSocket%20Idle_convertido.md) |
| 40 | 2026-09-09 | Comparar Eras dos GDD (ChatGPT) | Primeira tentativa de definir as "Eras" do jogo fundido, reaproveitando os atos de 2023: **Era I Descoberta e Colonização, II Ciclo do Ouro, III Família Real/Independência, IV Abolição/República**, cada uma com T1–T8. Modelo intermediário — em 24/09 já não vale mais ("a mistura de eras é a fantasia central"). | [2026-09-09_Comparar Eras Dos GDD_convertido.md](Conversas/GPT/2026-09-09_Comparar%20Eras%20Dos%20GDD_convertido.md) |
| 41 | 2026-09-11 | Revisar decisão de arte (ChatGPT) | **Virada para 3D low poly** (11/09, 22h21): *"Houve uma mudança e o jogo agora vai ser 3d low poly"* — no mesmo chat onde, dias antes, o ChatGPT tinha recomendado *não* migrar para 3D ainda. Sidinei pede visual "mais rústico" e mantém a logo antiga. | [2026-09-05_Revisar decisão de arte_convertido.md](Conversas/GPT/2026-09-05_Revisar%20decis%C3%A3o%20de%20arte_convertido.md) |
| 42 | 2026-09-14 | Nome para Tempera (ChatGPT) | "Têmpera" (bônus por uso contínuo da mesma arma) pede nome menos poético; ChatGPT sugere "Familiaridade". O nome que ficou no projeto é **Afinidade**. No mesmo dia o repo já aparece como `eras-do-brasil` no chat técnico. | [2026-09-14_Nome para Tempera_convertido.md](Conversas/GPT/2026-09-14_Nome%20para%20Tempera_convertido.md) |
| 43 | 2026-09-15 | Fusão assumida no código + pipeline de arte 3D (ChatGPT) | No chat técnico: *"escoria já não existe mais mas vou reaproveitar o estudo de arquitetura porque o jogo é o mesmo estilo e categoria só muda lore e mundo"* e, 40 minutos depois, **a primeira vez** que aparece *"eras do brasil será exatamente igual ao escoria"*. Em paralelo, o Project de arte do MVP produz o pipeline 3D (Blender → Godot, esqueleto com 6 sockets, 3.000 tris, as 4 zonas de A Travessia). | [chat técnico](Conversas/GPT/2026-08-26_Atual%20-%20Arquitetura%20Go%20do%20servidor_convertido.md) · [pipeline de arte](Conversas/GPT/2026-09-15_2%20-%20CHAT%201%20%E2%80%94%20Personagem%2C%20Esqueleto%20e%20Equipamento_convertido.md) |
| 44 | 2026-09-19 | Branch · Recomendação de jogo idle (ChatGPT) | No meio de uma busca por um idle para jogar, a frase: *"o game a escoria morreu ele virou eras do brasil que era outro que eu estava desenvolvendo e mesclei os 2"*. Rende a proposta (não implementada) de exploração automática por "ordens de comportamento", inspirada no jogo Wanderer. | [2026-09-19_Branch · Recomendação de jogo idle_convertido.md](Conversas/GPT/2026-09-19_Branch%20%C2%B7%20Recomenda%C3%A7%C3%A3o%20de%20jogo%20idle_convertido.md) |
| 45 | 2026-09-21 | World bootstrap implementation for Escoria (Claude) | Sidinei repete no Claude a frase dita no ChatGPT em 15/09 (*"eras do brasil será exatamente igual ao escoria"*) para construir o bootstrap do mundo a partir do repo arquivado da Escória. Documento oficial do projeto unificado lista o que deixou de existir (Lastro, deuses-em-armas, combate D20, zonas antigas, classes-como-classes). | [2026-09-21_World bootstrap implementation for Escoria.md](Conversas/Claude/2026-09-21_World%20bootstrap%20implementation%20for%20Escoria.md) |
| 46 | 2026-09-22 | Atual - Arquitetura Go do servidor (ChatGPT) | Sidinei explica os dois trilhos: *"antes quando o projeto era a escoria, eu estava usando o chatGPT… depois que mudou para o eras do brasil passei a usar o claude mas sinceramente não estou gostando muito do estilo de resposta dele"*, e diz que começou "o novo projeto do eras" no Claude em 1º/09. Decide criar um Project novo do Eras no ChatGPT. | [2026-08-26_Atual - Arquitetura Go do servidor_convertido.md](Conversas/GPT/2026-08-26_Atual%20-%20Arquitetura%20Go%20do%20servidor_convertido.md) |
| 47 | 2026-09-24 | Avaliação de projeto (Claude) + Reconstrução do projeto (ChatGPT) | Documentação normativa reorganizada no Claude; no mesmo dia, o **Project novo do ChatGPT passa num teste de contexto**, reconstruindo corretamente o estado do jogo e tratando "conceitos de A Escória" como histórico. Ver [estado real confirmado no repositório ativo](#estado-real-do-projeto-confirmado-no-repositório-ativo). | [2026-09-24_Avaliação de projeto e próximos passos.md](Conversas/Claude/2026-09-24_Avalia%C3%A7%C3%A3o%20de%20projeto%20e%20pr%C3%B3ximos%20passos.md) · [ChatGPT](Conversas/GPT/2026-09-24_Reconstru%C3%A7%C3%A3o%20do%20projeto_convertido.md) |

## Achado: o nome original era "1500 Caminhos do Brasil"

Ao validar a conversão do chat #2 (2023-07-01), percebi que o `.json` original tinha
uma mensagem que meu conversor estava descartando por engano: um documento de canvas
criado em **2025-04-17**, quando Sidinei voltou nesse chat antigo e pediu um "backup
resumido" para guardar como lembrança de como o jogo começou. Corrigi o conversor
(`converter_json.py`) para capturar esse tipo de conteúdo e o documento já está
incluído no arquivo do chat #2. Ele confirma, com data e tudo, que o nome de
trabalho original do jogo era **"1500 Caminhos do Brasil"** — mesmo nome que aparece
independentemente na conversa de WhatsApp do dia seguinte (chat #1), o que dá mais
confiança de que a reconstrução está certa.

## Validação dos chats já existentes

Os 6 arquivos que já estavam em `Conversas/GPT/` antes desta reorganização (convertidos
antigamente de HTML, não de JSON) foram comparados mensagem a mensagem com os `.json`
originais. Nenhum diálogo real está faltando — o HTML antigo até capturava *mais* linhas
(confirmações de sistema, resumos de memória automáticos e, em **RPG Eras do Brasil** e
**Setor Livro de Regras e Sistema**, o conteúdo bruto de documentos de canvas), mas nada
foi perdido. Não foram reconvertidos para não introduzir mudanças desnecessárias.

## Reorganização de `Conversas/Gemini/`

Os exports antigos `gemini-conversation (N).md` vinham de um plugin de navegador com um
bug que escondia parte do conteúdo (um deles chegou a exportar só a letra "c" no lugar
da data). O Sidinei refez manualmente os 6 exports relevantes — achou a conversa
correspondente no Gemini, exportou para o Google Docs e de lá para Markdown — e esses
são os que entraram na cronologia acima. Os 6 arquivos antigos (`(7)`, `(8)`, `(9)`,
`(12)`, `(13)`, `(15)`) foram removidos por estarem totalmente substituídos pelos novos;
os arquivos `(5)`, `(10)`, `(11)`, `(14)`, `(16)` já haviam sido removidos pelo Sidinei
antes desta reorganização.

Um detalhe: existiam dois exports idênticos de "Eras do Brasil, desenvolvimento do game"
(mesma data, mesma URL, mesmo conteúdo — só a formatação Markdown do Google Docs mudava
levemente escapes em blocos de código). Mantive só um.

O arquivo `eras-do-brasil-atividades.html` (um histórico de atividades do Gemini,
formato bem diferente das conversas individuais) não foi mexido — fica como pendência
abaixo.

## A era Copilot: o pivô de Unity para MUD Moderno (fev–mar/2026)

Antes do Claude, quem tocou o projeto por meses foi o **Copilot** — e é aqui, não em
14/03, que o pivô arquitetural de verdade acontece. Reconstruído a partir dos 11 logs
de sessão em [`Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/sessions/`](Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/sessions/)
(a cópia congelada do GDD de antes do jogo virar idle) e do log completo em
[`Conversas/Copilot/`](Conversas/Copilot/):

1. **11 e 13 de fevereiro de 2026 — ainda Unity.** Sprints de GDD (sistema de XP,
   troca de origem) e duas ADRs (organização do projeto Unity, workflow de UI/UX).
   O projeto tinha 38 POCs planejadas e 62 issues abertas no GitHub.
2. **7 de março de 2026 — diagnóstico.** Três sessões no mesmo dia: auditoria de
   ~120 arquivos do GDD; um diagnóstico honesto de 6 problemas (**"GDD 100% vs.
   código 0%"**, conhecimento fragmentado em 3 IAs, escopo descontrolado); e uma
   revisão de produto que confirma 90% do planejamento como sólido. Sidinei decide
   conscientemente adiar 4 gaps identificados (Steam/EA, i18n, etc.) para focar em
   execução.
3. **11 de março de 2026 — o pivô.** Frustração com **"3 anos de documentação sem
   nenhuma linha de código de jogo"** leva ao abandono do Unity Co-op P2P. **ADR-004**
   formaliza o novo rumo: **MUD Moderno** — servidor Go (goroutines, WebSocket),
   cliente web, arquitetura server-authoritative. ~30 arquivos do GDD reescritos ou
   arquivados na mesma sessão (Game Pitch, Project Plan, Roadmap).
4. **13 de março de 2026 — handover para o WSL.** Reestruturação física do repo
   (`game/server/`, `game/textClient/`), planejamento de comandos admin, e um
   "bota-fora" completo da sessão para não perder contexto na migração de ambiente
   (ZorinOS → WSL2) — preparando a virada para o Claude Code, que assume no dia
   seguinte.

## A era Claude: de MUD Moderno à fusão com Escória

A partir de 2026-03-14 o Claude assume o desenvolvimento no WSL, já com o pivô
arquitetural decidido pelo Copilot três dias antes. Essa fase tem um arco próprio,
reconstruído a partir de 47 conversas técnicas (ver [`Conversas/Claude/`](Conversas/Claude/)):

1. **Março–maio de 2026 — MUD Moderno.** O Eras do Brasil vira um MMORPG textual em Go
   (servidor autoritativo, cliente web), com arquitetura consolidada em ADRs, sistema
   de fofoca/conhecimento de NPCs, e a tese central **"o mundo não espera por herói"**
   (nascida em 17/03). A dúvida "devo trocar de linguagem?" volta 5 vezes em 2 meses —
   Claude nomeia isso como sintoma de cansaço, não problema técnico.
2. **Final de maio de 2026 — nasce um projeto paralelo.** Sidinei tenta encaixar
   elementos idle/ARPG no próprio Eras do Brasil (26/05); Claude recusa a mistura e
   pede uma escolha de gênero. A ideia migra para um spin-off **separado**, inspirado
   no Albion Online, batizado **"Albion Idle"** (31/05) — e cogita usar uma lore nova,
   **"Deuses-Armas"**, em vez do universo do Eras, com medo de desgastar o projeto
   principal.
3. **19 de junho de 2026 (não documentado — ver Pendências) — nasce "A Escória".** Em
   algum momento entre 31/05 e 23/06 o spin-off troca "Deuses-Armas" pelo nome
   **"A Escória"**, com codinome de repositório **"Outlander"**.
4. **23 de junho de 2026 — a decisão.** Sidinei pergunta explicitamente qual dos
   projetos priorizar. Claude recomenda A Escória/Outlander — não por ser melhor IP,
   mas por ser viável para um dev solo (o Eras do Brasil, com NPCs de rotina/fofoca/
   necessidades, é descrito como **"o pior primeiro projeto possível [...] jogo de
   estúdio de trinta pessoas"**). **O Eras do Brasil é congelado, não abandonado** —
   guarda-se a tese central para reaproveitar depois.
5. **Julho–agosto de 2026 — dois meses só de Escória/Outlander.** Arquitetura de
   servidor em Go, decisões de full loot, HTTP vs WebSocket, mockups de UI. Em 29 e
   31/08 a decisão de não mesclar os projetos é **reafirmada duas vezes**: *"Não
   mescle: a soma é um jogo maior que os dois, e mata os dois."*
6. **6 de setembro de 2026 — a fusão, sete dias depois.** Ao revisar a lore da
   Escória lado a lado com a do Eras, Claude reverte o próprio veredito: as duas
   "IPs" são o mesmo sistema por baixo (progressão paralela persistente, troca livre
   de build — como Albion/Orna). Proposta: **"o esqueleto da Escória, o mundo do
   Eras"** — a Escória nunca teve mundo próprio, e importar o do Eras custa quase
   zero em código. *"A Escória é o Eras com o número de série lixado."*
7. **11–24 de setembro de 2026 — consolidação.** A fusão vira fato de trabalho:
   backlog reestruturado, arquitetura de servidor sem coordenadas (só "zona"/"nó"),
   redesenho do tutorial (A Travessia, Feitoria da Cruz), bootstrap do mundo em
   21/09 (repetindo a frase dita no ChatGPT em 15/09: *"eras do brasil será
   exatamente igual ao escoria"*) e reorganização final da documentação em 24/09 —
   ponto onde este histórico para hoje.

## O lado ChatGPT (26/08–24/09)

O Claude não foi o único trilho desse período. Reconstruído a partir de 27 conversas
do ChatGPT (ver [`Conversas/GPT/`](Conversas/GPT/), arquivos de 2026-08 e 2026-09):

- **Por que dois trilhos.** Nas palavras do próprio Sidinei, em 22/09: *"antes quando o
  projeto era a escoria, eu estava usando o chatGPT… depois que mudou para o eras do
  brasil passei a usar o claude"*. Na prática os dois correram juntos: o **ChatGPT
  concentrou a implementação do servidor e a arte**; o **Claude, o design, a lore e as
  decisões de rumo**. Em 22/09 Sidinei decide voltar a ter um Project do Eras no
  ChatGPT, por não estar gostando do estilo de resposta do Claude; em 24/09 esse
  Project novo passa num teste de contexto.
- **Arquitetura.** O chat técnico "Atual - Arquitetura Go do servidor" ficou aberto de
  26/08 a 24/09 e foi ramificado duas vezes. A arquitetura oficial (comando → game loop
  com dono único do estado → eventos) já aparece na primeira resposta, em 26/08. Os
  ramos de 07/09 e 21/09 mostram o código regredindo para `PlayerManager + mutex`
  durante a implementação e sendo realinhado ao desenho original — não foi uma mudança
  de arquitetura em setembro. Postgres nunca foi questionado nesse trilho.
- **A decisão "qual projeto" vista pelo ChatGPT (28/08).** Um dia antes do Claude, o
  ChatGPT comparou Escória, Eras do Brasil e um terceiro projeto (RPG solo com LLM) e
  chegou ao mesmo lugar: *"Não mesclar os jogos em um só. Sim, mesclar conceitos."*
  Nenhum dos dois cogitava a fusão antes de 06/09.
- **A fusão vista pelo ChatGPT.** Não há um momento de decisão explícito desse lado — a
  fusão aparece já consumada: o repo vira `eras-do-brasil` sem anúncio (visto a partir
  de 14/09), e em 15/09 vem *"escoria já não existe mais"* e, pela primeira vez,
  *"eras do brasil será exatamente igual ao escoria"*. Em 19/09: *"o game a escoria
  morreu ele virou eras do brasil"*.
- **Direção de arte, em três passos.** 03–05/09: 2D cartum chibi vetorial, isométrico
  3/4 (Sidinei chega a pedir material de desenho para desenhar ele mesmo). 11/09: virada
  para **3D low poly**, contrariando a recomendação anterior do próprio ChatGPT de não
  migrar ainda. 15/09: pipeline de produção 3D montado (Blender → Godot, 6 sockets de
  equipamento, 3.000 tris, zonas de A Travessia).
- **Conceitos que passaram por aqui e mudaram depois.** As "Eras" I–IV com T1–T8 cada
  (09/09) foram abandonadas em favor de eras misturadas; "Têmpera" virou "Afinidade"
  (a sugestão do ChatGPT, "Familiaridade", não ficou).

### Estado real do projeto (confirmado no repositório ativo)

Tudo acima veio da interpretação dos chats. Fui conferir direto nos repositórios de
código para não ficar só na versão que o chat conta de si mesmo:

- **`eras-do-brasil-gdd`** (local, parado em 10/09/2026) é o **mesmo conteúdo** do
  `Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/` deste repositório — confirma que é a cópia congelada do GDD de
  antes da virada para idle, como o Sidinei apontou.
- **`eras-do-brasil`** (local, ativo até 23/09/2026 23:27) é o repositório unificado
  atual. O próprio `README.md` já abre confirmando a fusão na prática: *"Eras do
  brasil é um jogo idle [...] você é o que veste [...] árvore do destino do Albion
  Online adaptado para um cenário idle"* — mecânica 100% Escória, nome e ambientação
  100% Eras do Brasil.
- **Backlog do MVP** (`docs/backlog/00-mvp/BACKLOG.md`) confirma o que o chat de
  24/09 sugeria: fatias 1–3 (criação de conta, login, criação de personagem)
  **concluídas**; fatia 4 (entrar no mundo) **não iniciada** — é o próximo passo real.
- **Docs normativos confirmados no repo:** `contexto-do-projeto.md` (índice para o
  Project do ChatGPT), `o-jogo.md`, `decisoes-de-design.md`, `dados-do-mvp.md`,
  `formulas-e-balanceamento.md`, `direcao-de-arte.md`, `arquitetura-consolidada.md`,
  `historico-e-estudos.md`, `ROADMAP.md`.
- **Commits mais recentes** (todos de 23/09) são só limpeza de terminologia —
  removendo "PoC" em favor de "MVP" e consolidando documentos de promoção de dados.
  Nenhum código novo desde então; bate com o "próximo passo: fatia 4" do chat de 24/09.
- **Achado que o chat não mostra:** o `WORK_NOTES.md` do repo tem perguntas de design
  ainda em aberto (regras de PvP herdadas da página de PvP da Escória — fila de
  prioridade por consentimento, offline intocável, full loot só na fase 2; e uma
  dúvida não resolvida sobre se vale a pena o repo ainda citar "A Escória" pelo nome,
  agora que o Eras do Brasil é tratado como jogo "novo"). Parte disso vem das
  conversas do **ChatGPT** — as de 26/08 a 24/09 já estão em [O lado
  ChatGPT](#o-lado-chatgpt-26082409); o que veio depois de 24/09 ainda não foi
  exportado.

### Evolução do nome do jogo idle: Albion Idle → Deuses-Armas → A Escória → Outlander

| Nome | Quando | Contexto |
|---|---|---|
| *(sem nome, "mmo idle inspirado no Albion")* | 29/04 e 30/05/2026 | Ainda um conceito, não um projeto formal. |
| **Albion Idle** | 31/05/2026 | Nome de trabalho da PoC baseada nos dados públicos do Albion (`ao-data/ao-bin-dumps`). |
| **Deuses-Armas** | 31/05/2026 (mesma sessão) | Fantasia alternativa cogitada para não usar a lore do Eras do Brasil no spin-off. |
| **A Escória** / codinome **Outlander** | já consolidado em 23/06/2026 (transição não documentada — ver Pendências) | "Outlander" é o nome do repositório/código (`go mod init escoria`); "A Escória" é o nome do jogo/lore. |
| **Eras do Brasil** (repo `eras-do-brasil`) | decidido em 06/09/2026; repo renomeado de `escoria` para `eras-do-brasil` sem anúncio (visto a partir de 14/09) | Nome público prevalece após a fusão — mas tecnicamente é a arquitetura de A Escória por baixo. O repo antigo virou `escoria-arquivado`. Em 19/09: *"o game a escoria morreu ele virou eras do brasil"*. |

### Índice completo das sessões técnicas (`Conversas/Claude/`)

As 34 conversas abaixo (das 47 convertidas) não entraram na tabela principal — são
desenvolvimento técnico de detalhe, sem virar ponto de virada — mas estão todas em
`Conversas/Claude/` para consulta:

**MUD Moderno / refinamentos do GDD (mar–mai/2026):**
- `2026-04-04_GDD e conhecimento do projeto.md` — zona sem sub-locais no MVP; nasce a distinção NPC residente/itinerante.
- `2026-04-07_Escolher linguagem para servidor MMORPG textual.md` — cogita trocar Go por Node, reverte no mesmo chat; code review de WebSocket.
- `2026-04-17_Estrutura hierárquica do mapa mundi do jogo.md` — hierarquia Região→Zona→Sub-local; YAML para dados autorais.
- `2026-04-19_Design do client admin para gerenciamento do game.md` — client "modo Deus" em React + pub/sub por tópicos.
- `2026-04-21_Revisar estrutura de dados dos blocos do GDD.md` — schema de zonas corrigido; topologia final Vila↔Floresta↔Toca da Fera.
- `2026-04-21_Resumo de conversas recentes.md` — recap, sem decisão nova.
- `2026-04-25_Importando contexto de assistente de IA.md` — snapshot de preferências/regras de uso de IA.
- `2026-04-30_Ranking de linguagens para servidor MMORPG moderno.md` — Go reconfirmado (3ª vez).
- `2026-05-04_Refinamento 1.4 — movimento entre blocos e subzonas.md` — trânsito real de NPCs; expiração de conhecimento por tempo de jogo.
- `2026-05-11_Refinamento 1.5.md` — schema formal do sistema de fofoca/knowledge.
- `2026-05-23_Entendendo lazy e sweep no sistema de fofocas.md` — esclarecimento conceitual (sweep confirmado).

**Escória/Outlander — desenvolvimento técnico (mai–ago/2026):**
- `2026-05-30_Escolhendo plataforma de IA para projeto MMO idle.md` — o spin-off idle já existe como projeto distinto do Eras nesta data, ainda sem nome formal.
- `2026-06-23_Acesse a Wiki do albion: https....md` — pesquisa de referência (Destiny Board → "A Litania").
- `2026-07-21_Arquitetura de comunicação em MMORPGs idle.md` — padrão zona=loop/WS que reaparece em setembro.
- `2026-08-08_Identificando core loop e meta game em MMORPGs.md` — full loot como "dreno" que sustenta a economia.
- `2026-08-10_Full loot em MMORPG solo-dev: balanceando risco e retenção.md` — 3 abordagens de design de full loot.
- `2026-08-10_Ordenação parcial de eventos em EventBus Go.md` — padrões de concorrência para o EventBus.
- `2026-08-10_Testando respostas do Gemini em três cenários.md` — benchmark Gemini vs. Sonnet em 3 perguntas técnicas.
- `2026-08-17_Análise do jogo Oopsie Croco.md` — pesquisa de mercado idle/gacha; 1ª menção a "Eras do Brasil idle" antes da Escória existir formalmente.
- `2026-08-22_Escolher linguagem para jogo A Escoria.md` — Go confirmado para A Escória.
- `2026-08-24_Funcionamento teórico de servidores em Go.md` — arquitetura de zonas/goroutine que viraria decisão consolidada.
- `2026-08-29_Prompt para personagem 3D do game.md` — produção de asset (Lobo Lendário).
- `2026-08-29_Reorganizando carreira, projetos e uso de IA.md` — 1ª reafirmação "Escória primeiro, Eras congelado".
- `2026-08-29_Acesso a conteúdo de chat compartilhado.md` — nota curiosa: um chat do ChatGPT já se chamava "Com eras e escoria" antes da fusão formal.

**Pós-fusão (set/2026):**
- `2026-09-03_Mockup de interface para A Escória.md` — estilo pixel art (trocado por 3D low poly em 15/09).
- `2026-09-06_Arquitetura HTTP e WebSocket para jogo idle (20h06).md` e `(20h17).md` — WebSocket cortado da PoC em favor de HTTP + SSE.
- `2026-09-08_Comparação de jogos idle.md` — benchmark competitivo (Tibidle, Mu Idle RPG, etc.).
- `2026-09-11_Estrutura de backlog para desenvolvimento de jogo.md` — ROADMAP/BACKLOG/fatias já assumindo a fusão como fato.
- `2026-09-12_Arquitetura de MMORPG idle com backend autoritativo.md` — servidor sem coordenadas, só "zona"/"nó".
- `2026-09-15_Criador de mockups com ChatGPT MVP.md` — nomenclatura vira "MVP"; confirma **3D low poly**; "a arquitetura de A Escória é a que sobreviveu na fusão, só a lore que não".
- `2026-09-16_Estrutura da pasta data.md` — `data/` na raiz do monorepo, um JSON por conceito.
- `2026-09-19_Tutorial como travessia e limbo do mundo.md` — tutorial redesenhado como "A Travessia"; destino final Feitoria da Cruz/Costa do Pau-Brasil.
- `2026-09-20_Validação de valores do campo Risk.md` — validação de enum em Go.

### Índice das conversas ChatGPT de ago–set/2026 (`Conversas/GPT/`)

Das 27 conversas desse período, 12 estão na tabela principal. As outras 15:

**Servidor (implementação):**
- `2026-09-02_Branch · Servidor MMORPG em Go_convertido.md` — adota o modelo "dono único + canal de comandos" trazido por Sidinei; *"O banco não deveria ser o relógio do jogo."*
- `2026-09-04_Adaptar handler no http.go_convertido.md` — organização `server.go` / `network/http` / `network/ws`.
- `2026-09-05_Configurar PostgreSQL em Go_convertido.md` — `pgx`, migrations, Docker Compose; Postgres desde o início, sem ORM.
- `2026-09-07_Branch · Atual - Arquitetura Go do servidor_convertido.md` — ramo do chat técnico: login/JWT, middleware de autenticação, criação de personagem.
- `2026-09-15_Validar BodyType Go_convertido.md` — `BodyType` como tipo de domínio na criação de personagem.
- `2026-09-21_Branch · Branch · Atual - Arquitetura Go do servidor_convertido.md` — realinha o código ao desenho "dono único + canal" e confronta com o `arquitetura-consolidada.md` do repo: *"não é uma divergência arquitetural"*.

**Arte do MVP (Project de arte, 15/09):**
- `2026-09-15_1 - Atlas de paleta Ambiente_convertido.md` — paletas, kits das 4 zonas, mobs, ícones de recurso.
- `2026-09-15_1 - Gerar personagem base_convertido.md` — personagem base, esqueleto com 6 sockets, armas/armaduras T1–T2, NPCs.
- `2026-09-15_1 - Guia de UI Gamer_convertido.md` — prancha de UI com 8 blocos de HUD.
- `2026-09-15_Branch · 2 - CHAT 1 — Personagem, Esqueleto e Equipamento_convertido.md` — ramo do chat de personagem.
- `2026-09-15_Gerar personagem base_convertido.md` — teste de estilo do personagem "descartável".
- `2026-09-05_Recomendar materiais de desenho_convertido.md` — plano para Sidinei aprender a desenhar a arte em chibi (antes da virada para 3D).

**Referência e pesquisa:**
- `2026-09-07_Motivações Para O PvP_convertido.md` — motivações de PvP no Albion aplicadas à Escória: não uma justificativa única, mas várias.
- `2026-09-18_Escala de dano Albion_convertido.md` — Item Power do Albion; separar Tier de Poder de Item.
- `2026-09-22_Transformar prints em JSON_convertido.md` — prints de itens de referência convertidos em modelo de dados.

## Reorganização estrutural do repositório

As pastas soltas na raiz foram reagrupadas em dois eixos: **`Conversas/`** (por fonte
de IA — `GPT/`, `Gemini/`, `Claude/`, `WhatsApp/`, `Copilot/`) e **`Artefatos/`** (por
era do projeto, já que cada era é substituída pela seguinte — "histórico" não é uma
categoria à parte, é só a era que não é mais a atual):

| Pasta antiga | Pasta nova |
|---|---|
| `Conversas GPT/` | `Conversas/GPT/` |
| `Chats Gemini/` | `Conversas/Gemini/` |
| `Conversas Claude/` | `Conversas/Claude/` |
| `Conversas WhatsApp/` | `Conversas/WhatsApp/` |
| `Sessões copilot/` | `Conversas/Copilot/` |
| `Livros Antigos/` + `NotebookLM/` | `Artefatos/01-rpg-de-mesa-e-narrativa/` |
| `Decisoes Substituidas/` + `Docs Substituidos/` | `Artefatos/02-unity-tatico/` |
| `gdd-batalha-turno/` | `Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/` |

`gdd-batalha-turno/` entrou inteiro (não foi desmontado) por ser um snapshot de repo —
tem seu próprio `historico/` interno que já cobre desde a era Unity. `Imagens/` ficou
solta na raiz por não ter data confiável por arquivo para atribuir a uma era. Todos os
moves foram feitos com `git mv` (1746 arquivos, histórico de commits preservado).

## Pendências

Coisas encontradas durante a organização desta linha do tempo que ainda **não**
foram convertidas/incorporadas — ficam registradas aqui para não se perder de
novo:

- **`Conversas/Gemini/eras-do-brasil-atividades.html`** — histórico de atividades do Gemini
  (não é uma conversa individual). Ainda não mapeado nesta linha do tempo.
- **`Artefatos/01-rpg-de-mesa-e-narrativa/NotebookLM/`** — 15 notebooks, todos criados
  entre **09/11/2025 e 30/01/2026** (confirmado via `metadata.json` de cada um) —
  preenche exatamente o hiato entre os itens #13 e #14 da cronologia (Gemini). São
  análises/validações do GDD antigo (Livro de Classes, Livro de Regras, Enredo
  Principal) com `Sources/`, `Notes/`, `Chat History/` e `Artifacts/` por notebook.
  Ainda não lidos linha a linha — candidato à próxima passada de interpretação.
- **Chat "Marketing Era do Brasil"** (2025-05-01), encontrado no export antigo
  do ChatGPT (`2025-05-01_marketing-era-do-brasil_6814006c.json`) mas nunca
  citado/puxado para `Conversas/GPT/`. Parece ser o setor de marketing
  mencionado no chat #6 acima — candidato a próxima conversão.
- Outros setores citados no chat #6 (NPCs, inimigos, cenários/mapas, itens,
  recursos) não foram encontrados como chats separados no export — ou nunca
  foram criados, ou têm nomes diferentes dos esperados.
- **Mensagem de 2023-07-17** no fim da transcrição de WhatsApp (`@Emanuel Carvalho
  Responde ai...`) parece ser um questionário encaminhado, sem relação clara com o
  jogo — mantida na transcrição por estar no mesmo print, mas não entrou na cronologia
  acima.
- **"Chat 0 — Calibração" (2026-06-19)** — mencionado dentro do arquivo
  `2026-06-23_Próximo passo desenvolvimento do jogo Outlander.md` como a sessão onde
  "Deuses-Armas" virou "A Escória"/"Outlander", mas essa conversa **não está** entre
  os 203 exports do Claude disponíveis — provavelmente perdida (talvez excluída pelo
  Sidinei, como o próprio padrão de "limpar Projects antigos" descrito em setembro).
  Se aparecer em outro backup, é a peça que falta entre os itens #32 e #33 da
  cronologia.
- **Conversas do ChatGPT depois de 24/09/2026** — o export de 2026 vai até 25/09; o
  Project novo do Eras criado em 22–24/09 só tem o teste de contexto registrado. O que
  vier depois precisa de um novo export.
- **Export do ChatGPT de 2026 (50 chats)** — 27 entraram em `Conversas/GPT/`. Ficaram
  de fora 23: dúvidas genéricas de Go sem ligação com o projeto (fundamentos, `go get`,
  UUID, getters/setters, padrões de pasta, interface vs struct, listar rotas, `no rows`,
  autenticação genérica, middleware, hot reload, attach do VS Code), dois chats de
  estudo numerados ("1 - Fundamentos de Go", "2 - Arquitetura de Game Server", que se
  declaram independentes da Escória), a versão original do "Projeto RPG Solo com LLM"
  (só o terceiro projeto, sem comparar com os jogos), a "Recomendação de jogo idle"
  original (busca pessoal; o ramo de 19/09 entrou), "Engenharia reversa Unity"
  (Lootborne, sem ligação explícita), assuntos pessoais e dois chats vazios ("Gerar kit
  de cenário", "Versão dark do wallpaper"). O export completo continua em
  `/home/sidinei/Documentos/repartir gpt 2/chats/`, fora deste repositório.
- **Imagens geradas/anexadas nos chats do ChatGPT** — o export JSON só traz ponteiros,
  não os arquivos. Os mockups, pranchas e personagens gerados em set/2026 não estão
  neste repositório; nos `.md` aparecem como `[N imagem(ns) anexada(s)]`.
- **`Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/research/`** (`2026-03-07-pesquisa-mercado.md`,
  `diagnostico-completo-projeto.md`) e **`Artefatos/03-mud-moderno-pre-fusao/gdd-batalha-turno/historico/`**
  (`comparativo-gdd-legado-vs-atual.md`, `mapeamento-identificadores-codigo-markdown.md`)
  — lidos por cima ao confirmar a estrutura da pasta, mas não interpretados linha a
  linha para esta cronologia. Podem ter detalhes complementares aos 12 logs de sessão
  já incorporados.
- **`Conversas/Claude/`** cobre só os 47 arquivos (de 203 exportados) julgados
  relevantes por um agente de triagem — 27 ficaram de fora por menção incidental ao
  nome do jogo (ferramentas genéricas de IA, carreira, outros projetos). Se algo
  parecer faltando na reconstrução, a lista completa dos 203 nomes de arquivo ainda
  existe em `/home/sidinei/Documentos/repartir conversas claude/chats/` (fora deste
  repositório) menos os 47 já migrados.
- **`2026-06-23_Acesse a Wiki do albion: https....md`** e
  **`2026-08-10_Full loot em MMORPG solo-dev: balanceando risco e retenção.md`** têm
  `:` no nome do arquivo (herdado do título original da conversa) — funciona
  normalmente no Linux/ext4, mas pode causar problemas se este repositório for
  clonado em Windows/exFAT. Renomear se isso virar problema real.

## Como novos chats foram convertidos

Os `.json` do export do ChatGPT (formato `mapping` com árvore de mensagens)
foram convertidos com [`Conversas/GPT/converter_json.py`](Conversas/GPT/converter_json.py),
que segue a conversa a partir do `current_node` até a raiz (ramo principal,
ignorando edições/branches alternativos) e mantém só mensagens de texto de
`user`/`assistant` visíveis (descarta chamadas de ferramenta, raciocínio interno,
*system prompts* e placeholders vazios). Documentos de canvas entram inteiros;
mensagens com imagem mantêm o texto e marcam as imagens como
`[N imagem(ns) anexada(s)]`. Uso:

```bash
python3 converter_json.py <arquivo.json> <YYYY-MM-DD_Titulo_convertido.md>
```

O `converter.py` original (HTML → Markdown) continua no mesmo diretório para
referência, caso apareçam exports antigos em HTML.

Os exports do Claude (formato `chat_messages`, já lineares, sem árvore de branches)
foram convertidos com [`Conversas/Claude/converter_claude.py`](Conversas/Claude/converter_claude.py),
que mantém só blocos de texto visíveis de `human`/`assistant` (descarta `thinking`,
`tool_use`, `tool_result` e `injected_prompt_block` — ruído interno de execução de
ferramentas do Claude Code) e lista anexos por nome sem despejar o conteúdo (a maioria
é documento do próprio repo, redundante). Uso:

```bash
python3 converter_claude.py <arquivo.json> <YYYY-MM-DD_Titulo.md>
```
