# 📦 Livro de Itens e Equipamentos — Catálogo do Ato 1

> *"Cada objeto carrega uma história. A lança não é só madeira e pedra — é a memória do caçador, a sabedoria do ancião que a talhou, e a promessa de alimento para o clã."*
> — Provérbio Tupi-Guarani

Este livro é o **catálogo oficial de itens e equipamentos** de *Eras do Brasil*, servindo como referência para jogadores, mestres e para a engine do jogo. Aqui você encontrará a descrição completa da **Matriz 5×5** (Qualidade × Raridade), catálogo de itens do MVP focados no Ato 1, receitas de crafting, tabelas de preços e distribuição por localização.

---

## 📚 Índice

1. [Introdução — Como Usar Este Livro](#1-introdução--como-usar-este-livro)
2. [A Matriz 5×5 — Qualidade e Raridade](#2-a-matriz-5×5--qualidade-e-raridade)
3. [Catálogo de Itens por Categoria](#3-catálogo-de-itens-por-categoria)
   - [3.1 Armas Corpo a Corpo](#31-armas-corpo-a-corpo)
   - [3.2 Armas de Alcance](#32-armas-de-alcance)
   - [3.3 Armaduras e Proteções](#33-armaduras-e-proteções)
   - [3.4 Consumíveis](#34-consumíveis)
   - [3.5 Materiais de Crafting](#35-materiais-de-crafting)
   - [3.6 Itens Rituais e Culturais](#36-itens-rituais-e-culturais)
   - [3.7 Itens de Quest](#37-itens-de-quest)
4. [Receitas de Crafting](#4-receitas-de-crafting)
5. [Tabela de Preços e Comércio Regional](#5-tabela-de-preços-e-comércio-regional)
6. [Distribuição de Itens por Localização (Ato 1)](#6-distribuição-de-itens-por-localização-ato-1)

---

## 1. Introdução — Como Usar Este Livro

### 🎯 Propósito

Este livro foi criado para:

- **Jogadores:** Consultar itens disponíveis, entender mecânicas e planejar builds
- **Mestres:** Distribuir loot adequado, balancear economia e criar recompensas narrativas
- **Engine:** Servir como fonte de dados para instanciar itens no jogo digital

### 📖 Como Ler as Fichas de Item

Cada item neste livro segue um formato padronizado:

| Campo | Descrição |
|-------|-----------|
| **ID** | Identificador único no formato `ITM_XXX_YYY` |
| **Nome** | Nome temático brasileiro |
| **Tipo** | Categoria principal (Arma, Armadura, Consumível, etc.) |
| **Subtipo** | Categoria específica (Espada Longa, Armadura Leve, etc.) |
| **Matriz** | Qualidade + Raridade (ex: Média/Comum) |
| **Dano/Efeito** | Fórmula de dano ou efeito mecânico |
| **Propriedades** | Bônus especiais, restrições de uso |
| **Durabilidade** | Usos máximos antes de quebrar |
| **Valor (UC)** | Preço base em Unidades Comerciais |
| **Peso** | Unidades de peso para sistema de inventário |
| **Origem Narrativa** | De onde vem no mundo (bioma, cultura) |
| **Classes Recomendadas** | Quais classes se beneficiam mais |

### 🔗 Relação com Outros Sistemas

- **Crafting:** Ver [Cap. 6.3 — Criação de Itens](../01_Livro_de_Regras/06_Economia_Itens_e_Crafting.md#63--criação-de-itens-crafting)
- **Durabilidade:** Ver [Cap. 6.4 — Reparos e Manutenção](../01_Livro_de_Regras/06_Economia_Itens_e_Crafting.md#64--reparos-manutenção-e-durabilidade)
- **Comércio:** Ver [Cap. 6.5 — Economia Regional](../01_Livro_de_Regras/06_Economia_Itens_e_Crafting.md#65--comércio-e-economia-regional)
- **Proficiências:** Ver [Cap. 3.5 — Proficiências de Vida](../01_Livro_de_Regras/03_Criacao_de_Personagem.md)

---

## 2. A Matriz 5×5 — Qualidade e Raridade

### 🎨 Eixos da Matriz

Todos os itens em *Eras do Brasil* são classificados por dois eixos independentes:

**Qualidade:** Estado físico e técnico do item (durabilidade, acabamento, funcionalidade)
**Raridade:** Quão incomum, valioso ou místico é o item (disponibilidade, significado cultural)

### 📊 Tabela Completa da Matriz 5×5

| Qualidade / Raridade | ⚪ Comum | 🟤 Incomum | 🔷 Raro | 🟣 Épico | 🟡 Lendário |
|---------------------|---------|------------|--------|----------|--------------|
| **⚠️ Muito Baixa** | **Mod:** -1<br>**Dur:** 3-5 usos<br>**Valor:** 50%<br>**Ex:** Faca quebrada | **Mod:** -1<br>**Dur:** 3-5 usos<br>**Valor:** 75%<br>**Ex:** Ferramenta tribal improvisada | **Mod:** -1<br>**Dur:** 4-6 usos<br>**Valor:** 150%<br>**Ex:** Medalha rachada de herói | **Mod:** -1<br>**Dur:** 5-7 usos<br>**Valor:** 300%<br>**Ex:** Cajado corrompido | **Mod:** 0<br>**Dur:** 6-8 usos<br>**Valor:** 800%<br>**Ex:** Lâmina lendária partida |
| **🟠 Baixa** | **Mod:** -1<br>**Dur:** 6-8 usos<br>**Valor:** 75%<br>**Ex:** Espada mal forjada | **Mod:** 0<br>**Dur:** 6-8 usos<br>**Valor:** 125%<br>**Ex:** Poção turva | **Mod:** 0<br>**Dur:** 7-9 usos<br>**Valor:** 200%<br>**Ex:** Túnica surrada de ordem | **Mod:** 0<br>**Dur:** 8-10 usos<br>**Valor:** 400%<br>**Ex:** Tambor ritual danificado | **Mod:** +1<br>**Dur:** 10-12 usos<br>**Valor:** 1000%<br>**Ex:** Colar de alma fragmentada |
| **🟡 Média** | **Mod:** 0<br>**Dur:** 9-12 usos<br>**Valor:** 100%<br>**Ex:** Couraça de couro | **Mod:** 0<br>**Dur:** 10-13 usos<br>**Valor:** 150%<br>**Ex:** Poção de cura | **Mod:** +1<br>**Dur:** 11-14 usos<br>**Valor:** 250%<br>**Ex:** Amuleto espiritual | **Mod:** +1<br>**Dur:** 12-15 usos<br>**Valor:** 500%<br>**Ex:** Pederneira encantada | **Mod:** +2<br>**Dur:** 15-18 usos<br>**Valor:** 1500%<br>**Ex:** Diário de herói perdido |
| **🟢 Alta** | **Mod:** +1<br>**Dur:** 13-16 usos<br>**Valor:** 150%<br>**Ex:** Espada bem forjada | **Mod:** +1<br>**Dur:** 14-17 usos<br>**Valor:** 200%<br>**Ex:** Kit de ferramentas refinado | **Mod:** +2<br>**Dur:** 15-18 usos<br>**Valor:** 350%<br>**Ex:** Arco cerimonial | **Mod:** +2<br>**Dur:** 16-19 usos<br>**Valor:** 700%<br>**Ex:** Instrumento mágico | **Mod:** +3<br>**Dur:** 18-20 usos<br>**Valor:** 2000%<br>**Ex:** Máscara ancestral |
| **🔵 Excelente** | **Mod:** +2<br>**Dur:** 17-20 usos<br>**Valor:** 200%<br>**Ex:** Espada de mestre | **Mod:** +2<br>**Dur:** 18-20 usos<br>**Valor:** 300%<br>**Ex:** Elixir perfeito | **Mod:** +3<br>**Dur:** 19-22 usos<br>**Valor:** 500%<br>**Ex:** Relíquia de guerra | **Mod:** +3<br>**Dur:** 20-24 usos<br>**Valor:** 1000%<br>**Ex:** Cocar lendário | **Mod:** +4<br>**Dur:** 22-25+ usos<br>**Valor:** 3000%+<br>**Ex:** Orbe da Primeira Era |

### 📝 Legendas

- **Mod:** Modificador aplicado em testes usando o item
- **Dur:** Durabilidade base (número de usos)
- **Valor:** Multiplicador sobre o preço base
- **Ex:** Exemplo de item dessa combinação

### ✨ Efeitos Especiais por Raridade

Além dos modificadores numéricos, a raridade pode desbloquear efeitos narrativos:

| Raridade | Efeitos Narrativos Possíveis |
|----------|------------------------------|
| ⚪ **Comum** | Valor baixo, fácil substituição |
| 🟤 **Incomum** | Valorizado por certos NPCs, pode desbloquear diálogos |
| 🔷 **Raro** | Pode desbloquear recompensas ou acesso a áreas específicas |
| 🟣 **Épico** | Elemento narrativo, carrega história ou simbolismo, afeta reputação |
| 🟡 **Lendário** | Ativa eventos, legados ou magias ocultas, reconhecido por todas as facções |

---

## 3. Catálogo de Itens por Categoria

Esta seção apresenta os **15 itens principais do MVP**, focados no Ato 1 e com temática indígena/folclórica brasileira. Todos os itens foram balanceados para o nível 1-3 e consideram os 9 nós do mapa do Ato 1.

---

### 3.1 Armas Corpo a Corpo

#### 🪓 Tacape de Pedra Lascada

```
ID: ITM_ARM_001
Nome: Tacape de Pedra Lascada
Tipo: Arma
Subtipo: Clava
Matriz: Baixa / Comum
```

**Dano:** 1d4+1 Contundente  
**Propriedades:**
- Simples de usar, sem requisitos
- Pode ser arremessado (alcance: 6 metros, -1 ataque)

**Durabilidade:** 7 usos  
**Valor:** 8 UC  
**Peso:** 3 unidades  
**Origem Narrativa:** Arma básica dos povos originários, feita com madeira nativa e pedra lascada. Comum entre caçadores e guerreiros iniciantes.  
**Classes Recomendadas:** Guerreiro Tribal, Caçador de Feras  

**Descrição:** Um tacape robusto com cabeça de pedra amarrada com fibras de cipó. Eficaz contra animais e adversários levemente armados. A madeira é de pau-brasil jovem, ainda sem o peso das armas veteranas.

---

#### 🗡️ Lança de Madeira-Ferro

```
ID: ITM_ARM_002
Nome: Lança de Madeira-Ferro
Tipo: Arma
Subtipo: Lança
Matriz: Média / Incomum
```

**Dano:** 1d6+1 Perfurante  
**Propriedades:**
- Alcance: 2 metros (corpo a corpo estendido)
- Vantagem contra alvos Grandes (onças, jacarés)
- Pode ser usada com escudo

**Durabilidade:** 12 usos  
**Valor:** 35 UC  
**Peso:** 4 unidades  
**Origem Narrativa:** Forjada com madeira de aroeira e ponta endurecida no fogo. A madeira-ferro é uma das árvores mais densas da Mata Costeira, conferindo peso e durabilidade.  
**Classes Recomendadas:** Guerreiro Tribal, Explorador de Terras  

**Descrição:** Uma lança de 2 metros com haste de aroeira e ponta carbonizada ritualmente. Usada em caçadas e batalhas tribais. A ponta foi endurecida em fogueira sagrada durante três luas.

---

#### ⚔️ Machadinha de Obsidiana

```
ID: ITM_ARM_003
Nome: Machadinha de Obsidiana
Tipo: Arma
Subtipo: Machado
Matriz: Alta / Raro
```

**Dano:** 1d8 Cortante  
**Propriedades:**
- +2 em testes de Força ao quebrar objetos
- Crítico em 19-20 (afiada excepcionalmente)
- Pode ser usada como ferramenta (Carpintaria +1)

**Durabilidade:** 15 usos  
**Valor:** 120 UC  
**Peso:** 5 unidades  
**Origem Narrativa:** Lascada a partir de obsidiana vulcânica encontrada nas Ruínas Queimadas. Considerada sagrada por carregar "o fogo da terra".  
**Classes Recomendadas:** Guerreiro Tribal, Caçador de Feras  

**Descrição:** Machado com lâmina negra de obsidiana e cabo de jacarandá. A lâmina foi extraída de um sítio vulcânico antigo e polida por artesãos mestres. Reflete luz como vidro negro e corta com precisão mortal.

**Nota do Mestre:** Este item pode desbloquear diálogo especial com o Pajé de São Tomé, que reconhece a origem da pedra.

---

### 3.2 Armas de Alcance

#### 🏹 Arco Curto de Biriba

```
ID: ITM_ARM_004
Nome: Arco Curto de Biriba
Tipo: Arma
Subtipo: Arco
Matriz: Média / Comum
```

**Dano:** 1d6 Perfurante  
**Propriedades:**
- Alcance: 24 metros (curto) / 48 metros (longo, desvantagem)
- Requer munição (flechas)
- Pode atacar furtivamente (+1 em ataques surpresa)

**Durabilidade:** 10 usos  
**Valor:** 30 UC  
**Peso:** 2 unidades  
**Origem Narrativa:** Feito com madeira flexível de biriba, comum na Floresta do Norte. As cordas são de tendão de veado.  
**Classes Recomendadas:** Arqueiro Selvagem, Caçador de Feras, Explorador de Terras  

**Descrição:** Arco leve e compacto, ideal para caça e patrulha. A madeira de biriba oferece elasticidade perfeita para disparos rápidos. Vem com uma aljava de fibra trançada.

---

#### 🎯 Zarabatana Ritual

```
ID: ITM_ARM_005
Nome: Zarabatana Ritual
Tipo: Arma
Subtipo: Zarabatana
Matriz: Média / Incomum
```

**Dano:** 1d4 Perfurante + Efeito (veneno/sedativo)  
**Propriedades:**
- Alcance: 12 metros (silenciosa)
- Pode aplicar venenos/sedativos nas flechas
- Ataques não alertam inimigos (ideal para caça/stealth)

**Durabilidade:** 14 usos  
**Valor:** 45 UC  
**Peso:** 1 unidade  
**Origem Narrativa:** Tubo oco de bambu decorado com pinturas ritualísticas. Usada em caçadas silenciosas e cerimônias de iniciação.  
**Classes Recomendadas:** Xamã Curandeiro, Arqueiro Selvagem  

**Descrição:** Uma zarabatana de 1,5 metro decorada com padrões geométricos em urucum e jenipapo. Os dardos são feitos de espinhos de palmeira. Xamãs a usam para aplicar remédios à distância em animais feridos.

**Nota:** Combina com consumível "Veneno de Sapo-Cururu" (ITM_CNS_003)

---

### 3.3 Armaduras e Proteções

#### 🛡️ Veste de Fibra Trançada

```
ID: ITM_ARM_006
Nome: Veste de Fibra Trançada
Tipo: Armadura
Subtipo: Armadura Leve
Matriz: Média / Comum
```

**Defesa:** +1 CA  
**Propriedades:**
- Não impõe penalidade de movimento
- +1 em testes de Furtividade (silenciosa)
- Resistência a espinhos/vegetação densa

**Durabilidade:** 10 usos  
**Valor:** 25 UC  
**Peso:** 5 unidades  
**Origem Narrativa:** Tecida com fibras de cipó e embira. Leve e flexível, protetora contra cortes e arranhões da floresta.  
**Classes Recomendadas:** Todas as classes indígenas  

**Descrição:** Veste trançada que cobre torso e ombros. As fibras são tratadas com resina de jatobá para aumentar a resistência. Padrões tribais são pintados com tintas naturais.

---

#### 🦌 Couraça de Couro de Veado

```
ID: ITM_ARM_007
Nome: Couraça de Couro de Veado
Tipo: Armadura
Subtipo: Armadura Média
Matriz: Alta / Incomum
```

**Defesa:** +2 CA  
**Propriedades:**
- +1 em testes de Sobrevivência em florestas
- Leve (movimento normal)
- Respirável (não gera fadiga em climas quentes)

**Durabilidade:** 14 usos  
**Valor:** 60 UC  
**Peso:** 8 unidades  
**Origem Narrativa:** Curtida tradicionalmente com tanino de casca de angico. O couro de veado-campeiro é valorizado por sua leveza e durabilidade.  
**Classes Recomendadas:** Guerreiro Tribal, Caçador de Feras  

**Descrição:** Couraça que cobre peito, costas e parte dos ombros. O couro é flexível mas resistente, decorado com símbolos de proteção. Acompanha tiras de amarração ajustáveis.

**Nota:** Pode ser melhorada com "Escamas de Jacaré" (material de crafting) para +1 CA adicional.

---

### 3.4 Consumíveis

#### 🌿 Chá de Erva-Lua

```
ID: ITM_CNS_001
Nome: Chá de Erva-Lua
Tipo: Consumível
Subtipo: Poção
Matriz: Média / Incomum
```

**Efeito:** Reduz 1 nível de Fadiga Espiritual
**Propriedades:**
- Uso: Ação Principal
- Só pode ser coletada à noite sob lua cheia
- Sabor amargo, aroma calmante

**Durabilidade:** 1 uso (consumível)  
**Valor:** 30 UC  
**Peso:** 0,5 unidades  
**Origem Narrativa:** Erva mística que floresce apenas sob luz lunar direta. Cresce na Floresta do Norte em clareiras sagradas.  
**Classes Recomendadas:** Xamã Curandeiro, Encantador de Espíritos  

**Descrição:** Infusão verde-prateada que brilha levemente no escuro. Feita com folhas de uma planta que absorve energia lunar. Xamãs a usam antes de rituais para fortalecer a conexão espiritual.

**Receita:** Ver [4.1 — Receita: Chá de Erva-Lua](#41-receita-chá-de-erva-lua)

---

#### 🍖 Carne Seca de Capivara

```
ID: ITM_CNS_002
Nome: Carne Seca de Capivara
Tipo: Consumível
Subtipo: Alimento
Matriz: Baixa / Comum
```

**Efeito:** Restaura 1d6 PV e remove 1 nível de Fadiga  
**Propriedades:**
- Uso: Durante descanso curto (não consome ação)
- Pode ser empilhada (até 10 unidades)
- Dura 30 dias antes de estragar

**Durabilidade:** 1 uso (consumível)  
**Valor:** 5 UC  
**Peso:** 0,5 unidades  
**Origem Narrativa:** Carne defumada tradicionalmente, preparada por tribos ribeirinhas. Rica em proteína e sal natural.  
**Classes Recomendadas:** Todas  

**Descrição:** Tiras de carne de capivara salgada e defumada. Tem textura fibrosa e sabor forte. Essencial em longas jornadas pela mata.

---

#### 🐸 Veneno de Sapo-Cururu

```
ID: ITM_CNS_003
Nome: Veneno de Sapo-Cururu
Tipo: Consumível
Subtipo: Veneno
Matriz: Média / Raro
```

**Efeito:** Aplica "Envenenado" por 3 turnos (1d4 dano/turno, CD Vigor 12 para resistir)  
**Propriedades:**
- Uso: Aplicado em armas (1 dose = 3 ataques)
- Pode ser neutralizado por "Antídoto de Açafrão"
- Perigoso de manusear (teste Conhecimento CD 10 ou sofre 1d4 dano)

**Durabilidade:** 3 usos  
**Valor:** 50 UC  
**Peso:** 0,2 unidades  
**Origem Narrativa:** Extraído das glândulas do sapo-cururu, encontrado em pântanos e margens do Rio das Marés.  
**Classes Recomendadas:** Xamã Curandeiro, Arqueiro Selvagem  

**Descrição:** Líquido amarelo-esverdeado viscoso em frasco de bambu selado. Altamente tóxico. Xamãs usam em caçadas para paralisar presas grandes.

**Nota:** Combina perfeitamente com "Zarabatana Ritual" (ITM_ARM_005)

---

#### 🍯 Mel de Jataí

```
ID: ITM_CNS_004
Nome: Mel de Jataí
Tipo: Consumível
Subtipo: Remédio
Matriz: Média / Incomum
```

**Efeito:** Restaura 1d4 PV imediatamente e concede +1 em testes de Vigor por 1 hora  
**Propriedades:**
- Uso: Ação menor
- Pode ser usado como ingrediente de crafting (poções)
- Sabor doce e medicinal

**Durabilidade:** 1 uso  
**Valor:** 20 UC  
**Peso:** 0,3 unidades  
**Origem Narrativa:** Coletado de colmeias de abelhas jataí nativas. Tem propriedades anti-inflamatórias e cicatrizantes reconhecidas por curandeiros.  
**Classes Recomendadas:** Todas  

**Descrição:** Mel dourado e espesso em pequeno pote de cerâmica. As jataí são abelhas sem ferrão que produzem mel medicinal. Valorizado tanto por indígenas quanto por colonizadores.

---

### 3.5 Materiais de Crafting

#### 🪵 Madeira de Pau-Brasil

```
ID: ITM_MAT_001
Nome: Madeira de Pau-Brasil
Tipo: Material
Subtipo: Madeira Nobre
Matriz: N/A / Raro
```

**Propriedades:**
- Componente para armas de qualidade Alta ou superior
- +1 em durabilidade de itens craftados
- Pode ser vendido por preço alto (50 UC)

**Durabilidade:** N/A (não degrada)  
**Valor:** 50 UC  
**Peso:** 2 unidades  
**Origem Narrativa:** Madeira vermelha extraída da árvore símbolo do Brasil. Densa, resistente e bela. Alvo de exploração intensa por colonizadores.  
**Uso em Crafting:** Arcos, lanças, escudos de alta qualidade  

**Descrição:** Tronco ou tábua de pau-brasil, com cerne avermelhado intenso. A madeira é tão densa que afunda na água. Altamente valorizada para construção de armas e instrumentos.

**Localização:** Floresta do Norte (rara), áreas protegidas por indígenas

---

#### 🧵 Fibra de Cipó-Imbé

```
ID: ITM_MAT_002
Nome: Fibra de Cipó-Imbé
Tipo: Material
Subtipo: Fibra Vegetal
Matriz: N/A / Comum
```

**Propriedades:**
- Componente para armaduras leves, cordas, redes
- Flexível e resistente
- Fácil de encontrar na floresta

**Durabilidade:** N/A  
**Valor:** 3 UC  
**Peso:** 0,5 unidades  
**Origem Narrativa:** Cipó nativo abundante na Floresta do Norte. Tradicionalmente usado por povos originários para cestaria e construção.  
**Uso em Crafting:** Armaduras de fibra, cordas, redes de pesca  

**Descrição:** Rolo de fibras longas e flexíveis extraídas de cipó. Após secar e tratar, torna-se material resistente para tecelagem e amarração.

**Localização:** Floresta do Norte (abundante), margens de rios

---

#### 🪨 Pedra Lascada

```
ID: ITM_MAT_003
Nome: Pedra Lascada
Tipo: Material
Subtipo: Pedra
Matriz: N/A / Comum
```

**Propriedades:**
- Componente para armas simples (tacapes, machados, pontas de flecha)
- Pode ser afiada para criar ferramentas de corte

**Durabilidade:** N/A  
**Valor:** 2 UC  
**Peso:** 1 unidade  
**Origem Narrativa:** Sílex ou quartzo lascado em pontas afiadas. Técnica milenar dos povos originários.  
**Uso em Crafting:** Tacapes, machados, pontas de flecha e lança  

**Descrição:** Fragmento de pedra lascada com bordas afiadas. Simples mas eficaz. Base da tecnologia lítica indígena.

**Localização:** Margens de rios, Pico da Neblina, pedreiras

---

### 3.6 Itens Rituais e Culturais

#### 📿 Colar de Dentes de Onça

```
ID: ITM_RIT_001
Nome: Colar de Dentes de Onça
Tipo: Ritual
Subtipo: Amuleto
Matriz: Alta / Raro
```

**Efeito:** +1 em testes de Presença e Intimidação  
**Propriedades:**
- Símbolo de status entre guerreiros
- NPCs indígenas reagem com respeito
- Requer ter caçado uma onça pessoalmente (narrativo)

**Durabilidade:** N/A (não degrada)  
**Valor:** 80 UC  
**Peso:** 0,2 unidades  
**Origem Narrativa:** Troféu de caça valorizado. Cada dente representa uma vitória sobre a morte. Usado por guerreiros experientes.  
**Classes Recomendadas:** Guerreiro Tribal, Caçador de Feras  

**Descrição:** Colar com 12 presas de onça-pintada amarradas com fibra de tucum. Os dentes são polidos e gravados com símbolos de força. Usar este colar é declarar que você enfrentou a maior caçadora da floresta e sobreviveu.

**Nota do Mestre:** Desbloqueia diálogo especial com o Cacique de tribos indígenas.

---

#### 🥁 Tambor Cerimonial Pequeno

```
ID: ITM_RIT_002
Nome: Tambor Cerimonial Pequeno
Tipo: Ritual
Subtipo: Instrumento
Matriz: Média / Incomum
```

**Efeito:** Pode ser usado para realizar rituais tribais (bônus +1 em testes de Magia durante cerimônias)  
**Propriedades:**
- Necessário para certos rituais xamânicos
- Pode acalmar NPCs hostis (teste Presença CD 14)
- Som ecoa por até 200 metros

**Durabilidade:** 12 usos  
**Valor:** 40 UC  
**Peso:** 3 unidades  
**Origem Narrativa:** Feito com madeira oca e couro esticado. Usado em rituais de cura, invocação e celebrações.  
**Classes Recomendadas:** Xamã Curandeiro, Encantador de Espíritos  

**Descrição:** Tambor cilíndrico de 30 cm com couro de veado curtido. Pintado com padrões espirituais em urucum. O som grave ressoa nas florestas, chamando espíritos e reunindo tribos.

---

### 3.7 Itens de Quest

#### 🗺️ Mapa Fragmentado do Pajé

```
ID: ITM_QST_001
Nome: Mapa Fragmentado do Pajé
Tipo: Quest
Subtipo: Documento
Matriz: N/A / Épico
```

**Efeito:** Revela localização de uma câmara secreta nas Ruínas Queimadas  
**Propriedades:**
- Único (não pode ser vendido ou descartado)
- Necessário para progressão da quest principal
- Escrito em símbolos ancestrais (requer Conhecimento CD 14 para ler)

**Durabilidade:** N/A (não degrada)  
**Valor:** Sem valor comercial (narrativo)  
**Peso:** 0,1 unidades  
**Origem Narrativa:** Fragmento de mapa desenhado pelo Velho Pajé de São Tomé antes de sua morte. Indica o caminho para a Primeira Ruptura.  
**Classes Recomendadas:** Qualquer (quest item)  

**Descrição:** Pedaço de casca de árvore com desenhos feitos com carvão e sangue. Mostra símbolos de direção e marcos naturais. Parece antigo e profético.

**Nota:** Item inicial da quest "A Primeira Ruptura". Obtido na Sessão 1 do Ato 1.

---

#### 🌟 Amuleto Espiritual Apagado

```
ID: ITM_QST_002
Nome: Amuleto Espiritual Apagado
Tipo: Quest
Subtipo: Artefato
Matriz: N/A / Lendário
```

**Efeito:** Sem efeito (desativado). Pode ser reativado na Ruptura  
**Propriedades:**
- Evolui durante a campanha
- Quando ativado: +2 em todos os testes contra entidades espirituais
- Brilha na presença de rupturas temporais

**Durabilidade:** N/A (indestrutível)  
**Valor:** Sem valor comercial  
**Peso:** 0,2 unidades  
**Origem Narrativa:** Artefato ancestral criado na Primeira Era. Perdeu seu poder quando a Ruptura ocorreu. Chave para estabilizar a fenda temporal.  
**Classes Recomendadas:** Qualquer (quest item central)  

**Descrição:** Pingente circular de pedra verde-escura com entalhes complexos. Está frio ao toque e não reflete luz. Era usado por Guardiões da Raiz em eras passadas.

**Nota:** Item central do Ato 1. Recebido na Sessão 2. Evolui conforme a narrativa progride.

---

## 4. Receitas de Crafting

Esta seção apresenta as receitas para criar os itens do MVP. Todas seguem o sistema descrito em [Cap. 6.3](../01_Livro_de_Regras/06_Economia_Itens_e_Crafting.md#63--criação-de-itens-crafting).

### Formato das Receitas

| Campo | Descrição |
|-------|-----------|
| **Item Resultante** | O que você cria |
| **Proficiência Necessária** | Tipo e nível mínimo |
| **Materiais** | Lista de componentes e quantidades |
| **Local Requerido** | Onde pode ser craftado |
| **CD Base** | Classe de Dificuldade do teste |
| **Tempo** | Duração da criação |
| **Resultado Crítico** | Efeito de rolar 20 natural |

---

### 4.1 Receita: Chá de Erva-Lua

```
Item Resultante: Chá de Erva-Lua (ITM_CNS_001)
Proficiência: Herborismo (Aprendiz)
Materiais:
  - 2× Folhas de Erva-Lua (coletadas à noite)
  - 1× Água limpa
  - 1× Fogo para infusão

Local Requerido: Fogueira ou cozinha
CD Base: 10
Tempo: 10 minutos (1 cena)
Resultado Crítico: Cria 2 doses em vez de 1
```

**Notas:** As folhas devem ser coletadas sob lua cheia. Xamãs têm vantagem neste teste.

---

### 4.2 Receita: Veste de Fibra Trançada

```
Item Resultante: Veste de Fibra Trançada (ITM_ARM_006)
Proficiência: Tecelagem (Competente)
Materiais:
  - 10× Fibra de Cipó-Imbé (ITM_MAT_002)
  - 1× Resina de Jatobá
  - 1× Kit de Tecelagem

Local Requerido: Oficina ou aldeia
CD Base: 12
Tempo: 4 horas (meio dia)
Resultado Crítico: Qualidade sobe para "Alta" (+1 CA adicional)
```

**Notas:** O personagem pode trabalhar em uma veste enquanto o grupo descansa.

---

### 4.3 Receita: Lança de Madeira-Ferro

```
Item Resultante: Lança de Madeira-Ferro (ITM_ARM_002)
Proficiência: Carpintaria (Competente) ou Ferraria (Aprendiz)
Materiais:
  - 1× Madeira de Aroeira (similar à Madeira de Pau-Brasil)
  - 1× Carvão para tratamento térmico
  - 1× Kit de Ferramentas

Local Requerido: Oficina com fogo
CD Base: 11
Tempo: 2 horas
Resultado Crítico: +2 durabilidade e bônus narrativo (+1 dano em primeira caçada)
```

**Notas:** A ponta deve ser carbonizada em fogo sagrado para máxima durabilidade.

---

### 4.4 Receita: Veneno de Sapo-Cururu (Extração)

```
Item Resultante: Veneno de Sapo-Cururu (ITM_CNS_003)
Proficiência: Herborismo (Especialista) ou Alquimia (Competente)
Materiais:
  - 1× Sapo-Cururu capturado vivo
  - 1× Frasco de bambu
  - 1× Luvas de proteção ou conhecimento de manuseio

Local Requerido: Qualquer local seguro
CD Base: 14
Tempo: 30 minutos
Falha: Sofre 1d4 dano de veneno se falhar por 5 ou mais
Resultado Crítico: Extrai 2 doses (6 usos totais)
```

**Notas:** Sapos-cururu são encontrados no Rio das Marés e pântanos próximos às Ruínas Queimadas.

---

### 4.5 Receita: Couraça de Couro de Veado

```
Item Resultante: Couraça de Couro de Veado (ITM_ARM_007)
Proficiência: Coureira (Especialista)
Materiais:
  - 2× Couro de Veado (obtido por caça)
  - 1× Tanino de Casca de Angico
  - 1× Kit de Coureira

Local Requerido: Oficina de curtume
CD Base: 13
Tempo: 1 dia
Resultado Crítico: Qualidade sobe para "Excelente" (+1 CA adicional)
```

**Notas:** O couro deve ser curtido por pelo menos 8 horas. Tempo pode ser reduzido em 50% com Proficiência Mestre.

---

### 4.6 Receita: Machadinha de Obsidiana

```
Item Resultante: Machadinha de Obsidiana (ITM_ARM_003)
Proficiência: Ferraria (Especialista) + Conhecimento de Pedra Lascada
Materiais:
  - 1× Obsidiana Bruta (encontrada nas Ruínas Queimadas)
  - 1× Cabo de Jacarandá
  - 1× Resina para fixação
  - 1× Kit de Ferramentas

Local Requerido: Oficina com ferramentas de precisão
CD Base: 15
Tempo: 6 horas
Falha: Quebra a obsidiana (perde o material)
Resultado Crítico: Concede propriedade especial "Quebra-Escudos" (+2 contra defesas)
```

**Notas:** Obsidiana é material Raro. Lascar obsidiana exige técnica ancestral. Este item pode ser ensinado por um NPC mestre artesão nas Ruínas Queimadas.

---

## 5. Tabela de Preços e Comércio Regional

Esta seção apresenta os preços base em UC e os modificadores regionais conforme o sistema descrito em [Cap. 6.5](../01_Livro_de_Regras/06_Economia_Itens_e_Crafting.md#65--comércio-e-economia-regional).

### 5.1 Preços Base por Categoria

| Categoria | Preço Base Médio | Faixa Típica |
|-----------|------------------|--------------|
| **Armas Simples** | 8-15 UC | 5-25 UC |
| **Armas Comuns** | 25-40 UC | 20-60 UC |
| **Armas Raras** | 100-150 UC | 80-200 UC |
| **Armaduras Leves** | 20-40 UC | 15-60 UC |
| **Armaduras Médias** | 50-80 UC | 40-120 UC |
| **Consumíveis Comuns** | 3-10 UC | 2-15 UC |
| **Consumíveis Raros** | 20-50 UC | 15-80 UC |
| **Materiais Comuns** | 2-5 UC | 1-8 UC |
| **Materiais Raros** | 30-60 UC | 25-100 UC |
| **Itens Rituais** | 40-80 UC | 30-150 UC |

### 5.2 Modificadores Regionais (Ato 1)

| Localização | Tipo de Comerciante | Modificador | Disponibilidade |
|-------------|---------------------|-------------|-----------------|
| **Vila de São Tomé (HUB)** | Ferreiro, Taverna, Curandeiro | Preço Base | Todos os itens Comuns e Incomuns |
| **Floresta do Norte** | Escambo com Caçadores | -10% (abundância de recursos naturais) | Materiais, armas simples, armaduras leves |
| **Rio das Marés** | Comerciante Itinerante | +20% (difícil acesso) | Itens variados, pode ter Raros |
| **Mina de Ouro** | Contrabandista | +30% (risco e isolamento) | Ferramentas, itens coloniais |
| **Ruínas Queimadas** | Nenhum (apenas loot) | N/A | Artefatos, materiais raros |
| **Pico da Neblina** | Nenhum (apenas loot) | N/A | Minerais raros, itens espirituais |
| **Acampamento Rival** | Comércio hostil | +100% ou proibido | Apenas mediante negociação ou infiltração |

### 5.3 Modificadores por Eventos Especiais

| Evento | Modificador | Duração |
|--------|-------------|---------|
| **Feira Sazonal** | -15% | 3 dias de jogo |
| **Ataque de Bandeirantes** | +50% (escassez) | Até resolver a ameaça |
| **Lua Cheia** | Itens rituais -10% | 1 noite |
| **Escassez de Comida** | Consumíveis +40% | Até reabastecimento |

### 5.4 NPCs Comerciantes Importantes

#### 🔨 Joaquim, o Ferreiro (Vila de São Tomé)

**Especialidade:** Armas e ferramentas de metal  
**Inventário:** Espadas, machados, picaretas, pregos  
**Preços:** Base (100%)  
**Serviços:** Reparo de armas (CD 12, custa 30% do valor do item)  
**Particularidade:** Paga 20% a mais por Minério de Sangue

#### 🌿 Iara, a Curandeira (Vila de São Tomé)

**Especialidade:** Ervas, poções, remédios  
**Inventário:** Chás, antídotos, bandagens  
**Preços:** Base (100%)  
**Serviços:** Identificação de ervas desconhecidas (5 UC)  
**Particularidade:** Ensina receitas de Herborismo se a relação for Amigável

#### 🎯 Tupã, Caçador Errante (Floresta do Norte)

**Especialidade:** Armas tribais, couros, troféus  
**Inventário:** Arcos, lanças, peles, carne seca  
**Preços:** -10% (escambo favorável)  
**Serviços:** Ensina técnica de rastreamento (+1 Sobrevivência por 1 dia, 10 UC)  
**Particularidade:** Só aparece durante o dia, segue rotina de caça

#### 🚢 Capitão Rodrigo (Rio das Marés, Maré Baixa)

**Especialidade:** Itens coloniais, contraband
**Inventário:** Mosquetes (quando disponível), pólvora, mapas, rum  
**Preços:** +20% (itinerante)  
**Serviços:** Transporte para Mina de Ouro (15 UC, só na maré baixa)  
**Particularidade:** Pode ter itens Raros aleatórios (1d6, 5-6 = item raro disponível)

---

## 6. Distribuição de Itens por Localização (Ato 1)

Esta seção indica onde os itens podem ser encontrados, comprados ou saqueados nos 9 nós do mapa do Ato 1. Referência: [Atlas do Eco](01_Atlas_do_Eco_Ato1.md).

### 6.1 Vila de São Tomé (HUB)

**Tipo:** Urbano / Seguro  
**Comerciantes:** Ferreiro, Curandeira, Taverna  

**Itens Disponíveis para Compra:**
- Tacape de Pedra Lascada (8 UC)
- Veste de Fibra Trançada (25 UC)
- Arco Curto de Biriba (30 UC)
- Carne Seca de Capivara (5 UC)
- Mel de Jataí (20 UC)
- Fibra de Cipó-Imbé (3 UC)
- Pedra Lascada (2 UC)

**Loot (exploração/quests):**
- Couraça de Couro de Veado (quest de caça)
- Mapa Fragmentado do Pajé (quest inicial)

---

### 6.2 Floresta do Norte

**Tipo:** Mata Densa  
**Perigos:** Onças, espíritos menores, armadilhas naturais  
**Recursos:** Madeiras nobres, fibras, ervas  

**Itens Coletáveis:**
- Madeira de Pau-Brasil (Raro, CD Sobrevivência 14, 1d3 por dia)
- Fibra de Cipó-Imbé (Comum, CD Sobrevivência 8, 2d6 por hora)
- Folhas de Erva-Lua (Incomum, apenas à noite sob lua cheia, CD 12)

**Loot de Combate:**
- Pele de Onça (após derrotar Onça Pintada)
- Presas de Onça (2d2, para craftar Colar de Dentes)

**Encontros:**
- Tupã, Caçador Errante (escambo)

---

### 6.3 Rio das Marés

**Tipo:** Água / Lama  
**Perigos:** Jacarés, afogamento, maré alta  
**Recursos:** Peixes, sapos venenosos, argila  

**Itens Coletáveis:**
- Sapo-Cururu (para extração de veneno, CD Sobrevivência 13)
- Argila Medicinal (Comum, CD 8)

**Encontros:**
- Capitão Rodrigo (comerciante itinerante, só na maré baixa)

**Loot:**
- Escamas de Jacaré (após combate)

---

### 6.4 A Mina de Ouro

**Tipo:** Subterrâneo  
**Perigos:** Bandeirantes, armadilhas, desabamentos  
**Recursos:** Minérios  

**Loot:**
- Pepitas de Ouro (20-50 UC cada)
- Ferramentas Danificadas (baixa qualidade)
- Minério de Ferro (para crafting)

**Encontros:**
- Bandeirantes hostis (combate)
- Possível comerciante contrabandista (se infiltração for bem-sucedida)

---

### 6.5 Toca da Fera

**Tipo:** Caverna Natural  
**Perigos:** Onça Alfa (mini-boss)  
**Recursos:** Ossos, troféus de caça  

**Loot:**
- Pele de Onça de Qualidade Alta (1 unidade)
- Colar de Dentes de Onça (já crafted, se derrotar a Alfa)
- Ossos Grandes (material de crafting para armas)

---

### 6.6 Acampamento Rival (Bandeirantes)

**Tipo:** Acampamento Militar Hostil  
**Perigos:** Capitão Bandeirante (boss), soldados  
**Recursos:** Equipamento colonial  

**Loot:**
- Mosquete Enferrujado (25% chance, Baixa/Incomum)
- Espada de Ferro (Média/Comum)
- Munição de Mosquete (1d20 tiros)
- Moedas de Classe Colonizador (quest item)
- Documentos Roubados (quest)

---

### 6.7 Pico da Neblina

**Tipo:** Montanha Sagrada  
**Perigos:** Fadiga, quedas, espíritos ancestrais  
**Recursos:** Minerais raros, cristais  

**Itens Coletáveis:**
- Obsidiana Bruta (Raro, CD Mineração 15, 1d2 por dia)
- Cristal de Quartzo (Incomum, CD 12)
- Pedra Lascada (Comum, CD 8, abundante)

**Loot:**
- Amuleto Espiritual Apagado (quest, na câmara sagrada do topo)

---

### 6.8 Ruínas Queimadas

**Tipo:** Terra Arrasada / Pântano Espiritual  
**Perigos:** Espíritos corrompidos, alucinações, fogo fantasma  
**Recursos:** Artefatos antigos, cinzas espirituais  

**Loot:**
- Cinzas Espirituais (Comum, após derrotar espíritos)
- Obsidiana Vulcânica (Raro, escavação CD 14)
- Tambor Cerimonial Pequeno (Incomum, em altar abandonado)
- Fragmentos de Cerâmica Antiga (quest/narrativo)

**Encontros:**
- Espíritos Menores (combate)
- Possível NPC: Artesão Eremita (ensina receita da Machadinha de Obsidiana)

---

### 6.9 A Ruptura (Zona Final)

**Tipo:** Zona de Distorção Temporal
**Perigos:** Guardião da Fenda (boss final), anomalias mágicas
**Recursos:** Nenhum (apenas narrativo)

**Nota sobre o Guardião da Fenda:** O Guardião é uma manifestação defensiva da Raiz do Mundo, não um vilão. Ele foi criado automaticamente pela Raiz para selar a Ruptura e ataca qualquer criatura que se aproxime da fenda. Sua derrota (ou pacificação) é necessária para estabilizar o portal.  

**Loot:**
- Fragmento da Raiz (Lendário, quest item)
- Amuleto Espiritual Reativado (evolução do ITM_QST_002)
- Recompensa narrativa conforme escolhas da campanha

**Nota:** Itens lendários desta área são únicos e vinculados à progressão da história.

---

## 📊 Apêndice: Tabela Resumida de Itens

| ID | Nome | Tipo | Matriz | Dano/Def | Valor | Peso |
|----|------|------|--------|----------|-------|------|
| ITM_ARM_001 | Tacape de Pedra Lascada | Arma | Baixa/Comum | 1d4+1 | 8 UC | 3u |
| ITM_ARM_002 | Lança de Madeira-Ferro | Arma | Média/Incomum | 1d6+1 | 35 UC | 4u |
| ITM_ARM_003 | Machadinha de Obsidiana | Arma | Alta/Raro | 1d8 | 120 UC | 5u |
| ITM_ARM_004 | Arco Curto de Biriba | Arma | Média/Comum | 1d6 | 30 UC | 2u |
| ITM_ARM_005 | Zarabatana Ritual | Arma | Média/Incomum | 1d4+efeito | 45 UC | 1u |
| ITM_ARM_006 | Veste de Fibra Trançada | Armadura | Média/Comum | +1 CA | 25 UC | 5u |
| ITM_ARM_007 | Couraça de Couro de Veado | Armadura | Alta/Incomum | +2 CA | 60 UC | 8u |
| ITM_CNS_001 | Chá de Erva-Lua | Consumível | Média/Incomum | -1 Fadiga Espiritual | 30 UC | 0,5u |
| ITM_CNS_002 | Carne Seca de Capivara | Consumível | Baixa/Comum | 1d6 PV | 5 UC | 0,5u |
| ITM_CNS_003 | Veneno de Sapo-Cururu | Consumível | Média/Raro | Veneno 3t | 50 UC | 0,2u |
| ITM_CNS_004 | Mel de Jataí | Consumível | Média/Incomum | 1d4 PV+buff | 20 UC | 0,3u |
| ITM_MAT_001 | Madeira de Pau-Brasil | Material | N/A/Raro | - | 50 UC | 2u |
| ITM_MAT_002 | Fibra de Cipó-Imbé | Material | N/A/Comum | - | 3 UC | 0,5u |
| ITM_MAT_003 | Pedra Lascada | Material | N/A/Comum | - | 2 UC | 1u |
| ITM_RIT_001 | Colar de Dentes de Onça | Ritual | Alta/Raro | +1 Presença | 80 UC | 0,2u |
| ITM_RIT_002 | Tambor Cerimonial Pequeno | Ritual | Média/Incomum | Ritual+1 | 40 UC | 3u |
| ITM_QST_001 | Mapa Fragmentado do Pajé | Quest | N/A/Épico | - | - | 0,1u |
| ITM_QST_002 | Amuleto Espiritual Apagado | Quest | N/A/Lendário | Evolui | - | 0,2u |

---

## 🎯 Conclusão

Este **Livro de Itens e Equipamentos** estabelece a base sólida para a economia, progressão e imersão narrativa de *Eras do Brasil*. Com 15 itens completos (mais variantes de qualidade/raridade), o MVP tem conteúdo suficiente para:

✅ Suportar POC 06 (Matriz de Itens)  
✅ Suportar POC 24 (Inventário)  
✅ Suportar POC 26 (Crafting)  
✅ Alimentar a economia regional do Ato 1  
✅ Distribuir loot significativo em todos os 9 nós do mapa  
✅ Criar progressão tangível através de crafting e comércio  

### 📖 Próximos Passos

- **Expansão para Ato 2:** Adicionar itens coloniais (mosquetes, armaduras de metal)
- **Itens Folclóricos:** Artefatos místicos ligados a entidades (Boto, Caipora, Saci)
- **Sistema de Encantamento:** Permitir melhorias mágicas em itens Raros+
- **Itens Dinâmicos:** Armas que evoluem com o personagem (armas vivas)

---

**Documento criado por:** Vibe Flow — Sprint 3  
**Última atualização:** Ato 1 MVP  
**Referências:** [Cap. 6 — Economia e Crafting](../01_Livro_de_Regras/06_Economia_Itens_e_Crafting.md) · [Atlas do Eco](01_Atlas_do_Eco_Ato1.md) · [Schemas](../06_Dados_e_Assets/01_Schemas_Estruturais.md)
