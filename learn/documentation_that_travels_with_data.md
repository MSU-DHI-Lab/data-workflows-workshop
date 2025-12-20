# Documentation That Travels with Data (Plain Language)
## What this is
Documentation that travels with data includes README files, data dictionaries, origin-and-changes notes, and validation reports bundled alongside the data itself. It keeps meaning and context intact when files move between people or systems.
## Why it matters for collections and cultural heritage data
Collections data carries stories, rights, and sensitivities. When files leave your hands, good documentation prevents misuse, preserves origin-and-changes context, and helps others interpret fields correctly. Without it, downstream users can misread fields or lose track of redactions and rights.
## A simple mental model
Imagine buying a piece of furniture that arrives with no instructions. You could guess, but you would probably waste time or damage something. Documentation that travels with data is the instruction sheet taped inside the box: it tells you what each piece is, how it fits together, and how to care for it.

Now think about handing over your home Wi-Fi password to a guest. You might also share which network to pick and a reminder about a weak spot in the house. Those small notes go with the password so no one has to guess. The point is not to create busywork. It is to keep meaning, rights, and origin visible when the spreadsheet or images leave your server. In this workshop you will practice that habit every day: saving OpenRefine steps, writing validation summaries, and packaging README and dictionaries in Day 04.
## A concrete example (mini case study)
Mini case study: An archive shares a cleaned CSV and associated scans. They include a README describing the source system, a data dictionary defining each field, notes on what changed, and a validation report from Day 03 checks. A partner ingesting the files can see what changed, which rights tokens apply, and how to cite the dataset.
## How this shows up in this workshop
- Day 01–03 produce cleaning notes, an OpenRefine operations file (a saved record of the steps), and validation summaries you can place in the artifacts folder.
- Day 04 packages README, data dictionary, notes on what changed, and validation reports inside the dataset bundle.
- CITATION.cff and license files are part of the traveling documentation for publishing.
## What “successful understanding” looks like
- You bundle data with README, data dictionary, notes on what changed, and validation evidence.
- You keep rights and license information in the package, not in a separate email.
- You can hand the package to a partner and they can use it without asking basic field-meaning questions.
- You version your docs with the data so changes stay aligned.
## Common misconceptions (and the gentle correction)
- Misconception: “Docs live in a wiki elsewhere.” Correction: Keep a copy in the package so offline users have context.
- Misconception: “A table structure alone is enough.” Correction: Table structures still need human-friendly descriptions and origin-and-changes notes.
- Misconception: “Validation is only for coders.” Correction: Validation reports help non-technical colleagues trust the data.
## Practical decision guide
- If you are sending data outside your team, then include README, data dictionary, notes on what changed, and validation report in the same folder.
- If fields are new or renamed, then update the dictionary and note changes in your notes on what changed.
- If rights are sensitive, then state rights tokens and the license prominently in README and file-level notes.
- If you repeat the same steps later, then version the docs and include date and tool versions.
- If storage is constrained, then include at least a README and data dictionary; link to the full package if needed.
## Troubleshooting and where people get stuck
- Problem: Docs out of sync with data. Fix: update docs whenever fields change; keep versions together.
- Problem: Missing change details. Fix: log cleaning steps and tools used; store the OpenRefine operations file or notes.
- Problem: Rights not visible. Fix: add rights tokens and license text to README and dictionary; label sensitive fields.
- Problem: Validation report missing. Fix: rerun checks and place the summary in the package.
- Problem: Recipients ask repeated questions. Fix: expand dictionary examples and add a short “how to read this data” section in README.
- Problem: Files scattered. Fix: bundle docs and data in a single zip or folder with clear names.
## Quick glossary (local to this page)
- README: A plain-language overview of the dataset, notes on what changed, and reuse guidance.
- Data dictionary: A table describing each field, type, and allowed values.
- Validation report: Evidence from checks showing data quality status.
- License: Permissions for reuse.
