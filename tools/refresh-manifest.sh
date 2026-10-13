#!/bin/sh
# Regenerate MANIFEST.sha256 — run from anywhere; writes the repo root's manifest.
#
# The discipline (see ../provenance/COPIES-AND-TWINS.md and the CI workflow):
#   any deliberate change to a tracked file is committed TOGETHER with the
#   refreshed manifest. CI fails otherwise — which is the point.
set -e
cd "$(dirname "$0")/.."
find . -type f ! -name "MANIFEST.sha256" ! -path "./.git/*" | sort | xargs sha256sum > MANIFEST.sha256
echo "MANIFEST refreshed: $(wc -l < MANIFEST.sha256) entries"
