# ⚔️ Capítulo 4 – Sistema de Combate

O sistema de combate em *Eras do Brasil* é baseado em **turnos táticos estruturados**, onde personagens e inimigos alternam suas ações de forma ordenada.

Na primeira etapa de desenvolvimento (versão de mesa e primeira versão digital), o combate ocorre em **modo de turno estático**:
- Não há movimentação física em grid ou tabuleiro durante a luta.
- Cada personagem permanece em posição abstrata e escolhe suas ações a cada rodada.

Essa abordagem torna o sistema mais ágil para a mesa e mais acessível para o primeiro protótipo digital, sem sacrificar a profundidade tática de escolhas, atributos e habilidades.

Já está planejada uma futura **expansão de regras** ("Combate Avançado – Movimentação Tática") que introduzirá:
- Deslocamento por grids e alcances físicos.
- Ataques de oportunidade.
- Controle de terreno e posicionamento em combate.

Essa expansão será ativada naturalmente no sistema conforme o jogo evoluir para a segunda fase de digitalização (movimentação livre em tempo real, estilo *Stoneshard*).

---

## 🎯 Resumo da Fase Atual do Sistema de Combate

| Aspecto | Fase Atual (mesa e 1ª etapa digital) |
|:---|:---|
| Turnos | Sim, alternância ordenada |
| Movimento durante combate | Não (posição abstrata) |
| Tipos de Ação | Ataque, habilidade, magia, defesa, item |
| Trindade Tank-Healer-DPS | Sim, funcional |
| Alcance de magias ou ataques | Abstraído por descrição da habilidade |
| Controle de área | Por efeitos de habilidades, não posição |

> **Nota:** Habilidades futuras que envolvam movimento, empurrão, alcance ou área serão adaptadas naturalmente quando o módulo tático for ativado.

---

## 📚 Organização do Capítulo 4

Este capítulo está dividido nos seguintes blocos:

- Introdução ao Combate e Visão de Fases
- Estrutura de Turno
- Ações em Combate
- Tipos de Testes em Combate
- Iniciativa e Ordem de Ação
- Rolagens Críticas e Falhas Críticas
- Defesa, Esquiva e Resistência
- Condições de Status
- Magia e Uso de Habilidades
- Exemplo Completo de Turno
- Regras Especiais Futuras (Expansão Modular)


Cada seção explicará em detalhes como jogar e mestrar combates, utilizando o sistema de atributos, modificadores e habilidades que já foram apresentados na criação de personagens.

---
## ⚡ Estrutura de Turno

Em *Eras do Brasil*, o combate é dividido em **turnos organizados**. Cada turno representa um momento de ação, onde cada personagem, aliado ou inimigo, age seguindo uma ordem de iniciativa.

O fluxo básico de um combate é:

1. **Determinar Iniciativa** (quem age primeiro)
2. **Executar Turnos** de cada participante
3. **Resolver Ações e Efeitos**
4. **Atualizar o Estado do Combate** (condições, vida, efeitos contínuos)
5. **Novo Ciclo de Turnos** (até o fim do combate)

---

### 🎯 Etapas de um Turno Individual

Durante o turno de um personagem, ele pode:

- **Mover-se** (se aplicável futuramente)
- **Realizar uma Ação Principal**:
  - Atacar
  - Usar uma habilidade
  - Lançar uma magia
  - Utilizar um item
  - Realizar uma ação especial (ajudar, proteger, preparar)
- **Usar uma Reação** (em resposta a eventos específicos, se disponível)

**Observação:**
Na fase atual, **não há movimentação tática** durante o combate. O jogador apenas escolhe sua ação principal no turno.

---

### 🧭 Ordem de Resolução dos Turnos

1. O personagem com **maior valor de Iniciativa** age primeiro.
2. Em caso de empate, age o personagem com **maior Astúcia**.
3. Persistindo o empate, resolve-se no **dado (1D20)**.

Após o último personagem agir, **inicia-se uma nova rodada**.

---

### 🛡️ Ações em Combate

As ações possíveis em cada turno serão detalhadas no próximo bloco, mas resumidamente incluem:

| Tipo de Ação | Exemplos |
|:---|:---|
| Ataque | Golpear um inimigo com arma física ou habilidade |
| Magia | Lançar uma magia ofensiva, defensiva ou suporte |
| Item | Usar poções, artefatos, kits de primeiros socorros |
| Defesa | Preparar uma postura defensiva para reduzir dano |
| Ação Especial | Ajudar um aliado, provocar inimigo, preparar uma reação |

---

### 📜 Exemplo de Turno

**Jogador A – Arqueiro Selvagem:**
- Realiza ataque à distância contra inimigo (ação principal).

**Jogador B – Xamã Curandeiro:**
- Lança magia de cura em aliado ferido (ação principal).

**Inimigo – Espírito Corrompido:**
- Usa habilidade de maldição contra o Jogador A (ação principal).

---

> ⚡ Lembre-se: Cada jogador sempre pode consultar suas opções de ação, habilidades ativas e itens disponíveis no início do seu turno.

---
## 🛡️ Ações em Combate

Durante o seu turno em combate em *Eras do Brasil*, cada personagem pode realizar **uma ação principal**.
As ações representam o que o personagem pode fazer para atacar, se defender, usar habilidades, itens ou executar táticas especiais.

Na versão atual do sistema (combate estático), o foco está em **escolher a ação**.
Na futura expansão (combate tático), será adicionado o **movimento estratégico**.

---

### 🎯 Tipos de Ações

| Tipo de Ação | Descrição |
|:---|:---|
| **Ataque** | Realizar um ataque físico ou mágico contra um inimigo. |
| **Uso de Habilidade** | Utilizar uma habilidade ativa da classe (ex: Provocação, Tiro Furtivo). |
| **Magia** | Lançar uma magia, caso o personagem possua magias disponíveis. |
| **Item** | Usar um item do inventário (poção, ferramenta, artefato). |
| **Defesa** | Adotar postura defensiva para reduzir dano recebido até o próximo turno. |
| **Ação Especial** | Realizar ações táticas como Ajudar, Provocar, Preparar Reação. |

---

### ⚔️ Ação: Ataque

**Descrição:**
Tenta atingir um inimigo utilizando uma arma física, natural ou mágica.

**Regras Gerais:**
- Role 1D20 + Modificador de Atributo relevante (Força Bruta para ataques físicos, Conhecimento ou Sabedoria Ancestral para mágicos).
- Compare com a Defesa do alvo.
- Se a rolagem for **igual ou superior** à Defesa, o ataque acerta.
- Então, role o dano da arma ou habilidade.

> 💬 Observação: Em futuras versões com grid, ataques poderão exigir verificações de alcance.

---

### ✨ Ação: Uso de Habilidade

**Descrição:**
Ativa uma habilidade da classe atual (ex: habilidades ativas iniciais).

**Regras Gerais:**
- Cada habilidade define se exige teste, ataque ou apenas efeito automático.
- Algumas habilidades possuem **recarga** de turnos antes de serem reutilizadas.
- As habilidades herdadas de outras classes podem ser usadas se forem do tipo "ativa".

---

### 🔮 Ação: Magia

**Descrição:**
Conjura uma magia disponível para o personagem.

**Regras Gerais:**
- Segue as regras específicas de Magia descritas no Capítulo 7 (Magia e Espiritualidade).
- Pode exigir:
  - Teste de ataque mágico (1D20 + Conhecimento/Sabedoria)
  - Resistência do alvo
- Algumas magias afetam área, múltiplos alvos ou possuem efeitos contínuos.

---

### 🧪 Ação: Uso de Item

**Descrição:**
Utiliza um item do inventário, como:

- Poções de cura
- Artefatos mágicos
- Bombas ou armadilhas
- Kits de primeiros socorros

**Regras Gerais:**
- Gastar um item normalmente consome a ação principal.
- Algumas classes ou habilidades podem permitir usar itens como ação bônus futuramente.

---

### 🛡️ Ação: Defesa

**Descrição:**
Adota uma postura defensiva para reduzir dano até o próximo turno.

**Efeitos:**
- Recebe **+2 de Defesa** até o início do seu próximo turno.
- Pode anular efeitos de derrubada ou empurrão simples durante esse período (a critério do mestre).

**Regras Gerais:**
- Não pode atacar ou lançar magias no mesmo turno em que adota Defesa.

---

### 🎯 Ação Especial

**Descrição:**
Permite ao personagem realizar táticas não convencionais.

Exemplos:

- **Ajudar:** Dar vantagem no próximo teste de aliado adjacente.
- **Provocar:** Tentar forçar um inimigo a focar seus ataques.
- **Preparar Reação:** Definir uma resposta a um gatilho ("Se o inimigo chegar perto, atacar com espada").

**Regras Gerais:**
- A descrição do efeito deve ser aprovada pelo mestre.
- Algumas Ações Especiais podem exigir testes sociais (Presença) ou de resistência (Vigor, Astúcia).

---

## 📜 Resumo Visual – Ações por Turno

| Etapa do Turno | Opções |
|:---|:---|
| **Ação Principal** | Ataque, Habilidade, Magia, Uso de Item, Defesa, Ação Especial |
| **Reação (se disponível)** | Reagir a gatilhos específicos no turno do inimigo |

---

> ⚡ **Importante:** Em futuras atualizações (Combate Avançado com Grid), ações de **movimentação** serão adicionadas, mas não alteram as ações principais descritas acima.

---
## 🎯 Tipos de Testes em Combate

Em *Eras do Brasil*, quase todas as ações em combate exigem algum tipo de **teste** para determinar sucesso ou fracasso.
Os testes garantem que o combate seja dinâmico, baseado em atributos e no elemento de risco.

---

### ⚔️ Testes de Ataque

**Descrição:**
São realizados para determinar se um ataque (físico ou mágico) acerta o alvo.

**Procedimento:**
1. Role **1D20**.
2. Adicione o **Modificador de Atributo** apropriado:
   - Ataque físico: **Força Bruta** ou **Astúcia** (caso de armas à distância).
   - Ataque mágico: **Conhecimento** ou **Sabedoria Ancestral**.
3. Compare o resultado com a **Defesa do alvo**.

- **Se for igual ou superior**, o ataque acerta e o dano é aplicado.
- **Se for inferior**, o ataque erra.

> 💬 Observação: Algumas habilidades ou magias podem conceder bônus ou penalidades nas rolagens de ataque.

---

### 🛡️ Testes de Resistência

**Descrição:**
Usados para resistir a efeitos como veneno, medo, magia, quedas, entre outros.

**Procedimento:**
1. Role **1D20**.
2. Adicione o **Modificador de Atributo** indicado pelo efeito:
   - Resistir venenos: **Vigor**
   - Resistir manipulação mental: **Presença**
   - Resistir maldições ou magias: **Sabedoria Ancestral** ou **Conhecimento**

3. Compare com a **Classe de Dificuldade (CD)** definida pela fonte do efeito.

- **Se o resultado for igual ou superior à CD**, o personagem resiste total ou parcialmente (depende da descrição da habilidade).
- **Se for inferior**, sofre o efeito normalmente.

---

### 📊 Testes de Atributo Diretos

**Descrição:**
Em alguns casos, o mestre pode exigir testes diretos no meio do combate.

Exemplos:

- Saltar sobre um obstáculo: **Astúcia**
- Empurrar ou derrubar um oponente: **Força Bruta**
- Manter concentração ao conjurar magia: **Conhecimento**

**Procedimento:**
- Role **1D20 + Modificador de Atributo**.
- Compare com a **CD estabelecida** pelo mestre.

---

### 🧠 Classe de Dificuldade (CD)

**Definição:**
É o número-alvo que deve ser igualado ou superado para que um teste seja bem-sucedido.

**Padrões de CD sugeridos:**

| Grau de Dificuldade | Valor de CD | Exemplo |
|:---|:---|:---|
| Muito fácil | 5 | Pisar sobre um tronco sem cair |
| Fácil | 10 | Saltar uma pequena fenda |
| Moderado | 13 | Resistir a um feitiço comum |
| Difícil | 16 | Quebrar grilhões de ferro pesado |
| Muito difícil | 18 | Resistir a uma magia de grande poder |
| Quase impossível | 20+ | Evitar a ruptura de um ritual ancestral |

> ⚡ O mestre pode ajustar a CD conforme o contexto, condições do ambiente e situação narrativa.

---

### 🎯 Ataques Múltiplos e Testes em Área

Algumas magias ou habilidades podem afetar vários alvos ao mesmo tempo.

- Cada alvo realiza **testes individuais** para resistir (ou o atacante realiza rolagens separadas de ataque).
- Em magias de área, às vezes o dano é reduzido à metade caso o alvo passe no teste de resistência.

---

### 📜 Resumo Visual – Tipos de Testes

| Situação | Teste | Atributo Envolvido |
|:---|:---|:---|
| Ataque com arma física | Ataque | Força Bruta ou Astúcia |
| Ataque com magia | Ataque | Conhecimento ou Sabedoria Ancestral |
| Resistir a veneno, doenças | Resistência | Vigor |
| Resistir a magia mental | Resistência | Presença ou Conhecimento |
| Manter concentração | Teste de Atributo | Conhecimento |
| Saltar, esquivar, fugir | Teste de Atributo | Astúcia |

---

> ✍️ *Importante:* Mesmo em combates mais abstratos (1ª fase digital e mesa), manter a rolagem de testes torna o combate imprevisível, estratégico e emocionante.

---
## ⚡ Iniciativa e Ordem de Ação

A Iniciativa determina a ordem em que personagens e inimigos agem durante o combate.
Essa ordem se mantém fixa para toda a duração do combate, salvo efeitos que alterem a posição (como habilidades específicas).

---

### 🎲 Como Determinar a Iniciativa

**Procedimento:**

1. Cada participante (jogador ou inimigo) rola **1D20**.
2. Adiciona o **Modificador de Astúcia**.

> Fórmula:
> **Iniciativa = 1D20 + Modificador de Astúcia**

---

### 🥇 Ordem de Ação

- Quem obtiver o **maior valor total** na rolagem de Iniciativa age primeiro.
- A sequência segue em **ordem decrescente** dos valores.

---

### 🔄 Empates de Iniciativa

Se dois ou mais personagens obtiverem o mesmo resultado final:

**Desempate 1:**
- Aquele com **maior Astúcia bruta** (valor do atributo, não o modificador) age primeiro.

**Desempate 2:**
- Se persistir o empate, cada envolvido realiza uma nova rolagem de **1D20**.
  Quem tirar o maior valor ganha prioridade.

> 🔥 Observação: O desempate pode ser usado narrativamente para cenas simultâneas dramáticas, se o mestre desejar.

---

### 🎯 Mudanças de Iniciativa Durante o Combate

Em regra, a Iniciativa **não muda** após ser definida no início do combate.

**Exceções possíveis (quando regras futuras forem ativadas):**
- Habilidades ou magias específicas que alterem a ordem.
- Efeitos de emboscadas ou ações especiais preparadas.

> 🧪 Para a primeira fase de mesa e protótipo digital, **não haverá efeitos que mudam a iniciativa no meio do combate**.

---

### 📜 Exemplo de Iniciativa

#### Situação:
- Jogador A (Astúcia 3)
- Jogador B (Astúcia 5)
- Inimigo X (Astúcia 4)

#### Rolagens:
- Jogador A rola 1D20 = 12 → Total = 12 + 0 (modificador Astúcia 3) = 12
- Jogador B rola 1D20 = 8 → Total = 8 + 2 (modificador Astúcia 5) = 10
- Inimigo X rola 1D20 = 14 → Total = 14 + 1 (modificador Astúcia 4) = 15

#### Ordem Final:
1. Inimigo X
2. Jogador A
3. Jogador B

---

> ✍️ *Importante:* Iniciativa é apenas ordem de ação — não determina automaticamente sucesso ou falha nas ações realizadas durante o turno!

---
## 🎲 Rolagens Críticas e Falhas Críticas

Durante o combate, alguns resultados naturais no dado (sem considerar modificadores) têm efeitos especiais automáticos.
Esses são chamados de **Rolagens Críticas** (20 natural) e **Falhas Críticas** (1 natural).

---

### 🎯 Rolagem Crítica (20 Natural)

Quando um jogador ou inimigo **rola 20 natural em 1D20**:

- A ação ofensiva **acerta automaticamente**, mesmo que o valor final fosse inferior à Defesa ou CD do alvo.
- O **dano é maximizado**: ao invés de rolar o dado de dano, considera-se o valor máximo possível.
- Efeitos secundários da habilidade ou ataque (como status ou efeitos adicionais) têm **sucesso automático**.

#### Exemplo:
- Arco com dano 1D6 → Dano crítico: **6**
- Maça com dano 1D6 → Dano crítico: **6**

> 🎯 *Nota:* Em versões futuras com múltiplos dados (ex: 2D6), todos os dados seriam considerados no máximo.

---

### ⚡ Efeitos Adicionais de Críticos

- Algumas habilidades ou magias poderão ter **efeitos especiais adicionais** ao acertar com 20 natural (ex: derrubar, empurrar, cegar).
- Esses efeitos serão descritos individualmente em cada habilidade.

> 🔥 *Importante:* No sistema base de mesa e 1ª etapa digital, **não há multiplicação de dano** — apenas maximização do dano dos dados.

---

### 🚫 Falha Crítica (1 Natural)

Quando um jogador ou inimigo **rola 1 natural em 1D20**:

- A ação automaticamente **falha**, mesmo que o valor total após modificadores fosse suficiente para atingir η Defesa ou CD.
- O jogador fica **vulnerável** até o início do seu próximo turno:
  - O próximo ataque contra ele tem **+2** no teste de acerto.

#### Exemplo:
- Jogador tenta atacar, tira 1 no dado → Falha automática → Sofre vulnerabilidade.

---

### 📚 Opções Narrativas para Falhas Críticas

O mestre (ou o sistema digital futuramente) pode, a critério da narrativa, aplicar efeitos adicionais leves à falha crítica, como:

- Derrubar a arma no chão (ação de gastar movimento para recuperar).
- Perder equilíbrio (impor desvantagem no próximo teste).
- Expor fraquezas para o inimigo (fornecer bônus narrativo para adversário).

> ✍️ *Essas consequências extras devem ser aplicadas com parcimônia* para não punir excessivamente a aleatoriedade natural dos dados.

---

### 🧪 Resumo Rápido

| Resultado | Efeito |
|:---|:---|
| 20 natural | Acerto automático + Dano máximo + Sucesso em efeitos especiais |
| 1 natural  | Falha automática + Vulnerável (+2 para quem atacar até próximo turno) |

---
## 🗡️ Tipos de Dano

Todo ataque, habilidade ou efeito que causa dano possui um **tipo de dano** associado. O tipo de dano determina como a defesa e a resistência do alvo interagem com o ataque.

| Tipo de Dano | Descrição | Resistência |
|:---|:---|:---|
| **Corte** | Lâminas, garras, objetos cortantes | Defesa Base (armadura) |
| **Perfurante** | Flechas, lanças, mordidas, projéteis | Defesa Base (armadura) |
| **Contundente** | Clavas, socos, quedas, impacto | Defesa Base (armadura) |
| **Espiritual** | Ataques sobrenaturais, maldições diretas, toque de espíritos | Teste de Resistência: **Sabedoria Ancestral** |
| **Elemental** | Fogo, gelo, raio, ácido | Teste de Resistência: varia conforme o elemento |
| **Veneno** | Toxinas, peçonhas, gases nocivos | Teste de Resistência: **Vigor** |

> ⚠️ **Dano Espiritual** ignora armadura física. A única defesa contra ele é a **Sabedoria Ancestral** do alvo em um teste de resistência. Criaturas espirituais (como o Espírito Menor) causam exclusivamente dano Espiritual.

---
## 🛡️ Defesa, Esquiva e Resistência

Além de atacar, os personagens em *Eras do Brasil* precisam se proteger de ataques físicos, mágicos ou efeitos adversos.
O sistema de defesa, esquiva e resistência define como calcular as defesas básicas e como resolver testes contra ataques ou magias.

---

### 🛡️ Defesa Base

A **Defesa Base** de cada personagem determina o número que os inimigos precisam superar para acertar um ataque físico.

#### Cálculo da Defesa Base

**Defesa Base = 10 + Modificador de Astúcia + Bônus de Armadura (se houver)**

| Situação | Ajuste |
|:---|:---|
| Sem armadura | 10 + Mod. Astúcia |
| Com armadura | 10 + Mod. Astúcia + Bônus de Armadura |

> 🔔 *A Defesa representa a capacidade de esquiva, bloqueio parcial e proteção passiva*.

#### Exemplo:
- Personagem com Astúcia 4 (+1) e sem armadura:
  - Defesa Base = 10 + 1 = **11**
- Personagem com Astúcia 4 (+1) e armadura leve (+1):
  - Defesa Base = 10 + 1 + 1 = **12**

---

### 🏃 Esquiva (Teste de Astúcia)

Em algumas situações, esquivar-se é ativo e requer um teste.

**Esquiva Ativa = 1D20 + Modificador de Astúcia**

Usada em casos como:

- Evitar armadilhas
- Desviar de magias de área
- Fugir de um ataque de oportunidade

O Mestre define a **CD (Classe de Dificuldade)** necessária para a esquiva.

> 🎯 *Em combate corpo a corpo normal, a esquiva está abstraída na Defesa Base. Só em efeitos específicos é necessário teste ativo*.

---

### 🧪 Testes de Resistência

Quando um personagem é alvo de magias, efeitos espirituais ou condições debilitantes, ele pode precisar realizar um **Teste de Resistência**.

#### Tipos de Teste de Resistência

| Tipo de Resistência | Atributo Utilizado | Exemplos |
|:---|:---|:---|
| Física | Vigor | Resistir a venenos, doenças, fadiga |
| Mental | Presença | Resistir a medo, manipulação, controle mental |
| Espiritual | Sabedoria Ancestral | Resistir a maldições, visões, efeitos sobrenaturais |
| Reflexos | Astúcia | Esquivar de explosões, feitiços de área |

#### Estrutura do Teste

**Teste de Resistência = 1D20 + Modificador do Atributo**

Deve superar a **CD** definida pela habilidade ou ataque.

---

#### 📜 Exemplo de Resistência

- Um xamã inimigo lança uma maldição com CD 14.
- O jogador precisa fazer um **Teste de Resistência Espiritual**:
  - 1D20 + Modificador de Sabedoria Ancestral.
- Se superar 14, resiste.
- Se falhar, sofre o efeito da maldição.

---

### ⚡ Efeitos de Equipamentos e Bônus

Alguns equipamentos, habilidades ou magias concedem:

- **Bônus fixos** à Defesa Base.
- **Vantagem** em Testes de Resistência (rolar dois dados e escolher o maior).
- **Resistência Parcial** (reduz dano de uma fonte específica).

Esses bônus serão descritos individualmente nos equipamentos ou nas habilidades correspondentes.

---

### 📚 Resumo Rápido

| Conceito | Resumo |
|:---|:---|
| Defesa Base | 10 + Mod. Astúcia + bônus de armadura (se houver) |
| Esquiva | 1D20 + Mod. Astúcia contra CD em efeitos especiais |
| Teste de Resistência | 1D20 + Modificador apropriado (Vigor, Presença, etc.) |

---
## ⚠️ Condições de Status

Durante o combate e a exploração, personagens e inimigos podem sofrer **condições de status** — estados temporários que alteram suas capacidades físicas, mentais ou espirituais.

As condições são aplicadas por habilidades, magias, armadilhas ou efeitos ambientais, e podem impactar rolagens de dados, movimento, ações disponíveis e defesas.

---

### 🩸 Lista de Condições Comuns

#### 🐍 Envenenado
- **Efeito:** Sofre dano contínuo no final de cada turno.
- **Rolagem:** Teste de Resistência Física (Vigor) para se recuperar ao final do turno.
- **Notas:** Veneno pode variar em potência conforme a fonte.

---

#### 🌪️ Derrubado
- **Efeito:** O personagem fica no chão.
- **Consequências:**
  - Ataques contra o personagem têm vantagem corpo a corpo.
  - Ataques à distância têm desvantagem.
  - Para se levantar: Gasta a Ação Principal no turno.

---

#### 😵 Atordoado
- **Efeito:** Perde η Ação Principal no turno.
- **Rolagem:** Teste de Resistência Física ou Mental (varia pela origem do efeito).
- **Notas:** Durante o atordoamento, o personagem é considerado incapaz de se defender ativamente.

---

#### 😱 Assustado
- **Efeito:** Não pode se aproximar da fonte do medo.
- **Consequências:**
  - Desvantagem em testes de ataque e resistência enquanto puder ver a fonte.
  - Se já estiver a uma distância segura, pode agir normalmente.
- **Rolagem:** Teste de Resistência Mental (Presença) no final do turno.

---

#### 🔥 Queimando
- **Efeito:** Sofre dano de fogo ao início de cada turno.
- **Notas:**
  - Pode tentar apagar as chamas gastando a Ação Principal em um teste de Vigor CD 10.
  - Água, rolar no chão ou magia de água podem ajudar.

---

#### ❄️ Congelado
- **Efeito:** Imobilizado e sofre penalidades de ação.
- **Consequências:**
  - Perde o movimento.
  - Ações físicas têm desvantagem.
- **Notas:** A resistência à condição pode depender de armadura ou bônus elementais.

---

#### 🌫️ Cego
- **Efeito:** Não enxerga seu entorno.
- **Consequências:**
  - Desvantagem em ataques.
  - Ataques contra o personagem têm vantagem.
  - Testes de Percepção baseados em visão falham automaticamente.

---

#### 🧠 Confuso
- **Efeito:** Ações imprevisíveis.
- **Consequências:**
  - No início do turno, role 1D4:
    - 1-2: Faz ataque aleatório contra o alvo mais próximo.
    - 3: Fica paralisado (não age).
    - 4: Age normalmente.
- **Notas:** Teste de Resistência Mental (Presença) para tentar se recuperar ao final do turno.

---

### 🔄 Duração das Condições

- A maioria das condições dura até:
  - **Fim do turno** do personagem (teste de recuperação automático).
  - **X turnos** definidos pelo efeito/magia.
  - **Fim do combate**, se não for recuperada.

- Algumas condições podem ser removidas por:
  - Magias de cura ou bênçãos.
  - Sucesso em testes de resistência.
  - Uso de itens ou ações específicas.

---

### 🛡️ Resistências e Imunidades

Algumas classes, habilidades e equipamentos podem:

- Reduzir a duração das condições.
- Conceder **vantagem** em testes de resistência contra condições específicas.
- Tornar o personagem **imune** a certos efeitos (ex.: imune a medo ou veneno).

Esses bônus serão indicados nas descrições das habilidades, classes ou itens correspondentes.

---

### 📚 Resumo Rápido

| Condição | Efeito Principal |
|:---|:---|
| Envenenado | Dano contínuo |
| Derrubado | Penalidade defensiva e dificuldade para agir |
| Atordoado | Perda da Ação Principal |
| Assustado | Fuga ou desvantagem contra fonte do medo |
| Queimando | Dano de fogo por turno |
| Congelado | Imobilização e penalidades físicas |
| Cego | Ataques e percepção prejudicados |
| Confuso | Ações aleatórias e instabilidade |

---

## 🎭 Magia e Uso de Habilidades

Em *Eras do Brasil*, o uso de **magias** e **habilidades** é fundamental para personalizar o estilo de combate, reforçar estratégias e interagir de formas únicas com o ambiente.

Tanto magias quanto habilidades seguem **regras gerais** para sua utilização durante o combate.

---

### ✨ Diferença entre Magias e Habilidades

| Tipo           | Origem                                           | Exemplos                                | Notas                                     |
|----------------|--------------------------------------------------|-----------------------------------------|-------------------------------------------|
| **Habilidades**| Definidas pela classe ativa                      | Provocação Tática, Investida Tribal     | Usadas em combate ou exploração. Ativas ou passivas. |
| **Magias** | Definidas por classe mágica, habilidades espirituais ou equipamentos | Bênção Curativa, Maldição Ancestral, Encantamento de Arma | Requerem conjuração. Podem ser ofensivas, defensivas ou utilitárias. |

---

### 🧙‍♂️ Como Usar Habilidades e Magias

Durante o turno, ao invés de um ataque básico ou ação comum, o personagem pode optar por usar:

- Uma **Habilidade Ativa** (ex.: Investida Tribal, Proteção Ancestral)
- Uma **Magia** (ex.: Rajada de Chamas, Bênção de Vitalidade)

#### Regras Gerais

- Utilizar uma habilidade ou magia **consome a Ação Principal** do turno.
- Algumas habilidades podem ser usadas como **Reação** se indicado na descrição.
- Magias e habilidades **não consomem movimento** (caso haja movimentação no futuro).

---

### 📜 Testes e Resistências

Algumas habilidades e magias exigem que o alvo realize **Testes de Resistência** para evitar ou reduzir seus efeitos.

**Formato padrão:**

> **CD (Classe de Dificuldade) = 10 + Modificador de Atributo Base da Magia/Habilidade**

**Exemplo:**
Um Xamã Curandeiro usando uma magia espiritual terá a CD baseada em **Sabedoria Ancestral**.

---

#### Atributo Base de Magias

| Tipo de Magia         | Atributo Base         |
|------------------------|------------------------|
| Espiritual, Ritualística | Sabedoria Ancestral |
| Elemental, Técnica       | Conhecimento         |
| Ilusória, Mental         | Presença              |

---

### 🔋 Limitações e Recarga

- Habilidades possuem **tempo de recarga** após o uso (indicado na descrição: 1 turno, 2 turnos, etc.).
- Algumas magias poderão futuramente consumir **"Cargas Espirituais"** ou aplicar **"Fadiga"** (em desenvolvimento no Livro de Magias).
- Entre combates, todas as recargas são **reiniciadas**.

---

### 🔥 Alcance de Magias e Habilidades

Na fase atual (combate sem grid):

- Alcances são **descritivos** (ex.: "até 3 metros", "todos em alcance médio").
- Não é necessário medir grids ou quadrados — apenas seguir a descrição narrativa.

No futuro (com sistema tático ativado):

- Distâncias serão medidas em **blocos** ou **grids** (ex.: "alcance de 6 quadrados").

---

### 🛡️ Regras de Concentração (Planejado para Futuro)

- Algumas magias de longa duração exigirão **Concentração**.
- Enquanto concentrado:
  - O personagem **não pode** lançar novas magias que exijam concentração.
  - Se for **atordoado, derrubado ou sofrer dano**, poderá ser exigido um **teste de resistência** para manter a concentração.

Essas regras serão implementadas junto com o **Livro de Magias**.

---

### 📚 Resumo Rápido

| Ação                     | Efeito                                                 |
|---------------------------|--------------------------------------------------------|
| Usar Habilidade Ativa     | Consome Ação Principal                                 |
| Usar Magia                | Consome Ação Principal                                 |
| Recarga                   | Respeitar tempo indicado antes de reutilizar           |
| Teste de Resistência      | Necessário para muitas magias e habilidades de controle |
| Alcance                   | Narrativo atualmente; por grid no futuro               |

---

## 🎲 Exemplo Completo de Turno

Para ilustrar todo o funcionamento do sistema de combate em *Eras do Brasil*, vamos acompanhar um exemplo prático, simulando uma rodada de combate completa entre personagens e um inimigo.

---

### 📜 Cenário

- **Local:** Clareira em uma floresta densa.
- **Participantes:**
  - Jogador 1: **Conquistador** (Tank)
  - Jogador 2: **Xamã Curandeiro** (Healer)
  - Jogador 3: **Arqueiro Selvagem** (DPS à distância)
  - Inimigo: **Espírito Corrompido** (Criatura Mágica Hostil)

---

### 🎯 Fase 1: Determinar Iniciativa

Cada participante rola **1D20 + Modificador de Astúcia**.

| Personagem           | Rolagem | Modificador de Astúcia | Iniciativa Final |
|----------------------|---------|------------------------|------------------|
| Conquistador         | 12      | +0                     | 12               |
| Xamã Curandeiro       | 16      | +1                     | 17               |
| Arqueiro Selvagem     | 15      | +2                     | 17               |
| Espírito Corrompido   | 14      | +1                     | 15               |

**Ordem de Turnos:**
1. Xamã Curandeiro (Desempate: maior Astúcia)
2. Arqueiro Selvagem
3. Espírito Corrompido
4. Conquistador

---

### 🛡️ Fase 2: Execução dos Turnos

#### 🧙‍♂️ Turno 1 – Xamã Curandeiro

- **Ação:** Usa **Bênção Curativa** no Conquistador, preparando-o para o combate.
- **Descrição:** O Xamã invoca uma energia espiritual, curando levemente feridas antigas do aliado.
- **Recarga:** 2 turnos (não poderá usar novamente imediatamente).

---

#### 🏹 Turno 2 – Arqueiro Selvagem

- **Ação:** Atira uma flecha usando a habilidade ativa **Tiro Furtivo**.
- **Alvo:** Espírito Corrompido.
- **Teste:** Rola 1D20 + Modificador de Astúcia + Bônus de Ataque.
- **Resultado:** Acerta!
- **Dano:** 1D6 (arma) + 2 (bônus do Tiro Furtivo).

---

#### 👻 Turno 3 – Espírito Corrompido

- **Ação:** Usa **Maldição de Fraqueza** contra o Conquistador.
- **Teste:** O Conquistador faz um **Teste de Resistência** baseado em Vigor.
- **Resultado:** Falha! O Conquistador sofre -1 de dano em seus próximos ataques físicos por 2 turnos.

---

#### 🛡️ Turno 4 – Conquistador

- **Ação:** Usa **Provocação Tática**.
- **Efeito:** Força o Espírito Corrompido a focar ataques apenas nele no próximo turno (teste de Sabedoria do inimigo).
- **Resultado:** O Espírito falha no teste — ele será obrigado a atacar o Conquistador.

---

### 🔄 Fase 3: Atualizar Estado do Combate

- O Xamã está com **Bênção Curativa** em recarga (1 turno restante).
- O Conquistador está **enfraquecido** (devido à maldição).
- O Espírito Corrompido está **provocado** (obrigado a focar ataques no tank).

---

### 🛡️ Fase 4: Nova Rodada

A ordem de turnos permanece a mesma, e uma nova rodada se inicia.

---

### 📚 Aprendizados do Exemplo

- O **turno** é baseado em ações táticas claras e organizadas.
- As **habilidades** possuem tempos de recarga que precisam ser gerenciados.
- **Efeitos e condições** alteram a estratégia de combate e obrigam adaptações.
- Mesmo sem movimentação em grid, o **controle tático** permanece forte graças às habilidades, testes e efeitos.

---

> 🎯 Este exemplo é ideal para tutoriais iniciais em campanhas de mesa ou digital, ajudando jogadores e mestres a compreenderem rapidamente o fluxo de combate!

---
## 🛠️ Regras Especiais Futuras (Expansão Modular)

*Eras do Brasil* foi projetado para crescer em complexidade conforme o jogo evolui — tanto nas campanhas de mesa quanto nas versões digitais futuras.

Por isso, o sistema reserva este espaço para a inclusão de **módulos avançados**, que poderão ser ativados conforme a campanha, o mestre ou o sistema digital desejar.

---

### 🔮 Módulo Tático com Grid (Segunda Etapa Digital)

Este módulo substituirá o posicionamento abstrato por movimentação física em **blocos ou grids**, no estilo de jogos como *Solasta*, *Wartales* ou *Pathfinder*.

Inclui:

- **Movimentação por Distância (em blocos ou metros)**
- **Alcance real de magias e ataques**
- **Ataques de Oportunidade**
- **Controle de terreno, zonas de perigo e bloqueios**
- **Cobertura parcial ou total**

> 💡 Este módulo será opcional no RPG de mesa e ativado por padrão na segunda fase digital.

---

### 🌪️ Magias com Área e Direção

Algumas magias ou habilidades futuras afetarão **áreas em cone, linha, círculo ou raio**. Essas regras serão descritas no **Livro de Magias** com indicações visuais, medidas e efeitos adicionais.

---

### 💥 Duelos e Combate 1x1

Regra opcional para situações de duelo individual:

- Ações simultâneas ou semi-simultâneas.
- Resolução por prioridade de iniciativa + astúcia.
- Eventos narrativos de tensão e honra.

---

### 🧩 Modo Narrativo com Rolagens Condensadas

Para grupos que desejam combates mais rápidos e narrativos:

- Um único teste para definir o sucesso ou fracasso de uma cena de combate inteira.
- Utiliza o modificador de atributo relevante + uma descrição criativa.
- Ideal para campanhas com foco em história, exploração e desenvolvimento de personagens.

---

### 📌 Expansões Planejadas

| Nome do Módulo | Aplicação | Status |
|----------------|-----------|--------|
| Combate com Grid | Segunda Etapa Digital | Planejado |
| Reação por Alcance | RPG de Mesa e Digital | Em discussão |
| Inimigos com IA Estratégica | Versão Digital Persistente | Em design |
| Combate por Zona de Impacto | Ambientes mágicos ou espirituais | Em concepção |

---

> ✅ Estas regras não impactam o núcleo do jogo atual, mas serão incorporadas de forma modular e transparente sempre que forem ativadas.

---

---

## ⚖️ Dinâmica de Escala e Sincronia Temporal

### Escala de Dificuldade (Solo vs. Cooperativo)
* **Jogador Solo:** Inimigos têm **PV Padrão (100%)**.
* **Modo Cooperativo:** Inimigos recebem **+75% de PV**. O dano não aumenta para evitar hit-kill.

### ⏳ Sincronia Temporal (Sistema de Fila)
O jogo utiliza um sistema de **Processamento Assíncrono de Ações**:
1. **Custo da Ação:** Toda ação (viajar, craftar, lutar) tem um custo em tempo real (segundos/minutos).
2. **O Estado de "Ocupado":** Ao realizar uma ação longa (ex: viagem de ~10 minutos), o jogador entra em estado "Ocupado" e aguarda.
3. **Resolução:** O jogo libera o outro jogador para agir livremente até que ele também gaste tempo equivalente (ou entre em estado Ocupado).
4. **O Combate:** Cada rodada de combate consome tempo equivalente a uma ação simples.
    * *Exemplo:* O Jogador A viaja (~10 min). O Jogador B entra em combate. O Jogador B joga 10 rodadas de combate enquanto o Jogador A viaja. Ao final, ambos estão livres novamente.