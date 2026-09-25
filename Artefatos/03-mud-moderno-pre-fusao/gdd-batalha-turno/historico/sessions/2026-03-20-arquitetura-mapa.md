# Sessão de Design — Arquitetura do Mapa e Regiões

**Data:** 2026-03-20
**Tipo:** Sessão de design com Game Designer consultor
**Assunto:** Definição da arquitetura macro do mapa e das regiões do mundo

---

## Contexto

Sessão focada em estabelecer a estrutura do mundo persistente para suportar o crescimento por temporadas. O jogo precisava de uma lógica clara de como o mundo escala de uma única região (Ato 1) para um continente inteiro, mantendo coerência geográfica, de nível e narrativa.

---

## Decisões Aprovadas

### ✅ Decisão 1 — Mapa hierárquico em 3 camadas

O mundo é organizado em:
1. **Mapa-Múndi (Regiões):** Visão macro do Brasil colonial distorcido. Cada temporada abre 1-2 regiões.
2. **Mapa Regional (Zonas):** 8-15 zonas conectadas em grafo de nós. É o sistema de Blocos de Cenário já existente.
3. **Mapa Local (Sub-locais):** Expansão futura de zonas populosas. Não implementar no MVP.

### ✅ Decisão 2 — 5 regiões planejadas com gradiente de nível

O gradiente segue a lógica da Raiz do Mundo: quanto mais perto do centro do continente, maior a distorção, maior o nível.

| Região | Nível | Temporada |
|--------|-------|-----------|
| Mata Costeira | 1–5 | T1 |
| Sertão Distorcido | 5–10 | T2 |
| Serra dos Ecos | 10–15 | T3 |
| Pantanal Vivo | 15–20 | T4 |
| Coração da Raiz | 20+ | T5+ |

### ✅ Decisão 3 — Sub-locais ficam para Temporada 2+

MVP: cada zona é um nó único. Sem subdivisão interna de zonas. Isso simplifica a implementação inicial e evita trabalho prematuro.

### ✅ Decisão 4 — Só Mata Costeira tem zonas detalhadas agora

As outras 4 regiões existem como planejamento macro no GDD. Não geram trabalho de implementação neste momento.

### ✅ Decisão 5 — Regiões 2-5 documentadas como guia de design

Descrições de bioma, conflito, recursos e mobs temáticos registradas no GDD como referência futura para escritores e designers, sem comprometer o roadmap de desenvolvimento.

---

## Arquivos Modificados

| Arquivo | Tipo | Descrição da mudança |
|---------|------|---------------------|
| `gdd/01_Livro_de_Regras/05B_Arquitetura_do_Mapa.md` | **CRIADO** | Documento principal: 3 camadas, 5 regiões, migração de mobs, representação no cliente |
| `gdd/05_Livros_Auxiliares/01_Atlas_do_Eco_Ato1.md` | Editado | Nota de contexto no topo + seção 1B com tabela de zonas por nível |
| `gdd/01_Livro_de_Regras/05_Exploracao_e_Mundo.md` | Editado | Seção "Estrutura do Mundo: Camadas de Navegação" adicionada em §5.1 |
| `gdd/01_Livro_de_Regras/08_Mundo_Vivo_e_NPCs.md` | Editado | Referência ao gradiente de migração em §8.10 |
| `gdd/README.md` | Editado | Linha do 05B adicionada na tabela do Livro de Regras |
| `gdd/Game_Pitch.md` | Editado | Nota sobre 5 regiões após descrição da Mata Costeira |
| `gdd/99_Meta_e_Backlog/BACKLOG.md` | Editado | Tarefa de arquitetura de mapa marcada como concluída |

---

## TODOs registrados

- Seção de Sub-locais (Camada 3): implementar na Temporada 2 quando zonas populosas precisarem de expansão.
- Região 2 — Sertão Distorcido: detalhar zonas quando a Temporada 2 for planejada.
- Região 3 — Serra dos Ecos: detalhar zonas quando a Temporada 3 for planejada.
- Região 4 — Pantanal Vivo: detalhar zonas quando a Temporada 4 for planejada.
- Região 5 — Coração da Raiz: região inteira a definir quando Temporada 5+ for planejada.

---

## Próximos passos sugeridos

- Schemas JSON para `Region` e `RegionState` (análogo ao `Season` do backlog).
- Definir regras de desbloqueio de região: o que acontece no servidor quando uma nova temporada abre uma região.
- Bestiário: migração de mobs cross-região (dados concretos de como o sistema de §8.10 se aplica ao Sertão).
