#!/usr/bin/env python3
"""tools/check.py — the repository verifies itself.

Two guarantees, standard library only:

  1. MANIFEST — every tracked file's sha256 matches MANIFEST.sha256,
     and no tracked file is missing from the manifest.
  2. LINKS    — every relative markdown link resolves to a real file.

Run:   python3 tools/check.py
Exit:  0 all green · 1 anything red (with the exact failures listed)

After any deliberate change:  sh tools/refresh-manifest.sh  — then commit both together.
"""

import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "MANIFEST.sha256")


def tracked_files():
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d != ".git"]
        for fn in fns:
            rel = os.path.relpath(os.path.join(dp, fn), ROOT)
            if rel == "MANIFEST.sha256":
                continue
            out.append(rel)
    return sorted(out)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def check_manifest():
    fails = []
    if not os.path.exists(MANIFEST):
        return ["MANIFEST.sha256 not found — run tools/refresh-manifest.sh"]
    listed = {}
    for line in open(MANIFEST, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        digest, _, path = line.partition("  ")
        if path.startswith("./"):
            path = path[2:]
        listed[path] = digest
    actual = tracked_files()
    for rel in actual:
        if rel not in listed:
            fails.append(f"not in manifest: {rel}  (run tools/refresh-manifest.sh)")
        elif sha256(os.path.join(ROOT, rel)) != listed[rel]:
            fails.append(f"hash mismatch: {rel}  (file changed — refresh the manifest)")
    for rel in listed:
        if rel not in actual:
            fails.append(f"in manifest but missing on disk: {rel}")
    return fails


def check_links():
    fails = []
    checked = 0
    for rel in tracked_files():
        if not rel.endswith(".md"):
            continue
        p = os.path.join(ROOT, rel)
        text = re.sub(r"```.*?```", "", open(p, encoding="utf-8").read(), flags=re.S)
        for m in re.finditer(r"\]\(([^)]+)\)", text):
            t = m.group(1).strip()
            if t.startswith(("http://", "https://", "mailto:", "#")):
                continue
            t = t.split("#")[0]
            if not t:
                continue
            checked += 1
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), t))):
                fails.append(f"{rel} → {t}")
    return checked, fails


def main():
    m_fails = check_manifest()
    n_files = len(tracked_files())
    checked, l_fails = check_links()
    print(f"MANIFEST: {n_files} files checked, {len(m_fails)} problem(s)")
    for f in m_fails:
        print("  -", f)
    print(f"LINKS: {checked} relative links checked, {len(l_fails)} broken")
    for f in l_fails:
        print("  -", f)
    if m_fails or l_fails:
        print("FAIL — fix the list above, refresh the manifest, commit both together.")
        return 1
    print("ALL GREEN — the repository verifies against its own manifest and every relative link resolves.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
