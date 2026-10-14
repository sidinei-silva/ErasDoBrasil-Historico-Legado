# Memória do Project do Claude — Projeto Outland

Resumo e arquivos de memória que o Claude mantinha para este Project (export de 14/10/2026). É texto gerado pelo Claude a partir das conversas, não documento escrito pelo Sidinei.

## Resumo do Project

**Purpose & context**

Sidinei is a developer building a portfolio project — an idle MMO game mechanically inspired by Albion Online, developed in Go with net/http+Chi routing, SQLite via sqlc, and JSON-driven static content. The project serves multiple purposes: learning, portfolio building, and exploring original game IP. A partner is involved in the effort, though there are no deadline pressures.

The project has evolved significantly in both name and direction. It began as "Albion Idle" with placeholder names drawn directly from Albion Online (zone names, mob names, Destiny Board terminology). After a legal/IP review, Sidinei decided to replace all Albion-derived naming before any public distribution and to establish original IP from the start — so that the full commit history, including the evolution from Albion-inspired to original content, can be made public as part of his portfolio narrative.

The game design direction has settled on **"Deuses-Armas"** — a multi-mythology fantasy concept where gods, losing followers, materialize as weapons. This was chosen over "Eras do Brasil" (his Brazilian colonial eco-fantasy MMORPG IP) because: Eras do Brasil cannot logically exist as a spinoff of something not yet launched, releasing it first risks diminishing the flagship's impact, and the god-as-weapon concept maps elegantly onto Albion's core "you are what you wear" mechanic.

**Current state**

The project is in active design and early development. Nine mechanical anchors are fixed and non-negotiable:
1. Gear-defines-identity
2. Tier system
3. Abilities from equipment
4. Auto-battler with skill queue
5. Destiny Board equivalent
6. Zone-defines-action
7. PoC scope as island tutorial
8. JSON-driven content
9. Server-authoritative combat

Narrative decisions are developed but remain open to revision through the brainstorm process. Key established narrative elements:
- Power comes from being remembered through use, not formal worship
- Weapon tier determines the degree of divine domination over the wielder (creating progression-loop narrative tension)
- Each god governs an entire weapon category, not a single item
- "O Silêncio" — a simultaneous collapse event triggering all pantheons — serves as the world-opening premise, with monsters growing stronger as gods weaken
- Isekai framing was considered and set aside in favor of a survival-based opening (isekai deemed equally saturated as a trope)

A multi-AI brainstorm workflow has been set up, with Claude, Gemini, and ChatGPT/Codex operating as VS Code agents reading a shared local workspace. A complete file structure was generated: debate rules, project context, fixed decisions, current narrative state, a shared chat log, a decisions folder for ADRs, and orchestration prompts. Sidinei participates as `[SIDINEI]` with equal standing to propose ideas and cast deciding votes.

**On the horizon**

- Completing the narrative and world-building layer through the multi-AI brainstorm process
- Replacing all remaining Albion-derived naming with original IP
- Validating the core gameplay loop via a PoC scoped to a tutorial island equivalent
- Eventual public release of the full commit history as portfolio artifact

**Key learnings & principles**

- Game mechanics (gather-craft-equip-fame-tree loops) are not copyrightable; specific names, branding, and lore text are protected — the practical line is mechanics vs. expression
- Establishing original IP from the start is preferable to retrofitting it, especially when the commit history will be public
- The idle mechanic and full-loot PvP tension is the core unresolved design risk; scope must be conservative (Albion at original launch, not current state)
- Economy systems like a Black Market require player mass — not viable at PoC scale
- Art production scope is a significant constraint to plan around
- PoC should validate the core loop before any full-engine commitment

**Approach & patterns**

- Sidinei prefers direct, honest feedback with zero flattery; wants debate that surfaces contradictions rather than validation
- Design decisions are layered: fixed mechanical anchors are locked, narrative decisions remain open and iterative
- Multi-AI workflow is used deliberately — Claude for design analysis and architecture decisions, mid-tier models (Sonnet, Gemini Flash) for daily coding, Gemini as a second opinion (noted as tending toward optimism on critical design risks)
- PoC-first philosophy: validate assumptions before committing to stack or scope
- Scope is referenced against Albion Online's original launch state, not its current evolved form

**Tools & resources**

- **Backend:** Go, net/http + Chi routing, SQLite via sqlc
- **Content:** JSON-driven static game data
- **PoC frontend (planned):** Vite + TypeScript; REST (not WebSocket) for PoC phase
- **AI tooling:** Claude (architecture/design), Gemini via API in Copilot, ChatGPT/Codex — all as VS Code agents on a shared local workspace
- **Workflow artifacts:** Shared markdown workspace with debate rules, context docs, fixed decisions doc, narrative state tracker, ADR folder, and orchestration prompts

## Arquivo de memória `/index.md` (atualizado 2026-09-08)

---
name: "Projeto Outland"
description: Projeto Outland — Go-based idle MMO portfolio project "Deuses-Armas" — gods materialize as weapons.
---

## Arquivo de memória `/overview.md` (atualizado 2026-09-08)

---
name: overview
description: Idle MMO portfolio project (Deuses-Armas) — purpose, stack, fixed mechanical anchors, narrative direction, and current state
sources: [backfill]
aliases: [Deuses-Armas, Albion Idle, idle MMO]
---
- [stated] Sidinei is a developer building an idle MMO game as a portfolio project, mechanically inspired by Albion Online
- [stated] Project serves three purposes: learning, portfolio building, and exploring original game IP
- [stated] A partner is involved in the effort; there are no deadline pressures
- [stated] Backend: Go with net/http + Chi routing, SQLite via sqlc
- [stated] Game content is JSON-driven static data
- [stated] Planned PoC frontend: Vite + TypeScript, using REST (not WebSocket) for the PoC phase

## Fixed mechanical anchors (locked, non-negotiable)
- [stated] 1. Gear-defines-identity
- [stated] 2. Tier system
- [stated] 3. Abilities from equipment
- [stated] 4. Auto-battler with skill queue
- [stated] 5. Destiny Board equivalent
- [stated] 6. Zone-defines-action
- [stated] 7. PoC scope as island tutorial
- [stated] 8. JSON-driven content
- [stated] 9. Server-authoritative combat

## Narrative direction: "Deuses-Armas"
- [stated] Concept is multi-mythology fantasy: gods, losing followers, materialize as weapons
- [stated] Narrative decisions are developed but remain open to revision through the brainstorm process (unlike the locked mechanical anchors)
- [stated] Power comes from being remembered through use, not formal worship
- [stated] Weapon tier determines the degree of divine domination over the wielder, creating progression-loop narrative tension
- [stated] Each god governs an entire weapon category, not a single item
- [stated] "O Silêncio" — a simultaneous collapse event triggering all pantheons — is the world-opening premise, with monsters growing stronger as gods weaken
- [stated] Isekai framing was considered and set aside in favor of a survival-based opening; isekai deemed equally saturated as a trope

## Background & evolution
- [stated] Project began as "Albion Idle" with placeholder names drawn directly from Albion Online (zone names, mob names, Destiny Board terminology)
- [stated] After a legal/IP review, Sidinei decided to replace all Albion-derived naming before any public distribution and establish original IP from the start
- [stated] Goal is to make the full commit history public — including the evolution from Albion-inspired to original content — as part of his portfolio narrative
- [stated] "Deuses-Armas" was chosen over "Eras do Brasil" (his Brazilian colonial eco-fantasy MMORPG IP) because: Eras do Brasil cannot logically exist as a spinoff of something not yet launched, releasing it first risks diminishing the flagship's impact, and the god-as-weapon concept maps elegantly onto Albion's "you are what you wear" mechanic

## Current state
- [stated] Project is in active design and early development
- [stated] Multi-AI brainstorm workflow has been set up and a complete file structure generated: debate rules, project context, fixed decisions, current narrative state, shared chat log, decisions folder for ADRs, and orchestration prompts

## On the horizon
- [stated] Completing the narrative and world-building layer through the multi-AI brainstorm process
- [stated] Replacing all remaining Albion-derived naming with original IP
- [stated] Validating the core gameplay loop via a PoC scoped to a tutorial island equivalent
- [stated] Eventual public release of the full commit history as a portfolio artifact

## Arquivo de memória `/ways-of-working.md` (atualizado 2026-09-08)

---
name: ways-of-working
description: How Sidinei runs this project — multi-AI brainstorm workflow, decision layering, PoC-first philosophy, and design learnings
sources: [backfill]
aliases: [brainstorm workflow, multi-AI workflow]
---
## Collaboration & feedback
- [stated] Sidinei prefers direct, honest feedback with zero flattery; wants debate that surfaces contradictions rather than validation
- [stated] Participates in the brainstorm as `[SIDINEI]`, with equal standing to propose ideas and cast deciding votes

## Multi-AI brainstorm workflow
- [stated] Claude, Gemini, and ChatGPT/Codex operate as VS Code agents reading a shared local workspace
- [stated] Claude is used for design analysis and architecture decisions
- [stated] Mid-tier models (Sonnet, Gemini Flash) are used for daily coding
- [stated] Gemini serves as a second opinion; noted as tending toward optimism on critical design risks
- [stated] Gemini is accessed via API in Copilot
- [stated] Workflow artifacts: shared markdown workspace with debate rules, context docs, a fixed-decisions doc, a narrative state tracker, an ADR folder, and orchestration prompts

## Decision-making patterns
- [stated] Design decisions are layered: fixed mechanical anchors are locked; narrative decisions remain open and iterative
- [stated] PoC-first philosophy: validate assumptions before committing to stack or scope
- [stated] Scope is referenced against Albion Online's original launch state, not its current evolved form

## Key learnings & principles
- [stated] Game mechanics (gather-craft-equip-fame-tree loops) are not copyrightable; specific names, branding, and lore text are protected — the practical line is mechanics vs. expression
- [stated] Establishing original IP from the start is preferable to retrofitting it, especially when the commit history will be public
- [stated] The idle mechanic and full-loot PvP tension is the core unresolved design risk; scope must stay conservative
- [stated] Economy systems like a Black Market require player mass — not viable at PoC scale
- [stated] Art production scope is a significant constraint to plan around
- [stated] PoC should validate the core loop before any full-engine commitment
