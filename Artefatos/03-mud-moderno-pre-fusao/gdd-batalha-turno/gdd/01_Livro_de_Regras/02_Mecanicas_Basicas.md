# 📘 Capítulo 2 – Mecânicas Básicas

Este capítulo apresenta o sistema central de resolução de ações de _Eras do Brasil_, incluindo testes de atributos, dificuldade (CD), uso de proficiências, e o conceito de rolagens parciais, falhas e acertos críticos.

---

## 🎲 2.1 – Testes de Atributo

Todas as ações que exigem uma chance de sucesso são resolvidas com uma rolagem de **1D20 + modificadores**.

**Fórmula básica:**

`1D20 + Modificador de Atributo + Bônus de Proficiência (se aplicável)`

### Exemplos de uso:

- Atacar um inimigo
- Resistir a uma doença
- Saltar um obstáculo
- Criar ou refinar um item
- Convencer um NPC
- Identificar um ingrediente mágico

---

## 🧩 2.2 – Modificadores de Atributo

Cada atributo possui um valor de 1 a 6, que gera um **modificador** somado nas rolagens.

| Valor | Modificador |
|-------|-------------|
| 1     | –2          |
| 2     | –1          |
| 3     | +0          |
| 4     | +1          |
| 5     | +2          |
| 6     | +3          |


---

## 🧪 2.3 – CD e Níveis de Dificuldade

A **Classe de Dificuldade (CD)** representa o número que a rolagem deve igualar ou superar para ter sucesso.

| Nível de Dificuldade | CD sugerida | Exemplo                                                 |
|----------------------|-------------|----------------------------------------------------------|
| Muito fácil          | 5           | Lembrar um fato trivial                                 |
| Fácil                | 10          | Subir em uma árvore                                      |
| Moderada             | 13          | Rastrear pegadas na floresta                            |
| Difícil              | 16          | Negociar com um espírito desconfiado                    |
| Muito difícil        | 18          | Evadir uma armadilha oculta                             |
| Quase impossível     | 20+         | Saltar por uma ponte quebrada com armadura pesada       |


---

## 🎯 2.4 – Testes com Proficiência

Quando a ação envolve uma proficiência que o personagem possui, aplica-se o **bônus de proficiência**:

| Nível de Proficiência | Bônus |
|-----------------------|-------|
| Aprendiz              | +1    |
| Competente            | +2    |
| Especialista          | +3    |
| Mestre                | +4    |


> As proficiências de vida são descritas no Capítulo 3 e detalhadas no *Livro de Proficiências*.

---

## ⚖️ 2.5 – Tipos de Teste

### ✅ Teste Simples

Rolagem contra uma CD fixa definida pelo mestre. Sucesso se igualar ou superar.

### 🆚 Teste Oposto

Duas partes rolam 1D20 + modificadores. A maior vence.

| Exemplo                      | Atributo Envolvido       |
|-----------------------------|--------------------------|
| Disputa por um item         | Força Bruta vs Força Bruta |
| Fugir de uma perseguição    | Astúcia vs Astúcia        |


### 👥 Teste em Grupo

Quando todos tentam a mesma ação:

- O mestre pode pedir testes individuais
- Ou usar a **regra da maioria** (mais da metade obtém sucesso)
- Ou designar um líder com ajuda dos demais (vantagem)

---

## 🌀 2.6 – Rolagens Críticas

| Resultado no Dado | Tipo de Resultado | Efeito                                                   |
|-------------------|-------------------|-----------------------------------------------------------|
| 1 Natural          | Falha Crítica     | Erro grave com consequências narrativas negativas         |
| 20 Natural         | Sucesso Crítico   | Sucesso excepcional com efeitos adicionais positivos      |


> O mestre pode interpretar de forma narrativa os efeitos de falhas e acertos críticos.

---

## 🔄 2.7 – Sucesso Parcial (opcional)

O mestre pode permitir **sucesso parcial**, com custo, limitação ou consequência:

- Personagem convence o guarda, mas perde algo de valor.
- Escala a parede, mas derruba parte do inventário.
- A magia cura, mas atrai atenção indesejada.

> Essa regra é opcional, mas recomendada para campanhas com foco narrativo.

---

## 🛡️ 2.8 – Defesa e Resistência

### 🧬 Defesa Base

Todo personagem tem **Defesa Base** igual a:

`10 + Modificador de Astúcia + Bônus de Armadura (se houver)`

> A Defesa Base é usada para evitar ataques físicos simples. O Bônus de Armadura depende do equipamento utilizado (consulte o *Livro de Itens e Equipamentos*).

### 🧠 Testes de Resistência

Alguns efeitos exigem que o personagem **resista a uma condição** ou magia.

**Fórmula:**

`1D20 + Modificador de Atributo`

| Efeito                     | Atributo Usado           |
|---------------------------|--------------------------|
| Resistir a veneno         | Vigor                    |
| Resistir ao medo          | Presença                 |
| Resistir a maldição       | Sabedoria Ancestral      |
| Resistir a possessão      | Conhecimento ou Presença |


A **CD** é definida pelo efeito, magia ou criatura. Se a rolagem for menor, o personagem sofre o efeito.

---

## 2.9 – Tempo no Jogo

O tempo em *Eras do Brasil* é medido de formas diferentes conforme o contexto:

- **Turnos:** Usados exclusivamente em combate D20 (Iniciativa → Rodadas → Resolução).
- **Tempo Real:** Durations de habilidades, prazos de quests e eventos são medidos em segundos/minutos reais.
- **Relógio do Jogo:** O mundo possui um ciclo dia/noite com 4 períodos — **Manhã, Tarde, Noite, Madrugada**. 1 dia do jogo ≈ 2–4 horas reais. NPCs seguem rotinas baseadas nesses períodos.

### Equivalências Práticas

| Contexto | Unidade de Tempo | Exemplo |
|----------|-----------------|---------|
| Combate | Turnos | "Efeito dura 3 turnos" |
| Habilidade fora de combate | Tempo real | "Dura 5 minutos" |
| Rotinas de NPC | Período do dia | "O Ferreiro trabalha de Manhã a Tarde" |
| Prazo de quest | Tempo real ou dias do jogo | "Entregue em 2 horas reais" |
| Regeneração de recursos | Tempo do jogo | "Renasce a cada Manhã" |

> **Nota técnica:** Internamente, o servidor processa o mundo em ciclos ("ticks"), mas esse detalhe não é exposto ao jogador. Ver [Capítulo 8 — Mundo Vivo](08_Mundo_Vivo_e_NPCs.md) para detalhes de implementação.

---

## 📚 Considerações Finais

- Na versão digital, rolagens são automatizadas (com lógica de falha/sucesso/efeito).
- Habilidades, magias, condições e equipamentos podem alterar as regras aqui apresentadas.
- Para mais detalhes, consulte os livros complementares:

  - *Livro de Habilidades*
  - *Livro de Proficiências*
  - *Livro de Magias*
  - *Livro de Itens e Equipamentos*

---