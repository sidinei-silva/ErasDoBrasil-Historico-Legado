## Sidinei:

## 2 -  CHAT 1 — Personagem, Esqueleto e Equipamento

Tudo que usa o esqueleto humano único (jogador, Perdido, NPCs) e tudo que se pluga nele (armas, armaduras, ferramentas). Família `characters/` e `equipment/`.

**1. Personagem base**

> Releia antes de gerar, em `direcao-de-arte.md`: a seção 0 (orçamento técnico — o teto de 3.000 tris é do personagem **completo com equipamento**, não do corpo sozinho) e a seção 14 (o que evitar — a lista exata do que não pode aparecer). Gere uma prancha técnica do personagem base do MVP, sem equipamento: roupa crua, mãos vazias, nenhuma marca de facção — o forasteiro no estado "descartável". Formato: logotipo "ERAS DO BRASIL" no canto superior esquerdo, título da prancha ao lado, fundo azul-escuro de documento técnico, painéis com contorno claro, texto em português, infográfico de game design — nunca ilustração solta. Caixa de especificação no canto superior direito: "MVP – ILHA DA TRAVESSIA / ESTILO: LOW POLY ESTILIZADO / ORÇAMENTO: ATÉ 3.000 TRIS (PERSONAGEM COMPLETO) / FORMATO: PRANCHA TÉCNICA". Vista frontal e vista lateral **ortográficas exatas, sem perspectiva** — viram referência de modelagem no Blender —, mais vista de costas, e wireframe rotulado com a contagem de polígonos do personagem base ("POLÍGONOS: X TRIS"). Grade de escala atrás do personagem marcando a altura de 1,8 u. Painel separado "VISTA ISOMÉTRICA (NO JOGO)" com o personagem na câmera 3/4 fixa, dentro de uma cena mínima. Rodapé em três colunas: "USO NO MVP" (ponto de partida da curva descartável → equipado → competente → alinhado), "ESPECIFICAÇÕES" (tris, cores do atlas de Personagens), "OBSERVAÇÕES" (referência de produção, não ilustração final). Estilo 3D low poly estilizado, silhueta forte, cor chapada por face — sem gradiente dentro da mesma face, sem sombra suave nem oclusão de ambiente —, facetas do low poly visíveis a olho nu, luz ambiente suave, Brasil colonial. Proporção de cerca de 6 cabeças, cabeça e mãos um pouco maiores, sem musculatura detalhada, rosto quase sem volume. Proibido: realismo, PBR, iluminação cinematográfica, sombra suave/oclusão de ambiente, fantasia medieval europeia (castelo, elfo, anão, orc, armadura de cavaleiro).

---

## Sidinei:

**2. Esqueleto e sockets**

> Releia antes de gerar, em `direcao-de-arte.md`, seção 4: a árvore de ossos e a tabela de sockets — os nomes precisam bater exatamente, sem inventar osso a mais nem sigla diferente. Gere o diagrama do esqueleto humano único do jogo: ossos nomeados (raiz, quadril, coluna, peito, pescoço, cabeça, ombro/braço/antebraço/mão de cada lado, coxa/canela/pé de cada lado), com os seis sockets de equipamento destacados em cores diferentes: socket\_mao\_principal (arma), socket\_mao\_secundaria (off-hand), socket\_cabeca (capacete), socket\_torso (armadura), socket\_pes (botas), socket\_costas (mochila/bolsa). Mesmo cabeçalho institucional: logotipo "ERAS DO BRASIL", título, fundo azul-escuro, painéis com contorno claro. Formato de prancha técnica pura — não é ilustração de personagem, é diagrama, com o nome de cada osso legível ao lado da junta correspondente, útil como guia de nomenclatura ao montar o armature no Blender.

---

## Sidinei:

**3. Atlas de paleta — Personagens**

> Releia antes de gerar, em `direcao-de-arte.md`, seção 0: a regra de um atlas 256×256 por família, sem textura pintada. Gere o atlas de paleta da família "Personagens": cores de pele (variações), cabelo (variações) e roupa crua T1 (a cor já estabelecida no personagem-base desta conversa). Mesmo cabeçalho institucional (logotipo, título, fundo azul-escuro, painéis com contorno claro). Formato: atlas 256×256, faixas de cor chapada, sem gradiente, sem textura pintada — é referência técnica de produção, não ilustração.

---

## Sidinei:

**4. Atlas de paleta — Equipamento**

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Armaduras": as quatro linhas exatas (crua T1, pesada, média, leve) antes de definir as faixas de cor. Gere o atlas de paleta da família "Equipamento": uma faixa de cor para cada uma das quatro linhas de armadura (crua T1, pesada colonial T2, média indígena T2, leve encantada T2) e uma faixa para metal/madeira de arma. Mesmo cabeçalho institucional e mesmo formato técnico do atlas anterior.

---

## Sidinei:

**5. Armas T1**

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Armas" (nome e tier exatos da Lâmina Crua e do Broquel Cru), e em `direcao-de-arte.md`, seção 14, o que não pode aparecer. Gere uma prancha técnica da Lâmina Crua e do Broquel Cru — as armas T1 do MVP, sucata sem tradição, onde o jogador aprende a forjar. Formato: logotipo "ERAS DO BRASIL", título, fundo azul-escuro, painéis com contorno claro, texto em português. Caixa de especificação: "MVP – ILHA DA TRAVESSIA / ESTILO: LOW POLY ESTILIZADO / ORÇAMENTO: 150 A 500 TRIS POR PEÇA / FORMATO: PRANCHA TÉCNICA". Para cada peça: vista frontal e lateral ortográficas exatas, sem perspectiva, mais vista de costas e wireframe rotulado ("POLÍGONOS: X TRIS"). Painel separado com a peça na mão/braço do personagem-base desta conversa, vista de frente/lado/costas, mais painel "VISTA ISOMÉTRICA (NO JOGO)". Cores do atlas de Equipamento. Cor chapada por face, sem gradiente dentro da mesma face, sem sombra suave nem oclusão de ambiente — facetas do low poly visíveis a olho nu, como no personagem-base desta conversa. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES. Proibido: realismo, PBR, iluminação cinematográfica, fantasia medieval europeia.

---

## Sidinei:

**6. Armas T2**

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Armas": os cinco nomes exatos, o tier e a árvore de cada uma (Espada de lado, Zarabatana, Cabaça de Boitatá, Rodela, Patuá). Gere uma prancha técnica das cinco armas T2 do MVP. São a primeira decisão de identidade do jogo: a tradição só aparece a partir daqui. Mesmo cabeçalho institucional. Caixa de especificação com orçamento de 150 a 500 tris por peça. Para cada arma: vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado com a contagem de tris, e vista isolada na mão do personagem-base desta conversa. Painel "NO JOGO" com a vista isométrica. Cores do atlas de Equipamento, mesmo estilo, sem elemento de fantasia medieval europeia. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## Sidinei:

**7. Ferramentas T1**

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Ferramentas e transporte": os quatro nomes exatos e o material (seixo, pau-mole). Gere uma prancha técnica das quatro ferramentas T1 do MVP — machado, picareta, foice e faca de esfolar — mesma linha visual crua das armas T1. Mesmo cabeçalho institucional, mesma caixa de especificação (150 a 500 tris por peça). Vista isolada de cada uma, frontal e lateral ortográficas sem perspectiva, mais wireframe rotulado com a contagem de tris. Painel com cada ferramenta na mão do personagem-base. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## Sidinei:

**8. Armadura T1 crua**

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Armaduras": as três peças exatas da linha crua (Capuz, Colete, Botina) e o material (couro de capivara). Gere uma prancha técnica do conjunto, sem passiva, visualmente simples. Mesmo cabeçalho institucional. Caixa de especificação: orçamento de 150 a 500 tris por peça (dentro do total de até 3.000 tris do personagem completo). Conjunto montado no personagem-base desta conversa: vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, e wireframe rotulado mostrando a soma de tris do personagem + as três peças. Painel "NO JOGO" com a vista isométrica 3/4. Rodapé: USO NO MVP, ESPECIFICAÇÕES (tris de cada peça e o total somado), OBSERVAÇÕES.

---

## Sidinei:

**9. Armadura T2 pesada colonial**

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Armaduras": as três peças da linha pesada (morrião, couraça, grevas). Gere uma prancha técnica do conjunto, montado no personagem-base desta conversa. Mesmo cabeçalho institucional, mesma caixa de especificação (150 a 500 tris por peça, total somado ao personagem). Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado com o total de tris. Painel "NO JOGO" isométrico. Cores do atlas de Equipamento, linha pesada. Rodapé: USO NO MVP, ESPECIFICAÇÕES (tris de cada peça e total), OBSERVAÇÕES.

---

## ChatGPT:

Sidinei, gerei a prancha da **Armadura T2 Pesada Colonial**, com **morrião, couraça e grevas**, mantendo a leitura low poly e a montagem no personagem-base.

**Nota importante:** a documentação define o orçamento de **150–500 tris por peça**, mas não fixa uma contagem exata para cada modelo. Então os números de tris que aparecem na prancha são **estimativas de mockup**, não especificações fechadas de produção. fileciteturn0file0L100-L104

---

## Sidinei:

**10. Armadura T2 média indígena**

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Armaduras": as três peças da linha média (cocar, escaupil, alpercatas). Gere uma prancha técnica do conjunto, montado no personagem-base desta conversa. O escaupil é peça histórica real; mantenha fidelidade à referência sem virar estereótipo. Mesmo cabeçalho institucional e mesma caixa de especificação do conjunto anterior. Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado com o total de tris. Painel "NO JOGO" isométrico. Rodapé: USO NO MVP, ESPECIFICAÇÕES (tris de cada peça e total), OBSERVAÇÕES (nota sobre a referência histórica do escaupil).

---

## Sidinei:

**11. Armadura T2 leve encantada**

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Armaduras": as três peças da linha leve (carapuça, manto de retalhos, sandálias de piaçava). Gere uma prancha técnica do conjunto, montado no personagem-base desta conversa. Mesmo cabeçalho institucional e mesma caixa de especificação do conjunto anterior. Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado com o total de tris. Painel "NO JOGO" isométrico. Rodapé: USO NO MVP, ESPECIFICAÇÕES (tris de cada peça e total), OBSERVAÇÕES.

---

## Sidinei:

**12. Bolsa de couro** — *aproximação: o documento não define orçamento específico para este item; uso a faixa geral de peça de equipamento (150 a 500 tris), confira antes de aprovar.*

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Ferramentas e transporte": a Bolsa de couro T2 cai do mini-chefe, socket\_costas. Gere uma prancha técnica da peça no personagem-base desta conversa. Mesmo cabeçalho institucional. Caixa de especificação: orçamento estimado de 150 a 500 tris (faixa geral de peça de equipamento). Vista isolada frontal e lateral ortográficas sem perspectiva, mais vista de costas — a mais relevante, já que a peça fica nas costas —, e wireframe rotulado. Painel com a peça montada no personagem, vista de costas e 3/4, mais painel "NO JOGO". Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## Sidinei:

**13. Perdido**

> Releia antes de gerar, em `mvp_mobs.json`, a descrição exata do "Perdido" — use o texto literal do arquivo, não parafraseie de memória. Gere uma prancha técnica do mob humano: mesmo esqueleto e proporção do personagem-base, mudando só roupa e ferramenta. Mesmo cabeçalho institucional. Caixa de especificação: mesmo orçamento do personagem base (até 3.000 tris completo), já que reaproveita o esqueleto. Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado. Painel "NO JOGO" isométrico, sem rosto expressivo. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## Sidinei:

**14. O Primeiro Perdido (mini-chefe)** — *interpretação: assumo que reusa o esqueleto do jogador, como o Perdido comum; isso não está escrito no JSON, então confira antes de aprovar.*

> Releia antes de gerar, em `mvp_mobs.json`, a descrição exata do mini-chefe e o comportamento (tranca a saída de A Beira, solta a bolsa T2). Gere uma prancha técnica do mini-chefe. Mesmo cabeçalho institucional. Caixa de especificação: escala de chefe (2,5 a 4,0 u, contra 1,8 u do jogador), orçamento até 4.000 tris. Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado. Grade de escala mostrando a altura do chefe ao lado da altura do personagem-base (1,8 u). Painel "NO JOGO" isométrico. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## ChatGPT:

Sidinei, há uma lacuna importante na fonte: o JSON **não diz que O Primeiro Perdido reutiliza o esqueleto do jogador**. Ele só define que é um chefe T2, a descrição literal — “Chegou muito antes de voce e nunca atravessou. Ainda veste o que tinha no dia em que foi puxado.” — e o comportamento de trancar a saída e soltar a Bolsa T2. fileciteturn6file0L40-L50

Então tratei **esqueleto compartilhado, roupa, arma e demais detalhes visuais como interpretação de direção de arte**, não como decisão fechada. A escala de **2,5–4,0 u** e o teto de **4.000 tris** são, por outro lado, definidos na bíblia visual. fileciteturn7file0L5-L11 fileciteturn7file1L20-L28

---

## Sidinei:

**15. Bartolomeu, o Língua**

> Releia antes de gerar, em `mvp_npcs.json`, a descrição exata de Bartolomeu, o Língua — use o texto literal do arquivo. Gere uma prancha técnica do NPC, recepção e tutorial de A Beira. Mesmo esqueleto do personagem-base, identidade própria de morador antigo. Mesmo cabeçalho institucional, mesmo orçamento do personagem base. Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado. Painel "NO JOGO" isométrico. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## Sidinei:

**16. A Barqueira**

> Releia antes de gerar, em `mvp_npcs.json`, a descrição exata da Barqueira — use o texto literal do arquivo. Gere uma prancha técnica da NPC, do Porto de Passagem — mercado, montaria, armazém e travessia. Mesmo esqueleto do personagem-base. Mesmo cabeçalho institucional, mesmo orçamento do personagem base. Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado. Painel "NO JOGO" isométrico. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## ChatGPT:

Sidinei, a documentação define a Barqueira como NPC de **mercado e travessia**, com serviços de **mercado, montaria, armazém, Árvore do Destino e travessia**; a descrição literal é: **“Leva gente para o outro lado e cobra em trabalho. Nao explica para onde vai a travessia, e ninguem que embarcou voltou para perguntar.”** fileciteturn11file0L12-L28

Como o JSON **não especifica roupa, idade, acessórios, cabelo ou aparência física**, esses elementos da prancha são interpretações visuais para materializar o papel da NPC, não decisões fechadas do MVP. Mantive o orçamento dentro do teto de **3.000 tris do personagem completo**. fileciteturn11file1L52-L60

---

## Sidinei:

**17. O Ferramenteiro**

> Releia antes de gerar, em `mvp_npcs.json`, a descrição exata do Ferramenteiro — use o texto literal do arquivo. Gere uma prancha técnica do NPC, do Porto de Passagem — craft de ferramenta. Mesmo esqueleto do personagem-base. Mesmo cabeçalho institucional, mesmo orçamento do personagem base. Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado. Painel "NO JOGO" isométrico. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## ChatGPT:

Sidinei, a descrição literal do arquivo para **O Ferramenteiro** é: **“Faz o que todo mundo precisa e ninguem elogia. Explica a mesma regra de tier cinco vezes por dia.”** O papel é **“ferramentas”** e o serviço é **“craft de ferramenta”**. fileciteturn13file0L12-L18

Como a fonte não define aparência física, roupa, idade ou acessórios, esses detalhes visuais da prancha são **interpretações de direção de arte**, mantendo a função de artesão legível. O orçamento segue o teto documentado de **até 3.000 tris para personagem completo**. fileciteturn13file1L32-L38

---

## Sidinei:

**1. Atlas de paleta — Ambiente**

> Releia antes de gerar, em `direcao-de-arte.md`, seção 0: a regra de atlas 256×256 por família. Gere o atlas de paleta da família "Ambiente": faixas de cor para areia/praia, madeira de construção colonial, vegetação de mata, pedra de pedreira. Mesmo cabeçalho institucional (logotipo, título, fundo azul-escuro, painéis com contorno claro). Formato: atlas 256×256, faixas chapadas, sem gradiente — referência técnica.

---

## Sidinei:

**2. Atlas de paleta — Criaturas**

> Releia antes de gerar, em `mvp_mobs.json`: os materiais/cores mencionados na descrição de cada mob (carapaça, pelagem). Gere o atlas de paleta da família "Criaturas": faixas de cor para carapaça (caranguejo), pelagem (macaco, morcego) e pedra (Cascalho Vivo, se aplicável). Mesmo cabeçalho institucional e mesmo formato técnico.

---

## Sidinei:

**3. Kit de cenário — A Beira**

> Releia antes de gerar, em `mvp_zones.json`, a descrição exata de A Beira — use o texto literal do arquivo, não parafraseie. Gere uma prancha técnica do kit de cenário mínimo, zona de spawn. Mesmo cabeçalho institucional. Caixa de especificação: "GRADE DE 2×2 U / ORÇAMENTO: 50 A 300 TRIS POR PROP". Peças em vista isolada, isométrica 3/4 cada uma (sem exigir ortográfica/wireframe por peça — são vários props simples, o foco é a leitura do conjunto): chão de praia, duas pedras, uma palmeira, uma tora, um barril. Painel de composição mostrando as peças montadas juntas na grade de 2 u. Cores do atlas de Ambiente. Rodapé: USO NO MVP, ESPECIFICAÇÕES (lista de props com o orçamento de tris de cada um em texto), OBSERVAÇÕES.

---

## Sidinei:

**4. Kit de cenário — Porto de Passagem**

> Releia antes de gerar, em `mvp_zones.json`, a descrição exata do Porto de Passagem. Gere uma prancha técnica do kit de cenário da vila-hub. Mesmo cabeçalho institucional, mesma caixa de especificação (grade de 2×2 u, 50 a 300 tris por prop). Peças em vista isolada isométrica: barraca de mercado, estação de forja, estação de refino, doca simples. Arquitetura colonial modesta, sem ornamentação. Painel de composição na grade. Rodapé: USO NO MVP, ESPECIFICAÇÕES (lista com orçamento de cada prop), OBSERVAÇÕES.

---

## ChatGPT:

Sidinei, a descrição literal do **Porto de Passagem** é: **“Vila de quem espera a travessia. Mercado, estacoes de refino e craft, e a Barqueira.”**; o JSON também registra os serviços de mercado, forja, refino, descanso, armazenamento e troca. fileciteturn19file0L12-L28

A **doca simples** e os formatos arquitetônicos específicos dos quatro props não são detalhados no JSON, então foram tratados como interpretação visual para materializar o hub. Os valores de tris mostrados na prancha são **estimativas de mockup**, todos dentro da faixa documentada de **50–300 tris por prop**. fileciteturn19file1L44-L50

---

## Sidinei:

**5. Kit de cenário — Mata Revirada**

> Releia antes de gerar, em `mvp_zones.json`, a descrição exata de Mata Revirada. Gere uma prancha técnica do kit de cenário, T2. Mesmo cabeçalho institucional e mesma caixa de especificação. Vegetação com leitura ligeiramente desalinhada/estranha — sem virar floresta de fantasia. Peças em vista isolada isométrica, painel de composição na grade de 2 u. Rodapé: USO NO MVP, ESPECIFICAÇÕES (lista com orçamento de cada prop), OBSERVAÇÕES.

---

## Sidinei:

**6. Kit de cenário — Pedreira Torta**

> Releia antes de gerar, em `mvp_zones.json`, a descrição exata de Pedreira Torta. Gere uma prancha técnica do kit de cenário, T2. Mesmo cabeçalho institucional e mesma caixa de especificação. Rocha exposta, corte inacabado, sensação de obra abandonada. Peças em vista isolada isométrica, painel de composição na grade de 2 u. Rodapé: USO NO MVP, ESPECIFICAÇÕES (lista com orçamento de cada prop), OBSERVAÇÕES.

---

## ChatGPT:

Sidinei, a descrição literal de **Pedreira Torta** é: **“Corte de pedra que nunca foi terminado por ninguem. Fibra e minerio.”** fileciteturn21file0L9-L15

A documentação não especifica quais props individuais compõem o kit; portanto, os elementos da prancha — parede de rocha, blocos, andaime, entulho etc. — são **interpretações visuais minhas** para materializar a ideia de corte inacabado. O orçamento usado é o documentado para props de cenário: **50–300 tris por peça**. fileciteturn21file2L35-L42

---

## Sidinei:

**7. Caranguejo da Beira**

> Releia antes de gerar, em `mvp_mobs.json`, a descrição exata do Caranguejo da Beira — use o texto literal do arquivo. Gere uma prancha técnica do mob, fauna de A Beira, esqueleto de rastejante. Mesmo cabeçalho institucional. Caixa de especificação: "FAUNA PEQUENA (0,4 A 0,8 U) / ORÇAMENTO: 800 A 1.500 TRIS". Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado com a contagem de tris. Painel "NO JOGO" isométrico. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## Sidinei:

**8. Cascalho Vivo** — *pergunta aberta: a descrição não define estrutura corpórea, então gere como estudo de silhueta/conceito, não como modelo com esqueleto fechado; decida a abordagem antes de aprovar.*

> Releia antes de gerar, em `mvp_mobs.json`, a descrição exata do Cascalho Vivo — confirme que, de fato, não há nenhuma pista de estrutura corpórea além de "pedra que se junta e anda". Gere um estudo conceitual. Sem esqueleto humanoide, quadrúpede ou de ave — é um amontoado de pedras animado. Mesmo cabeçalho institucional, mas identificado como "ESTUDO — NÃO É DECISÃO FECHADA" na caixa de especificação, sem exigir wireframe ou vista ortográfica rígida (ainda não há malha a resolver). Proponha 1 a 2 leituras de silhueta possíveis, cada uma com uma vista isolada. Rodapé: OBSERVAÇÕES (marcando explicitamente que é estudo).

---

## Sidinei:

**9. Macaco Revirado**

> Releia antes de gerar, em `mvp_mobs.json`, a descrição exata do Macaco Revirado. Gere uma prancha técnica do mob, fauna de Mata Revirada, esqueleto de quadrúpede. Mesmo cabeçalho institucional. Caixa de especificação: "FAUNA MÉDIA (\~1,0 U, BASELINE DA CATEGORIA) / ORÇAMENTO: 800 A 1.500 TRIS". Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado. Painel "NO JOGO" isométrico. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## Sidinei:

**10. Morcego da Torta**

> Releia antes de gerar, em `mvp_mobs.json`, a descrição exata do Morcego da Torta. Gere uma prancha técnica do mob, fauna de Pedreira Torta, esqueleto de ave/voador. Mesmo cabeçalho institucional. Caixa de especificação: "FAUNA PEQUENA (0,4 A 0,8 U) / ORÇAMENTO: 800 A 1.500 TRIS". Vista frontal e lateral ortográficas exatas sem perspectiva, vista de baixo (útil por ser voador) no lugar da vista de costas, wireframe rotulado. Painel "NO JOGO" isométrico. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## Sidinei:

**11. Mula**

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Ferramentas e transporte": a Mula é T2, comprada no mercado, transporte e não combate — não há altura documentada. Gere uma prancha técnica da montaria, esqueleto de quadrúpede. Mesmo cabeçalho institucional. Caixa de especificação sem número de altura fixo (não documentado — escala compatível com o personagem montado nela) e orçamento de 800 a 1.500 tris (faixa de fauna). Vista frontal e lateral ortográficas exatas sem perspectiva, vista de costas, wireframe rotulado. Painel "NO JOGO" com o personagem-base montado nela, mostrando a escala relativa. Cores do atlas de Criaturas. Rodapé: USO NO MVP, ESPECIFICAÇÕES, OBSERVAÇÕES.

---

## Sidinei:

**12. Ícones dos recursos** — *interpretação: assumo "cinco recursos" = as cinco famílias que aparecem em* *`dados-do-mvp.md`**, seção "Materiais" (madeira, fibra, couro, minério, pedra) — o documento não lista "cinco recursos" explicitamente em lugar nenhum, é dedução a partir dos materiais T1/T2 listados lá.*

> Releia antes de gerar, em `dados-do-mvp.md`, a seção "Materiais" (T1 e T2, brutos e refinados) — confirme as cinco famílias antes de desenhar os ícones. Gere uma prancha de ícones dos recursos do MVP, como renderizados de modelo 3D em câmera ortográfica: uma família por categoria — madeira, pedra, fibra, couro e minério — nos tamanhos 24, 32, 48 e 64 px. Mesmo cabeçalho institucional. Cores do atlas de Ambiente/Criaturas conforme o caso. Rodapé: OBSERVAÇÕES (nota de que são renders do modelo, nunca desenho à mão).

---

## Sidinei:

**13. Prancha de escala comparativa** — *cole aqui a imagem do personagem-base do Chat 1 antes deste prompt.*

> Releia antes de gerar, em `direcao-de-arte.md`, seção 3 (escala e unidades): as alturas documentadas de cada categoria. Gere a prancha de escala e orçamento: o personagem de 1,8 u colado nesta conversa, ao lado da fauna pequena (Caranguejo, Morcego), fauna média (Macaco Revirado) e do mini-chefe (2,5 a 4,0 u), todos na mesma grade de 0,5 u, mostrando a proporção real entre eles. Mesmo cabeçalho institucional. Tabela de orçamento de tris por categoria ao lado. Rodapé: OBSERVAÇÕES (esta prancha é a referência de escala final — confira toda peça nova contra ela antes de modelar).

---

## Sidinei:

## 🟣 CHAT 3 — Sistema: UI e Produção

Não depende de nenhum conteúdo visual específico do jogo — pode abrir a qualquer momento, mesmo antes dos outros dois.

**1. Guia de UI e blocos**

> Releia antes de gerar, em `direcao-de-arte.md`, seções 11 (interface) e 12 (tipografia): os oito blocos exatos e a linguagem visual proibida (UI dourada). Gere a prancha de UI: os oito blocos independentes (Topo, Personagem, Equipamento, Cena, Ação, Ações da zona, Inventário, Eventos), arranjo lado a lado (desktop) e em abas (mobile), HUD em exploração, HUD em combate, inventário, equipamento com os sete slots, mapa, a Árvore do Destino com os quatro ramos, tela de crafting. Mesmo cabeçalho institucional (logotipo "ERAS DO BRASIL", título, fundo azul-escuro, painéis com contorno claro, texto em português, infográfico de game design). Linguagem visual: retângulo arredondado, contorno escuro, fundo escuro, ícone simples, título curto, número destacado, botão com três estados. Sem UI dourada ou ornamental. Tipografia sem serifa, grossa, legível, com suporte completo a acento/til/cedilha.

---

## Sidinei:

**2. Guia de produção**

> Releia antes de gerar, em `direcao-de-arte.md`, seção 13 (produção): estrutura de pastas, nomenclatura e checklist exatos. Gere a prancha de produção: fluxo do conceito ao asset final (Blender → Godot), estrutura de pastas (`art/source/`, `art/exports/`, `art/palettes/`, `art/references/`, `art/fonts/` — `source/` e `exports/` com `characters/ equipment/ environment/ creatures/ ui/`), convenção de nomenclatura (`char_player_base.glb`, `equip_weapon_sword_t2.glb` etc.), checklist de qualidade (orçamento de tris, pivô na origem, atlas de paleta, escala, exportação glTF, silhueta legível a três metros). Mesmo cabeçalho institucional.**2. Guia de produção**
>
> > Releia antes de gerar, em `direcao-de-arte.md`, seção 13 (produção): estrutura de pastas, nomenclatura e checklist exatos. Gere a prancha de produção: fluxo do conceito ao asset final (Blender → Godot), estrutura de pastas (`art/source/`, `art/exports/`, `art/palettes/`, `art/references/`, `art/fonts/` — `source/` e `exports/` com `characters/ equipment/ environment/ creatures/ ui/`), convenção de nomenclatura (`char_player_base.glb`, `equip_weapon_sword_t2.glb` etc.), checklist de qualidade (orçamento de tris, pivô na origem, atlas de paleta, escala, exportação glTF, silhueta legível a três metros). Mesmo cabeçalho institucional.**2. Guia de produção**
> >
> > > Releia antes de gerar, em `direcao-de-arte.md`, seção 13 (produção): estrutura de pastas, nomenclatura e checklist exatos. Gere a prancha de produção: fluxo do conceito ao asset final (Blender → Godot), estrutura de pastas (`art/source/`, `art/exports/`, `art/palettes/`, `art/references/`, `art/fonts/` — `source/` e `exports/` com `characters/ equipment/ environment/ creatures/ ui/`), convenção de nomenclatura (`char_player_base.glb`, `equip_weapon_sword_t2.glb` etc.), checklist de qualidade (orçamento de tris, pivô na origem, atlas de paleta, escala, exportação glTF, silhueta legível a três metros). Mesmo cabeçalho institucional.**2. Guia de produção**
> > >
> > > > Releia antes de gerar, em `direcao-de-arte.md`, seção 13 (produção): estrutura de pastas, nomenclatura e checklist exatos. Gere a prancha de produção: fluxo do conceito ao asset final (Blender → Godot), estrutura de pastas (`art/source/`, `art/exports/`, `art/palettes/`, `art/references/`, `art/fonts/` — `source/` e `exports/` com `characters/ equipment/ environment/ creatures/ ui/`), convenção de nomenclatura (`char_player_base.glb`, `equip_weapon_sword_t2.glb` etc.), checklist de qualidade (orçamento de tris, pivô na origem, atlas de paleta, escala, exportação glTF, silhueta legível a três metros). Mesmo cabeçalho institucional.

---
