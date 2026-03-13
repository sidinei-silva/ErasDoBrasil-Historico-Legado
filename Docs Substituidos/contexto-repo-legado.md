# 📚 Contexto do Repositório Legado

**Repo:** [sidinei-silva/ErasDoBrasil-Historico-Legado](https://github.com/sidinei-silva/ErasDoBrasil-Historico-Legado)
**Propósito:** Arquivo morto com todo o histórico de conversas com IAs e versões antigas dos livros.
**Status:** Somente leitura — referência histórica.

---

## Estrutura

```
ErasDoBrasil-Historico-Legado/
├── Conversas GPT/              # Conversas originais com ChatGPT
│   ├── RPG Eras do Brasil_convertido.md           (~1.2MB — conversa principal)
│   ├── Setor Livro de Regras e Sistema_convertido.md (~1.3MB)
│   ├── Setor de Arte_convertido.md                 (~34KB)
│   ├── Setor Enredo Narrativa_convertido.md        (~27KB)
│   ├── Setor Missões e Eventos_convertido.md       (~8KB)
│   ├── Setores para Desenvolvimento Eras_convertido.md (~6KB)
│   └── converter.py                                # Script de conversão HTML→MD
│
├── Chats Gemini/               # Conversas com Gemini (~20+ arquivos)
│   ├── gemini-conversation (1).md a (24).md        # Sessões de refinamento
│   └── eras-do-brasil-atividades.html              # Exportação de atividades
│
├── Livros Antigos/             # Versões originais dos livros (pré-auditoria)
│   ├── Livro de Regras.md      (~189KB — versão monolítica)
│   ├── Livro de Classes.md     (~101KB)
│   ├── Enredo Principal.md     (~43KB)
│   ├── Documento de Design Visual.md
│   ├── Checklist – Livro de Regras.md
│   └── ideias soltas.md        # Brainstorm original
│
└── Analise Notebook/           # Análises feitas com NotebookLM
    ├── Briefing Document.md                        # Resumo executivo do projeto
    ├── Project Plan.md                             # Plano de projeto gerado
    ├── Relatório de Auditoria de Projeto.md        # Auditoria independente
    ├── Relatório de Auditoria de Design.md         # Decisões Gemini integradas
    ├── Relatório de Evolução de Design.md          # Evolução do design ao longo do tempo
    ├── Analise fatias do livro/                    # Análises por capítulo
    ├── NotebookLM Mind Map.png                     # Mapa mental visual
    └── Eras_do_Brasil__Revivência.m4a              # Podcast gerado pelo NotebookLM
```

---

## O que foi migrado para o repo principal

Todos os livros foram reescritos e organizados em capítulos separados no repo `eras-do-brasil`:

| Livro Antigo | → | Estrutura Atual |
|-------------|---|-----------------|
| Livro de Regras.md (monolítico) | → | `gdd/01_Livro_de_Regras/` (9 capítulos + 3B) |
| Livro de Classes.md | → | `gdd/02_Livro_de_Classes/` (4 docs + 3 pastas de origem) |
| Enredo Principal.md | → | `gdd/03_Enredo_e_Mundo/` (3 docs + mini-campanhas) |
| Design Visual.md | → | `gdd/04_Design_Visual/` (6 documentos) |

## Decisões históricas importantes

As conversas Gemini revelam a evolução de decisões-chave:

1. **MMORPG → Coop P2P:** Decisão de reduzir escopo de MMO para cooperativo (sistema de Ticks + NPC IA incompatível com servidores massivos)
2. **D&D → Sistema D20 próprio:** Inspirado em D&D mas com atributos e progressão customizados
3. **Combate Estático → Grid:** Decisão de fases (Fase 1: static, Fase 2: grid isométrico)
4. **3 Origens:** Colonizador, Indígena, Folclórico — representam os 3 pilares da cultura brasileira
5. **Dom da Revivência:** Mecânica central que permite trocar de classe (diferencial do jogo)
6. **5 Atos:** Estrutura narrativa completa planejada, MVP foca no Ato 1

---

## Quando consultar o repo legado

- **Para entender "por que" uma decisão foi tomada** — as conversas Gemini contêm debates detalhados
- **Para recuperar conteúdo que possa ter sido perdido** na migração
- **Para referência histórica** sobre a evolução do design
- **NÃO usar como source of truth** — o repo `eras-do-brasil` é a verdade atual

---

*Este documento existe para que qualquer agente ou o próprio desenvolvedor saiba o que há no repo legado sem precisar navegar nele.*
