# Memória do Project do Claude — A Escória (Outlander)

Resumo e arquivos de memória que o Claude mantinha para este Project (export de 14/10/2026). É texto gerado pelo Claude a partir das conversas, não documento escrito pelo Sidinei.

## Resumo do Project

**Purpose & context**

Sidinei is a fullstack senior developer working solo on two game projects:

- **A Escória** (also called *Outlander*): An idle MMORPG reimagining Albion Online's core philosophy for players without time for active engagement. This is the **active, priority project**. Key design pillars: idle means *presence-rewarded*, not offline-first; the Têmpera mechanic is the core differentiator; all content must be original (no third-party names, data, or assets).
- **Eras do Brasil**: A Brazilian folklore-based MMORPG with multiple pivots over several years. Currently **frozen**.

A Escória has gone through significant cleanup: eliminating Albion-derived content, establishing a placeholder system (`PH_*` naming), renaming systems to original Portuguese lore names (e.g., "Destiny Board" → "A Litania"), and producing foundational documents (GDD, dialogue files, narrative lore book).

**Current state**

- Active development is on A Escória / Outlander.
- A monorepo skeleton exists with specs, ADRs, a backlog of vertical slices, and a RECEITA.md methodology document.
- A full narrative lore book ("A Escória — Livro de Imersão") has been created in both Google Drive and Notion.
- Sidinei has committed to writing all specs, rules, and code himself; Claude's role is **teaching, reviewing, and creative content generation only** — not producing specs or architecture on Sidinei's behalf.
- Core identifiers follow Portuguese lore naming: `internal/litania/`, `go mod init escoria`.

**Key learnings & principles**

- **The documentation trap**: Sidinei self-identified a multi-year pattern of converting every difficulty into more documentation rather than code — outsourcing learning that needed to happen through execution. This is the primary anti-pattern to guard against.
- **Reverting under pressure**: Sidinei has a documented tendency to revert prior decisions when challenged, and has explicitly asked to be flagged when this happens. Claude should surface this pattern rather than accommodate reversals quietly.
- **Validation vs. challenge**: Sidinei wants to be challenged, not validated. Claude should push back on weak reasoning, fuzzy design logic, or scope creep.
- **Lightweight methodology**: Agreed framework uses GDD system files with prose + numbered testable rules (e.g., `R-TEM-03`), ephemeral specs that die after delivery, executable GIVEN/WHEN/THEN acceptance criteria, and append-only ADRs — deliberately avoiding over-ceremonious workflows.
- **Core verb discipline**: When designing mechanics, Sidinei prefers to do the intellectual work himself (drafting, iterating) and bring output to Claude for critique — not receive completed answers.

**Approach & patterns**

- **Development order**: Vertical slices ordered by user journey, not technical layer.
- **Session management**: New chats for distinct task clusters to preserve context quality.
- **Model selection**: Sonnet for day-to-day work; Opus for deep architectural decisions.
- **Spec lifecycle**: Specs are ephemeral — they serve a delivery and are retired. Rules in GDD system files are the durable source of truth; specs reference rule IDs rather than restating them.
- **Creative methodology**: When learning game design concepts (e.g., core verb identification), Sidinei prefers guiding questions and frameworks over direct answers, submitting drafts for critique.

**Tools & resources**

- **Notion** (via MCP): Primary GDD workspace. Key operational notes: `notion-update-page` with `old_str`/`new_str` requires exact string matching including whitespace — minor differences cause silent failures. Updating select property options orphans previously assigned pages; workaround is to immediately reassign affected pages after the operation.
- **Google Drive**: Hosts the narrative lore book.
- **Monorepo**: Established with Go (`go mod init escoria`), structured around lore-named internal packages.

## Arquivo de memória `/index.md` (atualizado 2026-09-08)

---
name: "A Escória (Outlander)"
description: A Escória (Outlander) — Solo development of A Escória (Outlander), an original idle MMORPG built in Go.
---

## Arquivo de memória `/overview.md` (atualizado 2026-09-08)

---
name: overview
description: A Escória (Outlander) idle MMORPG — purpose, design pillars, current state of active development, and the frozen Eras do Brasil project
sources: [backfill]
aliases: [A Escória, Outlander, Escória, Eras do Brasil]
---

- [stated] Sidinei is a fullstack senior developer working solo on two game projects
- [stated] A Escória (also called Outlander) is the active, priority project: an idle MMORPG reimagining Albion Online's core philosophy for players without time for active engagement
- [stated] Eras do Brasil is a Brazilian folklore-based MMORPG that went through multiple pivots over several years; currently frozen

## Design pillars (A Escória)

- [stated] Idle means presence-rewarded, not offline-first
- [stated] The Têmpera mechanic is the core differentiator
- [stated] All content must be original — no third-party names, data, or assets

## Cleanup and foundations completed

- [stated] Eliminated Albion-derived content
- [stated] Established a placeholder system using `PH_*` naming
- [stated] Renamed systems to original Portuguese lore names (e.g., "Destiny Board" → "A Litania")
- [stated] Produced foundational documents: GDD, dialogue files, narrative lore book

## Current state

- [stated] Active development is on A Escória / Outlander
- [stated] A monorepo skeleton exists with specs, ADRs, a backlog of vertical slices, and a RECEITA.md methodology document
- [stated] A full narrative lore book ("A Escória — Livro de Imersão") has been created in both Google Drive and Notion
- [stated] Sidinei has committed to writing all specs, rules, and code himself; Claude's role is teaching, reviewing, and creative content generation only — not producing specs or architecture on his behalf
- [stated] Core identifiers follow Portuguese lore naming: `internal/litania/`, `go mod init escoria`

## Arquivo de memória `/ways-of-working.md` (atualizado 2026-09-08)

---
name: ways-of-working
description: Methodology, learnings, collaboration patterns, and tooling notes (Notion MCP quirks, monorepo, model selection) for A Escória
sources: [backfill]
aliases: [RECEITA.md, methodology]
---

## Key learnings and principles

- [stated] The documentation trap: Sidinei self-identified a multi-year pattern of converting every difficulty into more documentation rather than code — outsourcing learning that needed to happen through execution; this is the primary anti-pattern to guard against
- [stated] Sidinei has a documented tendency to revert prior decisions when challenged, and has explicitly asked to be flagged when this happens rather than having reversals accommodated quietly
- [stated] Sidinei wants to be challenged, not validated — push back on weak reasoning, fuzzy design logic, or scope creep
- [stated] Lightweight methodology: GDD system files with prose plus numbered testable rules (e.g., `R-TEM-03`), ephemeral specs that die after delivery, executable GIVEN/WHEN/THEN acceptance criteria, and append-only ADRs — deliberately avoiding over-ceremonious workflows
- [stated] Core verb discipline: when designing mechanics, Sidinei prefers to do the intellectual work himself (drafting, iterating) and bring output for critique rather than receive completed answers

## Approach and patterns

- [stated] Development order: vertical slices ordered by user journey, not technical layer
- [stated] Session management: new chats for distinct task clusters to preserve context quality
- [stated] Model selection: Sonnet for day-to-day work; Opus for deep architectural decisions
- [stated] Spec lifecycle: specs are ephemeral — they serve a delivery and are retired; rules in GDD system files are the durable source of truth, and specs reference rule IDs rather than restating them
- [stated] Creative methodology: when learning game design concepts (e.g., core verb identification), Sidinei prefers guiding questions and frameworks over direct answers, submitting drafts for critique

## Tools and resources

- [stated] Notion (via MCP) is the primary GDD workspace
- [stated] Notion quirk: `notion-update-page` with `old_str`/`new_str` requires exact string matching including whitespace — minor differences cause silent failures
- [stated] Notion quirk: updating select property options orphans previously assigned pages; workaround is to immediately reassign affected pages after the operation
- [stated] Google Drive hosts the narrative lore book
- [stated] Monorepo established with Go (`go mod init escoria`), structured around lore-named internal packages
