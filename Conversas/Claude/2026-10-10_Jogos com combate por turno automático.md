## Sidinei:

Quais jogos existe com combate de turno que tenha modo automático e movimentação seja em grid ou linha reta e como ele resolve a movimentação no modo manual e no modo automático.

Algo parecido com o deste video que é o anúncio do novo modo de batalha do ravenidle

[Arquivo anexado: RavenIdle_1.mp4]

---

## Claude:

Vou dar uma olhada no vídeo primeiro para entender o modo de batalha do RavenIdle.

O vídeo mostra um mapa em tiles visto de cima, no estilo Tibia. Os monstros andam casa a casa até você, e você solta uma **rotação** de skills em ordem (aparece "Casting: Meteor Strike"). Há toggles de **auto-heal** e **auto-mana**, e os botões "Mini mode" e "Cancel fight". Pelo que dá pra ver, o combate é por ticks e não por turnos rígidos, mas a lógica de movimento é a mesma de um jogo de turno em grid. Não achei nenhuma descrição pública de como esse modo resolve a movimentação, então o que segue vem de jogos que conheço bem.

## Jogos e como cada um resolve o movimento

**Tibia** (a inspiração visual óbvia do RavenIdle). Grid e ticks.
- **Manual:** setas ou clique no destino. O jogo calcula o caminho e anda uma casa por passo, e o tempo de cada passo depende da sua velocidade.
- **Automático:** você escolhe uma postura de combate. "Chase opponent" persegue o alvo por pathfinding até a casa vizinha. "Stand while fighting" não te move.
- **Monstros:** cada um tem parâmetros. Nos servidores OT, por exemplo, `targetdistance` é 1 para quem luta corpo a corpo e 4 para quem ataca à distância e se afasta para manter esse espaço. `runonhealth` faz o monstro fugir abaixo de um certo HP. Ou seja, o comportamento vem de dados, não de código específico por monstro.

**Dungeon Crawl Stone Soup / Brogue** (roguelikes, turno estrito em grid).
- **Manual:** cada passo custa um turno, e todos os outros agem depois de você.
- **Automático:** o *autoexplore* calcula um caminho até a área inexplorada mais próxima. O *autofight* do DCSS anda em direção ao inimigo visível mais próximo, ataca quando está adjacente e se recusa a agir com HP baixo.
- **O ponto principal:** o automático é só um "macro" que emite **os mesmos comandos** que o jogador emitiria, um por turno, e para quando algo novo acontece (um monstro aparece, você toma dano).
- **Dijkstra maps:** o Brogue popularizou essa técnica. Você calcula uma vez um mapa de distâncias a partir dos alvos, e cada monstro só "desce o morro" para a casa vizinha de menor valor. Inverter o mapa gera o comportamento de fuga. Fica barato com muitos monstros.

**Pokémon Mystery Dungeon.** Grid e turno.
- **Manual:** você controla o líder, e cada ação sua é um turno para todo mundo.
- **Automático:** os parceiros seguem uma "tática" escolhida por você, como "Follow me", "Go after foes" ou "Wait there". A tática é só a regra que decide **para onde ir**. Os ataques usam o mesmo sistema.

**Heroes of Might and Magic III.** Grid hexagonal, ordem de ação por velocidade.
- **Manual:** o jogo destaca as casas alcançáveis com uma busca em largura limitada pela velocidade da unidade (unidades voadoras ignoram obstáculos). Você clica no destino, ou clica no inimigo e o jogo escolhe a casa de ataque.
- **Automático:** o *Auto-combat* passa o seu lado para a **mesma IA do inimigo**. O *Quick combat* resolve tudo sem mostrar a batalha, que é literalmente o mesmo motor rodando sem renderização. Isso é ótimo como referência para idle.

**Fire Emblem Heroes / Langrisser Mobile.** Grid e fases por time.
- **Manual:** você arrasta a unidade, e o jogo mostra o alcance de movimento mais o alcance de ataque.
- **Automático:** o seu time passa a usar a IA do inimigo.
- **IA dos inimigos:** é por gatilhos. Alguns ficam parados até você entrar na área de ameaça deles, outros avançam sempre, outros nunca saem do lugar. São três comportamentos baratos que já dão variedade.

**Disgaea 6.** Grid.
- **Manual:** move e depois age, no estilo tático clássico.
- **Automático:** o *Demonic Intelligence* é uma lista de regras programável por unidade ("aproximar do inimigo mais próximo", "atacar o de menor HP", "curar aliado abaixo de X%"). A primeira regra válida executa. É o mesmo conceito dos *gambits* do FF XII.

**Darkest Dungeon.** Posições em linha, sem modo auto, mas é a melhor referência para "linha reta".
- Não existe deslocamento livre. Cada personagem ocupa um slot de 1 a 4.
- Mover é uma ação que troca de lugar com o vizinho, e alguns golpes empurram ou puxam.
- Cada skill exige que o usuário esteja em certas posições e só acerta certas posições do inimigo. A posição vira um recurso tático em vez de um mapa.

## O padrão que se repete

1. **Manual e automático produzem a mesma coisa:** uma ação (`mover para X`, `usar skill Y no alvo Z`). Um único resolvedor executa as duas. O auto é só outra fonte de decisões, e o idle é esse mesmo motor sem renderizar e com tempo acelerado (o Quick combat do HoMM).
2. **O movimento no automático quase sempre se divide em 3 perguntas:**
   - *Quem é o alvo?* O mais próximo, o de menor HP ou o que está me atacando.
   - *A que distância eu quero ficar?* Isso vem do alcance da próxima skill da rotação, ou de uma postura como aproximar, segurar posição, manter distância ou fugir.
   - *Qual casa satisfaz isso?* Se eu já estou no alcance e com linha de visão, não ando. Se não estou, ando pelo caminho (A*, busca em largura ou Dijkstra map) até a casa mais próxima que satisfaça.
3. **No manual, a diferença é só quem responde a pergunta 3.** O jogador clica na casa, mas o caminho e o custo vêm da mesma função.
4. **Uma regra de parada no auto** (HP baixo, alvo novo, inventário cheio) evita que ele faça besteira. É o que DCSS e Tibia fazem.

No Eras, como você quer modo ativo e caçada automática no mesmo motor, a decisão mais importante é a do item 1. Se a IA do jogador e a dos monstros escolherem ações pelo mesmo contrato, o modo auto sai quase de graça.

Uma pergunta para você pensar antes de escrever o doc de combate: no seu turno, mover e agir são duas coisas separadas (estilo Fire Emblem, com "anda até N casas e depois age"), ou mover é uma ação que gasta o turno (estilo roguelike e Darkest Dungeon)? Essa escolha muda bastante como o auto decide entre andar e atacar.

Fontes:
- [RavenIdle – RavenQuest](https://ravenquest.io/en/home/view/ravenidle) (página oficial; não detalha o novo modo de batalha)

[Arquivo anexado: image-0-0.jpg]

---
