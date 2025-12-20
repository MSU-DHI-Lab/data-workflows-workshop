# Documentation That Travels with Data (Plain Language)
## What this is
Documentation that travels with data includes README files, data dictionaries, provenance notes, and validation reports bundled alongside the data itself. It keeps meaning and context intact when files move between people or systems.
## Why it matters for collections and cultural heritage data
Collections data carries stories, rights, and sensitivities. When files leave your hands, good documentation prevents misuse, preserves provenance, and helps others interpret fields correctly. Without it, downstream users can misread fields or lose track of redactions and rights.
## A simple mental model
- Analogy 1: Documentation is like a gallery label that stays with an object even when it is loaned. It tells the story and handling instructions.
- Analogy 2: Documentation is like a field notebook that rides along with specimens. It explains where, when, and how items were collected.
## A concrete example (mini case study)
Mini case study: An archive shares a cleaned CSV and associated scans. They include a README describing the source system, a data dictionary defining each field, a provenance note about cleaning steps, and a validation report from Day 03 checks. A partner ingesting the files can see what changed, which rights tokens apply, and how to cite the dataset.
## How this shows up in this workshop
- Day 01–03 produce cleaning notes, operations JSON, and validation summaries you can place in the artifacts folder.
- Day 04 packages README, data dictionary, provenance, and validation reports inside the dataset bundle.
- CITATION.cff and license files are part of the traveling documentation for publishing.
## What “successful understanding” looks like
- You bundle data with README, data dictionary, provenance, and validation evidence.
- You keep rights and license information in the package, not in a separate email.
- You can hand the package to a partner and they can use it without asking basic field-meaning questions.
- You version your docs with the data so changes stay aligned.
## Common misconceptions (and the gentle correction)
- Misconception: “Docs live in a wiki elsewhere.” Correction: Keep a copy in the package so offline users have context.
- Misconception: “A schema alone is enough.” Correction: Schemas need human-friendly descriptions and provenance.
- Misconception: “Validation is only for coders.” Correction: Validation reports help non-technical stakeholders trust the data.
## Practical decision guide
- If sending data outside your team: include README, data dictionary, provenance, and validation report in the same folder.
- If fields are new or renamed: update the dictionary and note changes in provenance.
- If rights are sensitive: state rights tokens and license prominently in README and file-level notes.
- If you rerun a pipeline: version the docs and include date and tool versions.
- If storage is constrained: at minimum include README and data dictionary; link to the full package if needed.
## Troubleshooting and where people get stuck
- Problem: Docs out of sync with data. Fix: update docs whenever fields change; keep versions together.
- Problem: Missing provenance details. Fix: log cleaning steps and tools used; store the operations JSON or notes.
- Problem: Rights not visible. Fix: add rights tokens and license text to README and dictionary; label sensitive fields.
- Problem: Validation report missing. Fix: rerun checks and place the summary in the package.
- Problem: Recipients ask repeated questions. Fix: expand dictionary examples and add a short “how to read this data” section in README.
- Problem: Files scattered. Fix: bundle docs and data in a single zip or folder with clear names.
## Quick glossary (local to this page)
- README: A plain-language overview of the dataset, provenance, and reuse guidance.
- Data dictionary: A table describing each field, type, and allowed values.
- Provenance: The record of how data was sourced and cleaned.
- Validation report: Evidence from checks showing data quality status.
- License: Permissions for reuse.
