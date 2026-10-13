# Provenance — copies, sources, and twins

*Every file in this repository, where it came from, and its hash. Plus the duplicates found
during assembly that were deliberately **not** propagated — the account's "one copy of one
thing" discipline, applied.*

**Assembly date:** 2026-10-13. **Method:** byte-preserving copy (`cp`, no edits) from the
working repositories; one extraction (Blue Silver, below). Hashes are SHA-256, first 16
characters. A full-hash manifest of this repository ships as
[`../MANIFEST.sha256`](../MANIFEST.sha256) — run `sha256sum -c MANIFEST.sha256` at the repo
root to verify every file.

---

## 1. Canonical copies

| In this repo | Copied from (source repo → path) | SHA-256 (16) |
|---|---|---|
| `canon/MASTER-FOUNDATION.md` | kit → `SL_ARCHIVE/Adaptation-Talent-Definitive-Master-Foundation.md` | `eaced0a52af1ca30` |
| `canon/LEVEL-FRAMEWORK.md` | kit → `adaptive_prodigy/library/adaptation_talent_framework.md` | `7d49f87ccf34d057` |
| `canon/GENESIS-CODEX-ADAPTIVE.md` | kit → `CODEX/GENESIS_CODEX_ADAPTIVE.md` | `49898ca407e19d4a` |
| `canon/STORYOS-ADAPTATION-FIREWALL.md` | kit → `adaptive_prodigy/library/STORYOS_ADAPTATION_FIREWALL.md` | `d535cf570cf53a1e` |
| `modules/blue-silver.md` | kit → `_archive/2026-09-30_park/blue_silver/ADAPTATION_TALENT.md` (module half only — see §2) | `4195136600766429` |
| `modules/lan-shen.md` | kit → `soul_land_new/bible/ADAPTATION_MODULE.md` | `2fb62d952e6b7313` |
| `modules/lan-shen-log.md` | kit → `soul_land_new/bible/ADAPTATION_LOG.md` | `674473aa266914a7` |
| `modules/lan-shen-audit-2026-09-15.md` | kit → `soul_land_new/foundation/ADAPTATION_AUDIT_2026-09-15.md` | `045f2cb257740433` |
| `modules/qian-xunji.md` | kit → `qian_xunji/foundation/ADAPTATION_TALENT_QIAN_XUNJI.md` | `55883ef274e1748d` |
| `modules/fire-dragon-lizard.md` | kit → `soul_land_1_fire_dragon_lizard/bible/ADAPTATION_TALENT.md` | `075afdc25d13481c` |
| `modules/devouring-dragon.md` | kit → `soul_land_devouring_dragon/bible/ADAPTATION_MODULE.md` | `a6f43862285a2f9f` |
| `modules/devouring-dragon-log.md` | kit → `soul_land_devouring_dragon/bible/ADAPTATION_LOG.md` | `f382511f16aff58d` |
| `modules/luo-chen-holy-spirit.md` | kit → `soul_land_holy_spirit/bible/ADAPTATION_HUMAN.md` | `f478a48994d1e606` |
| `modules/su-yan-one-in-a-thousand.md` | kit → `soul_land_3_oc/bible/ADAPTATION_MODULE.md` | `ff96d5e9342f648d` |
| `modules/silver-golden-wolf.md` | kit → `soul_land_3_new/foundation/ADAPTATION_TALENT_MODULE.md` | `368a3141cab31a09` |
| `modules/seed-of-creation.md` | kit → `seed_of_creation/bible/ADAPTATION_TALENT_MODULE.md` | `881ce4eae7a67540` |
| `modules/yan-shuo-fire-phoenix.md` | kit → `soul_land_4_fire_phoenix/bible/ADAPTATION_TALENT_LOCAL.md` | `bbef1c1366f51eeb` |
| `modules/lan-xuanyu-pressure-adaptation.md` | kit → `soul_land_4_fire_phoenix/bible/LAN_XUANYU_PRESSURE_ADAPTATION.md` | `883a121c57fee883` |
| `modules/zhou-xu-dragon-prince-yuan.md` | kit → `dragon_prince_yuan_native_oc_fanfiction/bible/OC_ADAPTATION_TALENT.md` | `4e452a4582ed2df8` |
| `modules/mark-stark-heir-study.md` | **stark_heir** → `foundation/ADAPTATION_TALENT_STUDY.md` | `20f5171b685f281e` |
| `modules/eternal-oc-mcu.md` | **mcu-eternal-fanfic** → `bible/ADAPTATION_TALENT_LOCAL_MCU_ETERNAL.md` | `8d1bb17785be6e2d` |
| `practice/storyos-master-skill.md` | kit → `adaptive_prodigy/library/storyos_master_skill.md` | `339c992a8c6a860c` |
| `practice/storyos-master-skill-v3-universal.md` | kit → `adaptive_prodigy/library/storyos_master_skill_v3_UNIVERSAL.md` | `afdf9c82b19bd445` |
| `practice/storyos-system-index.md` | kit → `adaptive_prodigy/library/storyos_system_index.md` | `ecf9c7701ee51304` |
| `practice/naagin-s1-control-book.md` | kit → `adaptive_prodigy/library/StoryOS-Naagin-S1-Control-Book.md` | `eea640ae7280f68e` |
| `practice/lessons-absorbed.md` | kit → `adaptive_prodigy/library/LESSONS_ABSORBED.md` | `66e0b952798d4f77` |
| `practice/storyos-master-skill-ultimate.md` | kit → `adaptive_prodigy/library/STORYOS_MASTER_SKILL_ULTIMATE.md` | `eb8e9a4680ad21c9` |
| `practice/storyos-toolkit.md` | kit → `adaptive_prodigy/library/storyos_toolkit.md` | `f4cc820901a89c1e` |

("kit" = the `soul-land-universal-kit` working repository.)

**Copied files hash-match their sources.** For the module set, the copied file's hash equals
the source file's hash (spot-verified across the set); no content was edited in transit.

## 2. The one extraction: the Blue Silver single-file

The single file `_archive/2026-09-30_park/blue_silver/ADAPTATION_TALENT.md`
(full-file SHA-256 `d77b9c7aaed4655f`) had two halves:

1. **The universal core, verbatim** — Master Foundation v2.0. Its bytes there are
   **identical** to `SL_ARCHIVE/Adaptation-Talent-Definitive-Master-Foundation.md`
   (`eaced0a52af1ca30`) and to `stark_heir/reference/talent_master_v2.md`.
2. **The serial module** ("MODULE — Blue Silver (Soul Land) holder…", M1–M6) — unique to
   that file.

This repo keeps the universal core **once** (`canon/MASTER-FOUNDATION.md`) and the module
once (`modules/blue-silver.md`, extracted verbatim from the M1 header to end-of-file, with
a 4-line provenance comment prepended). Nothing was dropped; one duplicated universal copy
was not propagated. The original file remains untouched in the kit's archive.

## 3. Twins and duplicates found — deliberately not propagated

| Duplicate | Hash | Identical to | Where it remains |
|---|---|---|---|
| kit `adaptive_prodigy/library/Adaptation-Talent-Definitive-Master-Foundation-1.md` | `eaced0a52af1ca30` | `canon/MASTER-FOUNDATION.md` | kit (library index cites it as supplementary depth) |
| kit `adaptive_prodigy/library/GENESIS_CODEX_ADAPTIVE.md` | `49898ca407e19d4a` | `canon/GENESIS-CODEX-ADAPTIVE.md` | kit |
| **stark_heir** `reference/talent_master_v2.md` | `eaced0a52af1ca30` | `canon/MASTER-FOUNDATION.md` | stark_heir repo (it is that repo's working reference copy) |
| kit `_archive/…/blue_silver/ADAPTATION_TALENT.md` | `d77b9c7aaed4655f` | master half + blue-silver module | kit archive; module extracted to this repo (§2) |
| kit `SL_ARCHIVE/sl4_foundation_v2/bible/ADAPTATION_TALENT_LOCAL.md` | `87c29822a9a6b694` | **superseded** earlier version of the live Fire Phoenix module (`bbef1c1366f51eeb`) | kit archive |
| kit `SL_ARCHIVE/sl4_foundation_v2/bible/LAN_XUANYU_PRESSURE_ADAPTATION.md` and the `soul_land_4_fire_phoenix/audits/2026-09-13_*` before-snapshots | — | superseded audit-trail snapshots | kit audit trail (project history, not doctrine) |

Two files were found to be **byte-identical twins of the master inside the kit itself**
(the `-1.md` library copy and the codex twin); the third copy lives in stark_heir. All
three are recorded above so no future session re-discovers and re-imports them as if they
were new doctrine.

## 4. What was *not* treated as doctrine

Files that *mention* the Talent but are not its law — serial status panels, chapter texts,
canon ledgers, glossaries, battle plans — were **left in their home repositories**, where
they belong to their serials. This repository holds the doctrine family the serials point
at, not every file that contains the word "adaptation." For the same reason:

- **Lin Hao** (adaptive_prodigy) is excluded entirely: his martial soul is *named*
  Adaptation, and the account records that as an explicit divergence — not this Talent.
- **The Genesis Codex's Adaptation Core** is filed in `canon/` as the *sibling concept*
  it is, clearly labelled as adapting a document system, not a being.
- **IATS and IODS** appear only as the separated systems §5 requires them to be.

## 5. Current standing and the one-copy policy

- **This repository is the organized home of the doctrine family.** The working
  repositories (kit, stark_heir, mcu-eternal-fanfic) still carry their originals — untouched
  at assembly time.
- **A follow-up decision is open, by design:** whether the kit's talent files should become
  pointers to this repository (the account's one-copy law, applied across repos). Nothing
  was deleted anywhere; that pass is recorded as pending.
- **Verification:** full-hash manifest at [`../MANIFEST.sha256`](../MANIFEST.sha256);
  module-vs-source hash equality spot-verified at assembly.

---

*Assembled 2026-10-13 from the working repositories, byte-preserving. If a future session
moves any source file, update the paths here rather than deleting a row — provenance is a
ledger, not a snapshot.*

---

## Assembled for this repository (not byte copies)

Six files were **written for this repository** on 2026-10-13 rather than copied — no source
hash exists for them because this repo's public files are their only sources:

| In this repo | Assembled from | Discipline |
|---|---|---|
| `modules/evo-avengers.md` | `practice/storyos-master-skill*.md`, `practice/storyos-toolkit.md` (this repo), quoted verbatim | The serial's own `evo_status.md` / `evo_power_reference.md` are **not** among the account's public files — the module says so and leaves no gap filled by invention |
| `modules/sheshveer-naagin-s1.md` | `practice/naagin-s1-control-book.md` + `practice/storyos-system-index.md` (this repo), quoted verbatim | The project pack (41 locks) stays the serial's own foundation; the module lists the gates, it does not cross them |
| `modules/vihaan-naagin7.md` | `practice/storyos-system-index.md` rows (this repo) | Unawakened holder — written to register scope only |
| `docs/media/ten-orders.svg` · `docs/media/holders-map.svg` | Drawn for this repository (§48 Order map; holder census) | Self-contained SVG — no external assets |
| `docs/index.html` | Hand-written reader page for GitHub Pages | Links out to GitHub for the prose files |
