# Mecânicas e Conteúdos — Catálogo do Eras do Brasil

> Inventário de **todas as mecânicas e conteúdos** que o Eras do Brasil (e os projetos que
> se fundiram a ele) já teve, de jul/2023 a out/2026: **o que era**, **quando surgiu**,
> **por que existiu**, **de onde veio a inspiração** e **o que aconteceu com ela**.
> Organizado por **sistema**, não por data. A cronologia está em
> [LINHA-DO-TEMPO.md](LINHA-DO-TEMPO.md).
>
> **Como foi feito:** varredura completa de `Conversas/` (WhatsApp, ChatGPT, Gemini,
> Copilot, Claude) e de `Artefatos/` (Livros Antigos, NotebookLM, GDDs Unity/MUD,
> Projects do Claude), em 14/10/2026. Citações entre aspas são literais. **"Motivo não
> declarado"** = a fonte não dá justificativa; **(inferência)** = leitura do
> levantamento, não fala de ninguém.

## Legenda das fases

Para não repetir datas longas, cada item indica a(s) fase(s) em que existiu:

| Fase | Período | Roupagem |
|---|---|---|
| **F1** | jul/2023 | *1500 Caminhos do Brasil* — RPG de turno digital (WhatsApp + ChatGPT) |
| **F2** | fev–ago/2025 | RPG de mesa de mundo persistente / Livros de Regras (ChatGPT) |
| **F3** | nov/2025 | Plano em fases + versão híbrida Eco offline / Raiz online (Gemini, NotebookLM) |
| **F4** | dez/2025–mar/2026 | RPG tático **co-op P2P** em Unity (NotebookLM, Copilot) |
| **F5** | mar–jun/2026 | **MUD Moderno** — MMORPG textual em Go (Copilot → Claude) |
| **F6** | mai–ago/2026 | Spin-off idle: Albion Idle → Deuses-Armas → **A Escória/Outlander** |
| **F7** | set/2026 | **Eras idle** — fusão Escória + Eras, MVP "A Travessia" |
| **F8** | out/2026 | **Eras novo** — turno instanciado com modo ativo + caçada automática, TypeScript |

---

## Resumo: o que dá para tirar disso tudo

**O DNA que sobreviveu a todas as fases** (aparece de F1 ou F2 até F8):

1. **Brasil colonial + folclore + a Raiz do Mundo** como universo.
2. **"Sua classe é o que você usa/veste"** — dito por Sidinei *já no WhatsApp de julho de
   2023*: *"Vai ser uma mistura de jogo de turno com albion. Ou New World. Com a pegada de
   sua classe é o que você usa"*. Voltou em F2 ("classe ativa define equipamento") e virou
   pilar absoluto em F6–F8.
3. **Matriz Qualidade × Raridade / tier + qualidade** — itens que importam e progridem.
4. **Lifeskills no mesmo peso que combate** — *"para a pessoa não ficar precisando
   escolher entre combate e lifeskills"* (F2).
5. **Mundo que não espera o herói** — NPCs com rotina, mundo que muda com ou sem o
   jogador, o jogador "não é o escolhido".
6. **Risco real na morte** (full loot → durabilidade → teto) — sempre debatido, nunca
   resolvido do mesmo jeito duas vezes.
7. **Recompensar quem está presente** sem punir quem precisa sair (pai de bebê).

**Os motivos que mais se repetem para criar ou matar mecânicas:**

- **Escopo de dev solo** — o motivo nº 1 de corte: co-op P2P (F4), congelamento do Eras
  ("sistemas de estúdio de 30 pessoas", F5), simulação de população, vilas dinâmicas,
  luta eterna de NPCs, Black Market.
- **Gosto pessoal como jogador** — Albion (amava "você é o que veste", odiava PvP
  forçado), Orna (troca de classe sem perder progresso), BDO (AFK e durabilidade com
  teto), Stoneshard/Kingdom Come (mundo vivo).
- **A vida real** — o bebê (dez/2024) gerou: idle, "offline congela", botão de pânico,
  "o atacado nunca fica sem defesa", turno pausável.
- **"Não quero ser o escolhido"** — atravessa F5 a F8 e moldou lore, temporadas e tutorial.
- **Não querer arte que não consegue produzir** — blocos em vez de mapa livre (F2),
  MUD textual (F5), pixel → chibi → 3D low poly (F6–F7).

**Referência dominante por fase:** F1 Pillars/Solasta/Baldur's Gate/Wartales · F2
Orna/Stoneshard/D&D · F3–F4 Dwarf Fortress/Kingdom Come/Solasta · F5 Fortnite
(temporadas)/Dwarf Fortress/RimWorld · F6–F7 **Albion Online** (de longe) · F8 Raven
Idle/Norroth/Dofus/BDO.

---

## 1. Conceito, gênero e pilares

- **RPG de turno digital "1500 Caminhos do Brasil"** (F1) — RPG de turno sobre a
  história do Brasil, com companheiros e 3 tipos de personagem. *Por quê:* uma reportagem
  sobre a independência da Bahia: *"umas cenas da galera brigando ai eu pensei oxi isso ai
  dar um RPG massa"* (WhatsApp, 02/07/2023). *Refs:* Pillars of Eternity, Wartales,
  Baldur's Gate, Solasta. *Destino:* parado ~19 meses.
- **RPG de mesa de mundo persistente** (F2) — *Por quê:* *"até para eu poder testar o
  sistema do jogo que vou desenvolver"*; mundo persistente "como são os jogos MMORPG".
  *Refs:* D&D 5e, Pathfinder, GURPS (como opções). *Destino:* virou "Fase 1 – criação das
  regras" do plano em fases.
- **Spin-off dungeon crawler com universos compartilhados** (F2, 23/02/2025) — Solasta/BG3
  + Dark and Darker; partidas curtas, sai com o inventário ou morre e perde tudo; cada
  jogador tem um universo que vira crônica; em co-op os personagens passam a existir no
  universo um do outro e reaparecem como NPC aliado/vilão. *Destino:* a IA recomendou
  separar; reaparece como "roguelite espiritual" (Modelo 2 do Enredo) e, de longe, no RPG
  Solo com LLM (ago/2026).
- **Plano em 5 fases: mesa → texto → digital 1 (blocos) → digital 2 (grid) →
  multiplayer** (F3) — *Por quê:* validar regras e arquitetura "com o cliente mais
  barato"; os livros servem de "regras de negócio". *Destino:* retomado no pivô MUD como
  "Fase 1-On".
- **Co-op P2P "Host = Dono do Eco / Viajante da Raiz"** (F4) — *"A visão final não é um
  MMO massivo, mas uma experiência de RPG profunda que pode ser compartilhada."* *Por quê:*
  medo de escopo: *"devido ao medo de escopo, devido a requisitos, e a dificuldades de
  implementação meu jogo foi mudando"*. *Refs:* BG3 co-op, Divinity: Original Sin.
  *Destino:* abandonado em 11/03/2026: *"o meu sonho era fazer um mmorpg mas ele se moldou
  para um rpg coop acho que isso até me desanimou."*
- **MUD Moderno server-authoritative** (F5) — MMORPG textual, Go, cliente web (PWA).
  *Por quê:* voltar ao MMORPG com o cliente mais barato possível ("texto antes de imagem").
  *Refs:* RuneScape (padrão de servidor), Melvor/RavenIdle (UI). *Destino:* Eras congelado
  em 23/06/2026.
- **North Star — "o mundo não espera por herói"** (F5, 17/03 → `north-star.md` 29/04) —
  *"O player não é o ponto central, e sim o mundo. O player é apenas mais um no mundo. Ele
  organicamente vira herói porque todos o veem como herói."* *Por quê:* *"todos eles são o
  escolhidos? então se todos são os escolhido praticamente ninguém é escolhido"*. *Refs:*
  Guild Wars 2, EVE (citados pelo Claude). *Destino:* Claude mandou guardar como "seu ativo
  criativo mais valioso"; volta em F7 ("forasteiro puxado pela Raiz").
- **Idle de gestão de heróis** (F5, 29/04) — vila com vagas, heróis aleatórios, expedições.
  *Por quê:* *"um jogo que eu quero muito jogar mas que não existe ainda"*. *Refs:* Evil
  Hunter Tycoon, Clash of Clans (escudo), Idlescape, Melvor. *Destino:* descartado no mesmo
  dia ("vou anotar a ideia guardar e focar no eras").
- **Eras como Action RPG idle** (F5, 26/05) — fila de skills, mundo semi-instanciado,
  temporadas sem reset. *Por quê:* *"criar um genero que não existe"*. *Refs:* Path of
  Exile, Diablo. *Destino:* **recusado pelo Claude** com 8 contradições (d20 + AFK, mobs
  evolutivos + AFK = exploit, "novo gênero é hype interno"…); a ideia migrou para outro
  projeto.
- **Albion Idle** (F6, 27–31/05) — releitura idle do Albion. *Por quê:* jogar "um MMORPG
  estilo Albion" sem ficar 100% no teclado; tempo livre virou "das 21h às 23h/00h" após o
  bebê; e servir de portfólio público. *Destino:* virou Deuses-Armas.
- **Deuses-Armas** (F6) — deuses enfraquecidos viram armas. *Por quê:* mitologia como
  banco de criaturas/skills; e não "gastar" a lore do Eras num spin-off (*"o idle vim
  primeiro e esfriar a novidade do eras"*); medo de IP do Albion. *Gatilho:* a música "God
  Is A Weapon" (Falling In Reverse). *Refs:* American Gods, Hunger Games, Darkest Dungeon.
  *Destino:* virou A Escória.
- **A Escória / Outlander — 5 pilares** (F6, 23/06) — 1) você é o que veste; 2) progredir
  é ceder; 3) zona define a ação; 4) o lore se descobre, não se explica; 5) idle com peso.
  *Refs:* Albion (sistemas), American Gods (tom). *Destino:* Claude recomendou Escória
  sobre Eras por ser viável solo; absorvida pelo Eras na fusão.
- **Fusão Escória + Eras** (F7, 06–08/09) — *"O Eras é o conteúdo; a Escória é o
  recipiente"* (Claude). Da Escória ficam arquitetura, fluxo da PoC e "gramática do
  Albion"; do Eras ficam mundo, eras, folclore, Raiz. *Por quê:* *"escoria já não existe
  mais mas vou reaproveitar… o jogo é o mesmo estilo e categoria só muda lore e mundo"*.
  (Datas divergem nas fontes: 06/09 na linha do tempo, 08/09 no Project do Claude.)
- **Eras idle "MMORPG idle de fantasia folclórica brasileira"** (F7) — loop *coletar →
  produzir → equipar → combater → progredir → atravessar*; MVP A Travessia. *Por quê:* *"não
  devemos ampliar o MVP antecipando o MMORPG completo"*. *Destino:* substituído em 03/10.
- **Turno instanciado com modo ativo + caçada automática** (F8, 03/10) — escolhido entre
  autobattle total, turno com pause, turno+auto e action. *Por quê:* precisava de camada
  ativa, de pausa natural (o bebê) e de ser viável solo; autobattle "mata a camada ativa",
  action é o mais caro. *Refs:* Raven Idle 2.0, Norroth. *Destino:* vigente — e em 14/10:
  *"o jogo esta totalmente indeciso"*.
- **Público "jogador CLT, cansado"** (F8) — *"fácil de entender, profundo para quem
  quiser"*; todo sistema tem padrão; ninguém precisa de wiki. *Refs:* Wakfu (complexidade
  desnecessária), Last Epoch.
- **Releitura declarada do Albion** (F6–F7) — *Por quê (Claude):* Melvor copiou RuneScape,
  Idle Clans copiou Melvor; "releitura é ótimo pitch e escopo perigoso". Mecânicas não têm
  direito autoral, nomes e arte sim → trocar nomes antes de lançar.
- **RPG Solo com LLM** (paralelo, 28/08/2026) — dungeon crawler de texto, engine decide,
  LLM narra. *Por quê:* *"sempre quis jogar RPG de mesa mas nunca achei pessoas… ser o
  mestre o player e os npcs não era tão bom, porque eu sabia o que iria acontecer"*.
  *Refs:* Solo Leveling, Dark and Darker. *Destino:* arquivado como estudo; princípio
  "engine = verdade, narrativa = casca" reaparece no Eras.

---

## 2. Regras base (sistema D20)

- **1d20 + mod. de atributo + bônus de proficiência vs. CD** (F2–F5) — CDs 5/10/13/16/18/20+.
  *Por quê:* *"RPG que as coisas são sempre resolvidas no dado como é baldurs gate"*.
  *Refs:* D&D, Baldur's Gate. *Destino:* "inegociável" no pivô MUD; **descartado** na
  Escória/Eras idle (RECON de 24/09 o lista como "fora do design atual").
- **6 atributos temáticos** (F2–F5) — Vigor, Força Bruta, Astúcia, Sabedoria Ancestral,
  Conhecimento, Presença (= CON/FOR/DES/SAB/INT/CAR). *Por quê:* Sidinei pediu "nomes mais
  temáticos". *Destino:* somem em F7–F8, onde **atributos derivam do equipamento** (como no
  Albion).
- **27 pontos, valores 1–6, mod. −2 a +3** (F2–F5) — Sidinei pediu "sistema simples cada
  ponto com limite"; a escala 8–15 estilo D&D virou 1–6. F5 adicionou +1 ponto nos níveis
  3/6/9/12/15.
- **Proficiência em 4 níveis** (F2–F5) — Aprendiz +1, Competente +2, Especialista +3,
  Mestre +4. Motivo não declarado (inferência: espelho de D&D).
- **Tipos de teste** (F2–F5) — simples, oposto, em grupo; nat 20 = acerto automático e dano
  **maximizado**; nat 1 = falha + **Vulnerável** (+2 contra você). **Sucesso parcial**
  (falhar por até 3) para *"evitar travamentos frustrantes"*.
- **Vantagem/desvantagem (2d20)** e **Defesa Base = 10 + Astúcia + armadura** (F2–F5) — a
  armadura faltava em um capítulo e foi corrigida pelo Copilot em 07/03/2026.
- **4 resistências** (F2–F5) — Física (Vigor), Mental (Presença), Espiritual (Sabedoria
  Ancestral), Reflexos (Astúcia).
- **Modos por regra de risco** (F2) — Narrativo, Aventura (durabilidade + fuga),
  Sobrevivência (full loot), Hardcore (permadeath). *Por quê (IA):* calibrar público.

---

## 3. Personagem: origens, classes e progressão de classe (era D20)

- **3 Origens: Colonizador, Indígena, Ser Folclórico** (F1–F5) — *Por quê:* *"o outro lado
  da história"*, classes de quem já habitava o Brasil; tensão entre três povos. *Destino:*
  **removidas em F7** (*"se o Eras for o Albion ao pé da letra, não posso escolher
  origem"*) — o jogador vira forasteiro; a escolha de "tradição de armadura" no tutorial
  substitui.
- **Bônus mecânico de origem** (F2) — ex.: Indígena +1 percepção/caça e contra veneno;
  Folclórico vantagem contra medo/maldição. Sidinei: *"eu quero o bonus mecanico"*.
- **Folclóricos famosos são NPCs, não classes** (F1–F2) — *"Não quero personagens
  conhecidos como classe eles serão npc no jogo"*; Saci e Iara deixam de ser jogáveis.
  *Por quê:* *"outros atos irão apresentar mais folclore do seu tempo histórico"*.
- **Origem decide o começo da história** (F1) — Colonizador começa em Portugal; Indígena e
  Folclórico no Brasil pré-Cabral; enredos se cruzam. *Destino:* vira Ato 1 comum em 2025.
- **12 classes Tier 1, 4 por origem** (F1–F5) — Conquistador, Explorador de Terras,
  Mosqueteiro, Missionário · Guerreiro Tribal, Caçador de Feras, Arqueiro Selvagem, Xamã
  Curandeiro · Guardião Ancestral, Lobo Lendário, Ser Elemental, Encantador de Espíritos.
  *Por quê:* *"pelo menos 1 tank, 1 dps e 1 suporte"*, depois DPS melee + DPS à distância
  por tipo; Missionário entrou porque *"igreja… foi bem importante na colonização"*.
  *Refs:* trindade de MMO. *Destino:* congeladas com o Eras (jun/2026); **morrem** em F7
  ("classes como classes" no vocabulário morto).
- **Classe = "conhecimento" ligado a uma arma** (F1) — *"cada classe será um conhecimento
  que meu personagem principal vai poder ter"*. *Destino:* vira Proficiência → Moeda de
  Classe.
- **Proficiência aprendida com companheiro** (F1) — classes ocultas "(???)" até recrutar o
  companheiro; você aprende *"vendo ele em combate e aprendendo aos poucos como ele luta"*;
  ao completar a quest dele, *"me ensina totalmente"*. *Refs:* Solasta, Baldur's Gate,
  Wartales. *Destino:* descartado em 2025 ("companheiros vamos reformular do zero").
- **Subclasses por Era** (F1) — especialização na mesma arma ou subclasse com arma nova.
  Sidinei temia que "pode ficar muito grande". *Destino:* substituídas pelos Tiers.
- **Classes históricas por Ato** (F1, rascunho) — Bandeirante, Capitão do Mato, Cangaceiro,
  Quilombola, Pirata, Abolicionista… *Destino:* descartadas.
- **Tiers 1–3 por classe** (F2–F5) — ex.: Missionário → Pregador da Luz → Arcanjo da Fé;
  Lobo → Sombra da Floresta → Avatar Lupino. *Por quê:* não *"obrigar a pessoa a ter que
  mudar de classe ao passar de era"* nem ficar *"preso em lançar mais era para lançar mais
  classe"*. F5: Tier 2 no nível 5, Tier 3 no 10 exigindo outra classe em Tier 2.
- **Moeda de Classe + NPC mentor + missão** (F2–F5) — *Por quê:* *"manter o jogador
  engajada em conseguir uma determinada moeda"*; progressão *"semelhante ao Orna"*.
  *Refs:* Orna, Hero of Aethric. *Destino:* auditoria do NotebookLM achou que quase nenhuma
  missão dava a moeda → **Regra 2-1-3**. Guardada em F7 ("vou guardar essa progressão do
  Eras").
- **Troca livre de classe fora de combate, XP separado** (F2–F5) — *"Não quero zerar a
  progressão toda vez que muda… quero tambem manter parte do aprendizado da classe
  anterior"*. *Ref:* Orna.
- **Herança: só ativas, nunca passivas** (F2–F5) — *"para permitir que ele monte builds"*
  sem empilhar passivas.
- **Equipamento só com a classe ativa** (F2) — *"Acho que isso dar um dinamismo bom da
  pessoa ficar ativando ou querendo ativar uma determinada classe"* — eco do "classe é o
  que você veste" de 2023.
- **Todas as classes visíveis desde o início** (F2–F5) — *"vai que ele decida mudar de
  origem quando ver uma classe que chamou atenção"*.
- **Dom da Revivência / troca de origem** (F2–F5) — a IA ofereceu 4 soluções; Sidinei
  escolheu evento mágico porque *"me permite eu trabalhar bastante nesse evento magico ou
  espiritual para trabalhar minha lore algo parecido com assassin's creed"* e abrir quick
  campaigns. *Refs:* Assassin's Creed, Baldur's Gate, Orna, Tree of Savior.
- **Espelho do Eco** (F3–F5) — consumível do fim do Ato 1 para trocar de origem (máx. 2
  úteis). Em 19/03/2026: troca de classe desde o início, de origem só com o Espelho.
- **Personagens secundários de outra origem compartilhando conta** (F2, futuro) — *Ref:*
  Tree of Savior.
- **1 ativa + 1 passiva por classe** (F2–F5) — ex.: Conquistador: Provocação Tática /
  Postura Inabalável; Xamã: Oferenda Curativa / Chamado dos Espíritos. Textos "a critério
  do mestre" reescritos porque não eram programáveis.
- **Equipamento inicial "tudo Muito Baixa"** (F2–F5) — *"eu quero os iniciais com todas as
  variantes baixa, para não começar no normal… qualquer item com melhoria… ja é valido"*.
- **PV por classe** (F2–F5) — a IA deu 3 opções; *"gostei a opção 2"* (PV base por papel):
  tanks 14, médios 12, frágeis 10.
- **Níveis 1–15 e XP** (F5) — curva 100/300/700…44.500; XP de combate, quest, exploração e
  roleplay.
- **Ficha com opções fechadas, não campo aberto** (F2) — *"para não dificultar quando
  adaptar para digital"*; PDF preenchível.
- **Classes boas para solo** (F4, análise do Gemini) — tanks e Caçador; Missionário e
  Explorador fracos sozinhos.

---

## 4. Identidade pelo equipamento e progressão (era Albion)

- **"Você é o que veste" — sem classes** (semente em F1; pilar em F6–F8) — sem classe,
  slots dão skills; trocar a peça tira as skills dela da fila. *Por quê:* o que Sidinei
  mais amava no Albion; em F8, "identificação": não descobrir no endgame que não se vê mais
  na classe (experiência do BDO). *Ref:* Albion. *Destino:* **mantido em todas as fases
  desde F6** — substituiu as 12 classes/3 origens.
- **Sem classe presa, sem alts** (F8) — trocar de caminho tem custo mas *"nunca joga o
  investimento fora"*.
- **Equipamento aparece no personagem** (F7–F8) — *"o equipamento não é apenas um número
  na interface"*; Sidinei sentia falta disso no Scapewatch. Foi o argumento central para
  3D modular.
- **Slots** — 4 (arma, cabeça, torso, botas) na Escória; 7 no Eras idle; 6 sockets no
  esqueleto 3D (mão principal, secundária, cabeça, torso, pés, costas).
- **Skills por arma: Q/W/passiva por família, E por arma** (F7) — Sidinei corrigiu o
  ChatGPT: *"no albion o E muda entre tipo de armas… o Q/W e passiva são o mesmo"*. Custo
  de cada arma nova = arte + 1 skill E.
- **3 árvores de arma (Físico, Projétil, Mágico) × 2 papéis** (F7) — *Por quê:* o Albion
  tem 20 kits, o Eras só aguenta 3; *"dividir é aditivo, juntar quebra build"*. Descartadas
  as 6 árvores (Lâminas, Contundentes…) e as 20 do Albion. Na Escória eram Guerreiro /
  Caçador / Conjurador.
- **Regra "Era não cria família de armas nova"** (F7) — orçamento por Era (0–2 famílias,
  3–6 variantes) para evitar "explosão de conteúdo".
- **3 linhas de armadura** (F7) — placa/couro/tecido → **pesada colonial, média indígena,
  leve encantada** (morrião/couraça/grevas; cocar/escaupil/alpercatas; carapuça/manto de
  retalhos/sandálias de piaçava). Torso carrega identidade; botas = logística (carga,
  viagem, fuga) porque *"sem posicionamento botas não podem ser sobre movimento"*.
  Escaupil como peça histórica real.
- **Tradições ≠ facções** (F7) — tradição do equipamento atravessa as eras; facção
  política é só da Era 1.
- **6 slots ativos + 4 passivos com prioridade** (F7) — pedido de Sidinei, "a alma do
  combate". *Refs:* Raven Idle, MU Idle Classic, Albion.
- **Atributos derivados do equipamento** (F8) — vida, energia, resistências vêm da peça.
  *Refs:* Albion; livros *Game Balance*, *Game Mechanics*.
- **Energia** como recurso comum das habilidades (F7).
- **Tiers T1–T8** (F6–F8) — Sidinei: *"Não existe t9, t10 e nem t11 no albion o máximo é
  t8… o tier está intimamente ligado ao quanto 'evoluída' é essa arma"*. **T1 = sucata sem
  dono, não craftável**; **T2 = as três tradições** (*"o Albion não tem nada para mostrar
  no T2, e você tem… O tutorial ensina o mundo pelo equipamento"*); T4 = base de PvP real.
  Na Escória: T1–T3 ruído, T4 cristaliza um deus, T8 irreversível ("progredir é ceder").
- **Poder de Item (IP) multiplicativo** (F7) — `1,0918^(IP/100)`, +9,18% a cada 100 IP;
  dano e energia escalam, recarga não. *Por quê:* *"qualidade e encantamento conseguem
  atravessar um tier"* (T4 obra-prima ≈ T5), senão misturar peças perde sentido.
  Recomendação: *"copiar a filosofia, não o sistema"*; teto de IP como sistema futuro.
- **Encantamento até +4, duas portas** (F8) — craft com material encantado (garantido, mais
  caro) ou encantar item existente (risco visível, falha reduz o teto, só até +3); +4
  exclusivo de crafter. *Refs:* refino do Albion; +N do Cabal (congelado).
- **Essência (ex-Sopro)** (F7) — recurso de encantamento, só de mob/chefe/baú. Renomeada
  porque *"não lembrava o que era o Sopro; mecânica que precisa ser lembrada já falhou"*.
- **Fama por uso → Destiny Board → A Litania → Árvore do Destino** (F6–F7) — fama vai ao nó
  do item usado; 4 ramos (combate, coleta, refino, craft); maestria dá IP (~30 níveis ≈ 1
  tier). *Ref:* Destiny Board do Albion. Renomeada em 14/09 porque *"item pode ter nome
  próprio, mecânica não"* (não "poetizar" nome de sistema).
- **Sem nível global e sem rebirth/prestige** (F7) — *"A progressão ocorre pelo que o
  jogador faz."* Prestige rejeitado por parte da audiência.
- **Têmpera → Afinidade** (F6–F7) — multiplicador 1,0→1,5 em 60 ações com a mesma arma;
  **congela offline**, reseta ao trocar de arma; visual "não é barra, é calor" (lâmina em
  âmbar). *Por quê:* *"recompensa por perseverança, não punição por troca"*; recompensar
  presença ativa; *"você se tornando esse conjunto de arma (classe)"*. **A única mecânica
  realmente "dele"** segundo o Claude (reproduzida de memória, ideia de contrato com a
  arma). O Claude a descartou como "overengineered" e Sidinei a trouxe de volta.
  Renomeada em 14/09 (*"algo mais genérico, ou menos poético… não pode ser
  especialização"*): ChatGPT sugeriu Familiaridade, ficou **Afinidade**. *Destino:* não
  aparece mais em F8.
- **Fama ≠ Lastro ≠ Têmpera** (F6) — três eixos que "nunca embolam". Lastro ("mito
  coagulado") era a moeda; **morreu** na fusão (vira "prata").
- **Maestria por arma** (F7) — +2 IP por nível até 100, a partir de T4. Registrada, fora do
  MVP.
- **Criação de personagem mínima** (F7) — só nome + BodyType (NORMAL_MALE/FEMALE), 1
  personagem por conta; conta sem nick. A criação não pode virar escolha de classe.

---

## 5. Lifeskills, crafting e economia

- **16 Proficiências de Vida em 3 grupos** (F2–F5) — Coleta (Caça, Pesca, Herborismo,
  Mineração, Exploração Espiritual), Refinamento (Couro, Fundição, Carpintaria Naval,
  Construção, Negociação), Produção (Culinária, Alquimia, Ferraria, Marcenaria, Tecelagem,
  Encantamento). *Por quê:* *"quero ter proficiência de lifeskill e proficiência de combate
  para a pessoa não ficar precisando escolher… Quero ter as principais profissões e
  lifeskills que tem nos mmorpg"*. Sidinei brigou para manter o Refinamento quando a IA o
  removeu. *Refs:* Albion, Orna, New World, Ravendawn.
- **Evolução por uso + NPC mestre + missão** (F2–F5) — *"não quero… avanço imediato ao
  encontrar o npc"*.
- **Bônus de XP de lifeskill por Tier da classe** (F2–F5) — Tier 1 coleta, 2 refino, 3
  craft, *"para a pessoa ter um incentivo de upar a classe progressivamente para ter o
  craft como objetivo"* (reverteu a decisão anterior de "sem bônus").
- **Qualidade do item pelo resultado do dado** (F2–F5) — *"a qualidade do item ser
  relacionado a quanto tirou"*: =CD Média, >CD+5 Alta, nat 20 Excelente; falha perde
  recursos.
- **Matriz 5×5 Qualidade × Raridade** (F2–F5) — Muito Baixa→Excelente × Comum→Lendário.
  *Por quê:* *"o que vou ganhar se eu usar um item de nível 5 ao invés do 1, o que vai
  fazer incentivar querer um item melhor?"* e *"qualidade e raridade possa ser combinados
  todas as opções, que seria 5x5"*; desde a Era 1 *"para poder ir ambientando e ensinando o
  player"*. Qualidade também mexe na CD das habilidades. *Ref:* Diablo (afixos). Um dos 3
  sistemas que Sidinei pediu para manter em 07/03/2026. *Destino:* em F7 vira tier +
  qualidade + encantamento.
- **Crafting com receita + recursos + local + proficiência** (F2–F5) — CD = 10 +
  raridade; tempos simples/intermediário/complexo. **Crafting contextual** (F5): craft só
  perto da estação, *"incentivar voltar à vila"*.
- **Cadeia coleta → refino → craft + Estações** (F6–F7) — 5 recursos × 6 tiers; refino em 5
  estações; craft em Forja/Posto/Torre. "Barracas" → "Estações", "Bigorna" → "Forja".
  Coleta por escolha de nó, sorteio só na qualidade.
- **Recursos com regeneração** (F2–F5) — Madeira 1–2 ticks, Erva 3–5, Minério Espiritual
  6–10, Flor do Eclipse só em evento; ResourceNodes fixos por zona em F5 (esgotamento
  distribui jogadores). Recursos regionais do Atlas: Madeira de Ferro, Erva-Lua (rio, à
  noite), Minério de Sangue, Cinzas Espirituais.
- **Recursos Espirituais exclusivos do online** (F3) — "portão de risco" do Eco para a Raiz.
  Removido com o modo offline.
- **Durabilidade, reparo, fusão e melhoria** (F2–F5) — usos por qualidade (3–5 até 17–20+);
  a 0 pode quebrar. Nota de Sidinei: *"durabilidade de item com opção de conserto caso não
  conserte quebra o item / lutar perde a durabilidade"*. Em F5 vira o custo da morte.
- **Durabilidade no Eras idle** (F7) — Sidinei corrigiu: *"no Albion as armas não
  desgastam com uso, só ferramentas"*; a via de desgaste é ser derrubado; conserto custa
  prata (sink). "Perda de XP" recusada pelo Claude (catraca).
- **Durabilidade em duas camadas: atual + teto** (F8) — teto cai com morte e falha de
  upgrade; teto 0 não destrói. *Ref:* BDO. *"Só não posso deixar o teto descer rápido se
  durabilidade for zero"*. **"Descarte de luxo"**: raro ruim vira material de restauração.
- **Kit de reparo por tipo** (F8) — recarregável em campo com material refinado. *Por
  quê:* levar refinado ao campo sem voltar sempre.
- **Moeda UC (Unidades Comerciais) + escambo** (F2–F5) — "criada pelas grandes caravanas";
  depois Lastro (F6) e prata (F7).
- **Economia regional dinâmica** (F2–F5) — −20% abundância, +30% escassez, +100% facção
  hostil; 5 tipos de comerciante.
- **Itens rituais/culturais/de missão** (F2–F5) — Incenso Ancestral, Chocalho, Tambor,
  Cocar; "chaves narrativas".
- **Protocolo de troca atômica P2P** (F4) — quarentena no host + rollback para evitar
  duplicação por Alt+F4. Removido no MUD (servidor autoritativo).
- **Loot tables com afixos e RNG com seed** (F3) — *Refs:* Diablo, Minecraft, Stardew.
  Proposta. Seed volta no RPG Solo e no mini RPG (simulação determinística).
- **Economia de jogador (alma do Albion)** (F6–F7) — *"pegar toda a alma do albion: você é o
  que veste, a economia toda feita por player, o full loot no pvp"*. *Risco levantado:*
  massa crítica (200 jogadores = sem mercado); a demanda do crafter depende de gente
  perdendo equipamento → ralos PvE, durabilidade, perda na morte. *Refs:* Albion, Milky
  Way Idle.
- **Artefatos: drop bruto que vira craft** (F7) — purificação exige reputação de facção;
  cria a profissão emergente de purificador. Artefato bruto só cai para sinalizado (liga
  ao PvP).
- **Inventário por peso + slots, Mula, Bolsa** (F6–F7) — peso enche antes do espaço;
  montaria = velocidade × carga; bolsa vai no socket das costas.
- **Transporte e teleporte com custo** (F7) — *"Carga não pode teleportar de graça"*;
  teleporte cobra por carga, só cidade a cidade. *"Parar significa parar, não voltar"*: o
  farm para quando enche a bolsa, sem teleporte — preserva a economia de transporte.
- **Black Market, Leilão, Codex, Guilda, Ranking** (F6–F7) — descartados/IDEIAS.md: exigem
  população.
- **Modelo de item em JSON a partir de prints** (F7, 22/09) — 20 prints de equipamentos de
  um jogo não nomeado; `valor` separado de `alteracao`. Motivo não declarado.

---

## 6. Combate

- **Turnos "estáticos" sem grid (Fase 1) e grid tático (Fase 2)** (F2–F5) — 6 ações
  (Ataque, Habilidade, Magia, Item, Defesa, Ação Especial), trindade tank/healer/DPS.
  *Por quê:* *"validar o núcleo matemático… antes de introduzir a complexidade de um grid"*;
  Sidinei temia fazer dois sistemas. *Refs:* Pokémon, Sea of Stars, Darkest Dungeon,
  Broken Ranks (estático); Solasta, Wartales, Stoneshard, Pathfinder (grid). Em 2023 o
  combate era "tempo real com pausa". *Destino:* o grid foi adiado e em 07/03/2026 Sidinei
  admitiu "posso até abrir mão".
- **Iniciativa 1d20 + Astúcia** (F2–F5) — "Paradoxo da Iniciativa" (quem entra tarde)
  resolvido: entra na próxima rodada.
- **8–9 condições de status** (F2–F5) — Envenenado, Derrubado, Atordoado, Assustado,
  Queimando, Congelado, Cego, Confuso (1d4) + Vulnerável.
- **6 tipos de dano** (F5) — Corte, Perfurante, Contundente, Espiritual (ignora armadura),
  Elemental, Veneno.
- **Magia: 4 fontes e 4 caminhos** (F2–F5) — Espiritual, Elemental, Mental, Ritualística;
  *"todos podem acessar magia"* porque nasce da Raiz. Concentração, contra-magia, magia
  mais forte por bioma/ciclo.
- **Fadiga Espiritual substitui Mana** (F2 → F5) — 3 usos de magia avançada → teste de
  Vigor; Chá de Erva-Lua reduz. Mana removida em 19/03/2026.
- **Sanidade → teste de Medo** (F5) — "Regra de Terror" das Ruínas vira Presença CD 13;
  Sanidade/Moral removida.
- **Combate consome tempo do mundo / Bolha de Combate** (F2–F5) — turno = meio tick, mundo
  segue em paralelo → no co-op a "Bolha" pausava o tempo → no MUD: *"o combate… como se
  fosse um bolha separada… porque se a pessoa não fazer uma ação no combate o tempo no
  mundo não pode parar"*.
- **Escalonamento co-op** (F4) — +75% de PV dos inimigos, sem aumentar dano (evitar
  hit-kill). Removido com o co-op.
- **Inimigos que evoluem ao matar o jogador** (F2 → F5) — nota de 2025: *"inimigos ganham
  xp ao vencer uma batalha contra você"* ("o ladrão que me roubou voltou como líder de um
  clã"). Em F5 (ADR-011): Normal → Veterano → Alfa → Lenda; migra de região ao bater o cap
  ("o prata muito bom que virou ouro"); proteções contra death farming; NPCs fofocam sobre
  o lobo perigoso. *Por quê:* *"acho maneiro um boss que upou tanto que ninguém ainda
  consegue matar"*; *"inimigos estáticos tornam a exploração previsível"*. *Destino:* MVP
  do MUD; o Claude lembrou que é incompatível com AFK; não volta depois.
- **Inimigos do Ato 1** (F2–F4) — Espírito Menor, Onça-Pintada (Bote Veloz), Capitão
  Bandeirante (drop garantido de Moeda de Classe), Guardião da Fenda. Simulação do
  NotebookLM: solo "altamente desafiador".
- **Auto-battler com fila de skills** (F6) — a fila pula as skills em cooldown, ataque
  básico entra na fila; o jogador "monta a fila e assiste". *Refs:* Albion Q/W/E, Gambits
  do FFXII.
- **Dois relógios, sem tick** (F7) — ataque básico a cada 1÷velocidade, cada skill com
  recarga própria; simulação por evento, linha do tempo para o cliente animar. O ciclo
  fixo "QQQQE" anterior era "placeholder consciente". *Ref:* Raven Idle.
- **Onda fechada, até 50 rodadas** (F7) — servidor resolve a onda inteira; "impasse" se
  passar. *Ref:* Sword X Staff.
- **Mobs em grupos/acampamentos escolhidos pelo jogador** (F7) — combate com a mesma forma
  da coleta; aleatoriedade na composição. *Ref:* camps do Albion.
- **Sem posicionamento no servidor (Decisão 7)** (F6–F7) — servidor nunca manda
  coordenada; teste: "o mesmo servidor alimentaria um cliente de texto?". Em F8 vira
  "posicionamento abstrato dentro do combate".
- **Turno com 3 filas (lanes)** (F8) — uma à frente e uma de cada lado; melee anda, ranged
  não, mas tem empurrar/saltar/teleportar. *Por quê:* identidade melee × ranged sem grid
  pesado. *Refs:* Darkest Dungeon (slots), Raven Idle 2.0, Norroth, Dofus.
- **Modo ativo + caçada automática no mesmo motor** (F8) — o auto é "modo espectador"; a IA
  do jogador usa o mesmo contrato que a dos monstros. *Refs:* HoMM3 quick combat, DCSS
  autofight, Pokémon Mystery Dungeon, Disgaea, FFXII gambits. Princípio: *"AFK entrega
  volume, ativo entrega qualidade"*.
- **Intenção do inimigo visível só no ativo** (F8) — compensa o ativo com informação.
- **Automação / presets** (F8) — prioridade (a própria barra), 1 condição por skill
  baseada em HP, preferência de alvo, regra de fuga; presets por tipo de luta. *Ref:*
  Dominus Automa ("demais por enquanto"). Em F7 se chamava "doutrina".
- **Botão de pânico** (F8) — pausa, não perde nem ganha nada; no PvP o auto assume. *Por
  quê:* "ninar o bebê".
- **Marca "houve ação manual"** (F8) — se você agiu manualmente, a morte custa o preço do
  ativo; fecha o exploit de "ir para o auto ao ver que vai morrer".
- **Fuga** (F2 → F8) — F2: teste de Atletismo/Destreza, falha = ataque de oportunidade. F6:
  "gato e rato" do gank. F7: fórmula `30% + 0,1×pontos − 0,08×anti-fuga`, piso 5%, teto
  75%; pontos de projétil, botas, montaria; Curupira dobra anti-fuga; contra a Raiz nada
  funciona. *Por quê:* sem fuga *"cada luta é ganhar ou sair morto"*; a chance não sobe a
  cada falha (decisão de Sidinei). **Largar Carga** (+4, descarta tudo) — descartada em F8
  porque a morte deixou de ser full loot. F8: fugir consome a ação; *"todo mundo possa
  fugir do seu jeito"*.
- **Combate de turno no RPG Solo** (ago/2026) — a ideia inicial era a LLM ser "mestre da
  batalha"; o ChatGPT recusou: *"A LLM é o diretor da batalha. Mas não o sistema de
  combate."*
- **Mini RPG / playground de combate** (F8, 08/10) — *"como um teste automatizado"*: lib
  pura com seed e simulação em massa antes de UI. Virou o playground do monorepo TS.

---

## 7. Morte, risco e PvP

O sistema mais debatido do projeto: mudou em quase todas as fases.

- **Full loot ao morrer** (F2) — nota de Sidinei: *"full loot morrer perde os itens"*; no
  dungeon crawler, *"perde tudo que carrega no inventário, antes de entrar ele pode guardar
  no bau"*. Modos: Normal (moedas + 1 item), Hardcore (tudo), espólio narrativo (NPC equipa
  o item); recuperar o corpo "estilo soulslike". *Refs:* Dark and Darker, Albion, New
  World.
- **Full loot sai do MVP** (F5, 17/03 — ADR-009) — *Por quê:* PK predatório transformaria
  quests em isca: *"o jogador forte só mata o fraco que está fazendo a quest"*.
- **Penalidade de morte PvE** (F5, ADR-010) — −10% do XP do nível (sem perder nível), −15%
  durabilidade, sem drop. *Por quê:* *"significativa sem ser punitiva a ponto de afastar
  jogadores casuais"*.
- **Full loot volta como alma do PvP — só na V2 e só em zona vermelha/preta** (F6). *Por
  quê:* full loot num idle sem filtro é "máquina caça-níquel que rouba" (Claude).
- **Três saídas para o risco solo** (10/08/2026) — zonas graduadas, seguro de itens
  (cartório colonial × pacto folclórico), loot parcial por slot. Pergunta de origem: manter
  o risco *"sem punir demais o solo e sem PvP forçado"*.
- **Gank com matchmaking por consentimento** (F6) — prioridade: 1) outro ganker; 2) quem
  viaja; 3) quem faz atividade; 4) quem está ocioso. **Offline é intocável**. Defesa =
  postura (enfrentar ou fugir) com o loadout único. *Destino:* **"gank por adjacência"
  morreu** em 12/09 (a zona é a unidade).
- **Sinalização invertida + contador de caçadores** (F7, proposta do Claude) — Sidinei
  lembrou que no Albion a flag é **mútua**; o Claude admitiu que num idle ninguém
  sinalizaria sem ganho → artefato bruto só cai para sinalizado.
- **PvP consentido e mútuo** (F7) — flag só liga/desliga na cidade; não sinalizado não pode
  ser atacado; quantos sinalizados há na zona é público; **O Faro** revela quem são.
  *Ref:* bandas do Albion.
- **Bandas de risco** (F6–F7) — Albion azul/amarela/vermelha/preta → Firme / Trêmula /
  Rachada (eixo = distorção da Raiz) → em 14/09 **Segura / Disputada / Mortal / Selvagem**.
  *Por quê da renomeação:* *"o jogador não deveria precisar lembrar que 'rachada' significa
  full loot"*. Selvagem só no Emaranhado, pós-lançamento. Disputada como "laboratório"
  antes da perda total.
- **Motivações para o PvP** (F7, 07/09) — Sidinei: *"Na Lore do albion qual a motivação
  para o pvp? E para o pk?"* → território, recursos, rivalidade, prestígio, vingança; *"PvP
  = consequência natural da sociedade"*. Divergiu do resultado final (PvP consentido).
- **"Zonas vivas" (segura ↔ letal por hora)** (29/08) — *"o risco deixa de ser onde e passa
  a ser quando"*. Guardada.
- **"O caminho de volta já é o castigo"** (F7) — com viagem em minutos reais, a morte
  contra mob pune pela viagem.
- **PvP do Eras novo** (F8) — ativo contra ativo, auto contra auto; o atacado recebe
  "aviso, não convite" e escolhe o modo; AFK = auto com preset de PvP; atacante não pode
  fugir nos primeiros turnos e *"se atacar e perder, perde mais"*; marcação de quem mata,
  lista de vingança; quem está em caçada automática nunca é atacado por ativos. *Por quê:*
  *"o atacado nunca fica sem defesa"*, ausência não é derrota (bebê no colo).
- **Morte no ativo × auto** (F8) — no ativo zera o teto de durabilidade; no auto só
  desgasta; todos perdem **parte do inventário carregado, com teto** (substitui o full
  loot).
- **Tempo limite do turno no PvP** (F8) — se estourar, o auto assume.

---

## 8. Mundo, mapa e tempo

### Mapa e movimento
- **Blocos de cenário conectados ("quadrantes")** (F2–F5) — setinhas para os quatro
  cantos, loja e NPC por bloco. *Por quê:* *"sou o único desenvolvedor… não tenho muitas
  habilidades com desenhos… iria me apegar bastante à IA para a parte visual"* e ter
  *"aonde salvar esse mundo persistente"*. *Refs:* formato novel, Zork, Myst, Azure
  Dragon's Treasure, Slay the Spire. *Destino:* manteve-se até o MUD.
- **Movimento livre por turno onde "o mundo faz o turno dele"** (F2, digital 2) — *"casa
  bem com o que eu falava sobre os ticks"*. *Ref:* Stoneshard.
- **Mesa também em blocos, mestre como guia** (F2) — *"o jogo na versão de mesa vai ser
  muito parecido com a versão digital 1"*.
- **Névoa de guerra** e **obstrução + percepção** (F2–F3) — NPC em bloco adjacente pode
  testemunhar crime (Percepção vs. Furtividade) e reportar.
- **8 tipos de ambiente** (F2) — Floresta, Montanha, Pântano, Vila, Ruínas, Costeira,
  Caverna, Sítio Místico.
- **Atlas da Mata Costeira (Ato 1)** (F3–F5) — 9 nós: Vila de São Tomé (hub), Rio das
  Marés, Floresta do Norte, Mina de Ouro, Toca da Fera, Acampamento Bandeirante, Pico da
  Neblina, Ruínas Queimadas, A Ruptura. Custos em ticks, atalho submerso. Regras de bioma:
  **Ciclo da Maré de 100 ticks** (Mina acessível só em janelas), Exaustão no Pico, Terror
  nas Ruínas. Em F5 o Claude se recusou a apagar: *"cada zona tem identidade mecânica e
  narrativa"*.
- **Mapa em 3 camadas** (F5) — mapa-múndi → regiões (8–15 zonas) → sub-locais (adiados).
  *Por quê:* *"o mapa não pode ser tão pequeno"* com muitos jogadores, NPCs e mobs. Princípio:
  a camada 3 não pode voltar "sob outro nome".
- **5 regiões em gradiente rumo à Raiz** (F5) — Mata Costeira (1–5), Sertão Distorcido,
  Serra dos Ecos, Pantanal Vivo, Coração da Raiz (20+). *"Quanto mais longe da Raiz, menos
  distorção."*
- **Zona como contêiner, sem X,Y** (F5) — "encontro" é estar na mesma zona.
- **Movimento = ação com duração real** (F5) — Vila→Floresta ~25 min; eventos no caminho.
- **POIs dentro do bloco** (F5, R1.4) — oficina do ferreiro, taverna, capela… O Claude
  tinha recusado "POIs como filtro de UI" por ser "Camada 3 disfarçada"; Sidinei os
  adotou depois.
- **Mundo semi-instanciado** (F5, 26/05) — proposto; sem persistência "não existe fofoca
  de NPC". Não adotado.
- **"Zona define a ação"** (F6–F7) — cada zona diz o que dá para coletar, lutar ou gankar,
  sem menu global. *Ref:* Forgotten Woods do Albion, como diferença para Melvor. Em F7:
  *"Zona é a unidade de gameplay"*.
- **Cenas estáticas por zona com janela do personagem agindo** (F6) — *"Ela ilustra; não
  informa."* *Refs:* Ragnarok, MU, Pristontale.
- **Eras lado a lado ao redor da Raiz** (F7, 08/09) — *"Era = região, distância da Raiz =
  tier e risco, bioma = a cara da região"*. *Por quê:* *"o tema do game é a raiz do mundo e
  a mistura de eras"*. *Ref:* Martlock/Lymhurst/Caerleon do Albion.
- **Continentes** (F7) — A Travessia (T1–T2), As Eras / Continente da Raiz (T1–T5/T6), O
  Emaranhado (T4/T6–T8, só zona preta, futuro). Coração da Raiz = Caerleon (passagem, não
  destino). *Ref:* Royal Continent × Outlands.
- **Zona = nó com tier; grafo, não linha** (F7) — "toda zona precisa de pelo menos dois
  caminhos"; facção por zona; geografia não reproduz o Brasil real.
- **Era 1 planejada: 22 zonas, 5 regiões, 41 materiais, 43 mobs** (F7) — Costa do
  Pau-Brasil, Mata dos Engenhos, Sertão de Dentro, Rio das Almas, Mata Sem Fim. Custo por
  era (~9 habilidades + ~24 artes): *"Isso é o que diz se o projeto cabe numa pessoa."*
- **Mundo do Eras novo** (F8) — servidor só conhece zonas e pontos de interesse; movimento
  livre por clique é do cliente; grupos de mobs visíveis no mapa (estilo Dofus); comuns
  pessoais, elites/chefes compartilhados. *Refs:* Norroth, Dofus/Wakfu.

### Eras como tempo histórico
- **Atos/Eras históricas** (F1) — 1497 Preparativos; 1500–1654 Descoberta e Colonização;
  1695–1789 Ouro e Diamantes; 1808–1822 Família Real e Independência; 1888–1889 Abolição e
  República. *Por quê:* *"desbloquear classes, itens, locais e npc no seu tempo histórico
  correto"*. Reencontrado em F7 como "doc antigo" (sem a era pré-colonial).
- **Sem viagem no tempo** (F1) — *"eu não quero permitir viagem no tempo, quero que cada
  exploração respeite seu ato"*. Em 2025 a Revivência reintroduz eras por visões ("não
  viajam no tempo… vivem numa realidade fragmentada"); em F7 a **mistura de eras vira a
  fantasia central**.
- **Exploração marítima** (F1) — navios, piratas, corsários. Descartada.

### Tempo
- **Sistema de Ticks** (F2–F5) — mover 1, coletar 1, falar 1, descanso curto 1 / longo 3;
  online = ticks invisíveis, offline = tick por ação. *Por quê:* o mundo avança com ou sem
  o jogador. *Refs:* Stoneshard, Wartales. 1 turno = 1 tick = 10 min (Cap. 2.9).
- **Tick Comutável (reativo/proativo)** (F3) — o mesmo `ProcessarTick()` em offline e
  online. Removido no co-op, recuperado no MUD.
- **Relógio da Ruptura — 500 ticks** (F3–F4) — Sinais (0–200), Instabilidade (201–400, CD
  +2), Colapso (401–500); depois "Mundo Quebrado" sem Game Over ("falha narrativa
  positiva"). *Por quê:* urgência real. *Refs:* enrage de MMO. *Destino:* absorvido pelas
  Temporadas.
- **Tempo Fluido (Heartbeat), Bolha e Tick Debt** (F4) — pulso do host no co-op; criticado
  por ter três relógios e deixar o jogador B "preso no tempo". Removido.
- **Decisão 16: tick deixa de ser mecânica** (F5, 17/03) — durações em tempo real, ciclo
  dia/noite, 4 períodos, 1 dia de jogo = 2–4 h reais; *"Turnos ficam exclusivamente pro
  combate"*. *Por quê:* *"estava pensando em um mmorpg deixaria os npcs e mobs se moverem
  em tempo real… movimentação por turno em servidor ja não vai dar certo"*.
- **Ciclos do mundo** (F2–F5) — Lua Nova abre portais, Lua Cheia +1 em magia, estações,
  Véu Enfraquecido ("a cada 7 dias o véu enfraquece por 24 h").
- **Tempo do RPG Solo** (ago/2026) — identificar item leva ~3 dias de jogo (ideia de
  Sidinei).

---

## 9. NPCs, mundo vivo e facções

- **NPCs com rotina, memória e conhecimento** (F2–F5) — *"tipo um stardew valley, ou
  kingdom come… se o npc 1 vai na taberna todo dia a noite e o npc 2 se encontrou tanto com
  o npc 1… o npc 2 começa as vezes ir na taberna"*. O jogador pode perguntar sobre locais,
  recursos e monstros. *Refs:* Stardew Valley, Kingdom Come, Stoneshard.
- **IA híbrida Agenda + Necessidades (Utility AI)** (F3–F5) — needs Fome/Sede/Energia/
  Social/Segurança, traits, humor e memórias. *Por quê:* o conflito de prioridades faz "a
  vida" emergir (o ferreiro larga a forja para comer). *Refs:* Dwarf Fortress, RimWorld,
  The Sims. Em F5 implementado com 3 needs (Fome, Fadiga, Solidão), sono e refeições
  emergindo do scoring: *"Todo npc precisa dormir pelo menos 8 horas… acorda… com fome"*;
  NPC *"não pode ficar andando toda hora"* para o player não correr atrás do comerciante.
- **Solidão com companhia por (bloco, POI)** (F5) — Tomás na forja e Naila na cabana não
  contam como "juntos".
- **Residentes vs. itinerantes** (F5) — Sidinei: como NPCs que nunca saem da vila trocam
  conhecimento? → caçador, guarda e mercador levam fofoca. Adiado.
- **knowledgeBase e Fofoca** (F3–F5) — dois NPCs no mesmo lugar trocam 1–2 informações;
  rumores Confirmado/Incerto/Falso/Emergente; expiração (5.000 ticks → 500 → 48 h de jogo);
  "Importante" não expira; anti-loop. R1.5 com cooldown por par, dedup, lazy + sweep. *Por
  quê:* o NPC ser fonte de informação que o jogador precisa. *Destino:* parcialmente
  implementada, congelada com o Eras. Em F7 a fofoca como mecânica de informação foi
  **rejeitada** (vira pedágio) → **boletim público** da zona.
- **Afinidade com NPC** (F2–F5) — Hostil a Leal; presente +2, trair −3; dá desconto e
  missões.
- **Ciclo de vida de NPC** (F2–F5) — nascem, envelhecem, morrem, deixam herdeiros.
- **Turnos de NPC por período** (F5) — o Aprendiz assume a forja à noite. *Por quê:* o
  serviço nunca fecha, não punir o casual.
- **Vilas dinâmicas** (F5, 29/04) — vagas por tier, NPCs migrantes, prosperidade, decay,
  sobreviventes de vilas destruídas. *Refs:* Ashes of Creation, Dwarf Fortress. O Claude
  chamou de "design febril"; arquivado (T2/T3). **Simulação de população** (reprodução,
  genética): rejeitada, "astronômica".
- **Companheiros** — F1: 1 por classe com cidade e história (Rodrigo em Lisboa, Jatobá,
  Yara…), modelo Solasta/BG/Pillars (não contratado, *"se junta pelo diálogo"*) escolhido
  sobre o Wartales (que o amigo Guilherme preferia). F2: mercenários, aliados de facção,
  animais, podem ir embora. F7: companheiros/mercenários cortados (*"multiplicam a
  complexidade"*).
- **6 tipos de facção** (F2–F5) — Espirituais (Guardiões da Mata, Filhos da Lua),
  Militares (Bandeirantes, Exército Colonial), Culturais (Ordem dos Cronistas),
  Mercenárias (Irmandade das Lâminas, Corsários do Atlântico), Comerciais (Caravanas do
  Ouro), Ocultas (Culto dos Olhos Selados, Sociedade dos Ecos). 5 níveis de reputação;
  **Progresso Global** compartilhado.
- **Bandeirantes de Sangue** (F3 → F5) — F3/F4: rival IA numa **corrida** (avança 1 bloco a
  cada 15 ticks) com sabotagem física/social/mística. F5 (ADR-007): facção antagonista NPC
  controlada pelo StoryManager. *Por quê:* a corrida era o substituto single/co-op da
  corrida de quests do MMO; com o MMO de volta, a corrida voltou a ser entre jogadores.
  *Ref:* New World (balanço de facções).
- **Folclóricos divididos: Restauradores × Fatalistas** (F5) — consertar o erro × usar o
  caos.
- **Reputação de facção** (F7) — adiada: *"não tenho nenhuma mecânica em cima disto"*; só
  a purificação de artefatos dava sentido.
- **Admin "Modo Deus"** (F5) — widgets, pausar/acelerar a simulação, console. *Por quê:*
  *"o admin é um grande observador… meu foco total antes de colocar o player é ter isso de
  ver todo o mundo funcionar por conta própria"*. Regra: sistema novo só está pronto quando
  tem widget. *Refs:* Dwarf Fortress, The Sims. **Ordem "criação divina"**: mundo → tempo →
  recursos → mobs → NPCs → needs → fofoca → missões → só então o player.

---

## 10. Missões, narrativa e temporadas

- **Quests lineares com 2–3 secundárias por local** (F1) — *"todo local de quest
  principal precisa no mínimo ter 2 ou 3 secundarias"*; a última quest da Era leva à
  próxima. Descartadas na forma em 2025.
- **Abertura narrada + prólogo-tutorial "valendo"** (F2) — o jogo *"pergunta o player quem
  é ele ou manda ele acordar… Ao criar o personagem a Campanha prólogo inicia, é um
  tutorial… já vai ser 'valendo'"*. Frase de abertura: *"Antes da primeira palavra, havia o
  Sussurro. Antes do primeiro império, havia a Raiz."*
- **Ato 1 "1497 – Sinais da Primeira Era"** (F2–F5) — 5 sessões (Sussurros na Floresta →
  A Primeira Ruptura); versão "Mundo Vivo" de 4 sessões com Relógio, Corrida e Guardião da
  Fenda; recompensa Moeda Universal ("Ouro da Raiz") + Espelho do Eco. *Por quê:* o Ato 1
  é o *"tutorial jogável do sistema"*. Epílogos: floresta floresce × "Bosque das Sombras".
- **18 mini-campanhas (6 por origem) com "Gancho Maior"** (F2–F5) — ex.: O Caçador que Não
  Voltou, O Tambor que Silenciou o Céu, Justiça das Mãos Sujas, O Ouro que Nunca Brilha,
  Os Relógios do Porto Morto, A Canção que Não Dorme, A Máscara do Vazio. *Por quê:* *"Eu
  quero ganchos maiores de campanha para cada mini campanha"*. Versão "Mundo Vivo" usa
  rotina de NPC e janelas de tick porque a auditoria disse que as missões tratavam NPCs
  como *"estátuas informativas"*. Sinergias com o Ato 1 (o Tambor congela o Relógio).
- **Adaptação de missão por classe** (F2–F5) — qualquer classe joga qualquer missão; o
  mundo *"responde ao estilo de cada personagem"*.
- **Regra 2-1-3** (F3–F4) — em cada 6 missões: 2 dão Moeda de Classe, 1 desbloqueia
  mentor, 3 padrão. *Por quê:* progressão rara e justa.
- **Linha Eco-Histórica (7 Rupturas)** (F2–F5) — 1497, 1530 Fogo da Coroa, 1584 Tratado
  do Silêncio, 1612 Lua sobre São Luís, 1640 Guerra dos Dois Reinos, 1661 O Alquimista de
  Salvador, 1680 Colônia do Sacramento. *Por quê:* fatos reais "reimaginados" como ganchos.
- **Quick Campaigns / Ecoera** (F2–F5) — uma cena em outra origem/classe; *"pode até abrir
  portas para fazer as quicks campanha"*. Termo "Ecoera" removido em 19/03/2026.
- **Recompensas mecânicas pequenas** (F2) — reroll 1×/sessão, "evita a morte 1×/jornada",
  "Relógio Invertido" (prever o turno do inimigo).
- **StoryManager / calendário de eventos com branching** (F3, F5) — invasão no tick 10.000;
  vitória = "Era da Reconstrução", derrota = "Era da Ocupação". *Por quê:* *"o mundo é o
  protagonista e os jogadores são atores"*. *Refs:* WoW (parque temático) × EVE / Ultima
  Online (simulação). Removido no co-op, recuperado no MUD.
- **Quests competitivas ("Corrida pela Recompensa")** (F3, F5) — o primeiro a entregar
  leva tudo; quem já aceitou e entrega no timeout leva parte; verificação no servidor
  contra alt-farming. *Por quê:* *"um mmorpg onde o npc entrega a quest e ele fala sobre
  outros players que ele ja pediu, e isso virar uma disputa"*. Removida no co-op
  ("completamente ausente"), recuperada no MUD.
- **Quadro de missões e de requisitos de materiais / BountyManager** (F3, F5) — metas
  coletivas ("100 couros"), thresholds, consequência se falhar. *Por quê:* o NPC ser alguém
  que o jogador *"vai querer falar"*. *Refs:* EVE, Ultima Online.
- **"Quests não são tarefas, são necessidades do mundo"** (F5) — se ninguém faz, outro
  jogador faz, o mundo se vira, ou a necessidade muda de forma.
- **Votação nas escolhas de história** (F3, F5) — "votar jogando" ou votação diegética de
  24 h (executar, prender ou libertar); no MUD, maioria simples. Crítica: guilda grande
  vota em bloco.
- **Temporadas — ciclos longos sem reset de personagem** (F5) — 4–6 meses, mundo muda
  permanentemente, uma feature de sistema por temporada. *Por quê:* *"o que o fortinet faz
  com as sessons"* — quem não estava lá só *"vai ficar sabendo de como aconteceu"*. *Refs:*
  Fortnite, PoE/Diablo, Destiny; Claude: Caves of Qud. Absorveu o Relógio da Ruptura.
  Fechamento em 3 estados (Tensão, Apogeu, Legado) por threshold coletivo — guerra de 7
  dias simulada era "bomba nuclear", Sidinei: *"esse é o ponto chave do meu jogo… posso
  implementar de maneiras mais simples"*. Em F7: adiado (*"temporada é o que vai distanciar
  do Albion; só depois de lançar"*), com a **regra do resíduo** (todo evento deixa marca
  permanente).
- **Legado "Eu Estava Lá"** (F3, F5) — nome no desfecho, NPCs que lembram, placa dos
  heróis (ou dos que "não conseguiram conter"), itens limitados ao número de participantes,
  títulos Pioneiro/Participante/Historiador. *Por quê:* legado e FOMO saudável sem punir
  casual.
- **Raiz e Eco híbridos** (F3) — Eco = campanha offline pessoal; Raiz = mundo online com
  temporadas. *Por quê:* *"cura o FOMO"*. Removido no co-op e de vez no MUD.
- **Ecos Instanciados** (F5 → F7) — reviver temporadas passadas em instância solo, menos
  épica, sem item exclusivo. Em F7: Ecos = dungeons instanciadas (como as solo dungeons do
  Albion).
- **Justificativa do conflito** (F4, 18/02/2026) — escolhidas a "Febre da Raiz" (feras sob
  Dissonância) e a "Extração da Alma" (Bandeirantes sugam Ecos); herói como *"resposta
  imunológica de um mundo agonizante"*.
- **Causa da Ruptura de 1497** (F5) — um Folclórico tenta usar a Raiz para proteger a terra
  do presságio, o ritual falha e a tempestade desvia Cabral. *Por quê:* *"boas intenções
  com resultado catastrófico é mais interessante que vilão genérico"*. Em F7, o Claude
  rejeitou reaproveitar isso (conceito superado); **causa da Ruptura fica em aberto de
  propósito**.
- **Guardião da Fenda** (F4–F5) — boss do Ato 1; vira "sistema imunológico" da Raiz, não
  vilão.
- **Remoção do "Desperto/Escolhido"** (F5, ADR-007) — *"todo mundo é o escolhido quebra a
  suspensão de descrença"*; o Dom passa a ser adaptação natural à Raiz.
- **Tutorial de 8 passos (Escória)** (F6) — chegada → 1ª arma → 1º combate → coleta →
  forja → outro portador → 2ª arma → saída. *Ref:* tutorial do Albion, consultado *"para
  não inventar"*; só a lição "uma coisa por vez". Implementado como máquina de estados em
  dados. 22 blocos de diálogo + 11 barks; chave temática *"você só assina depois"*.
- **A Travessia — continente-tutorial descartável** (F7, 19/09) — 4 zonas (A Beira, Porto
  de Passagem, Mata Revirada, Pedreira Torta), T1–T2, segura, nunca revisitada, 18 passos.
  *Por quê:* desacoplar o MVP do mundo; *"você não volta porque estava indo"*. *Refs:*
  ilha tutorial do Albion, Pillars of Eternity 2 (jogador não escolhido). PoC → MVP porque
  *"não era prova de conceito e sim o mínimo produto viável"*.

---

## 11. Lore e conteúdo do mundo

- **Raiz do Mundo** (F2–F8) — teia espiritual que conecta eras, culturas e memórias; viva
  para indígenas, criação divina para missionários, consciência das histórias para
  folclóricos. *Por quê:* justificar a troca de origem e a mistura de eras. Metáfora do
  tear (Raiz = urdidura, ticks = pente). Em F7: o jogador é *"um forasteiro puxado pela
  Raiz"*, a Raiz visível no skybox da Travessia. **O núcleo imutável do universo.**
- **Dom da Revivência** (F2–F5) — viver memórias de vidas que nunca viveu; justificou troca
  de classe/origem/era.
- **Rupturas** (F2–F5) — fissuras entre eras com monstros híbridos e dungeons espirituais.
- **"Eco" — o termo que mudou de sentido 4 vezes** — fragmento/artefato (F2) → campanha
  offline pessoal (F3) → sessão co-op do host (F4, "Sincronia dos Ecos": *"Caminhamos em
  nossos próprios sonhos, mas nas horas mais sombrias a Raiz nos permite sonhar juntos"*)
  → instância de temporada passada (F5–F7).
- **Elementos do Ato 1** (F2) — Fragmento de Eco, "Aquele que Sonha as Eras", Trilha das
  Raízes, Pedra do Chamado, Cavernas do Sussurro.
- **Folclore e bestiário** (F1–F7) — Saci, Curupira, Iara, Boitatá, Boto, Caipora, Cuca,
  Mapinguari, Anhangá, Jurupari, Ipupiara; em F7 pesquisa de folclore atestado no séc. XVI
  (Boitatá por Anchieta 1560, Ipupiara por Gandavo 1576). Leituras sugeridas: Boris
  Fausto, Laurentino Gomes, Lilia Schwarcz.
- **Lore da Escória** (F6) — mapa entre panteões (A Margem, As Carcaças, As Encruzilhadas,
  A Forja Calada, A Fome); antagonista o Incrédulo; monstros Mitos sem Pacto; o Catador
  (*"NÃO é o escolhido"*); o Guia (ex-portador que parou perto do T8 por medo); zonas A
  Ressaca, A Bigorna, O Verde Surdo, A Costela. Tom metalúrgico mantido porque *"pode
  trazer uma narrativa boa principalmente em jogo onde deuses são armas… nunca vi o
  principal não ser o heroi"*. *Refs:* American Gods. *Destino:* **morreu na fusão**.
- **Críticas de Sidinei à lore da Escória** (F7, 06/09) — *"muito dark"*, motivos fracos:
  por que os deuses foram para as armas, qual a motivação do player. Claude: *"a lore não é
  sua"*. Nova premissa "panteões vivos em guerra fria de cultos" (a arma como altar
  portátil) — também morta na fusão.
- **Lore mínima viável** (F7) — *"Albion é sandbox, precisa de vazio"*: premissa + ~10
  nomes + "o que não está decidido".
- **Regra "material de IA = brainstorm"** (F7, 08/09) — duas lores de IA convergiram no
  mesmo motivo = *"o caminho estatístico mais genérico"* → reescrever à mão.
- **Conteúdo da Travessia** (F7) — NPCs Bartolomeu, o Língua (intérprete) e A Barqueira
  (*"ninguém que embarcou voltou para perguntar"*), O Ferramenteiro; facção dos **Perdidos**
  (*"Gente que a Raiz puxou antes de você e que não chegou do outro lado"*; reusam o
  esqueleto do jogador, custam quase nada de arte); mini-chefe **O Primeiro Perdido**; mobs
  Caranguejo da Beira, Cascalho Vivo, Macaco Revirado, Morcego da Torta. Armas T1 Lâmina
  Crua/Broquel Cru; T2 Espada de lado, Zarabatana, Cabaça de Boitatá, Rodela, Patuá.
- **Regras de texto** (F7) — sem vocabulário técnico no jogo ("servidor", "tick"); sem
  fantasia europeia (castelo, elfo, orc); escaupil *"sem virar estereótipo"*.

---

## 12. Idle e automação

- **Spin-offs de treino** (F4) — Idle "Ticks da Raiz", card game, quiz. Arquivados em
  07/03/2026 como *"procrastinação disfarçada de preparação"* — o idle voltou sozinho dois
  meses depois.
- **Idle sem progresso offline / "idle com presença"** (F5–F8) — *"não quero que avance
  sozinho tipo o idle champions… quero que a pessoa esteja no minimo com o jogo rodando"*;
  *"Quero recompensar e premiar quem vai 'jogar'"*. Idle = "sem APM exigido, não joga
  sozinho enquanto você dorme". Offline **congela, não decai** (Melvor "errou" ao decair).
  Em F8: *"AFK faz de tudo, mas reduzido"*.
- **Idle com animação, não "idle de menu"** (F7) — *"quero um idle com animação, ver o
  boneco coletar, lutar"*. *Refs:* Femur Idle, Ygg Idle, Tibidle, MU Idle, Epic Idle
  Journey.
- **Idle como "segundo foco" no trabalho** (19/09) — exigências de Sidinei ao procurar um
  idle: fantasia, sem cara de planilha (Melvor), sem AI slop, sem exigir movimento.
- **Ordens de comportamento** (F7, proposta) — explorar/caçar/coletar com plano B e
  condições de emergência; o equipamento define quais comportamentos existem. *Ref:*
  Wanderer. Sidinei achou "sensacional… um bom estudo". Não implementado.
- **Caça automática rende menos** (F8) — menos recurso e drop raro bem menor que o ativo;
  chefes fora do auto.
- **Peso e carga como limite do auto** (F8).
- **Mini Mode / janela pequena** (F7–F8) — "um super futuro".
- **Medo de saturação do idle** (28/09) — o Claude respondeu que o sonho é "ter feito um
  MMORPG" e idle é *"o que torna o MMORPG viável para você"*.

---

## 13. Multiplayer e modos

- **Co-op leve e personagens que coexistem nos universos** (F2, spin-off).
- **Online × offline** (F2–F3) — online com ticks globais, offline tick por ação;
  personagens de mesa migram para o digital.
- **Co-op P2P Host/Viajante** (F4) — save no PC do host; só o host decide narrativa crítica;
  anti-grief ("Sincronia de Intenção" contra o viajante que queima ticks). Abandonado.
- **MMORPG de mundo único** (F5–F7) — servidor autoritativo; HTTP até entrar no mundo,
  depois WebSocket com comandos e eventos; sem coordenadas.
- **Modos PvE/PvP/Ironman/permadeath** (F2) — sugeridos pela IA, nunca desenhados.

---

## 14. Arte, UI e áudio

- **2D por limitação** (F1) — *"Acho que 2D seria melhor para nós, mas se rolasse um 3d
  seria massa"*; o amigo avisou que 3D demora.
- **Pixel art moderna com identidade brasileira** (F2–F5) — tons terrosos, roxos
  espirituais, grid 32×32, UI "ritualística" (madeira, cordas, penas), fontes Londrina
  Solid / TinyUnicode / Press Start 2P. *Refs:* Sea of Stars, Wartales, Solasta, Children
  of Morta, Stoneshard, Eastward, Blasphemous, Octopath, Chained Echoes.
- **Layout "sanduíche"** (F4, 14/02/2026) — topo com relógio de ticks, cena no centro,
  pergaminho/botões embaixo; dano "math-transparent".
- **Mapa de nós estilo Slay the Spire + modo cena** (F4–F5) — *Refs:* Slay the Spire,
  Roadwarden.
- **Mockup do MUD: 4 painéis e UI contextual** (F5) — personagem, narrativa, mapa de nós +
  quests, feed do mundo; craft só perto de estação. *Refs:* Fallen London, Roadwarden,
  Stoneshard, Melvor.
- **Pixel isométrico "amador competente"** (F6, 29/08) — 32×32, ≤16 cores, âmbar como
  único acento. *Por quê:* custo para um dev sem arte; *"se parecer profissional demais,
  está errado"*. *Refs:* Diablo 2, MU, Ultima Online.
- **Cartum vetorial chibi** (F6, 03/09) — *"NÃO pixel art, NÃO pintura realista"*, contorno
  grosso, ≤3 tons; Sidinei ia desenhar à mão: *"deixe mais lofi"* → biblioteca mínima de
  10–15 assets "como LEGO"; treino de desenho com caderno e lapiseira porque *"nunca
  desenhei"*.
- **Isométrico simplificado** (F6–F7) — mostra personagem e equipamento ao mesmo tempo.
- **3D low poly** (F7, 08–11/09) — *Por quê:* em 2D cada peça × direções × poses (162
  peças só de armadura na Era 1); em 3D uma peça encaixa no osso. Estilo rústico porque o
  anterior era *"muito infantilizado e 'muito profissional', preciso de algo mais rústico
  porque estarei aprendendo"*. Esqueleto humano único com 6 sockets; personagem até 3.000
  tris; atlas de paleta 256×256; ícones renderizados do 3D, *"nunca desenho à mão"*. O
  ChatGPT tinha preferido chibi: *"eu não acho que você deveria gastar meses aprendendo
  Blender antes de descobrir se o core… é divertido"*. Chibi 3D × 6 cabeças ficou em aberto.
- **Paleta urucum + jenipapo** (F7) — as tintas corporais tupis.
- **HUD funcional: o loadout é protagonista** (F6–F7) — *"Arma equipada → kit de skills →
  fila → combate"*, não botões Personagem/Inventário; painéis fixos, lido de relance.
- **Câmera 3D levemente inclinada** (F8) — como o Raven Idle; cada item muda o visual.
- **Nenhuma arte final gerada por IA** (F6) — conceitos de IA são "norte, não asset"; a
  Steam exige divulgação.
- **Música** (F4, 30/01/2026) — viola caipira, pífano, atabaque, berimbau, coro em Tupi;
  tic-tac de madeira que acelera com o Relógio; tema "Ecos da Raiz". *Refs:* Skyrim,
  Witcher, Zelda BotW. Ferramentas Suno/Udio. Só material de pitch; trilha nunca
  implementada. **Trailer de voz** (07/12/2025): *"Disseram que a história foi escrita em
  1500… Eles mentiram… 500 Ticks… Qual passado você vai salvar?"*

---

## 15. Referências externas — quem inspirou o quê

| Referência | O que emprestou | Fases |
|---|---|---|
| **Albion Online** | Você é o que veste, tiers T1–T8, IP, Destiny Board, Q/W/E, economia de jogador, artefatos, bandas de risco, Caerleon, tutorial na ilha, refino, mula/bolsa, "zona define a ação", lifeskills | F1 (citado), F2, F6–F8 — **a mais citada do projeto** |
| **Solasta / Baldur's Gate / Pillars / Wartales** | RPG de turno, companheiros, diálogos que mudam o rumo, d20 | F1–F4 |
| **Stoneshard** | Movimento por turno em que o mundo também age; ticks | F2–F4 |
| **Orna / Hero of Aethric / Tree of Savior** | Troca de classe sem perder progresso, Moeda de Classe, alts compartilhando conta | F2–F5 |
| **D&D / Pathfinder** | Sistema D20, CDs, vantagem | F2–F5 |
| **Stardew / Kingdom Come / Dwarf Fortress / RimWorld / The Sims** | NPCs com rotina, necessidades, memória; admin "modo Deus" | F2–F5 |
| **Fortnite / Destiny / PoE / Diablo** | Temporadas que mudam o mundo | F5 |
| **EVE / Ultima Online / Guild Wars 2** | Mundo como protagonista (contra o "parque temático" do WoW) | F3–F5 |
| **Sea of Stars / Pokémon / Darkest Dungeon** | Combate estático; filas (Darkest Dungeon volta em F8) | F2–F8 |
| **Raven Idle / Norroth / Dofus / Wakfu** | Combate de turno com auto, câmera inclinada, mobs visíveis no mapa | F7–F8 |
| **Melvor / Idle Clans / Femur / Ygg / Tibidle / Wanderer** | Idle (como fazer e como não fazer) | F5–F8 |
| **BDO / Cabal / New World / Last Epoch** | Durabilidade com teto, AFK de lifeskill, +N, profundidade opcional | F8 |
| **Dark and Darker / Solo Leveling** | Extração e perda na morte | F2, RPG Solo |
| **Assassin's Creed** | Memórias ancestrais → Dom da Revivência | F2 |
| **American Gods** | Tom de deuses enfraquecidos | F6 |
| **História do Brasil + folclore** | Tudo: a reportagem da independência da Bahia, Cabral, bandeirantes, jesuítas, Anchieta, Gandavo | F1–F8 |

---

## 16. Lacunas desta varredura

- **Não lidos por inteiro:** os dois exports gigantes do ChatGPT (2025-03-19 e Setor
  Livro de Regras, ~1,2 MB cada — muito é recolagem dos livros), o Livro de Regras
  monolítico, PDFs e áudios do NotebookLM, e conversas puramente técnicas (Go, EventBus,
  bootstrap).
- **Números finais de balanceamento** (penalidades, tiers de mob, constantes de fuga) são
  propostas das IAs, nem sempre confirmadas.
- **Contagens divergentes nas fontes:** mini-campanhas 6/6/6 vs. 6/7/7; expiração da
  knowledgeBase 5.000 / 500 ticks / 48 h; data da fusão 06 vs. 08/09.
- **Sem data:** os commits do pivô co-op (`c4fff4a`, `820ad6e`, `16132ad`, `ed287af`) não
  estão neste repositório; as versões co-op dos documentos do NotebookLM são de ~03–05/12/2025.
- **Origem não identificada:** os 20 prints de itens convertidos em JSON (22/09/2026) — o
  jogo de origem não é nomeado.
- **"Kingdom Come" e "Tarkov"** não aparecem nas conversas do Claude; Kingdom Come só nas
  do ChatGPT/Gemini.
