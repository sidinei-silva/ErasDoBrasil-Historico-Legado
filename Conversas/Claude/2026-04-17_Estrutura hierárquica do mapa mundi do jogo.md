## Sidinei:

Estou um pouco confuso sobre a disposição do mapa mundi do jogo, mesmo pensando no mvp eu quero conseguir ter uma visão de como será a divisão nas fases mais avançadas do jogo.

Por exemplo eu tenho regiões (mapa costeira), dentro tenho zonas(vila de são tome) e dentro dela vou ter o que? pontos de interesses? tipo praças e estabelecimentos que posso entrar. como posso chamar isso dentro da zona? ou isso será a zona, quero entender a disposição do mapa mundi do jogo. Quero entrar e sentir o mundo tipo me imergir e me ajudar a criar e desenvolver o jogo, por conta própria.

---

## Claude:

Boa pergunta, mas você está mexendo num assunto que **já foi decidido formalmente** na sessão de 2026-03-20 (Cap. 5B — Arquitetura do Mapa). Antes de te ajudar a "imergir", preciso te alertar sobre um risco que você mesmo documentou:

> **Princípio que você confirmou:** "Features que pertencem à Temporada 2+ (sub-locais, POIs como construtos de UI) não podem ser trazidas pro MVP sob outro nome."

A pergunta que você está fazendo agora é exatamente o caminho para violar isso. Vou destrinchar.

## A hierarquia que já existe (e está correta)

Está tudo no `05B_Arquitetura_do_Mapa.md`:

1. **Camada 1 — Mapa-Múndi (Regiões):** Mata Costeira, Sertão Distorcido, etc.
2. **Camada 2 — Mapa Regional (Zonas):** 8–15 nós por região conectados por grafo. Vila de São Tomé é um nó.
3. **Camada 3 — Mapa Local (Sub-locais):** Vila de São Tomé se desdobraria em "Praça Central", "Forja", "Taverna", "Capela" como nós internos. **Explicitamente adiado para Temporada 2+.**

Então sua pergunta "o que vem dentro da zona?" tem duas respostas diferentes dependendo da fase do jogo.

## O que está dentro da zona NO MVP

Olha o mockup atual de Vila de São Tomé (`ExplorationView`):

```
━━━ Vila de São Tomé ━━━
O sol da tarde aquece as paredes de pau-a-pique. O Ferreiro Tomás
bate seu martelo na forja. O cheiro de peixe seco e mandioca vem
da taverna.

Você vê: Ferreiro Tomás (NPC), Curandeira Naila (NPC), Guarda
Saídas: [Norte] Floresta · [Leste] Rio · [Oeste] Pico
```

Aqui a forja, a taverna e a capela **não são lugares navegáveis**. Elas são **elementos de cenário e contexto** mencionados na descrição. O que é interativo de verdade são:

- **Os NPCs** (Ferreiro Tomás → comércio/diálogo; Curandeira → cura/diálogo; Guarda → quests/diálogo)
- **As saídas** (para outras zonas)
- **Comandos contextuais da zona** (descansar, olhar ao redor, examinar mural)

A "forja" só existe como flavor narrativo que justifica a presença do Ferreiro Tomás. Você não "entra na forja" — você **fala com o ferreiro**, e o sistema abre a UI de comércio. A "taverna" justifica que NPCs vão pra lá no período da Tarde (rotina). A "capela" justifica os serviços anti-maldição.

**Nome correto pra isso:** não é "ponto de interesse". É **conteúdo da zona** — composto por NPCs, recursos coletáveis, eventos disponíveis e flavor descritivo. Uma estrutura típica seria:

```yaml
zona_vila_sao_tome:
  tipo: urbano_seguro
  descricoes: [manha, tarde, noite, madrugada]  # textos por período
  npcs: [ferreiro_tomas, curandeira_naila, guarda_vila, taverneiro_X]
  servicos: [reparo_armas, cura_maldicoes, descanso_longo_rapido]
  recursos_coletaveis: []  # vila não tem coleta
  eventos_possiveis: [chegada_mercador, briga_taverna, missao_guarda]
  saidas: [floresta_norte, rio_mares, pico_neblina]
```

Isso é tudo flat. Não tem hierarquia interna.

## O que muda na Temporada 2+ (Camada 3)

**Aí sim** Vila de São Tomé vira um sub-grafo de nós:

```
Vila de São Tomé (zona-mãe)
├─ Praça Central       (hub interno, mural, poço)
├─ Forja do Tomás      (Ferreiro mora aqui)
├─ Taverna do Bento    (NPCs vão pra cá à noite)
├─ Capela              (Padre, anti-maldição)
└─ Cais                (saída para Rio das Marés)
```

Agora cada um vira um nó próprio com sua própria descrição, sua própria lista de NPCs presentes (Ferreiro fica na Forja de manhã, vai pra Taverna à noite — e o player vê isso refletido em qual sub-local ele está), seus próprios eventos. **Mas isso só faz sentido implementar quando uma zona ficar populosa demais** (muitos players concorrendo pelos mesmos NPCs/recursos), o que é problema de Temporada 2+.

## O risco que você está prestes a cometer

Quando você pergunta "como posso chamar isso dentro da zona?", você está pedindo um **nome para uma camada que o MVP não tem**. Isso é o típico anti-padrão de smuggling: você inventa "Pontos de Interesse" ou "Estabelecimentos" como conceito de UI, começa a desenhar como NPCs se distribuem entre eles, como o player navega entre eles — e três semanas depois você tem Camada 3 implementada com outro nome, pra uma única zona, sem necessidade real.

**Pergunta de pressão:** Você está pedindo isso porque (a) a UX atual da Vila parece pobre demais, ou (b) você quer só visualizar o futuro do jogo? São problemas diferentes.

- Se for (a): o problema **não é falta de sub-locais**. É falta de descrição rica, eventos contextuais e NPCs com presença narrativa forte. Imersão se faz com texto e reatividade, não com mais cliques.
- Se for (b): você já tem o documento. A Camada 3 existe no GDD com exemplo da Floresta do Norte. Não precisa duplicar.

## O que eu recomendo

1. **Não invente nomenclatura nova agora.** A trinca Região → Zona → Sub-local já cobre tudo. Adicionar "POI" no MVP só vai gerar confusão depois.
2. **Para imersão da Vila no MVP, invista em três coisas dentro da zona:**
   - **Descrições por período do dia** (4 variantes: manhã/tarde/noite/madrugada já alinhadas com a periodização do `world.go`)
   - **Mensagens sistêmicas reativas** ("[Tarde] O Ferreiro Tomás guardou as ferramentas e foi à taverna" — isso já está no mockup, mantém)
   - **Comandos contextuais** (`olhar mural`, `olhar poço`, `examinar forja`) que retornam descrição extra sem mudar de zona
3. **Quando começar a planejar Temporada 2**, aí sim você abre o ticket de "Camada 3 — sub-locais da Vila" e desenha o sub-grafo. Aí faz sentido. Hoje, não.

Quer que eu desenhe a estrutura de dados completa do "conteúdo de zona" pro MVP (NPCs + serviços + eventos + descrições por período), ou prefere primeiro discutir como tornar a descrição da Vila mais imersiva sem subdividir?

---

## Sidinei:

Você colocou yaml ele é melhor que json para colocar os dados dos npcs? E locais e dados estáticos inicias do jogo?

---

## Claude:

Depende do que você vai colocar no arquivo, mas pro seu caso específico a resposta honesta é: **YAML é melhor pra dados editados à mão por você, JSON é melhor pra dados que o servidor lê/escreve em runtime**. E tem uma pegadinha no seu backlog que quero apontar antes.

## Primeiro, uma contradição no seu próprio GDD

Seu `BACKLOG.md` tem:

- `Schema JSON: CompetitiveQuest`
- `Schema JSON: EnemyEvolution`

Isso pode significar duas coisas:
1. "Vou usar **JSON Schema** pra validar meus dados" (JSON Schema é um padrão de validação que funciona tanto com JSON quanto com YAML)
2. "Vou armazenar esses dados em **arquivos .json**" (decisão de formato já tomada)

Você sabe qual das duas? Porque se for (2), mudar pra YAML agora invalida essa decisão. Se for (1), tá tudo em aberto.

## A comparação técnica (sem romantizar nenhum)

**YAML vence em:**
- **Comentários** — o grande trunfo. Você vai precisar deixar "por que o Ferreiro Tomás tem +20% em Minério de Sangue?" registrado no dado, e em JSON puro isso é impossível.
- **Multiline strings** — descrições narrativas de zona (manhã/tarde/noite/madrugada) ficam MUITO mais legíveis
- **Menos ruído visual** — menos aspas, menos chaves, menos vírgulas
- **Anchors/references** (`&` e `*`) — pode reutilizar blocos comuns (um "template de guarda genérico" reutilizado em 10 vilas)

**JSON vence em:**
- **Performance de parsing** — a lib `encoding/json` do Go é ~3-5x mais rápida que `gopkg.in/yaml.v3`. Irrelevante pra dados estáticos carregados no startup, relevante se carrega com frequência.
- **Menos edge cases** — JSON tem poucas formas de errar. YAML tem muitas.
- **Tooling** — qualquer editor, qualquer linguagem, qualquer ferramenta come JSON sem biblioteca externa. Go tem `encoding/json` na stdlib; pra YAML você precisa de `gopkg.in/yaml.v3`.
- **Save/load de estado** — serializar o estado do mundo em YAML seria insano; JSON é o formato natural.

## As pegadinhas reais do YAML que você VAI encontrar

Essas não são teóricas, são bugs que devs perdem horas caçando:

1. **O "Norway Problem":** se um ferreiro tiver país de origem `NO` (Noruega), YAML 1.1 parseia como `false`. Versões `YES`/`NO`/`ON`/`OFF` viram booleanos. Solução: sempre aspas em strings suspeitas. Sua classe `Missionário` num diálogo tipo `origem: NO` vira bug de lore.
2. **Versões como números:** `versao: 1.0` → float `1.0`. Se você escrever `1.10` fica `1.1`. Aspas obrigatórias.
3. **Datas automáticas:** `data: 1497-04-22` vira objeto de data, não string. Pode ou não ser o que você quer.
4. **Tabs são proibidos.** Só espaços. E indentação errada por 1 espaço = arquivo quebrado sem mensagem clara.
5. **Trailing whitespace** em multiline strings pode entrar no valor final e você nem vê.

JSON não tem nenhum desses problemas.

## O que eu recomendo pro seu caso

Um modelo **híbrido**, baseado em quem edita o arquivo:

| Tipo de dado | Formato | Por quê |
|---|---|---|
| NPCs, zonas, quests, itens, diálogos, loot tables | **YAML** | Você edita à mão, precisa de comentários, tem descrições longas |
| Estado do mundo (save do servidor) | **JSON** | O servidor escreve/lê, ninguém edita à mão |
| Mensagens WebSocket cliente↔servidor | **JSON** | Padrão da web, qualquer cliente consome |
| Schema de validação | **JSON Schema** | Funciona pra validar ambos; mais maduro que alternativas YAML-native |

Na prática isso significa: seus arquivos em `gdd/06_Dados_e_Assets/` viram `.yaml`, e o servidor valida no carregamento usando JSON Schema (via uma lib tipo `github.com/santhosh-tekuri/jsonschema`), convertendo YAML→struct internamente. O estado persistente em disco continua JSON.

## Exemplo prático com um dos seus NPCs

**Em JSON puro** (sofrível de manter):

```json
{
  "id": "ferreiro_tomas",
  "nome": "Ferreiro Tomás",
  "zona": "vila_sao_tome",
  "rotina": {
    "manha": "forja",
    "tarde": "forja",
    "noite": "taverna",
    "madrugada": "casa"
  },
  "descricao": "Um homem de meia-idade, braços fortes, olhar cansado. Veio de Portugal com Cabral, ficou porque sua esposa morreu no desembarque."
}
```

**O mesmo em YAML** (com o que você realmente precisa):

```yaml
id: ferreiro_tomas
nome: Ferreiro Tomás
zona: vila_sao_tome

# Rotina padrão de residente. Se for atacado na forja ou
# se a Vila entrar em estado de alerta, o AIManager sobrescreve.
rotina:
  manha: forja
  tarde: forja
  noite: taverna
  madrugada: casa

descricao: |
  Um homem de meia-idade, braços fortes, olhar cansado.
  Veio de Portugal com Cabral, ficou porque sua esposa
  morreu no desembarque.

# TODO: decidir se ele dá desconto em reparo pra Colonial
# após 3 missões de afinidade. Ver Cap. 6.5.
precos:
  modificador_base: 1.00
  bonus_minerio_sangue: 1.20  # aspas? não, número mesmo
```

O segundo é mais leve, tem comentários ancorados no próprio dado, e a descrição não vira `"...desembarque.\n\nSegunda linha..."`.

## O que eu não faria

- **TOML:** bom pra configs de app (tipo `config.toml`), ruim pra dados hierárquicos profundos como os seus. Vira sopa de `[[section.subsection]]`.
- **JSON5/JSONC:** resolve o problema dos comentários mas Go não tem suporte nativo e o ecossistema é fraco. Fica numa terra-de-ninguém.
- **CSV/planilha:** pra tabelas planas (loot tables simples, preços) pode até servir, mas pros seus NPCs com estrutura aninhada, não.

## A decisão que você precisa tomar agora

Antes de escrever 50 arquivos de dados, responda:

1. Aquele "Schema JSON" no BACKLOG era JSON Schema (validação) ou formato de armazenamento?
2. Você está disposto a aprender as pegadinhas do YAML ou prefere viver com JSON sem comentários?
3. Quem edita os dados é só você, ou você planeja que contribuidores futuros mexam nisso?

Se a resposta for "só eu mesmo" pra (3), YAML compensa. Se um dia você abre o projeto pra colaboradores menos técnicos, pode valer a pena construir um editor visual e manter JSON por baixo.

Qual é seu cenário?

---
