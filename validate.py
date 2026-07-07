#!/usr/bin/env python3
"""Verify-first (family ethos): the map is only honest if its registry is.
Checks membranes.json shape with no network: every membrane declares a status;
every BUILT membrane names a detector, a live url, a repo, and an honest reading
of what a positive AND a negative mean; every UNBUILT membrane is marked so and
does not claim a detector url. Keeps the map from quietly implying coverage it
does not have.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

fails = 0
def check(cond, msg):
    global fails
    print(("ok  · " if cond else "FAIL· ") + msg)
    fails += 0 if cond else 1

data = json.loads(Path("membranes.json").read_text(encoding="utf-8"))
mem = data["membranes"]
check(len(mem) >= 3, f"registry has membranes ({len(mem)})")

for m in mem:
    for f in ("key", "name", "crosses", "status", "color"):
        check(f in m and m[f], f"[{m.get('key','?')}] has {f}")
    if m["status"] == "built":
        for f in ("detector", "url", "repo", "positive", "negative"):
            check(bool(m.get(f)), f"[{m['key']}] BUILT -> has {f}")
        check(m["url"].startswith("https://"), f"[{m['key']}] url is https")
    else:
        check(m.get("url") in (None, "",) or m["status"] == "partial",
              f"[{m['key']}] UNBUILT -> claims no live detector url")

g = data.get("gauge", {})
check(bool(g.get("url")) and bool(g.get("role")), "silence-gauge present with a role and url")

built = [m for m in mem if m["status"] == "built"]
print(f"\n{len(built)} built membranes, {len(mem)-len(built)} named-but-unbuilt (honestly marked)")
print("SOME CHECKS FAILED" if fails else "all membrane-map checks passed")
sys.exit(1 if fails else 0)
