# Data Vaults in Plain Language
## What this is
Data vaults are a modeling approach that separates core entities (hubs), their relationships (links), and descriptive details over time (satellites). It is built to capture history and change without constant remodels.
## Why it matters for collections and cultural heritage data
Collections data often changes as records are corrected or enriched. A data vault keeps every version and link visible, which supports origin-and-changes tracking, audit trails, and reproducible research.
## A simple mental model
- Analogy 1: A data vault is like an accession log that records every object, every relationship (loan, exhibition), and every note over time in separate, stable ledgers.
- Analogy 2: Hubs are the stable object IDs, links are the loan or exhibit ties, satellites are the evolving descriptions or rights notes attached to those objects.
## A concrete example (mini case study)
Mini case study: A museum has objects (hubs), exhibits and loans (links), and descriptive metadata that changes (satellites). Instead of overwriting records, each description update is a new satellite row with a timestamp. Researchers can see how a description or rights note evolved, and the system never loses history when an exhibit relationship changes.
## How this shows up in this workshop
- When you keep original and cleaned values side by side, you are thinking like a vault (never losing history).
- Run record notes captured in Day 02 flows and Day 03 validation echo the vault goal: track change rather than overwrite.
- Publishing in Day 04 benefits from vault thinking because you can cite exactly what changed and when.
## What “successful understanding” looks like
- You can name hubs (stable IDs), links (relationships), and satellites (changing details) in your data.
- You know why keeping history matters for trust and reproducibility.
- You can explain when to avoid overwriting fields and instead add a new record with a timestamp.
- You can describe how vault ideas map to your current table structures, even if you do not build a full vault.
## Common misconceptions (and the gentle correction)
- Misconception: “Vaults are only for banks.” Correction: Vaults suit any domain where history matters, including collections.
- Misconception: “Vaults are too complex.” Correction: You can borrow the idea of hubs/links/satellites without using every pattern; start by not overwriting values.
- Misconception: “Vault means no curation.” Correction: You still curate; you retain each version and capture when changes happened.
## Practical decision guide
- If history and auditability are critical, then structure data so original and updated values both remain.
- If relationships change often (loans, exhibits), then log them as separate link records with dates.
- If descriptions or rights frequently update, then store them as timestamped satellite rows instead of overwriting.
- If storage is tight and changes are rare, then log only major versions but still avoid silent overwrites.
- If you are building repeatable movement, then include timestamps and source markers to mimic vault traceability.
## Troubleshooting and where people get stuck
- Problem: Overwriting values loses history. Fix: add effective dates and keep old records; mark the latest version separately.
- Problem: Hard to query changing relationships. Fix: store relationships as dated link records; filter by date for current state.
- Problem: Too many satellite versions. Fix: set retention rules (e.g., keep key milestones) and document them.
- Problem: Confusion about current vs. historical values. Fix: flag current records and keep timestamps visible; document in your data dictionary.
- Problem: Linking across systems with different IDs. Fix: use mapping tables as links; keep source IDs and timestamps.
- Problem: Performance concerns. Fix: index hub keys and dates; archive old versions if needed but never discard without policy.
## Quick glossary (local to this page)
- Hub: table of stable business keys (e.g., object IDs).
- Link: table capturing relationships between hubs (e.g., object-to-exhibit).
- Satellite: table holding descriptive attributes over time for hubs or links.
- Effective date: timestamp when a satellite record became valid.
- Business key: the stable identifier used to tie records together.
