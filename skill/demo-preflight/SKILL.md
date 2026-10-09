---
name: demo-preflight
description: Turn a Salesforce demo script (and optionally a presenter cheat sheet) into a demo-preflight page, a single self-contained HTML dry-run walkthrough. It has Pass/Fail/Skip per step, screenshot paste, AI fix suggestions, a flat agent hand-off (fix-brief.md, JSON and labeled PNGs) and a one-click narrated movie bundle for autonomous-demo-recorder. Use when someone wants to "do a dry run", "preflight the demo", "test the demo before the call", "QA the org", "hand failures to Mesh or Claude Code", or "make a demo video from the dry run". Not for writing the live talk track.
---

# demo-preflight

You author a **`demo.json`** from the user's demo script, then build the page with `scripts/build.py`. The template is in `assets/preflight-template.html`. Never hand-edit it per demo; everything demo-specific goes in `demo.json` (full schema: `reference/config-schema.md`).

## 1. Gather

- **The demo script** (PDF, doc or pasted text) is required. Pull every click path in order, and every **concrete expected value** (amounts, counts, statuses, names, dates).
- A **presenter cheat sheet**, if one exists. Map its scenes to `scene` numbers.
- **Golden record**: the record the demo shows. **Test record**: a spare record that mirrors it. Ask if neither is clear.
- **Builder**: who fixes failures (a person, Mesh, Claude Code).

## 2. Write demo.json

- **Phases:** 0 Setup (safe) → 1 Read-only checks on the golden record (safe) → 2 Action tests on the test record, in demo order (change) → 3 AI/agents with resets around them (change, or safe if look-only) → 4 Cleanup (safe). Aim for 20–35 steps.
- Each step needs `t`, `c` (clicks), `e` (expected) and `f` (if not). Split any step with more than about 4 expectations.
- **Don't invent values.** If the script is silent, write `Confirm with <builder>: expected ___`.
- Flag real-world side effects (emails, signatures, notifications): confirm the recipient is a test address first.
- **Step ids are permanent.** When updating an existing page, add new ids (`2.3a`) and keep the `storage_key`, or saved notes disappear.
- **Video** (optional, recommended): list `scenes` in script order. Use `_intro`/`_close` slides from `slides`, with archetype layouts and claim-style titles. Each scene gets a `say` line (1–3 sentences, contractions, no hype words) and a `shot` brief. `live` actions use autonomous-demo-recorder verbs with quoted intents and `{ORG}`.
- **No customer PII** in shared copies. Use personas and placeholder IDs.

## 3. Build and verify

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/build.py" demo.json -o <slug>-preflight.html
```

- The build validates required keys, phase tags, unique ids, and that scenes map to steps. Fix and re-run until it prints ✓.
- Open or screenshot the page. Check that phases render, the sidebar dots work and the toast shows on Pass.
- If autonomous-demo-recorder is available, check the movie bundle: `python3 <recorder>/scripts/record_demo.py <slug>-screens.md --lint` should report 0 errors.

## 4. Hand-off message (2–3 sentences)

Say which record to leave untouched, which test record to use, that everything autosaves in this browser, and that **📦 Agent hand-off** produces the files to drag into the builder's agent, while **🎬 Make the movie** produces the recorder bundle.
