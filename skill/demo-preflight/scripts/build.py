#!/usr/bin/env python3
"""Build a demo-preflight page from a demo.json config.

Usage:
  python3 skill/demo-preflight/scripts/build.py examples/lakeshore-pm/demo.json            # -> lakeshore-pm-preflight.html
  python3 skill/demo-preflight/scripts/build.py my-demo.json -o out/my-demo-preflight.html

The output is one self-contained HTML file (no network, no install). Open it in a browser.
"""
import argparse, json, re, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL / "assets" / "preflight-template.html"
MARK = "/*__CONFIG_JSON__*/{}"
REQUIRED = ["name", "slug", "golden_record", "phases"]

def validate(cfg):
    errs = [f"missing required key: {k}" for k in REQUIRED if k not in cfg]
    seen = set()
    for p in cfg.get("phases", []):
        if p.get("tag") not in ("safe", "change"):
            errs.append(f"phase '{p.get('name')}': tag must be 'safe' or 'change'")
        for s in p.get("steps", []):
            sid = s.get("id")
            if not sid: errs.append(f"phase '{p.get('name')}': a step has no id")
            if sid in seen: errs.append(f"duplicate step id {sid} (ids are permanent; never renumber)")
            seen.add(sid)
            for k in ("t", "c", "e"):
                if k not in s: errs.append(f"step {sid}: missing '{k}'")
    for v in cfg.get("video", {}).get("scenes", []):
        if not v["id"].startswith("_") and v["id"] not in seen:
            errs.append(f"video scene '{v['id']}' doesn't match any step id")
        if v["id"].startswith("_") and v["id"] not in cfg.get("video", {}).get("slides", {}):
            errs.append(f"video scene '{v['id']}' is a slide but has no entry in video.slides")
    return errs

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("config"); ap.add_argument("-o", "--output")
    a = ap.parse_args()
    cfg = json.loads(Path(a.config).read_text())
    errs = validate(cfg)
    if errs:
        print("Config problems:\n  - " + "\n  - ".join(errs)); sys.exit(1)
    cfg.setdefault("storage_key", f"preflight-{cfg['slug']}")
    tpl = TEMPLATE.read_text()
    assert MARK in tpl, "template is missing the config marker"
    js = json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")
    out = Path(a.output or f"{cfg['slug']}-preflight.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(tpl.replace(MARK, js, 1))
    n = sum(len(p["steps"]) for p in cfg["phases"])
    print(f"✓ {out}  ({n} steps, {len(cfg.get('video',{}).get('scenes',[]))} video scenes, storage key '{cfg['storage_key']}')")

if __name__ == "__main__":
    main()
