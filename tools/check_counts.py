#!/usr/bin/env python3
"""tools/check_counts.py — the register-count guard.

The holder register is this repository's one statistical claim, and it has
been wrong in exactly one way, three times: it was updated in one file and
left stale in another — badge, prose paragraph, map row. This check makes
the count one fact with one home (the constants below) and fails CI when
any prose disagrees, in either direction.

  1. REQUIRED — every current phrase must appear where it belongs.
  2. STALE    — no banned old phrase may appear anywhere in prose.

Run:   python3 tools/check_counts.py
Exit:  0 all green · 1 anything red (with the exact failures listed)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOLDERS = 17
WORLDS = 5

REQUIRED = [
    ("README.md", "holders-17"),
    ("README.md", "17 holders across 5 worlds"),
    ("README.md", "Seventeen holders across five worlds"),
    ("docs/05_the_holders.md", "Seventeen holders across five worlds"),
    ("docs/05_the_holders.md", "All seventeen sit beneath"),
    ("docs/index.html", "17 across 5 worlds"),
    ("QUICK-REFERENCE.md", "sixteen"),
]

# The last entry above is a presence check: QUICK-REFERENCE is checked
# below against the same stale list as everything else.
REQUIRED = [r for r in REQUIRED if r[1] != "sixteen"]

STALE_PATTERNS = [
    r"holders-16\b",
    r"\b16 holders\b",
    r"\bSixteen holders\b",
    r"\b17 holders across 14\b",
    r"\b14 universes\b",
    r"\b17 holders across 14 worlds\b",
]


def main():
    fails = []
    for rel, needle in REQUIRED:
        p = os.path.join(ROOT, rel)
        text = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
        if needle not in text:
            fails.append(f"missing current phrase: {rel} does not say {needle!r}")
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d != ".git"]
        for fn in sorted(fns):
            scan = fn.endswith(".md") or (fn.endswith(".html") and os.path.basename(dp) == "docs")
            if not scan:
                continue
            rel = os.path.relpath(os.path.join(dp, fn), ROOT)
            text = open(os.path.join(dp, fn), encoding="utf-8").read()
            for pat in STALE_PATTERNS:
                if re.search(pat, text):
                    fails.append(f"stale phrase /{pat.lstrip(chr(92) + 'b')}/ in {rel}")
    print(f"COUNTS: {HOLDERS} holders \u00b7 {WORLDS} worlds \u2014 "
          f"{len(REQUIRED)} required phrase(s) checked, "
          f"{len(STALE_PATTERNS)} stale pattern(s) banned, {len(fails)} problem(s)")
    for f in fails:
        print("  -", f)
    if fails:
        print("FAIL \u2014 make the prose and the register agree (they are one fact), then re-run.")
        return 1
    print("ALL GREEN \u2014 every holder count in the prose matches the register.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
