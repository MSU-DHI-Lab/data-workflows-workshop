# Licensing for Datasets and Media (Plain Language)
## What this is
Licensing spells out how others can reuse your datasets and media. It is the permission slip that sets expectations for credit, sharing, and restrictions.
## Why it matters for collections and cultural heritage data
Collections data often mixes institutional records, donor constraints, and third-party media. A clear license reduces legal ambiguity and protects sensitive content while encouraging reuse where appropriate.
## A simple mental model
- Analogy 1: A license is like exhibit signage with rules for photography and handling. It tells visitors what is allowed.
- Analogy 2: A license is like loan paperwork that spells out conditions and attribution requirements.
## A concrete example (mini case study)
Mini case study: A library releases a metadata-only CSV under CC BY 4.0 so others can use and remix it with credit. The same collection has images with donor restrictions, so those files are marked “Rights Reserved” and kept separate. The README lists both, preventing accidental misuse.
## How this shows up in this workshop
- Day 04 asks you to pick a license, record it in README, LICENSE, CITATION.cff, and .zenodo.json.
- Rights tokens are normalized in Day 01–03 to keep publishing choices clear.
- The publishing checklist reminds you to align license text and metadata.
## What “successful understanding” looks like
- You can choose a license that matches data sensitivity and reuse goals.
- You can keep different licenses clear when data and media differ.
- You can state the license consistently across README, LICENSE file, and metadata.
- You can explain why a specific license (e.g., CC BY for metadata) fits the release.
## Common misconceptions (and the gentle correction)
- Misconception: “Any open license works.” Correction: Choose the least restrictive license that fits the data; sensitive content may need stricter terms.
- Misconception: “Metadata is always public domain.” Correction: Institutional policies vary; make an explicit choice and document it.
- Misconception: “One license covers everything.” Correction: Different assets (metadata, images, code) may need separate terms; document them clearly.
## Practical decision guide
- If metadata only and low risk: consider CC0 or CC BY.
- If attribution is important but sharing is encouraged: CC BY 4.0.
- If sensitive media exists: separate it and mark “Rights Reserved” or a stricter license.
- If third-party content is included: keep it out of the open package or note separate terms.
- If unsure: consult institutional policy and pick the least restrictive license that fits.
## Troubleshooting and where people get stuck
- Problem: License text missing. Fix: include a LICENSE file and repeat the license in README and metadata.
- Problem: Mixed assets with different terms. Fix: document each asset type’s license in README; separate folders by license when possible.
- Problem: Inconsistent license across files. Fix: ensure LICENSE, CITATION.cff, .zenodo.json, and README match.
- Problem: Downstream users ignore terms. Fix: place license notices in prominent files and in the data package docs.
- Problem: Unsure about donor restrictions. Fix: pause publishing; clarify with rights holders; document decisions in provenance.
- Problem: Confusion between rights token and license. Fix: rights tokens describe reuse status; the license formalizes permissions. Keep both explicit.
## Quick glossary (local to this page)
- License: A legal permission statement defining reuse terms.
- CC BY: Creative Commons Attribution license; requires credit.
- CC0: Public domain dedication; no restrictions.
- Rights Reserved: A catch-all for content not licensed for open reuse.
- Metadata: Descriptive information about objects (fields like title, creator, date).
