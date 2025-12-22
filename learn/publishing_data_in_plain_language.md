# Publishing Data in Plain Language
## What this is
Publishing means preparing data with rights, origin-and-changes notes, documentation, and a stable reference so others can reuse and cite it. It goes beyond sharing a file by adding context and permissions inside the package.
## Why it matters for collections and cultural heritage data
Collections data can be sensitive and easily misunderstood. Publishing with care protects the institution, honors donor and rights agreements, and helps peers trust and cite your work accurately. Without clear publishing steps, people may misuse data or lose track of origin-and-changes context.
## A simple mental model
Think about packing a fragile item to mail to a friend. You add padding, include a note with handling tips, and write who to contact if something breaks. The box is more than the object; it carries instructions and credit. Publishing data should feel the same: the files travel with clear notes and permission signals.

Now picture sharing a photo album link with a short description of what is inside and how to credit the people in the photos. The point is not to drown anyone in paperwork. It is to stop others from guessing about reuse, context, or how to cite you. In this workshop you will practice that mindset in Day 04 by bundling README, dictionary, license, citation, and validation notes before you even consider depositing to Zenodo.
## A concrete example (mini case study)
Mini case study: A repository cleans a set of oral history metadata. They bundle the data, a README with rights and notes on what changed, a data dictionary, a validation report, and choose CC BY for the metadata. They deposit to Zenodo, mint a DOI, and record it in README and CITATION.cff. Partners can cite the exact version and understand reuse boundaries.
## How this shows up in this workshop
- Day 04 walks through packaging data, adding LICENSE and CITATION.cff, and preparing Zenodo metadata.
- Practice path: you bundle everything locally to rehearse without depositing.
- Live path: you can deposit to Zenodo and mint a DOI if you have an account.
## What “successful understanding” looks like
- You can list the required publishing files (README, dictionary, license, citation, metadata, validation report).
- You can state reuse terms clearly and consistently.
- You can record a DOI and version in README and CITATION.cff.
- You can explain why publishing differs from sharing a file without context.
- You can adjust the bundle for different asset types while keeping rights clear.
## Common misconceptions (and the gentle correction)
- Misconception: Publishing is only uploading. Correction: It requires documentation, rights clarity, and stable references.
- Misconception: One license fits all. Correction: Different assets may need different terms; document them separately.
- Misconception: Practice runs are wasted time. Correction: Dry runs reduce mistakes before a public release.
## Practical decision guide
- If you need a citable release, then prepare README, dictionary, LICENSE, CITATION.cff, validation report, and `.zenodo.json` (a structured text metadata file Zenodo can read).
- If you have no Zenodo account or are not ready, then run the practice path and keep the bundle in `05-deliverables/`.
- If sensitive data exists, then redact before bundling and state redactions and rights in README.
- If multiple asset types exist, then document each license and keep sensitive items separate.
- If you update data, then version the package, update CITATION.cff and README, and note changes.
## Troubleshooting and where people get stuck
- Problem: Inconsistent license info. Fix: align LICENSE, README, CITATION.cff, and the `.zenodo.json` file.
- Problem: Missing change notes. Fix: add notes describing the source and cleaning steps.
- Problem: DOI not recorded locally. Fix: add DOI to README and CITATION.cff and keep a copy in the package.
- Problem: Unclear contents. Fix: list files and purposes in README and include validation status.
- Problem: Hesitation to publish. Fix: use the practice path to test the bundle; get a peer review before a live deposit.
- Problem: Large files. Fix: check Zenodo limits, compress or split, and describe external files in README if excluded.
## Quick glossary (local to this page)
- Publishing bundle: the set of data and documentation prepared for reuse.
- DOI: persistent identifier for citation.
- CITATION.cff: citation file describing how to reference the dataset.
- License: permissions for reuse.
