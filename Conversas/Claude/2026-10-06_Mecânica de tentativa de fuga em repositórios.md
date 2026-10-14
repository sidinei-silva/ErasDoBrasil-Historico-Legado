## Sidinei:

Olhando esses 2 repositorios: 

* https://github.com/sidinei-silva/ErasDoBrasil-Historico-Legado
* https://github.com/sidinei-silva/eras-do-brasil-idle


Quero entender como funciona a mecanica de tentativa de fuga, como ela esta definida e como eu posso especificar ela nesse arquivo.

[Anexo:  (7660 bytes)]

---

## Claude:

Achei a mecânica. Ela foi desenhada de verdade só na versão idle: está nos números de `data/shared/balance/combat.json` (blocos `retreat` e `escape`) e no raciocínio da conversa de 06/09/2026 com o Claude, que está no repo legado. O backend em Go não implementa fuga, então ela existe como regra e como simulação, não como código. No legado mais antigo, da época do RPG de mesa, fugir era só um teste de Astúcia ou Destreza, e quem tinha sucesso aparecia num bloco vizinho do mapa. Isso foi abandonado.

## Como ela está definida no idle

**A ideia central** veio de uma frase daquela conversa: fuga não quer dizer "eu escapo", quer dizer "eu escapo barato". A mesma conta vale para PvE e PvP. Foi isso que fez o atributo de fuga deixar de ser exclusivo do PvP, onde a maioria dos jogadores nunca ia usá-lo, e passar a valer para qualquer um.

**A chance.** A fórmula não está escrita por extenso, mas os campos do JSON a definem assim:

```
chance = base + pontosDeFuga × 0,1 − antiFugaEfetiva × 0,08
         limitada entre 5% e 75%   (base = 30%)

antiFugaEfetiva = anti-fuga do inimigo mais forte vivo
                  + 0,5 por inimigo vivo além do primeiro
```

Exemplo: com 3 pontos de fuga contra um elite sozinho (anti-fuga 2,5), a chance é 0,3 + 0,3 − 0,2 = 40%. Contra quatro humanos normais, a anti-fuga efetiva é 1,5 + 1,5 = 3,0, e a chance cai para 36%. O bônus por inimigo extra foi o que corrigiu a "build imune": antes dele, quem otimizava fuga praticamente nunca morria.

**De onde vem cada lado da conta.** Os pontos de fuga vêm do equipamento: árvore Projétil, botas, torso médio, montaria e bolsa. Há exclusividade por slot, então Recuar exclui Rastro Falso, Pé Solto exclui Sumir no Mato, e assim por diante. A anti-fuga vem do arquétipo do mob (fauna 0,5, humano 1,5, elite 2,5, chefe 4,0) e de algumas skills do lado Físico, como Encurralar e Amarração. A intenção era que quem se vestiu para correr conseguisse correr, e quem se vestiu para bater conseguisse segurar o outro.

**O custo da tentativa que falha.** O jogador perde o turno, o inimigo ataca, e o equipamento perde 3 de durabilidade. A chance não aumenta nas tentativas seguintes; foi uma decisão sua para que a fuga não funcionasse sempre. Morrer durante as tentativas continua possível. A simulação mostrou um efeito que ninguém tinha planejado: em quase todos os tiers, a durabilidade perdida em fugas fracassadas supera a perdida em mortes.

**O custo da tentativa que dá certo.** O jogador perde o loot daquela luta, leva um golpe de despedida e fica 20 segundos sem poder lutar.

**Largar Carga** é a saída de emergência. Dá +4 pontos de fuga, só pode ser usada uma vez por combate e descarta toda a carga. Na simulação, o personagem pesado a pé caiu de 67% para 33% de mortes em emergências. Ou seja, ela socorre justamente quem não investiu em fuga e cobra em material.

**No automático**, a fuga é disparada por um limiar de vida configurável, fora da lista de prioridades. A ordem de verificação a cada evento é: condição de parada, depois limiar de retirada, depois limiar de cura, depois skill.

**Mobs com regra própria:**
- O Curupira dobra a anti-fuga e inverte a direção: quem foge dele volta ao mesmo lugar.
- Um mob de água anula automaticamente uma tentativa de fuga a cada três turnos.
- Contra a Raiz, nenhuma fuga funciona enquanto ela estiver viva.

## O que o combate novo muda

O seu documento já trouxe coisas que o idle não tinha, e cada uma gera uma pergunta que a versão antiga não precisava responder:

1. **Filas e distância.** Fugir depende de onde o jogador está? Recuar até a borda esquerda poderia dar bônus, e estar colado num corpo a corpo poderia dar penalidade. As skills de recuo e de puxar que você já descreveu viram ferramentas naturais de fuga e de anti-fuga.
2. **Golpe de despedida.** Quem dá o golpe? Todos os inimigos, ou só os que estão ao alcance da própria arma? Com filas, a segunda opção faz sentido e conversa com a posição.
3. **Tempo de recarga.** Você escreveu que fugir tem recarga, mas no idle a recarga vinha depois da fuga bem-sucedida (os 20 segundos sem lutar), não entre uma tentativa e outra. Se você puser recarga entre tentativas, ela passa a ser outro custo de falhar. Decida qual dos dois você quer, ou se quer os dois.
4. **Fugir conta como ação do turno?** No modo ativo, fugir disputa o turno com atacar e usar item? Dá para usar um item e tentar fugir no mesmo turno?
5. **Turno em PvP.** Quando o atacado escolhe "fugir" na notificação, ele já começa tentando fugir no primeiro turno, ou ganha alguma vantagem por ter percebido o ataque? E se o timer de 30 segundos acabar, o automático respeita o limiar de retirada dele?
6. **Para onde o jogador vai.** No idle ele ficava na zona. Aqui, ele volta ao ponto do mapa aberto onde estava? O inimigo continua lá, e ele pode ser re-engajado logo em seguida?

## Como encaixar no seu arquivo

Como a seção "Como funciona" é sem números de balanceamento, a fórmula com os valores fica nos dados. No documento entram as regras e as relações: "a chance é a sua fuga contra a anti-fuga do inimigo", "mais inimigos dificultam", "tem piso e teto". Os números vão para o arquivo de balance e o documento só aponta para ele.

Um esqueleto com as perguntas que cada parte precisa responder (o texto é seu):

```markdown
#### Fugir do combate
<!-- Ideia em uma frase: o que a fuga promete e o que ela NÃO promete -->

##### Chance de fuga
<!-- O que entra contra o quê. De onde vêm os pontos de fuga e a anti-fuga.
     Como o número de inimigos e a posição na fila afetam. Existe piso e teto? -->

##### Quando falha
<!-- Perde o turno? Quem ataca? Que marca fica (durabilidade?) A chance sobe ou não? -->

##### Quando dá certo
<!-- O que se perde (loot, golpe de despedida, tempo sem lutar). Para onde o jogador vai. -->

##### Ativo
<!-- Ocupa a ação do turno? Combina com item? Tem recarga entre tentativas? -->

##### Automatizado
<!-- Limiar de retirada no loadout. Ordem: parada → retirada → cura → skill. -->

##### Contra outros jogadores
<!-- A escolha "fugir" na notificação. Timer de 30s. -->

##### Exceções
<!-- Mobs que mudam a regra (anula, dobra, proíbe). Largar Carga. -->
```

O restante do template também tem lugar para a fuga:

- **Sem configurar nada:** qual é o limiar de retirada padrão para quem nunca abre a tela. No idle, a decisão foi que o limiar é estratégia e deve ser configurável, mas com um padrão razoável.
- **Para quem quer ir fundo:** a build de fuga, a exclusividade por slot e o Largar Carga.
- **Liga com:** durabilidade, loot, equipamento, PvP e carga/peso.
- **Decisões:** vale registrar as duas que já foram tomadas lá atrás, com o porquê: "a chance não sobe a cada falha, para que fuga alta signifique fugir barato" e "a anti-fuga cresce com o número de inimigos, para fechar a build imune".

---

## Sidinei:

Muda alguma coisa dado a nova reformulação do jogo tendo esses consolidados?

[Anexo:  (9736 bytes)]

---

## Claude:

Muda, sim. A espinha da fuga continua de pé: a chance é a sua fuga contra a anti-fuga do inimigo, a anti-fuga sobe com o número de inimigos, a chance não aumenta a cada falha e o limiar de retirada vale para o auto. O que mudou foram as coisas ao redor que davam peso a ela. Cinco pontos mexem de verdade, e um sexto é uma contradição entre os dois documentos.

## 1. O custo da falha perdeu o dente

No idle, a falha custava durabilidade, e a simulação mostrou que fugir mal saía quase tão caro quanto morrer. Era isso que dava ao atributo de fuga seu segundo motivo para existir.

No consolidado, a durabilidade virou a camada barata: o kit de reparo é recarregável em qualquer lugar, sem peso e sem prata. A camada cara é o teto, e você escreveu que ele cai "com falha de upgrade e com morte (por enquanto só isso)". Ou seja, hoje a fuga fracassada só arranha uma coisa que se conserta de graça no meio do mato.

Você precisa decidir onde a falha dói. As opções que vejo:
- **Falha mexe no teto, um pouco.** Isso restaura a lógica antiga de "fugir mal custa quase tanto quanto morrer", mas aí o "por enquanto só isso" do teto ganha um terceiro item.
- **O custo fica só no turno perdido.** Você não age e todo mundo bate. Isso é mais simples, e com intenção visível e filas o turno perdido pesa mais do que pesava no idle.
- **Falha consome a carga do kit em vez de durabilidade direta.** Assim o custo vira material refinado, que é um ralo que você já tem.

## 2. Largar Carga ficou pior que morrer

No idle, Largar Carga descartava tudo para garantir a saída. Agora a morte "perde parte do inventário carregado". Se largar a carga custa tudo e morrer custa uma parte, o jogador racional prefere morrer.

Para a ferramenta continuar fazendo sentido, ela precisa custar menos que a morte em carga. Por exemplo, largar uma fração maior que a da morte, mas não tudo. A troca seria: perde mais carga do que se morresse, porém não leva o golpe no teto. Ela só vale a pena por essa diferença.

## 3. O botão de pânico concorre com a fuga

"Pausa, não perde nada, não ganha nada." Se pausar também permite sair da luta, ninguém usa fuga, porque o pânico vira uma fuga perfeita e gratuita.

Você precisa deixar escrito que o pânico congela a luta e, ao voltar, ela continua exatamente no mesmo estado. Ele resolve "meu filho acordou", não "estou perdendo". Também precisa definir o que ele faz em PvP, onde não dá para congelar o outro jogador. Provavelmente ele entrega a luta ao auto com o preset de PvP, e aí quem decide se foge é a regra de fuga.

## 4. A inversão de incentivo entre ativo e auto passa pela fuga

Morrer no ativo zera o teto; morrer no auto só desgasta. Somado ao fato de que só o ativo enxerga a intenção do inimigo, isso cria duas forças opostas:
- A punição empurra luta arriscada para o auto, que custa menos se der errado.
- A informação puxa para o ativo, onde o jogador vê o golpão chegando e foge no turno certo, enquanto o auto só foge pelo HP.

A fuga é justamente a ferramenta que o ativo usa melhor, então talvez ela seja a resposta para o item em aberto. A lógica seria: o ativo pune mais a morte, mas dá tudo o que você precisa para não morrer. Se você aceitar essa leitura, vale registrá-la como decisão. Se não, a diferença de punição precisa de outra justificativa.

## 5. Filas e movimento dão à fuga um eixo que o idle não tinha

Agora o ranged não anda e tem skills de empurrar, saltar para trás e teletransportar. Isso combina com o idle, onde Projétil era a árvore de fuga, e permite que a posição entre na conta sem um número novo:
- O golpe de despedida vem só de quem está ao alcance da própria arma.
- Não ter nenhum corpo a corpo adjacente pode valer como bônus.

Com isso, empurrar e recuar viram preparação para fugir, e não só dano evitado.

Há ainda duas mudanças menores nessa parte:
- As fontes de pontos de fuga encolheram. Montaria ajudando na fuga foi para o "Futuro", e a bolsa não aparece mais. Sobram a árvore Projétil, as botas e o peito.
- O "20 segundos sem lutar" era tempo real de um idle por ondas. Num jogo por turnos, com encontros visíveis no mapa, você precisa decidir se essa espera continua em tempo real ou se o custo vira o próprio encontro. Por exemplo, o mob comum some e o elite compartilhado continua lá para outro pegar.

## 6. PvP: os dois documentos divergem

No seu arquivo de combate, o atacado escolhe "entrar ou fugir" na notificação. No consolidado, ele escolhe o modo (manual ou auto), e o padrão é o auto.

As duas regras cabem juntas se a fuga deixar de ser uma opção da notificação e virar só a primeira ação possível do turno, ou uma regra do preset de PvP. Mas a notificação precisa ter uma pergunta só.

Junto com isso vêm três perguntas que antes não existiam:
- O atacante não pode fugir nos primeiros turnos. O atacado pode fugir já no primeiro?
- Se a vantagem do atacante for agir primeiro, ele ganha um turno para segurar o alvo antes da primeira tentativa de fuga. Isso é intencional?
- Como o HP não reseta quando alguém ataca um jogador que está lutando, quem acabou de fugir de um mob com pouca vida é o alvo ideal. Fugir com sucesso pode dar alguma proteção curta? Seria parecida com a janela que o atacado vitorioso ganha.

## Para o documento

No seu arquivo, o item "Fuga: custo e chance" em "Em aberto" pode ser aberto nestas quatro decisões:
- onde a falha dói (pontos 1 e 2);
- o que o pânico pode e não pode fazer (ponto 3);
- se a fuga é a resposta para a inversão entre ativo e auto (ponto 4);
- como fica a notificação no PvP (ponto 6).

A chance e a anti-fuga por inimigo podem ir direto para "Decisões", porque nada no consolidado as contradiz.

---

## Sidinei:

Tenho alguns pontos:

* Se morrer não tem tanta penalidade como era com o full loot ou algo mais penalizado não faz sentido a habilidade soltar carga
* Porque agora eu quero fugir da batalha porque não quero perder a parte do meu loot e nem perder meu teto com a morte
* Recarregar não ficou tão barato assim porque preciso de recurso refinado e o kit vai ter tiers porque o kit tier 2 só repara item tier 2 e ele é recarregavel com recurso refinado tier 2 talvez encantado eu coloque para consumir mais para não precisa ter kit encantado ou recarregado com material encantado
* Sobre a falha mexer no teto não sei se funciona bem porque se eu tentar falhar varias vezes pode bater quase a mesma coisa que morrer a não ser que falha fuga diminui o teto mas não perde item ai faz um pouco mais de sentido
* O turno perdido vai acontecer tentar fugir é uma ação se eu tentar fugir e falhar perdi o turno (mas pensando bem isso tira um pouco de soltar uma habilidade de distanciar e tentar fugir porém facilita a fuga, pensando no caso eu sou arqueiro solto habilidade de distanciar para o proximo turno eu tentar fugir o guerreiro solta habilidade de aproximar ele ja não pode fugir ou fica mais dificil fugir se ele não tiver outra habilidade de distanciar complica a não ser que ele tenha habilidade de prender ai ele prende, depois distancia, depois foge.) Tenho que equilibrar bem não tenho certeza se vai consumir uma ação ou não.
* A falha consumir a carga do kit dar no mesmo que diminuir a durabilidade porque se diminuir a durabilidade eu vou ter que consertar que vai usar uma carga do kit
* Sobre 2. Largar Carga ficou pior que morrer estou quase achando que ele não faz mais sentido
* Ao trocar por turno 3. O botão de pânico concorre com a fuga não existe mais porque se for pve o turno me espera se for pvp vai entrar o automatico
* Não entendi o problema do 4. A inversão de incentivo entre ativo e auto passa pela fuga você começa falando que é problema depois fala que é solução e concordo com o que você fala sobre "A lógica seria: o ativo pune mais a morte, mas dá tudo o que você precisa para não morrer"
* Sobre 5. Filas e movimento dão à fuga um eixo que o idle não tinha concordo com os 2 pontos, mas acredito que não quero deixar que a fuga seja exclusiva de somente 1 arvore, se não mago e guerreiro nunca vai poder fungir, tudo mundo vai ter oportunidade de fugir mas cada um do seu jeito
* Não é um problema colocar que a montaria ajuda nos numeros da fuga
* Se eu entendi sobre os 20 segundos faz sentido que fugiu ficar com uma marcação temporaria e não pode engajar por alguns segundos de jogo, mas ainda to pensando se ele pode ser engajado por quem ele conseguiu fugir
* Sobre 6. PvP: os dois documentos divergem eu removi a opção de escolher entre auto e ativo, e deixei fugir e combater sendo fugir o padrão, quando escolhe fugir ja começar tentado fazer a fuga no primeiro turno e ai entra a regras se automatico, ou é melhor manter ativo e auto e o fugir automatico ser configuração, pensando bem acho que pode ser assim a pessoa pode configurar se vai fugir como primeira ação ou não e a notificação será ativo ou automatico.
* O atacante não pode fugir nos primeiros turnos. O atacado pode fugir já no primeiro? Sim o atacado pode fugir porque ele não escolheu a luta
* Se a vantagem do atacante for agir primeiro, ele ganha um turno para segurar o alvo antes da primeira tentativa de fuga. Isso é intencional? Não pensei sobre isso acho que vou trocar essa regra para ter algo como rodar iniciativa em algum atributo melhor se não atacado sempre vai ser dificil fugir 
* Como o HP não reseta quando alguém ataca um jogador que está lutando, quem acabou de fugir de um mob com pouca vida é o alvo ideal. Fugir com sucesso pode dar alguma proteção curta? Seria parecida com a janela que o atacado vitorioso ganha. Falei um pouco a cima e acho que faz sentido fugir faz não entrar em nenhum combate por um tempo

---

## Claude:

Concordo com quase tudo, e várias respostas suas se resolvem umas às outras. Vou pelos pontos que ainda têm algo a dizer.

## Durabilidade, kit e teto

Você tem razão em duas coisas. Eu errei ao chamar o reparo de "quase de graça": com kit por tier e recarga com material refinado do mesmo tier, a durabilidade é um custo real que cresce sozinho com o tier. E consumir carga do kit dá no mesmo que perder durabilidade, porque é a mesma conta passando por um caminho a mais.

Com isso, a falha de fuga custando durabilidade volta a funcionar, e eu deixaria o teto fora da fuga. Assim cada camada ganha um significado limpo:
- **Durabilidade** é desgaste. Uso e fuga mal feita entram aqui.
- **Teto** é consequência grave. Só morte e falha de upgrade entram aqui.

A sua variante (a falha reduz o teto, mas não perde item) até funciona, mas apaga essa fronteira. O jogador passaria a ter duas formas de perder teto, e a morte deixaria de ser especial.

## Largar Carga

Concordo, pode sair. Ela era resposta a uma morte que custava tudo. Com a morte custando parte do inventário mais o teto, o motivo para fugir passa a ser exatamente o que você escreveu: preservar o loot e o teto. Largar tudo para preservar uma parte não fecha a conta.

Uma ressalva: as zonas pretas estão no "Futuro". Se alguma delas tiver morte mais pesada (full loot, por exemplo), a Largar Carga volta a fazer sentido ali. Vale registrar como decisão com essa condição, para você não ter que redescobrir o motivo depois.

## Fugir consumir a ação

O seu exemplo do arqueiro contra o guerreiro é justamente o argumento para fugir consumir a ação, e não contra.

Se fugir fosse gratuito, todo turno seria "ataca e tenta fugir", e não haveria decisão nenhuma. Consumindo a ação, aparece o jogo que você descreveu: o arqueiro se distancia, o guerreiro se aproxima, o arqueiro prende e só então foge. Isso é a disputa de fuga contra anti-fuga, que no idle era só um número, virando decisões de turno. E a posição entrando na chance (do ponto 5 anterior) faz o preparo valer a pena.

Os riscos que eu vigiaria:
- **Trava infinita.** Se o guerreiro conseguir aproximar e prender todo turno, o arqueiro nunca foge. A recarga de prender e de aproximar precisa ser maior que o ciclo de fuga.
- **O que "preso" faz com a fuga.** Ela fica impossível ou só mais difícil? Impossível é mais claro de ler; mais difícil mantém o piso de chance funcionando.
- **Skills que juntam as duas coisas.** O idle tinha uma skill que "arranca e ganha grande bônus de fuga". Uma skill assim encurta o ciclo para quem investiu, sem tornar a fuga gratuita para todo mundo.

## Pânico

Concordo, o turno resolve isso: em PvE a luta espera e em PvP o auto assume. Eu só deixaria escrito que o pânico não encerra a luta, para ninguém achar que é uma saída.

## O ponto 4

Fui confuso, então reformulo. O problema é este: se o ativo pune mais a morte, o jogador racional vai para o auto justamente nas lutas arriscadas, e o modo que exige mais atenção acaba sendo o pior para jogar o conteúdo difícil.

Isso só é um problema se o ativo não compensar. A fuga com intenção visível é essa compensação. Como você concordou, a frase vira decisão: o ativo pune mais a morte, mas dá tudo o que você precisa para não morrer.

A consequência é que o auto foge pior (só por limiar de HP, sem ver a intenção do inimigo), e esse é o preço da morte mais leve. Fica coerente.

## Todo mundo foge, cada um do seu jeito

Concordo, e há uma forma de estruturar isso: cada árvore mexe numa parte diferente da fuga em vez de todas somarem o mesmo número.
- **Projétil aumenta a chance.** Distância, salto para trás, pontos de fuga.
- **Físico reduz o custo.** Aguenta ou anula o golpe de despedida, quebra o "preso".
- **Mágico ignora a posição.** Teleporte, névoa, um turno sem ser alvo.

Além disso, botas, peito e montaria dão pontos para qualquer um, o que conversa com "você é o que veste": um mago de botas leves foge melhor que um mago de botas pesadas. E montaria nos números de fuga, como você disse, não tem problema.

## Proteção depois de fugir

Juntando o seu ponto dos 20 segundos com o último, a regra fica: quem foge com sucesso ganha uma marcação temporária e não entra em nenhuma luta por um tempo, nem atacando nem sendo atacado. Isso resolve de uma vez três coisas:
- o perseguidor que reengaja logo em seguida;
- o abutre que espera o fugitivo sair com pouca vida;
- o mob que continua no mapa.

Duas perguntas para fechar a regra:
- **A proteção acaba se ele engajar alguém?** A janela do atacado vitorioso acaba, então seria coerente que esta também acabasse.
- **A fuga pode virar travessia?** Alguém com build de fuga alta poderia cruzar uma zona de risco encadeando fugas e proteções. Talvez a proteção não deva se renovar se ele for atacado de novo logo depois, ou deva ficar mais curta a cada fuga seguida. Pode ficar em aberto até você testar.

## PvP

O seu desenho final fecha:
- A notificação pergunta o modo (ativo ou auto).
- "Fugir como primeira ação" é uma configuração do preset de PvP.
- O atacado pode fugir no primeiro turno; o atacante não pode nos primeiros turnos.
- A iniciativa sai de um atributo.

Pelo pilar de "funciona sem configurar nada", eu deixaria "fugir primeiro" ligado por padrão. O atacado não escolheu a luta, e o seu público é o pai cansado que não quer ser surpreendido. E lembre de atualizar o arquivo de combate, que ainda diz "entrar ou fugir".

Sobre a iniciativa: um atacante com iniciativa alta e uma skill de prender vai segurar o defensor antes da primeira tentativa. Eu acho que isso é desejável, porque é a build de caçador (o Capitão do Mato do idle tinha exatamente essa identidade). Só não pode ser a regra para todo mundo, e com iniciativa por atributo não é.

## O que já dá para levar para "Decisões"

- A chance de fuga é a sua fuga contra a anti-fuga do inimigo, e a anti-fuga cresce com o número de inimigos.
- A chance não sobe a cada falha.
- Fugir consome a ação do turno.
- A falha custa o turno e durabilidade, e não mexe no teto.
- A Largar Carga sai, a menos que exista uma zona com morte pesada.
- Todas as árvores fogem, cada uma por um caminho, e equipamento e montaria somam pontos de fuga.
- A fuga bem-sucedida dá proteção temporária contra qualquer luta.
- O ativo pune mais a morte e compensa com fuga melhor.
- Em PvP, o atacado pode fugir no primeiro turno, o atacante não, e "fugir primeiro" vem ligado no preset.

Para "Em aberto" ficam:
- o que "preso" faz com a fuga;
- a trava infinita de aproximar e prender;
- se a proteção acaba ao engajar e se ela se renova em fugas seguidas;
- como a iniciativa é calculada.

---

## Sidinei:

Tem um ponto que eu estava pensando: 

* Se no ativo morrer zero o teto e no auto não, o player pode querer ir para o auto de proposito quando ver que vai morrer, mesmo aceitando que vai morrer, então tenho 2 saidas ou se em algum momento eu soltei alguma skill ativa a morte sempre considera o ativo ou se entrou no modo automatico não sai do modo automatico até acabar a batalha


No outro chat ele respondeu:

Bem visto. É exatamente a inversão de incentivo que tinha ficado anotada, só que agora em forma de exploit: no meio da luta, perceber que vai morrer e trocar para o auto só para pagar a morte mais barata.
As duas saídas fecham o exploit, mas com custos diferentes.
Opção 1: se você agiu manualmente em algum momento, a morte conta como do ativo.
O jogador continua podendo trocar para o auto quando quiser, por conveniência ou porque precisou sair, e a troca simplesmente não muda o preço da morte. É simples de entender e de implementar: a sessão só guarda uma marca dizendo "houve ação manual".
Opção 2: entrou no auto, fica no auto até o fim da luta.
Fecha o exploit, mas cria outros problemas. Você volta de ninar o bebê e não consegue retomar o controle de uma luta que o auto está jogando mal. E o PvP passa a ter uma armadilha: se o tempo do turno estourar uma vez e o auto assumir, você fica preso nele até o fim. Isso vai contra o pilar de não punir quem precisa sair.
Por isso eu iria na opção 1, e dá para simplificar ainda mais: o preço da morte é definido pelo modo em que a luta começou. Começou no ativo, é morte de ativo, não importa o que aconteça depois. Para o jogador, a regra fica fácil de entender: "se eu escolhi lutar manualmente, assumi o risco do manual". E a troca para o auto continua livre como rede de proteção.
Existe ainda uma terceira saída, mais radical: acabar com a diferença. Se a morte custasse o mesmo no ativo e no auto, não haveria nada a explorar, e a vantagem do ativo ficaria só na recompensa maior e nas decisões melhores. Você perde o "o ativo arrisca mais", mas elimina toda essa classe de problema de uma vez. Vale pensar se a diferença no preço da morte está realmente servindo a algum pilar, ou se a diferença na recompensa já basta.

---

## Claude:

Eu concordo com o diagnóstico e com a escolha da opção 1. Discordo só da simplificação final, e acho que a terceira saída tira uma coisa que está servindo a um pilar.

## "Houve ação manual" é melhor que "modo em que começou"

A simplificação fecha o exploit num sentido só. Pense no caminho inverso: a luta nasce na caçada automática, você volta do quarto, vê o auto jogando mal e assume. Pela regra do "modo em que começou", você está jogando no manual, com intenção visível e fuga no turno certo, mas paga a morte barata do auto.

Isso desfaz a decisão que você acabou de tomar, de que o ativo pune mais e compensa com informação. Quem usou a compensação tem que pagar o preço.

A marca de "houve ação manual" cobre os dois sentidos com uma regra só. Ir do ativo para o auto não barateia a morte, porque a marca já existe. Ir do auto para o ativo encarece, porque a marca passa a existir. E de quebra ela resolve o item em aberto de "voltar do auto para o manual": é permitido sempre, só muda o preço.

Para o jogador, a frase continua simples: "se eu joguei manualmente em algum momento da luta, assumi o risco do manual". Para isso não virar armadilha, a interface precisa avisar no momento de assumir o controle, algo como "a partir daqui esta luta conta como manual". Sem esse aviso, o pai cansado descobre a regra pela pior via.

## Fugir também conta como ação manual

Isso é uma consequência que vale escrever. Se tomar o controle só para tentar fugir não marcasse a luta, o auto ganharia a fuga do ativo de graça, e a decisão de que o auto foge pior por limiar de HP deixaria de valer.

Então quem assume para fugir e falha morre com preço de ativo. É duro, mas coerente: ele tinha a informação e escolheu agir.

## Sobre acabar com a diferença

A pergunta do outro chat é boa ("a diferença no preço da morte serve a algum pilar?"), mas acho que a resposta é sim, e não é o pilar de o ativo arriscar mais. É o pilar de idle × ação: progredir AFK e não ser punido por sair de repente.

A morte do auto é mais barata porque o jogador não estava lá para reagir. A diferença na recompensa não faz esse papel: ela premia quem está presente, mas não protege quem está ausente. São funções diferentes, e tirar a diferença na morte faria o AFK pagar o preço cheio por uma luta que ele não podia jogar.

Então eu manteria a diferença e fecharia o exploit com a marca.

## Para o documento

Em "Decisões":
- O preço da morte é o do ativo se houve qualquer ação manual na luta, fuga incluída. Caso contrário, é o do auto.
- A troca entre modos é livre nos dois sentidos, e a interface avisa quando a luta passa a contar como manual.
- A diferença no preço da morte existe para proteger o jogador ausente, não para premiar o presente.

A terceira decisão é a que vale ter escrita com o porquê, porque é a que você vai querer rediscutir quando estiver balanceando.

---

## Sidinei:

Para esse documento o que muda? Dado o que decidimos? E como fica a parte da fuga no formato e padrão do documento?

[Anexo:  (7777 bytes)]

---

## Claude:

Pelo que decidimos, o documento muda em quatro lugares fora da seção de fuga e ganha conteúdo nas seções de baixo que estão vazias.

## O que muda no resto do documento

**1. Engajamento > Contra outros jogadores > Ativo.** O texto atual diz que a notificação oferece "entrar no combate ou fugir". Pelo que você decidiu, a notificação pergunta o modo (ativo ou automatizado), e o padrão é o automatizado. Tentar fugir no primeiro turno virou uma configuração do preset de PvP, ligada por padrão. O parágrafo também precisa dizer que o atacado pode fugir já no primeiro turno e que o atacante não pode fugir nos primeiros turnos.

**2. Formato do combate.** Hoje ele diz que "cada jogador tem um turno", mas não diz quem age primeiro. Falta escrever que a ordem dos turnos sai de um atributo. O atributo ainda está em aberto.

**3. Troca entre modos.** Ela está meio escondida em "Contra outros jogadores", na frase "pode retornar ao modo ativo a qualquer momento". Agora ela é uma regra geral: vale para PvE também e muda o preço da morte. Eu daria a ela uma subseção própria dentro de "Formato do combate". Junto entra a frase de que sair da luta não a encerra: em PvE o turno espera, e em PvP o automático assume.

**4. Outras ações.** A frase "Ambos com suas regras e mecânicas próprias e tempo de recarga" afirma que a fuga tem recarga, e isso não foi decidido. Como fugir consome a ação e a falha custa o turno, talvez a recarga nem seja necessária. Eu tiraria a fuga dessa frase e mandaria a dúvida para "Em aberto".

Duas coisas não mudam, mas tocam a fuga. A frase "paralisado" em Movimentação é o "preso" da nossa conversa, e o que ele faz com a fuga está em aberto. A regra de "ativo nunca ataca automatizado" que você acrescentou já bate com o consolidado.

## A subseção de troca de modo

```markdown
#### Troca entre modos
O jogador pode trocar entre o modo ativo e o automatizado a qualquer momento da luta, nos dois sentidos. Sair da luta não a encerra: contra NPCs o turno espera o jogador voltar, contra outros jogadores o modo automatizado assume.

Se o jogador fez qualquer ação manual durante a luta, incluindo tentar fugir, a luta conta como ativa para o preço da morte, mesmo que ela termine no automatizado. Quando o jogador assume o controle de uma luta que estava no automatizado, a interface avisa que a partir dali ela passa a contar como ativa.
```

## A seção de fuga

```markdown
#### Fugir do combate
Fugir não é garantia de escapar, é a chance de escapar pagando menos do que morrer. Quem foge perde o que juntou naquela luta, mas preserva o que carrega e o teto do equipamento.

##### Chance de fuga
A chance é a fuga do jogador contra a anti-fuga dos inimigos. A fuga vem do equipamento, da montaria e das habilidades; a anti-fuga vem do tipo do inimigo e das habilidades dele. Quanto mais inimigos vivos, mais difícil fugir. A chance tem um piso e um teto: nunca é impossível e nunca é garantida. A chance não aumenta a cada tentativa que falha.

A posição também conta: estar longe dos inimigos facilita a fuga, e estar colado num inimigo de corpo a corpo dificulta.

##### Tentativa
Tentar fugir é a ação do turno. O jogador não ataca nem usa habilidade naquele turno.

Se falhar, o jogador perde o turno, os inimigos agem normalmente e o equipamento perde durabilidade. A luta continua e o jogador pode tentar de novo nos turnos seguintes. Se a vida acabar durante as tentativas, o jogador morre.

Se conseguir, o jogador leva um golpe de despedida dos inimigos que estão ao alcance da própria arma, perde o loot daquela luta e volta para o mapa aberto. Por um tempo, ele não pode atacar nem ser atacado por ninguém.

##### Cada um foge do seu jeito
Todas as árvores conseguem fugir, mas por caminhos diferentes:
- Projétil aumenta a chance, com distância e habilidades de recuo.
- Físico reduz o custo, aguentando o golpe de despedida e quebrando o que prende.
- Mágico ignora a posição, com teleporte e efeitos que tiram o jogador de alvo.

Botas, torso e montaria somam fuga para qualquer árvore.

##### Ativo
No combate ativo o jogador escolhe quando tentar fugir. Como enxerga a intenção do inimigo, pode fugir antes de um golpe grande e preparar a fuga com habilidades de recuo.

##### Automatizado
No combate automatizado o jogador define um limiar de vida na automação; ao cruzá-lo, o personagem tenta fugir. A automação não enxerga a intenção do inimigo, então foge só pela vida. A cada turno o automatizado verifica, nesta ordem: fuga, cura e habilidade.

##### Contra outros jogadores
O atacado pode tentar fugir já no primeiro turno, porque não escolheu a luta. O atacante não pode fugir nos primeiros turnos. O preset de PvP pode configurar a fuga como primeira ação.

##### Exceções
Alguns inimigos mudam a regra da fuga: anulam tentativas, dificultam mais que o normal ou impedem a fuga enquanto estiverem vivos.
```

Duas observações sobre o texto:

- "Perde o loot daquela luta" e o golpe de despedida vieram do idle. Você não chegou a reconfirmá-los nesta conversa, só concordou com o golpe vir de quem está ao alcance. Confira se continuam valendo.
- Na ordem de verificação, o idle tinha "condição de parada" antes de tudo. Ela é da caçada, não da luta, então eu a deixaria no documento de caçada automatizada.

## As seções de baixo

```markdown
## Sem configurar nada
- O automatizado já vem com um limiar de fuga razoável.
- O preset de PvP já vem com "fugir como primeira ação" ligado.

## Para quem quer ir fundo
- Ajustar o limiar de fuga por preset (comum, chefe, PvP).
- Montar a build para fugir barato ou para segurar quem foge.
- Preparar a fuga no ativo: recuar, prender, depois fugir.

## Liga com
- Durabilidade (custo da fuga que falha)
- Morte e teto (preço da morte no ativo e no automatizado)
- Equipamento e montaria (fontes de fuga)
- Caçada automatizada (condições de parada)
- PvP e marcação (proteção depois da fuga, atacante e atacado)

## Em aberto
- O que "preso" faz com a fuga: impede ou só dificulta?
- Como evitar que aproximar e prender trave a fuga para sempre.
- A proteção depois da fuga acaba se o jogador atacar alguém? Ela se renova em fugas seguidas?
- Qual atributo define a ordem dos turnos.
- A fuga precisa de tempo de recarga entre tentativas, ou o turno perdido basta?
```

E a tabela de decisões:

```markdown
| Data | Decisão | Por quê |
| ---- | ------- | ------- |
| 2026-10-06 | A chance de fuga não aumenta a cada falha | Fuga alta tem que significar fugir barato, não só fugir mais rápido |
| 2026-10-06 | A anti-fuga cresce com o número de inimigos | Sem isso, uma build de fuga ficava imune |
| 2026-10-06 | Tentar fugir é a ação do turno | Cria o jogo de preparar a fuga e de impedi-la |
| 2026-10-06 | A fuga que falha custa durabilidade, não teto | Teto fica reservado para consequências graves: morte e upgrade |
| 2026-10-06 | Largar Carga saiu | A morte não custa mais tudo; volta se alguma zona tiver morte pesada |
| 2026-10-06 | Todas as árvores fogem, cada uma do seu jeito | Ninguém fica sem saída por causa da arma |
| 2026-10-06 | Quem foge fica protegido de qualquer luta por um tempo | Evita reengajar na hora e o abutre que espera a vida baixa |
| 2026-10-06 | Qualquer ação manual faz a morte contar como ativa | Fecha o exploit de trocar para o automatizado para morrer barato |
| 2026-10-06 | A morte no automatizado continua mais barata | Protege quem não estava presente para reagir |
| 2026-10-06 | O ativo pune mais a morte e compensa com fuga melhor | A informação do ativo é o que paga o risco maior |
```

---
