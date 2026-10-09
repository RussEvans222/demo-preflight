# Changelog

## 0.1.0 (Oct 2026)
- Config-driven template: one `demo.json` → one self-contained preflight page (`scripts/build.py`, with validation).
- Dry run: phased steps, golden-record vs test-record safety, Pass/Fail/Skip, notes, autosave, org and record quick links.
- Screenshots: paste with ⌘V, drag in, or Add image; a gallery in the summary.
- ✨ AI fix suggestions: in-page Claude when hosted as a Cowork artifact, copy-and-paste prompt otherwise.
- 📦 Agent hand-off: flat `00-fix-brief.md`, `01-dryrun-report.json` and one labeled PNG per failed step.
- 🎬 Make the movie: autonomous-demo-recorder bundle (screens and live specs, lint-clean) with `make-movie.command`.
- ▶ Preview: narrated in-browser slideshow, plus `narration.json` and `captions.srt`.
- Import: JSON report, HTML fix pack or hand-off zip contents.
- Claude Code light theme.
