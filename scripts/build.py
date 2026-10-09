#!/usr/bin/env python3
"""Convenience wrapper: python3 scripts/build.py <demo.json> [-o out.html]"""
import runpy, sys
from pathlib import Path
sys.argv[0] = "build.py"
runpy.run_path(str(Path(__file__).resolve().parent.parent / "skill" / "demo-preflight" / "scripts" / "build.py"), run_name="__main__")
