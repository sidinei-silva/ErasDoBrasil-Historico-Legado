## Sidinei:

Em cima deste compandio eu quero achar um outro nome para Tempera algo que seja mais generico, ou menos poetico e que se encaixe melhor para o que ele é, não pode ser especialização porque as arvores de armas e armadura ja vai ter especialização

---

## ChatGPT:

Sim, Sidinei. Lendo o compêndio, eu também acho que **“Têmpera” está ficando poético demais e, principalmente, não descreve bem o que o sistema realmente faz**.

O ponto central é este:

> **não é uma especialização da arma; é um modificador temporário de desempenho gerado pelo uso contínuo daquela arma.**

No documento, ela vai de **1,0 a 1,5**, sobe ao longo de **60 ações com a mesma arma**, congela offline e zera quando você troca de arma. E o próprio compêndio diz que ela é a **“régua do projeto inteiro”**. fileciteturn1file0L36-L43

Então eu procuraria um nome que seja:

- genérico;
- fácil de entender;
- aplicável a qualquer arma;
- não pareça uma árvore de progressão;
- não concorra semanticamente com **Maestria/Especialização**;
- possa aparecer naturalmente na UI: `Arma 87% de X`;
- não dependa da fantasia brasileira para fazer sentido.

### Minha primeira escolha: **Familiaridade**

Acho que **Familiaridade** encaixa muito bem.

> **Familiaridade:** aumenta conforme o jogador usa continuamente a mesma arma, chegando a 1,5×. É perdida ao trocar de arma.

Por quê?

Porque o conceito não é que o personagem esteja **se especializando permanentemente** naquela arma. Ele simplesmente está **mais familiarizado com ela naquele momento**.

E isso cria uma distinção muito boa:

**Especialização**
→ progressão permanente  
→ pertence à Árvore do Destino  
→ representa domínio de uma linha

**Familiaridade**
→ progressão temporária  
→ pertence ao equipamento em uso  
→ representa costume com aquela arma específica

Exemplo:

> **Especialização em Espadas: nível 23**  
> **Familiaridade: 82%**

Isso é muito mais intuitivo para mim do que:

> Especialização em Espadas: nível 23  
> Têmpera: 82%

---

## Outras opções que eu consideraria

| Nome | Minha avaliação | Ideia transmitida |
|---|---:|---|
| **Familiaridade** | ⭐⭐⭐⭐⭐ | Quanto você está acostumado com aquela arma |
| **Prática** | ⭐⭐⭐⭐⭐ | Quanto você praticou com ela |
| **Uso** | ⭐⭐⭐⭐ | Quanto aquela arma vem sendo utilizada |
| **Experiência** | ⭐⭐⭐⭐ | Experiência recente com aquela arma |
| **Adaptação** | ⭐⭐⭐⭐ | O personagem se adapta ao equipamento |
| **Ajuste** | ⭐⭐⭐ | Equipamento/personagem se ajustando |
| **Preparo** | ⭐⭐⭐ | Prontidão para usar aquela arma |
| **Domínio** | ⭐⭐⭐ | Forte, mas começa a invadir o território de Maestria |
| **Afinidade** | ⭐⭐⭐ | Boa, mas tem uma conotação mais abstrata |
| **Hábito** | ⭐⭐ | Conceitualmente correto, mas estranho como atributo |
| **Condicionamento** | ⭐⭐ | Muito técnico |
| **Proficiência** | ⭐⭐ | Parece progressão permanente/especialização |

### Eu descartaria "Domínio", "Proficiência" e "Afinidade"

Principalmente porque temos uma hierarquia conceitual muito importante no projeto.

A **Árvore do Destino já possui maestria**. Ela representa a progressão permanente do jogador: combate, coleta, refino e craft, com bônus específicos por nível. fileciteturn1file0L16-L34

Se colocarmos:

> **Domínio da Espada**

fica difícil explicar por que existe também:

> **Maestria da Espada**

E aí o jogador inevitavelmente pergunta:

*"Qual a diferença entre domínio e maestria?"*

Não precisamos desse problema.

---

# Mas existe uma opção ainda mais simples: **Prática**

Eu gosto **muito** de "Prática" para esse projeto.

Porque o sistema essencialmente diz:

> **Quanto mais você usa uma arma, melhor você fica usando ela.**

E não diz:

> Você desbloqueou uma nova capacidade permanente com essa arma.

Então:

**Prática: 73%**

é extremamente direto.

Poderia até ser:

> **Prática com a arma**  
> 73%

E a descrição:

> **Aumenta com o uso contínuo da arma. É perdida ao trocar de arma.**

Isso é quase impossível de interpretar errado.

---

# Minha hierarquia

Se eu estivesse fechando o GDD agora, eu testaria nesta ordem:

### 1. **Familiaridade** — melhor nome conceitual

É o que melhor explica o comportamento temporário.

> "Estou familiarizado com essa arma."

Não significa que você desbloqueou uma especialização.

### 2. **Prática** — melhor nome de gameplay

É mais seco e mais "sistema de jogo".

> "Usei essa arma por bastante tempo, então tenho mais prática com ela."

Também combina muito com a proposta de o jogo ser mais **rústico e direto**, que você vem buscando na direção do projeto.

### 3. **Uso** — melhor nome minimalista

Se vocês quiserem reduzir ainda mais a linguagem:

> **Uso: 42/60**

Isso inclusive pode ser melhor do que mostrar um multiplicador.

---

## E tem uma mudança que eu faria além do nome

Eu **não mostraria 1,0–1,5 para o jogador**.

Internamente, tudo bem:

```text
temperamento = 1.0 → 1.5
```

Mas para o jogador eu faria algo como:

> **Familiaridade**  
> ███████░░░ 70%  
> **Bônus: +35%**

Ou:

> **Prática**  
> 42 / 60 ações  
> **Bônus atual: +35%**

Isso deixa a regra muito mais concreta.

Porque `1.35×` é linguagem de balanceamento.  
`35% de bônus` é linguagem de jogador.

---

# E eu mudaria "Têmpera" no próprio conceito

Hoje o compêndio diz:

> **Têmpera: multiplicador de 1.0 a 1.5 ao longo de 60 ações com a mesma arma. Congela offline, reseta na troca. Custo de oportunidade, nunca punição. É a régua do projeto inteiro.** fileciteturn1file0L36-L43

Eu escreveria:

> **Familiaridade:** aumenta com o uso contínuo da mesma arma, chegando a um bônus máximo de 50% após 60 ações. Congela offline e é perdida ao trocar de arma. É um bônus temporário de uso, não uma progressão permanente.

E manteria **Maestria** exclusivamente para a progressão da Árvore do Destino.

Isso cria uma separação semântica muito limpa:

**Maestria = aquilo que você aprendeu permanentemente.**  
**Familiaridade = aquilo com que você está acostumado agora.**

Na minha opinião, **Familiaridade é o nome mais correto para o sistema que vocês realmente desenharam**. "Têmpera" é bonito, mas parece nome de mecânica/lore que foi inventado para soar interessante, enquanto **Familiaridade parece nome de sistema que o jogador entende imediatamente**.

---

## Sidinei:

E sobre **Firme, trêmula e rachada.** São as bandas de risco. O Albion usa azul, amarelo, vermelho e preto — cor pura, sem metáfora, e todo jogador de MMO entende na hora.

Qual nome poderia ser?

---

## ChatGPT:

Sim, Sidinei. Aqui eu faria uma escolha **bem diferente de "Têmpera"**.

Como essas bandas são uma regra fundamental de leitura do mundo — elas determinam **se existe PvP, quanto se perde e qual é o risco** — eu concordo com a lógica de usar nomes extremamente fáceis de entender. No compêndio, hoje elas são:

- **Firme** → ninguém ataca ninguém
- **Trêmula** → PvP sinalizado, perda parcial
- **Rachada** → PvP sinalizado, perda total
- **Emaranhado** → continente 2, sem flag e perda total fileciteturn1file3L192-L226

O problema é que **Firme / Trêmula / Rachada não são imediatamente escaláveis**. O jogador precisa aprender o significado de cada uma.

Eu procuraria um nome de **categoria**, e não nomes metafóricos para cada banda.

## Minha escolha: **Risco**

Simplesmente:

> **Risco 1 — Seguro**  
> **Risco 2 — Perigoso**  
> **Risco 3 — Mortal**

Mas eu acho que dá para fazer ainda melhor.

### Opção que mais gosto: **Segura / Disputada / Mortal**

| Banda | Nome | Regra |
|---|---|---|
| Azul | **Segura** | Sem PvP |
| Amarela | **Disputada** | PvP consentido, perda parcial |
| Vermelha | **Mortal** | PvP consentido, perda total |
| Preta | **Selvagem** | PvP aberto, perda total |

Isso comunica a progressão quase sozinho:

**Segura → Disputada → Mortal → Selvagem**

E "Selvagem" diferencia bem o Emaranhado porque ele não é simplesmente "uma rachada mais perigosa": lá **entrar já significa consentir e não existe flag**. fileciteturn1file3L224-L226

---

## Mas eu faria um teste ainda mais "MMO"

### **Segura / Hostil / Letal / Mortal**

A progressão fica:

> 🟦 **Segura**  
> 🟨 **Hostil**  
> 🟥 **Letal**  
> ⬛ **Mortal**

É muito fácil de entender.

**Segura:** ninguém pode te atacar.  
**Hostil:** existe conflito, mas existe proteção/perda parcial.  
**Letal:** você pode perder tudo.  
**Mortal:** não existe proteção de flag.

O problema é que **Hostil** pode sugerir que qualquer jogador pode te atacar, o que não é verdade na banda amarela.

---

# Uma opção que acho particularmente boa para o Eras

### **Paz / Disputa / Conflito / Caos**

Tem uma lógica muito natural:

> **Paz** → ninguém luta  
> **Disputa** → PvP consentido e perda parcial  
> **Conflito** → PvP consentido e full loot  
> **Caos** → PvP aberto/full loot

Mas aqui voltamos a algo um pouco mais **temático/poético**, justamente o que você está tentando reduzir.

Por isso eu não escolheria essa.

---

# Outra linha: usar literalmente o grau de perigo

### **Baixo / Médio / Alto / Extremo**

É extremamente genérico.

> **Risco: Baixo**  
> **Risco: Médio**  
> **Risco: Alto**  
> **Risco: Extremo**

Vantagem: ninguém precisa aprender nada.

Desvantagem: fica com cara de **interface de sistema**, e não de mundo.

Eu acho genérico demais para um jogo que quer ter identidade própria.

---

# O que eu evitaria

Eu não tentaria encontrar outra sequência de palavras poéticas como:

> Estável → Instável → Fraturado

ou

> Inteiro → Trincado → Partido

Porque isso é exatamente o mesmo problema de **Firme / Trêmula / Rachada**.

São nomes legais quando você já conhece o sistema, mas não são bons **rótulos de gameplay**.

E principalmente: **o jogador não deveria precisar lembrar que "rachada" significa full loot**.

---

# Minha recomendação final

Eu testaria estas três candidatas:

### 🥇 **Segura / Disputada / Mortal / Selvagem**

Minha favorita.

É clara, tem personalidade e ainda diferencia o continente 2.

### 🥈 **Segura / Hostil / Letal / Mortal**

Mais agressiva e com uma linguagem mais típica de MMO.

### 🥉 **Baixo / Médio / Alto / Extremo**

A mais funcional, mas a menos interessante.

---

E tem uma coisa importante: **eu não usaria "Risco" como nome da banda individual**.

Faria:

> **Nível de Risco: Disputada**

ou simplesmente:

> **Zona Disputada**

Porque "Risco" é a **categoria mecânica**, enquanto "Disputada" é o **estado da zona**.

Isso combina muito bem com a estrutura que vocês já definiram, onde **risco é um dos cinco campos independentes da modelagem** — continente, era, região, tier e risco. fileciteturn0file0L43-L50

**Se fosse meu projeto, eu substituiria Firme/Trêmula/Rachada por _Segura/Disputada/Mortal_ e deixaria _Selvagem_ exclusivamente para o Emaranhado.** É simples o suficiente para um jogador entender em segundos, mas ainda tem personalidade própria.

---
