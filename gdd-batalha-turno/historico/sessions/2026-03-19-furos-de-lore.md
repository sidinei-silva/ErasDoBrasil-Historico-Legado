# Session Log — 2026-03-19 — Furos de Lore

**Branch:** `furos-lore-2026-03-19`
**Objetivo:** Resolver 9 furos de lore identificados no BACKLOG.md

---

## Furos Resolvidos

### Furo 1 — Dom da Revivência: troca de classe vs troca de origem
- **Decisão:** Troca de classe (dentro da mesma origem) disponível desde o início. Troca de origem requer Espelho do Eco (desbloqueado no fim do Ato 1).
- **Arquivos:** `01_Ato_1_A_Primeira_Ruptura.md`, `03_Criacao_de_Personagem.md`

### Furo 2 — Causa canônica da Ruptura de 1497
- **Decisão:** Ritual Folclórico fracassado na Raiz do Mundo causou o colapso parcial.
- **Arquivos:** `00_Conceitos_Centrais_do_Mundo.md` (nova seção §2.1), `01_Ato_1_A_Primeira_Ruptura.md`
- **TODO:** Definir nome e identidade do Folclórico que liderou o ritual.

### Furo 3 — Motivação Folclórica no Ato 1
- **Decisão:** Folclóricos divididos em Restauradores (fechar a Ruptura) e Fatalistas (usar o caos).
- **Arquivos:** `00_Conceitos_Centrais_do_Mundo.md` (nova subseção), `01_Ato_1_A_Primeira_Ruptura.md`
- **TODO:** Alinhar as 6 mini-campanhas Folclóricas com a divisão Restauradores/Fatalistas.

### Furo 4 — Mana vs Fadiga Espiritual
- **Decisão:** Mana removida. Fadiga Espiritual é o limitador de magia (independente da Fadiga Física).
- **Arquivos:** `07_Magia_e_Espiritualidade.md` (nova seção formal), `03_Livro_de_Itens_e_Equipamentos.md`, `01_Atlas_do_Eco_Ato1.md`, `03_Dados_Iniciais_Ato1.md`, `01_Ato_1_A_Primeira_Ruptura.md`
- **Detalhes:** Chá de Erva-Lua agora "Reduz 1 nível de Fadiga Espiritual". Níveis de fadiga com efeitos progressivos definidos.

### Furo 5 — Dano Espiritual como tipo oficial
- **Decisão:** Dano Espiritual adicionado à tabela de tipos de dano. Ignora armadura, resistência via Sabedoria Ancestral.
- **Arquivos:** `04_Sistema_de_Combate.md` (nova seção "Tipos de Dano")
- **Detalhes:** Tabela inclui Corte, Perfurante, Contundente, Espiritual, Elemental, Veneno. "Exaustão Espiritual" padronizado para "Fadiga Espiritual".

### Furo 6 — Contradição Tier 2/3
- **Decisão:** Fonte de verdade é `01_Tiers_e_Evolucao.md` (Tier 2 = Nível 5, Tier 3 = Nível 10).
- **Arquivos:** `03B_Progressao_e_Experiencia.md`
- **Detalhes:** Tabela XP corrigida (Tier 2 começava no nível 6, agora nível 5; Tier 3 começava no 11, agora 10). Texto de benefícios alinhado.

### Furo 7 — Guardião da Fenda
- **Decisão:** Guardião é manifestação defensiva da Raiz do Mundo, não vilão. Ataca por instinto de proteção.
- **Arquivos:** `01_Ato_1_A_Primeira_Ruptura.md` (Sessão 4), `03_Livro_de_Itens_e_Equipamentos.md` (zona da Ruptura)
- **TODO:** Definir stats completos do Guardião (PV, Defesa, ações de combate, loot).

### Furo 8 — Sanidade/Moral removida
- **Decisão:** Sistema removido. Substituído por teste de Resistência contra Medo (Presença CD 13).
- **Arquivos:** `01_Atlas_do_Eco_Ato1.md`, `Game_Pitch.md`

### Furo 9 — Ecoera removida
- **Decisão:** Conceito removido por não estar definido no lore canônico.
- **Arquivos:** `Indigena_04_O_Sabio_que_Viu_o_Amanha.md`
- **Detalhes:** Referência substituída por "era futura alternativa através da Raiz do Mundo".

---

## Verificação Final

Greps executados confirmando que não restam ocorrências órfãs de:
- "Mana" (como recurso de jogo) — limpo
- "Sanidade" (como mecânica) — limpo (apenas no BACKLOG como resolvido)
- "Ecoera" — limpo (apenas no BACKLOG como resolvido)
- "Exaustão Espiritual" — limpo (apenas no BACKLOG como resolvido)
- "latente" / "Dom ativo" — limpo (apenas no BACKLOG como resolvido)

---

## TODOs Gerados

1. `<!-- TODO: definir nome e identidade do Folclórico que liderou o ritual -->` — em `00_Conceitos_Centrais_do_Mundo.md`
2. `<!-- TODO: alinhar as 6 mini-campanhas Folclóricas com a divisão Restauradores/Fatalistas -->` — em `00_Conceitos_Centrais_do_Mundo.md`
3. `<!-- TODO: definir stats completos do Guardião da Fenda (PV, Defesa, ações de combate, loot) -->` — em `01_Ato_1_A_Primeira_Ruptura.md`

---

## Commits (branch `furos-lore-2026-03-19`)

1. `fix(lore): distinguir troca de classe vs troca de origem (Furo 1)`
2. `fix(lore): definir causa canonica da Ruptura de 1497 (Furo 2)`
3. `fix(lore): motivacao Folclorica — Restauradores vs Fatalistas (Furo 3)`
4. `fix(lore): substituir Mana por Fadiga Espiritual em todo o GDD (Furo 4)`
5. `fix(lore): adicionar Dano Espiritual como tipo oficial de dano (Furo 5)`
6. `fix(lore): alinhar Tier 2/3 com fonte de verdade — Nível 5 e 10 (Furo 6)`
7. `fix(lore): definir identidade do Guardião da Fenda como protetor (Furo 7)`
8. `fix(lore): remover Sanidade/Moral, usar Resistência contra Medo (Furo 8)`
9. `fix(lore): remover conceito Ecoera do GDD (Furo 9)`
10. `docs(meta): atualizar BACKLOG e criar session log furos-de-lore`
