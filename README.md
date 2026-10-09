# demo-preflight

**Rehearse your Salesforce demo before it's live.**

A Claude skill. Give Claude your demo script and it builds a click-by-click **dry-run page**. Mark each step pass or fail, paste screenshots as you go, hand the failures to a coding agent with fix suggestions, and turn the same run into a **narrated demo movie**.

**[⬇ Download demo-preflight.skill](https://github.com/RussEvans222/demo-preflight/releases/latest/download/demo-preflight.skill)** · works in **Claude Cowork** and **Claude Code**

```
demo script ─► Claude (demo-preflight) ─► dry-run page ─► pass / fail / notes / screenshots
                                                               │
                         ┌─────────────────────────────────────┼─────────────────────────────┐
                         ▼                                     ▼                             ▼
               📦 Agent hand-off                      ✨ AI fix suggestions           🎬 Make the movie
          fix brief + labeled PNGs                 cause · fix · done-when         narrated .mp4 via
          (Mesh, Claude Code, a teammate)                                           autonomous-demo-recorder
```

---

## Install (about a minute)

**Claude Cowork**
1. [Download `demo-preflight.skill`](https://github.com/RussEvans222/demo-preflight/releases/latest/download/demo-preflight.skill).
2. Drop it into a Cowork chat, say **"install this skill"**, and click **Save skill**.
3. Start a **new** session. Skills load when a session starts.

**Claude Code**
```bash
mkdir -p ~/.claude/skills && unzip -o ~/Downloads/demo-preflight.skill -d ~/.claude/skills/
```
Or ask Claude Code: *"Unzip ~/Downloads/demo-preflight.skill into ~/.claude/skills/."*

**Updating:** install the newer `.skill` the same way and it replaces the old one. Your saved dry-run notes live in your browser and aren't affected.

> Have the older **demo-dry-run** skill? Turn it off so Claude doesn't pick it instead.

## Use it

Attach your demo script (PDF, doc or pasted text) and say:

> **Use the demo-preflight skill to preflight this demo.** The demo record is `<golden record>` and my spare test record is `<test record>`.

Claude pulls every click path and expected value from your script and gives you a single `<demo>-preflight.html`. Open it next to your org and work top to bottom.

## What's in the page

| | Feature | What it does |
|---|---|---|
| ✓ | **Dry run** | Phased steps: setup → read-only checks → actions → AI → cleanup. Each step has **Click / You should see / If not**, Pass · Fail · Skip and notes. |
| 🛡 | **Golden-record safety** | Read-only checks run on the demo record. Anything that changes data runs on a spare test record, in demo order. Cleanup steps restore the starting state. |
| 📸 | **Screenshots** | Click a step and press **⌘V**, or drag an image in. *Tip: ⌘⇧⌃4 copies a screenshot straight to the clipboard.* |
| 🎬 | **Video shots** | Steps that are movie scenes show what to frame and the line they'll narrate. A meter tracks your coverage, and **Recording mode** fades out everything else. |
| ✨ | **Suggest fixes (AI)** | Every failure gets a likely cause, a fix and a "done when" check. It runs on Claude when hosted as a Cowork artifact; otherwise it gives you a copy-and-paste prompt for any AI. |
| 📦 | **Agent hand-off** | `00-fix-brief.md`, `01-dryrun-report.json` and **one labeled PNG per failed step**, all flat. Unzip, press **⌘A** and drag them into Mesh or Claude Code. |
| 🎬 | **Make the movie** | A bundle for autonomous-demo-recorder. Double-click `make-movie.command` and you get a narrated MP4 on your Desktop. |
| ▶ | **Preview** | A narrated slideshow in the browser, with `captions.srt` and `narration.json` exports. |
| ⬆ | **Import / export** | JSON report, HTML fix pack or hand-off files. Pick up on any machine, or share with a teammate. |
| 🔗 | **Org links** | Paste your org URL once to get one-click links to the right screen from each step. |

## Make the movie

1. Install Vaibhav Varshney's **[autonomous-demo-recorder](https://git.soma.salesforce.com/vvarshney/autonomous-demo-recorder)** once (Salesforce internal; see its README). On a Mac the built-in voice needs no key.
2. In your dry-run page, capture the 📸 shots, then click **🎬 Make the movie**.
3. Unzip the bundle and **double-click `make-movie.command`**. If macOS blocks it, right-click → Open. It finds the recorder, installs anything missing, renders `~/Desktop/<demo>-screens.mp4` and opens it.

The bundle has two specs in the recorder's own format, both lint-clean:

| Spec | Records | Needs |
|---|---|---|
| `<demo>-screens.md` | Branded intro and close slides, plus your screenshots as narrated image slides | Nothing: no org, no login |
| `<demo>-live.md` | The same story, driving the live org | A logged-in session, and `bash make-movie.command live` (uses `--smart`) |

## Hand fixes to a coding agent

Click **📦 Agent hand-off**, unzip, press **⌘A** and drag everything into your agent, then add any decisions it needs. The brief tells the agent:

- work only the fix list, in order;
- the presenter's notes win over the script;
- never change the golden record (except to restore it);
- make subscriber-side changes only, never managed-package metadata;
- reply as a table: step · what changed · how it was verified · blocked.

## Privacy

- Notes and screenshots stay in **your browser's local storage**. Nothing is uploaded unless you export it.
- Bundles and hand-offs **never include org credentials**.
- Use demo personas and placeholder IDs in anything you share outside the deal team. **Don't commit customer data to this repo:** `.gitignore` excludes reports, fix packs, bundles, screenshots and `private/`.

---

## For contributors

```
skill/demo-preflight/              ← the skill (this folder is what's packaged as demo-preflight.skill)
  SKILL.md                         how Claude authors demo.json and builds the page
  assets/preflight-template.html   the page: one template, all demo content comes from demo.json
  scripts/build.py                 demo.json → <slug>-preflight.html (validates ids, phases, scenes)
  reference/config-schema.md       demo.json schema
scripts/build.py                   wrapper: run the build from the repo root
examples/lakeshore-pm/             fictional sample (31 steps, 17 movie scenes) + a built page to try
docs/config-schema.md
```

**Try the sample without installing anything:**
```bash
python3 scripts/build.py examples/lakeshore-pm/demo.json
open lakeshore-pm-preflight.html
```

**Ship a new version**
```bash
cd skill && zip -r ../demo-preflight.skill demo-preflight -x "*.DS_Store" && cd ..
gh release create v0.2.0 demo-preflight.skill --title "demo-preflight v0.2.0" --notes "What changed…"
```
Keep the asset name `demo-preflight.skill` so the download link always serves the newest version. Never change a demo's `storage_key` or renumber step ids: saved notes are keyed to them.

## Credits

- Built by **Russ Evans**, Solutions Engineer, Salesforce.
- Movie rendering by **autonomous-demo-recorder** (Vaibhav Varshney).
- Feedback, ideas and PRs welcome. Ping me on Slack.

See [CHANGELOG.md](CHANGELOG.md) for version history.
