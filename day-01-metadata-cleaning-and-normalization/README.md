# Day 01: Metadata Cleaning and Making Values Consistent for Reuse

Welcome. This day focuses on cleaning messy metadata, making key fields consistent, and capturing a repeatable recipe others can trust.

## What you'll learn and produce
- How to use OpenRefine facets to see patterns before changing anything.
- How to make rights, places, and creator strings consistent without losing meaning.
- How to export an OpenRefine operations file (a saved record of the cleaning steps) that makes your cleaning reproducible.
- How to run a light validation pass in Colab to confirm the cleaned file is ready to hand off.

## Suggested timing (so you can plan your session)
- Lab 01 (Inspect with facets): ~15 minutes
- Lab 02 (Clean + make values consistent + export recipe): ~30 minutes
- Lab 03 (Validate basics): ~20 minutes

If you have only 30 minutes, do Lab 01 and the first half of Lab 02 to capture the OpenRefine operations file; validation can happen later.

## Why these tools today
- **OpenRefine** keeps cleaning work transparent, lets you facet before changing values, and exports a sharable recipe so others can replay your steps.
- **Colab + Python** provide a quick, install-free way to sanity-check results with readable code and simple counts.

## Navigation
- Primer: `00-primer/concepts.md` and `00-primer/glossary_day.md`
- Labs: `01-labs/` (Lab 01, Lab 02, Lab 03)
- Job aids: `02-job-aids/`
- Assessments: `03-assessments/`
- Diagrams: `04-diagrams/`
- Artifacts drop zone: `05-artifacts/`

## What success looks like
- You can explain, in plain language, what you changed and why.
- You export a cleaned CSV and an OpenRefine operations file.
- Your cleaned file has consistent rights, place, and creator formats.
- A basic validation pass (Lab 03) runs and flags anything that still needs attention.

## Where people get stuck (and quick fixes)
- OpenRefine will not open: confirm address 3333 is free, then restart OpenRefine.
- Facets show unexpected blanks: clear filters and confirm the correct column is selected.
- You are worried about losing meaning: keep a short note explaining any normalization rule that collapses values.
- You are worried about losing meaning: keep a short note explaining any rule that collapses multiple values into one.
- Exports look different than expected: confirm you exported the current project view and used UTF-8.

## If you're short on time
- Read the Primer.
- Run Lab 01 to spot issues.
- In Lab 02, apply the provided operations file and export a cleaned CSV.
- Skim Lab 03 to see the validation checks you should run before sharing.
