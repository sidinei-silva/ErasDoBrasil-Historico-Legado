# 🔍 Auditoria do GDD — Eras do Brasil

> **Data:** 2026-02-11
> **Objetivo:** Avaliar coesão, consistência, completude e viabilidade do GDD, com foco em: sistema de classes (inspiração FFT), enredo e mecânicas, sistema de NPCs (amizade/fofoca), e erros gerais.

---

## 📋 Sumário de Achados

| Categoria | Críticos | Importantes | Menores |
|:---|:---:|:---:|:---:|
| Inconsistências Numéricas | 1 | 0 | 0 |
| Referências Incorretas | 1 | 1 | 0 |
| Sistema de Classes (FFT) | 0 | 3 | 1 |
| Enredo e Mecânicas | 0 | 2 | 2 |
| Sistema de NPCs (Amizade/Fofoca) | 0 | 1 | 0 |
| Sobreposição de Conteúdo | 0 | 1 | 1 |
| Livros Referenciados Inexistentes | 0 | 1 | 0 |
| **Total** | **2** | **9** | **4** |

---

## 🔴 1. Inconsistências Numéricas (CRÍTICO)

### 1.1 — Tabela de CD divergente entre Capítulos 2, 4 e 9

**Problema:** A tabela de Classes de Dificuldade (CD) possui valores **completamente diferentes** entre o Capítulo 2 (Mecânicas Básicas), o Capítulo 4 (Sistema de Combate) e o Capítulo 9 (Apêndices).

| Grau | Cap. 2 (Mecânicas) | Cap. 4 (Combate) | Cap. 9 (Apêndices) |
|:---|:---:|:---:|:---:|
| Muito fácil | 5 | 5 | 5 |
| Fácil | 10 | 10 | 10 |
| Moderada/Médio | **13** | **15** | **13** |
| Difícil | **16** | **20** | **16** |
| Muito difícil | **18** | **25** | **18** |
| Quase impossível/Épico | **20+** | **30+** | **20+** |

**Impacto:** Os valores do Capítulo 4 são drasticamente mais altos. Se a escala de atributos vai de 1 a 6 (modificador -2 a +3) e proficiência de +1 a +4, o máximo que um personagem pode alcançar sem dado é +7. Uma CD 30+ em combate (Cap. 4) seria inalcançável mesmo com 20 natural (+27 total máximo). Isso torna certas dificuldades épicas de combate matematicamente impossíveis de superar.

**Status:** ✅ CORRIGIDO — Tabela do Cap. 4 harmonizada com Cap. 2/9.

### 1.2 — Referência incorreta a "Capítulo 9" no Capítulo 4

**Problema:** No arquivo `04_Sistema_de_Combate.md`, linha 183, a ação de Magia referencia "regras específicas de Magia descritas no Capítulo 9 (Magias e Espiritualidade)". O capítulo correto é o **Capítulo 7**, não o 9. O Capítulo 9 é de Apêndices e Referências.

**Status:** ✅ CORRIGIDO.

---

## 🟡 2. Sistema de Classes — Inspiração Final Fantasy Tactics

### 2.1 — Análise de Alinhamento com FFT

O sistema de classes de *Eras do Brasil* já possui **forte alinhamento com Final Fantasy Tactics** nos seguintes aspectos:

| Característica FFT | Implementado em Eras do Brasil? | Observação |
|:---|:---:|:---|
| Múltiplas classes acessíveis | ✅ | Jogador pode desbloquear e alternar entre classes |
| Tiers de evolução | ✅ | Tier 1 → 2 → 3 (similar ao Job Level) |
| Herança de habilidades ativas | ✅ | Habilidades ativas são herdadas entre classes |
| Passivas exclusivas da classe ativa | ✅ | Alinhado com "Support Abilities" do FFT |
| Requisitos de desbloqueio | ✅ | Moeda de Classe + Missão NPC (no FFT: Job Points) |
| Troca fora de combate | ✅ | Idêntico ao FFT |

### 2.2 — Lacunas identificadas vs. FFT (Importantes)

#### A) Ausência de limite de habilidades ativas herdáveis

**Problema:** No FFT, cada classe permite equipar um número limitado de habilidades de outras classes (geralmente 1 set de habilidades ativas de outra classe + 1 passiva + 1 reação). Em *Eras do Brasil*, não há limite explícito de quantas habilidades ativas herdadas um personagem pode usar simultaneamente. O documento `03_Heranca_de_Habilidades.md` menciona em "Expansões Futuras" a possibilidade de "Slots de habilidades ativas herdáveis (limite por nível)", mas isso ainda não está definido como regra.

**Recomendação:** Definir um sistema de **slots de habilidades herdadas** para evitar que personagens de alto nível acumulem dezenas de habilidades ativas, quebrando o balanceamento. Sugestão: 1 slot no Tier 1, 2 slots no Tier 2, 3 slots no Tier 3.

**Status:** ✅ CORRIGIDO — Sistema de slots implementado em `gdd/02_Livro_de_Classes/03_Heranca_de_Habilidades.md`.

#### B) Ausência de pré-requisitos entre classes (multi-class paths)

**Problema:** No FFT, certas classes avançadas só são desbloqueadas após atingir níveis em classes específicas (ex: Ninja requer Archer Lv.4 + Thief Lv.5). Em *Eras do Brasil*, qualquer classe Tier 1 da mesma origem pode ser desbloqueada apenas com Moeda de Classe + Missão NPC, sem exigir progresso em outras classes.

**Recomendação:** Considerar pré-requisitos de classe como mecânica futura para Tier 2/3, incentivando caminhos de progressão mais profundos e dando propósito ao multi-classing.

**Status:** ✅ CORRIGIDO — Pré-requisitos multi-class implementados em `gdd/02_Livro_de_Classes/01_Tiers_e_Evolucao.md`. Tier 3 agora requer ter pelo menos 1 outra classe em Tier 2.

#### C) Sistema de Reaction Abilities ausente

**Problema:** No FFT, cada classe possui "Reaction Abilities" (habilidades que disparam automaticamente em resposta a ações inimigas, como "Counter" ou "Auto-Potion"). O sistema atual de *Eras do Brasil* tem "Reações" mencionadas no combate (Cap. 4), mas não há habilidades de reação definidas nas classes documentadas.

**Recomendação:** Definir pelo menos 1 habilidade de reação por classe nos Tiers futuros. Isso enriqueceria o combate tático e se alinharia com a inspiração FFT.

**Status:** 📝 Documentado como recomendação.

#### D) Habilidades de Tier 2 e 3 não detalhadas (Menor)

**Problema:** Todos os 12 arquivos de classes Tier 1 estão completos e bem estruturados. Porém, as habilidades e mecânicas de Tier 2 e 3 são mencionadas apenas como nomes genéricos (ex: "Veterano da Floresta", "Protetor do Clã") sem detalhamento de novas habilidades, requisitos específicos ou mecânicas.

**Recomendação:** Priorizar o detalhamento dos Tier 2 pelo menos para as classes do MVP (Guerreiro Tribal), pois o Ato 1 concede "Ouro da Raiz" que permite evolução para Tier 2.

**Status:** 📝 Documentado como recomendação.

---

## 🟡 3. Enredo e Mecânicas

### 3.1 — Enredo está bem estruturado, mas com lacunas menores

**Pontos Fortes:**
- O Ato 1 ("A Primeira Ruptura") é completo, com 4 sessões, mecânica de Relógio da Ruptura, rivalidade com Bandeirantes de Sangue, e recompensas bem definidas.
- 18 mini-campanhas (6 por origem) estão documentadas.
- A sinergia entre mini-campanhas e o Ato 1 está claramente tabelada.
- A Linha Eco-Histórica oferece 7 marcos para campanhas futuras.

**Lacunas Identificadas:**

#### A) Troca de Origem — Mecânica vaga (Importante)

**Problema:** O "Espelho do Eco" é prometido como recompensa do Ato 1, permitindo trocar de Origem (ex: Colonizador → Indígena). O `00_Conceitos_Centrais_do_Mundo.md` menciona que essa troca é justificada narrativamente como "visões, reencarnações, pactos ou rituais", mas não há regras mecânicas definidas em nenhum documento. Questões em aberto:
- O personagem perde acesso às classes da origem anterior?
- Os atributos são resetados?
- Há custo em tempo, itens ou missões?
- Como isso interage com o sistema de herança de habilidades?

**Recomendação:** Criar uma seção dedicada no Livro de Classes ou no Livro de Regras (talvez como extensão do Cap. 3) detalhando a mecânica de troca de origem.

**Status:** ✅ CORRIGIDO — Mecânica completa implementada em `gdd/02_Livro_de_Classes/04_Troca_de_Origem.md`.

#### B) Sistema de Nível/XP não definido (Importante)

**Problema:** O GDD menciona "PV por Nível" em todas as classes e "XP de proficiência", mas não existe nenhum capítulo ou seção que defina como funciona a **progressão de nível do personagem**. Questões em aberto:
- Quanto XP é necessário para subir de nível?
- De onde vem o XP (combate, quests, exploração)?
- O que se ganha ao subir de nível além de PV?
- Os atributos sobem com nível?

O Capítulo 3 menciona distribuição de 27 pontos na criação, mas nenhum mecanismo de evolução de atributos por nível é descrito.

**Recomendação:** Adicionar uma seção "Progressão e Experiência" no Livro de Regras (como seção 3.11 ou capítulo dedicado).

**Status:** ✅ CORRIGIDO — Sistema completo implementado em `gdd/01_Livro_de_Regras/03B_Progressao_e_Experiencia.md`.

#### C) Defesa Base vs. Bônus de Armadura (Menor)

**Problema:** No Cap. 2 (seção 2.8), a Defesa Base é definida como `10 + Modificador de Astúcia`. No Cap. 9 (Apêndices), a fórmula é `10 + Mod. Astúcia + Bônus de Armadura (se houver)`. O bônus de armadura não é mencionado na definição original do Cap. 2.

**Status:** ✅ CORRIGIDO — Fórmula do Cap. 2 atualizada para incluir "Bônus de Armadura (se houver)".

#### D) Inteligência mencionada no Ato 1 mas não é atributo (Menor)

**Problema:** No `01_Ato_1_A_Primeira_Ruptura.md`, a ação de Desinformação Social menciona "Inteligência do Líder Rival" como atributo de resistência. O atributo "Inteligência" não existe no sistema — o equivalente seria "Conhecimento" ou "Astúcia".

**Status:** ✅ CORRIGIDO — Alterado para "Conhecimento".

---

## 🟡 4. Sistema de NPCs — Amizade e Fofoca (Conversa Gemini 8)

### 4.1 — Análise de Cobertura no GDD

A conversa Gemini 8 define sistemas detalhados de NPCs que foram **amplamente integrados** ao Capítulo 8 do Livro de Regras. Segue a análise de cobertura:

| Mecânica da Conversa Gemini 8 | Presente no GDD? | Onde? |
|:---|:---:|:---|
| IA por Fusão (Agenda + Necessidades) | ✅ | Cap. 8.3 |
| Needs (Fome, Sede, Energia, Social, Segurança) | ✅ | Cap. 8.3 |
| Traits (Gula, Preguiçoso, Ranzinza, Valente) | ✅ | Cap. 8.3 |
| Mood & Thoughts (Humor e Memórias) | ✅ | Cap. 8.3 |
| Utility AI (prioridade de decisão OnTick) | ✅ | Cap. 8.3 |
| knowledgeBase (Percepção Cognitiva) | ✅ | Cap. 8.3 |
| Tipos de conhecimento (Recurso, Entidade, Rotina) | ✅ | Cap. 8.3 |
| Esquecimento por prazo de validade | ✅ Parcial | Mencionado no Cap. 5.3 mas não no Cap. 8.3 |
| Relacionamentos NPC↔NPC | ✅ | Cap. 8.3 |
| Sistema de Fofoca (troca de informação) | ✅ | Cap. 8.3 |
| Sistema de Afinidade (Jogador↔NPC) | ✅ | Cap. 8.6 |
| Tabela de modificadores de Afinidade | ✅ | Cap. 8.6 |
| Acesso do jogador à knowledgeBase via diálogo | ✅ | Cap. 8.3 |
| Ciclo de Vida dos NPCs (nascer, morrer) | ✅ | Cap. 8.6 |
| Companheiros e Seguidores | ✅ | Cap. 8.6 |

### 4.2 — Lacuna: Esquecimento e prazo de validade da memória (Importante)

**Problema:** Na conversa Gemini 8, o sistema de "Esquecimento" está bem definido: a cada OnTick, a knowledgeBase é varrida e entradas onde `(TickAtual - ultimo_visto) > limite` são removidas. Isso garante que as informações dos NPCs sejam recentes. No Cap. 8.3 do GDD, a knowledgeBase está documentada com campos de `ultimo_visto`, mas **não há menção explícita à mecânica de esquecimento** (expiração das memórias). O Cap. 5.3 menciona que "informações possuem um prazo de validade" nas entrelinhas, mas sem formalização.

**Recomendação:** Adicionar ao Cap. 8.3 uma subseção sobre "Expiração e Esquecimento" da knowledgeBase, formalizando a regra de decaimento.

**Status:** ✅ CORRIGIDO — Subseção adicionada ao Cap. 8.3.

### 4.3 — Integração da Fofoca com o Gameplay

O sistema de Fofoca se entrelaça com o jogo das seguintes formas (todas documentadas):

1. **Exploração:** Jogador precisa falar com NPCs para obter localização de recursos, monstros e outros NPCs (Cap. 8.3).
2. **Ato 1 — Sessão 1:** Triangulação da localização da Ruptura depende da knowledgeBase dos NPCs aldeões e caçadores (Ato 1, Sessão 1).
3. **Sabotagem:** Ação de Desinformação Social usa a rede de fofoca para espalhar boatos contra rivais (Ato 1).
4. **Comércio:** Afinidade com NPCs afeta preços e acesso a informações exclusivas (Cap. 6.5, Cap. 8.6).
5. **Missões:** NPCs só revelam informações se a Afinidade for alta o suficiente (Cap. 8.3, 8.6).

**Conclusão:** O sistema de Fofoca e Amizade da Gemini 8 está **bem integrado** ao GDD, com entrelaçamento em exploração, narrativa, combate (sabotagem) e economia.

---

## 🟡 5. Sobreposição de Conteúdo

### 5.1 — Duplicação entre Cap. 5 e Cap. 8 sobre NPCs (Importante)

**Problema:** O Capítulo 5 (Exploração e Mundo), seções 5.3 e 5.4, contém descrições sobre o ciclo de tempo para NPCs, conhecimento de NPCs, interação entre NPCs, e sistema de afinidade. O Capítulo 8 (Mestres, Campanhas e Mundo Vivo) também aborda esses mesmos temas com **mais profundidade e detalhamento técnico**. As informações não são contraditórias, mas são redundantes.

**Recomendação:** Manter o Cap. 5 focado na perspectiva do jogador (como interagir com NPCs durante exploração) e o Cap. 8 como referência técnica completa (como a IA funciona). Adicionar referências cruzadas claras entre ambos para evitar confusão.

**Status:** ✅ CORRIGIDO — Referências cruzadas adicionadas nas seções 5.3 e 5.4 direcionando ao Cap. 8.

### 5.2 — Adaptação Digital em dois locais (Menor)

**Problema:** As informações sobre adaptação digital aparecem em dois locais: `03_Enredo_e_Mundo/03_Adaptacao_Digital_e_Campanhas.md` e `01_Livro_de_Regras/09_Apendices_e_Referencias.md` (seção 9.5). Ambos são válidos mas abordam perspectivas diferentes (enredo vs. regras).

**Status:** 📝 Menor, não requer ação imediata.

---

## 🟡 6. Livros Referenciados mas Inexistentes

**Problema:** O GDD referencia múltiplos "Livros" complementares que **ainda não existem** no repositório:

| Livro Referenciado | Referenciado em | Status |
|:---|:---|:---:|
| Livro de Magias e Rituais | Cap. 7 (7 referências) | ❌ Não existe |
| Livro de Itens e Crafting | Cap. 6, Cap. 9 | ❌ Não existe |
| Livro de Proficiências de Vida | Cap. 2, Cap. 3, Cap. 5, Cap. 9 | ❌ Não existe |
| Livro de Habilidades | Cap. 2 | ❌ Não existe |
| Livro de Inimigos e Bestiário | Cap. 9 | ❌ Não existe |
| Livro de Itens e Equipamentos | Cap. 2 | ❌ Não existe |

**Impacto:** Não é um erro per se, pois o ROADMAP indica que esses livros estão planejados. Porém, é importante saber que muitas regras estão intencionalmente incompletas (delegadas a esses livros futuros).

**Status:** 📝 Documentado para rastreamento. Esses livros devem ser priorizados conforme o desenvolvimento avançar.

---

## ✅ 7. Pontos Positivos do GDD

É importante registrar o que está **bem feito**:

1. **Coesão geral:** O GDD é notavelmente coeso para um documento desta escala. Os sistemas se conectam de forma orgânica (Ciclo de Tempo → NPCs → Economia → Combate → Narrativa).
2. **Escalabilidade faseada:** A divisão em Fases (Mesa → Digital Estático → Digital Tático → Multiplayer) é bem planejada e cada fase adiciona complexidade sem quebrar a anterior.
3. **Filosofia Data-Driven:** A separação Motor/Conteúdo está bem articulada nos Schemas e no Apêndice A.
4. **12 Classes Tier 1 completas:** Todas as classes possuem habilidades, equipamentos, PV, proficiências e descrições narrativas detalhadas.
5. **Ato 1 bem integrado:** O Relógio da Ruptura, a rivalidade IA, e a sinergia com mini-campanhas criam uma experiência não-linear de qualidade.
6. **Sistema de NPCs robusto:** A integração dos conceitos da Gemini 8 (Necessidades, Traits, Utility AI, Fofoca) no Cap. 8 é profissional.
7. **Atlas do Eco:** O mapa de conexões com custos de tempo e regras de terreno por zona é um excelente documento de referência.

---

## 📊 Resumo de Ações Tomadas

| # | Ação | Tipo | Status |
|:---|:---|:---|:---:|
| 1 | Harmonizar tabela de CD do Cap. 4 com Cap. 2/9 | Correção Crítica | ✅ |
| 2 | Corrigir referência "Capítulo 9" → "Capítulo 7" no Cap. 4 | Correção | ✅ |
| 3 | Corrigir "Inteligência" → "Conhecimento" no Ato 1 | Correção | ✅ |
| 4 | Adicionar seção de Esquecimento ao Cap. 8.3 | Adição | ✅ |
| 5 | Definir slots de habilidades herdadas (estilo FFT) | Recomendação | ✅ |
| 6 | Definir pré-requisitos multi-class para Tiers 2/3 | Recomendação | ✅ |
| 7 | Criar Reaction Abilities por classe | Recomendação | 📝 |
| 8 | Detalhar habilidades de Tier 2/3 | Recomendação | 📝 |
| 9 | Definir mecânica de troca de Origem | Recomendação | ✅ |
| 10 | Definir sistema de XP e progressão de nível | Recomendação | ✅ |
| 11 | Reduzir sobreposição Cap. 5 vs Cap. 8 | Recomendação | ✅ |
| 12 | Harmonizar fórmula de Defesa Base (Cap. 2 = Cap. 9) | Correção | ✅ |

---

> **Conclusão:** O GDD de *Eras do Brasil* é um documento **sólido e coeso**, com poucos erros críticos. As inconsistências encontradas foram corrigidas, e as recomendações apontam caminhos para aprofundamento que enriquecerão o sistema de classes (inspiração FFT), a progressão do personagem e a formalização de mecânicas que já estão conceitualmente presentes mas ainda não formalizadas.
