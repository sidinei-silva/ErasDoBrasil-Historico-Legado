# Sessão 2026-02-13 — Decisões Técnicas: Organização Unity e Workflow UI/UX

**Data:** 2026-02-13
**Duração:** ~1 hora
**Objetivo:** Resolver dúvidas sobre organização do projeto Unity, separação POCs/jogo e planejamento de UI/UX

---

## 📋 Resumo

Antes de iniciar a Sprint 4 (Setup Unity), três dúvidas foram levantadas:

1. **Usar o mesmo projeto Unity para todas as POCs?**
2. **Como organizar código das POCs vs. projeto real?**
3. **Onde fica UI/UX, wireframes e prototipagem no roadmap?**

Foram criadas duas ADRs (Architecture Decision Records) e documentação técnica para resolver essas questões, além de atualizar todos os documentos de referência.

---

## ✅ Decisões Tomadas

### ADR-001: Organização do Projeto Unity
**Decisão:** Projeto Unity **único** para todas as POCs e o jogo final.
- Scripts organizados por **módulo funcional** (Core, Combat, World...), não por POC
- Cada POC tem sua **cena isolada** em `Scenes/POC/`
- O código é escrito para **produção desde o início** — não existe código descartável
- Namespaces C# seguem a estrutura: `ErasDoBrasil.Core`, `ErasDoBrasil.Combat`, etc.
- Integração no MVP é natural — os scripts já estão no lugar certo

### ADR-002: Workflow de UI/UX
**Decisão:** Incorporar wireframes e prototipagem **dentro das sprints existentes**.
- **Sprint 4:** Wireframes de baixa fidelidade (HUD, Mapa, Cena, Combate)
- **Sprint 6:** Protótipo navegável antes de implementar POCs de UI
- **Sprint 7:** Validação de usabilidade durante o playtest do MVP
- O GDD já tem specs detalhadas de UI em `gdd/04_Design_Visual/` — elas servem como referência
- Ferramenta sugerida: Excalidraw (gratuito, versionável)

---

## 📄 Arquivos Criados
- `vibe/decisions/ADR-001-organizacao-projeto-unity.md`
- `vibe/decisions/ADR-002-workflow-ui-ux.md`
- `docs/tech/organizacao-projeto-unity.md`
- `docs/tech/workflow-ui-ux.md`
- `docs/tech/wireframes/.gitkeep`
- `vibe/sessions/2026-02-13_decisoes-unity-uiux.md` (este arquivo)

## 📝 Arquivos Modificados
- `docs/GUIA_RETOMADA.md` — Sprint 4 (org Unity + wireframes), Sprint 6 (protótipo UI), Sprint 7 (validação UX)
- `ROADMAP.md` — Referências para ADRs e docs técnicos
- `README.md` — Estrutura do repositório atualizada, novos docs na tabela
- `vibe/backlog.md` — Tarefas de wireframe e protótipo adicionadas
- `vibe/project-status.md` — Novas decisões e status de UI/UX

---

## 🎯 Estado Final

| Área | Status |
|------|--------|
| Organização Unity | ✅ Definida (ADR-001) |
| Workflow UI/UX | ✅ Definido (ADR-002) |
| Documentação | ✅ Atualizada (todos os docs de referência) |
| Sprint 4 | 📝 Atualizada com wireframes e organização |
| Sprint 6 | 📝 Atualizada com protótipo de UI |

---

## ➡️ Próximos Passos

1. **Sprint 3** — Livros Auxiliares (Habilidades, Itens, Proficiências, Bestiário)
2. **Sprint 4** — Setup Unity (projeto único) + POCs Fundação + Wireframes

---

**Mantido por:** @vibe-keeper
