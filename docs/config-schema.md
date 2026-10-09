# demo.json schema

`scripts/build.py` validates the required keys, phase tags, unique step ids, and that every video scene points at a real step.

```jsonc
{
  "name": "Acme · Contracts Demo",          // required: shown in the header, reports and bundles
  "slug": "acme-contracts",                 // required: file names (acme-contracts-screens.md, …)
  "storage_key": "preflight-acme-contracts",// browser save slot. NEVER change after first use.
  "date": "Thu Oct 15 · 1:00 ET",
  "tagline": "Contract Console · Dana's Monday",
  "sources": "acme-demo-script-v2.pdf",     // shown as "Built from …"
  "builder": "the demo builder",            // who fixes failures
  "golden_record": "Contract 00001234",     // required: read-only during the dry run
  "test_record_label": "Test contract",
  "persona": "Dana Diaz, Contracts Manager",
  "presenter": "", "presenter_title": "",   // shown on the movie's title slide
  "record_links": [ { "key": "golden", "label": "Golden contract" } ],  // sidebar paste-a-URL boxes; steps can use go:"golden"
  "extra_notes": [ { "kind": "info|warn", "title": "Heads-up:", "html": "…" } ],
  "reset": [ "Contract 00001234: Status back to Draft" ],   // listed in bundles and briefs
  "agent_rules": [ "Managed package X: configure around it" ],

  "phases": [                                // required
    { "name": "Phase 1 · Read-only checks", "tag": "safe",   // "safe" | "change"
      "steps": [
        { "id": "1.2",                       // PERMANENT: add 1.2a instead of renumbering
          "t": "Contract record: path + fields",
          "c": ["Click path, HTML ok: <b>labels</b>"],
          "e": ["Expected result with <b>specific values</b>"],
          "f": "If not: likely cause + what to tell the builder",
          "go": "golden",                    // optional quick-link chip (home|opps|dash|reports|setup|record_links key)
          "scene": 2, "tw": [1] }            // optional cheat-sheet scene + win tags
      ] }
  ],

  "video": {                                 // optional: enables 📸 shots, Preview and Make the movie
    "spec_title": "Acme Closes Contracts in Days, Not Weeks",
    "theme": "corporate", "engine": "auto",
    "wow": "One click from signed to active.",
    "title_slide": { "title": "…", "say": "…", "subtitle": "…" },
    "scenes": [                              // movie order. "_" ids are slides.
      { "id": "_intro", "title": "…", "card": "…", "say": "Narration…" },
      { "id": "1.2", "title": "The contract", "shot": "What to frame", "say": "Narration…" }
    ],
    "slides": { "_intro": { "layout": "value-overview", "title": "A Claim With a Verb", "bullets": ["…"] } },
    "live":   { "1.2": ["navigate: {ORG}/lightning/o/Contract/list", "click: \"Contract 00001234\"", "wait: 3"] }
  }
}
```

**Rules of thumb**

- **Don't invent expected values.** If the script doesn't say, write `Confirm with the builder: expected ___`.
- Anything that **changes data** goes in a `change` phase, which runs on the test record.
- Slide `layout` values follow autonomous-demo-recorder's archetypes: `title`, `value-overview`, `how-to-steps`, `cards`, `stat-tiles`, `quote`, `wrap`, …
- `live` actions use the recorder's verbs. Quoted strings are intents that resolve at record time with `--smart`, and `{ORG}` becomes the org URL from the sidebar.
