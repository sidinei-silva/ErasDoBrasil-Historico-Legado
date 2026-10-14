# Memória do Project do Claude — Eras do Brasil - Arquivado

Resumo e arquivos de memória que o Claude mantinha para este Project (export de 14/10/2026). É texto gerado pelo Claude a partir das conversas, não documento escrito pelo Sidinei.

## Resumo do Project

**Purpose & context**

Sidinei is a senior fullstack developer (primary background in PHP/Node/TS/JS with Go exposure) building **"Eras do Brasil"** — a text-based MMORPG/MUD set in colonial Brazil (1497) with folkloric and mystical elements. The project is a personal hobby (~6 hours/week) with full community transparency about development pace. It lives across two GitHub repos: `sidinei-silva/eras-do-brasil-gdd` (design/lore/docs) and `sidinei-silva/eras-do-brasil-game` (code), both synced to the Claude project knowledge base.

The game features: D20 combat resolution, Utility AI-driven NPCs with needs/schedules/routines, a gossip/knowledge system, persistent world simulation, crafting economy, seasonal narrative with permanent consequences, and a five-region world (Mata Costeira T1 through Coração da Raiz T5+). The server is written in Go with WebSocket communication and a web client.

**Core design pillars confirmed:** No full loot (ADR-009/010 removed it; death = XP% + durability% loss only), no PvP in MVP, no offline mode, no visible ticks (replaced by game clock and D20 turns for combat), seasons as 4-6+ month narrative arcs with a three-state finale machine (Tensão → Apogeu → Legado).

---

**Current state**

The project has completed refinements through **1.4 (POIs e Localização Validada de NPCs)**, merged to main. The active implementation phase is **1.5 (Sistema de Fofocas / KnowledgeBase)** — a gossip and knowledge system for NPCs using schema with 10 fields (`Type`, `EntityId`, `BlockId`, `PoiId`, `FirstSeenAt`, `LastSeenAt`, `SeenCount`, `LearnedAt`, `Source`, `Important`), single knowledge type `AVISTAMENTO_NPC` for this phase, expiration against `LastSeenAt`, sweep-based cleanup each tick.

A **two-phase empirical language test** (Go vs. Node.js, AI tools disabled, structured developer diary in Notion) was proposed and partially started. The Go phase was underway but interrupted. The test remains open and unresolved — it can resume without consequence.

An open **genre identity question** was raised in the most recent session: Sidinei explored pivoting toward a hybrid Modern MUD + idle/AFK auto-combat + ARPG loot loop (PoE/Diablo-inspired). Claude identified architectural incompatibilities with the existing D20 turn-based system, tensions with the "Living World" pillar if core gameplay moves to private instances, and economic risks from combining persistent markets with AFK farming without resets. The genuinely novel elements (D20 + Brazilian folklore + permanent narrative season consequences) were distinguished from established genre territory. A clarifying question remains open: **is the core fantasy strategic management, tactical adventure, or idle progression?**

Known technical debts carried forward: sleep effect wastes points when fatigue is already low (fixed delta vs. dynamic); Loneliness chronically high due to coarse zone granularity (resolves naturally with inter-block movement in a future refinement).

---

**On the horizon**

- Resolving the genre identity / core fantasy question before further architecture decisions
- Completing or resuming the Go vs. Node.js empirical test
- Refinement 1.6 (Itinerantes — traveling NPC type enabling inter-zone information flow); StoryManager deferred to Phase 3
- Admin God Mode dashboard (React + Vite + Tailwind mockup produced; pub/sub topic-based protocol recommended over full-snapshot broadcast for scalability)
- Inter-block NPC movement (deferred from 1.4, will resolve Loneliness granularity debt)
- An idle/hero-management game concept (inspired by Evil Hunter Tycoon, Melvor Idle) was documented separately and shelved — Sidinei chose to return focus to Eras do Brasil

---

**Key learnings & principles**

- **GDD as compass, not truth:** Implementation decisions informed by development reality take precedence when GDD is outdated. ADRs (Architecture Decision Records) are the authoritative source for resolved decisions.
- **Sequential game loop is non-negotiable:** EventBus with parallel manager goroutines is an anti-pattern for deterministic simulation. Correct architecture: single-threaded sequential loop (WorldManager → NPCManager → CombatManager → StoryManager → EconomyManager → PersistManager), goroutines only for I/O.
- **Scope inflation detection:** Recurring pattern of deferred features being smuggled into MVP under new nomenclature (e.g., sub-locais reframed as POIs, idle mechanics reframed as a different genre). Flag this directly when it appears.
- **Language doubt as proxy:** At least five distinct language-change debates occurred across two months. The root issue diagnosed is process/simulation-modeling confidence, not Go's paradigm. Changing languages would not resolve this.
- **AI delegation pattern:** Sidinei's firm policy of writing all code himself is sincere but has been inconsistently maintained in practice (full implementations delegated for maintenance tasks and some core features). The pattern is honest self-reflection after the fact. His prior analysis confirmed the overall pattern is healthy — he brings ideas, validates, catches AI errors using domain knowledge, and implements himself. If he raises concern about AI overuse, check this against the confirmed healthy pattern before validating the concern.
- **Starting a second project during ungratifying architectural phases** is a recognized solo developer procrastination pattern — flagged and resolved once already.
- **Simulation calibration method that works:** Describe the character/system in words → rank priorities → translate to numbers → run and observe → adjust based on behavioral symptoms. Do not give ready-made values.

---

**Approach & patterns**

- Works iteratively with **explicit refinement documents before coding**, using a fixed 10-section template (O que é, Referência no GDD, Decisões em aberto, Escopo entra, Escopo não entra, Critérios de aceite, Invariantes e edge cases, Como validar, O que destrava, O que ainda não resolve).
- Expects Claude to **audit the knowledge base before any design discussion**, surface contradictions directly, and recommend against scope inflation.
- **Prefers critical analysis over validation.** When reviewing code or ideas: identify flaws, contradictions, balance problems, and exploit risks first. If an idea is bad, say so and explain why. If good, confirm it but surface the risks. Never praise ideas to please.
- **Zero flattery.** Direct feedback including corrections is explicitly preferred. Responds well to data-based arguments even when conclusions are uncomfortable.
- Pattern of bringing previously deferred decisions back under new framing — recognize and flag this.
- Thinks in OOP/Node.js terms first, then translates to Go idioms, which produces friction. This is a known workflow artifact, not a signal to relitigate the language choice.
- **Real skill gap is simulation modeling** (calibration, emergent behavior, balancing) — this is new territory. Teaching method: help him think through the problem, not provide ready-made recipes. Pattern: describe in words → rank → translate to numbers → iterate and observe.
- Uses structured developer diary (Notion) for self-diagnosis during experimental phases.

---

**Tools & resources**

- **Languages/runtime:** Go (server), TypeScript/React (web client and admin dashboard)
- **Frontend tooling:** React + Vite + Tailwind (recommended for admin dashboard)
- **Repos:** `sidinei-silva/eras-do-brasil-gdd`, `sidinei-silva/eras-do-brasil-game` (synced to Claude project knowledge)
- **AI tools during dev:** Claude (design/lore/analysis/code review), GitHub Copilot (IDE autocomplete — counts as AI assistance for test validity purposes), prior Gemini consultations (evaluated critically; identified as producing defensible conclusions with flawed arguments)
- **Reference games:** Path of Exile, Diablo (loot loop), Evil Hunter Tycoon / Melvor Idle / Idlescape / Idle Clans (idle genre research), Dwarf Fortress / The Sims (admin dashboard UX inspiration)
- **Documentation:** Notion (developer diary), GDD repo as design source of truth, ADRs for architectural decisions

## Arquivo de memória `/index.md` (atualizado 2026-09-08)

---
name: "Eras do Brasil"
description: "Eras do Brasil — Eras do Brasil: a Go/WebSocket text-based MMORPG set in colonial Brazil with folkloric elements."
---

## Arquivo de memória `/overview.md` (atualizado 2026-09-08)

---
name: overview
description: Eras do Brasil — text-based MMORPG/MUD in colonial Brazil: purpose, design pillars, world/systems scope, tooling, and current implementation state (1.5 gossip system, open genre question)
sources: [backfill]
aliases: ["Eras do Brasil", "eras-do-brasil-game", "eras-do-brasil-gdd"]
---
- [stated] Sidinei is a senior fullstack developer; primary background in PHP/Node/TS/JS with Go exposure
- [stated] Building "Eras do Brasil" — a text-based MMORPG/MUD set in colonial Brazil (1497) with folkloric and mystical elements
- [stated] Personal hobby project, ~6 hours/week, with full community transparency about development pace
- [stated] Two GitHub repos, both synced to the Claude project knowledge base: `sidinei-silva/eras-do-brasil-gdd` (design/lore/docs) and `sidinei-silva/eras-do-brasil-game` (code)
- [stated] Server written in Go with WebSocket communication and a web client
- [stated] Game systems: D20 combat resolution, Utility AI-driven NPCs with needs/schedules/routines, gossip/knowledge system, persistent world simulation, crafting economy, seasonal narrative with permanent consequences
- [stated] Five-region world: Mata Costeira T1 through Coração da Raiz T5+

## Design pillars (confirmed)
- [stated] No full loot — ADR-009/010 removed it; death costs XP% + durability% only
- [stated] No PvP in MVP
- [stated] No offline mode
- [stated] No visible ticks — replaced by game clock and D20 turns for combat
- [stated] Seasons are 4-6+ month narrative arcs with a three-state finale machine (Tensão → Apogeu → Legado)

## Tools & resources
- [stated] Languages/runtime: Go (server), TypeScript/React (web client and admin dashboard)
- [stated] Frontend tooling: React + Vite + Tailwind (recommended for admin dashboard)
- [stated] AI tools during dev: Claude (design/lore/analysis/code review), GitHub Copilot (IDE autocomplete — counts as AI assistance for test-validity purposes), prior Gemini consultations (evaluated critically; identified as producing defensible conclusions with flawed arguments)
- [stated] Reference games: Path of Exile, Diablo (loot loop); Evil Hunter Tycoon / Melvor Idle / Idlescape / Idle Clans (idle genre research); Dwarf Fortress / The Sims (admin dashboard UX inspiration)
- [stated] Documentation: Notion (developer diary), GDD repo as design source of truth, ADRs for architectural decisions

## Current state (as of import — re-verify)
- [stated] Refinements complete through 1.4 (POIs e Localização Validada de NPCs), merged to main
- [stated] Active implementation phase: 1.5 (Sistema de Fofocas / KnowledgeBase) — gossip and knowledge system for NPCs
- [stated] 1.5 schema has 10 fields: `Type`, `EntityId`, `BlockId`, `PoiId`, `FirstSeenAt`, `LastSeenAt`, `SeenCount`, `LearnedAt`, `Source`, `Important`
- [stated] 1.5 uses a single knowledge type `AVISTAMENTO_NPC` for this phase; expiration checked against `LastSeenAt`; sweep-based cleanup each tick
- [stated] Two-phase empirical language test (Go vs. Node.js, AI tools disabled, structured developer diary in Notion) was proposed and partially started; Go phase was underway but interrupted — the test remains open and unresolved, and can resume without consequence
- [stated] Open genre identity question: Sidinei explored pivoting toward a hybrid Modern MUD + idle/AFK auto-combat + ARPG loot loop (PoE/Diablo-inspired)
- [stated] Claude's analysis of that pivot: architectural incompatibilities with the existing D20 turn-based system, tensions with the "Living World" pillar if core gameplay moves to private instances, economic risks from combining persistent markets with AFK farming without resets
- [stated] The genuinely novel elements were distinguished from established genre territory: D20 + Brazilian folklore + permanent narrative season consequences
- [stated] Clarifying question still open: is the core fantasy strategic management, tactical adventure, or idle progression?
- [stated] Technical debt: sleep effect wastes points when fatigue is already low (fixed delta vs. dynamic)
- [stated] Technical debt: Loneliness chronically high due to coarse zone granularity — resolves naturally with inter-block movement in a future refinement

## On the horizon
- [stated] Resolve the genre identity / core fantasy question before further architecture decisions
- [stated] Complete or resume the Go vs. Node.js empirical test
- [stated] Refinement 1.6 (Itinerantes — traveling NPC type enabling inter-zone information flow); StoryManager deferred to Phase 3
- [stated] Admin God Mode dashboard — React + Vite + Tailwind mockup produced; pub/sub topic-based protocol recommended over full-snapshot broadcast for scalability
- [stated] Inter-block NPC movement, deferred from 1.4 — will resolve the Loneliness granularity debt
- [stated] An idle/hero-management game concept (inspired by Evil Hunter Tycoon, Melvor Idle) was documented separately and shelved; Sidinei chose to return focus to Eras do Brasil

## Arquivo de memória `/ways-of-working.md` (atualizado 2026-09-08)

---
name: ways-of-working
description: How Sidinei works on Eras do Brasil — refinement-document workflow, expectations for Claude (critical analysis, KB audit, scope-inflation flagging), and durable architectural/process learnings
sources: [backfill]
aliases: []
---

## Workflow
- [stated] Works iteratively with explicit refinement documents before coding, using a fixed 10-section template: O que é, Referência no GDD, Decisões em aberto, Escopo entra, Escopo não entra, Critérios de aceite, Invariantes e edge cases, Como validar, O que destrava, O que ainda não resolve
- [stated] Uses a structured developer diary in Notion for self-diagnosis during experimental phases

## Expectations for Claude
- [stated] Audit the knowledge base before any design discussion; surface contradictions directly
- [stated] Recommend against scope inflation
- [stated] Prefers critical analysis over validation — when reviewing code or ideas, identify flaws, contradictions, balance problems, and exploit risks first; if an idea is bad, say so and explain why; if good, confirm it but surface the risks
- [stated] Zero flattery; direct feedback including corrections is explicitly preferred; responds well to data-based arguments even when conclusions are uncomfortable
- [stated] Teaching method for the simulation-modeling skill gap: help him think through the problem rather than provide ready-made recipes — describe in words → rank → translate to numbers → iterate and observe; do not give ready-made values

## Learnings & principles
- [stated] GDD as compass, not truth: implementation decisions informed by development reality take precedence when the GDD is outdated; ADRs are the authoritative source for resolved decisions
- [stated] Sequential game loop is non-negotiable: EventBus with parallel manager goroutines is an anti-pattern for deterministic simulation; correct architecture is a single-threaded sequential loop (WorldManager → NPCManager → CombatManager → StoryManager → EconomyManager → PersistManager), with goroutines only for I/O
- [stated] Scope-inflation detection: recurring pattern of deferred features being smuggled into MVP under new nomenclature (e.g. sub-locais reframed as POIs, idle mechanics reframed as a different genre) — flag this directly when it appears
- [stated] Pattern of bringing previously deferred decisions back under new framing — recognize and flag it
- [stated] Language doubt as proxy: at least five distinct language-change debates occurred across two months; root issue diagnosed as process/simulation-modeling confidence, not Go's paradigm — changing languages would not resolve it
- [stated] Thinks in OOP/Node.js terms first, then translates to Go idioms, which produces friction; a known workflow artifact, not a signal to relitigate the language choice
- [stated] Real skill gap is simulation modeling (calibration, emergent behavior, balancing) — new territory for him
- [stated] Simulation calibration method that works: describe the character/system in words → rank priorities → translate to numbers → run and observe → adjust based on behavioral symptoms
- [stated] AI delegation pattern: his firm policy of writing all code himself is sincere but has been inconsistently maintained in practice (full implementations delegated for maintenance tasks and some core features); the pattern is honest self-reflection after the fact
- [stated] His prior analysis confirmed the overall AI-use pattern is healthy — he brings ideas, validates, catches AI errors using domain knowledge, and implements himself; if he raises concern about AI overuse, check it against this confirmed healthy pattern before validating the concern
- [stated] Starting a second project during ungratifying architectural phases is a recognized solo-developer procrastination pattern — flagged and resolved once already
