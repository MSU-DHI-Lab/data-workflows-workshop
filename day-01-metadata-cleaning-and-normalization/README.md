# Day 01: Metadata Cleaning and Normalization for Reuse

Welcome. This mini-repo is the Day 01 box from the full workshop. You will clean messy metadata, normalize key fields, and capture a repeatable recipe others can trust. Everything here is already battle-tested from a live run.

## What you'll learn and produce
- How to use OpenRefine facets to see patterns before changing anything.
- How to normalize rights, places, and creator strings without losing meaning.
- How to export an operations JSON that makes your cleaning reproducible.
- How to run a light validation pass in Colab to confirm the cleaned file is ready to hand off.

## Timebox
- Lab 01 (Inspect with facets): ~15 minutes
- Lab 02 (Clean + normalize + export recipe): ~30 minutes
- Lab 03 (Validate basics): ~20 minutes

If you have only 30 minutes, do Lab 01 and the first half of Lab 02 to capture the operations JSON; validation can happen later.

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

## If you're short on time
- Read the Primer.
- Run Lab 01 to spot issues.
- In Lab 02, apply the provided operations JSON and export a cleaned CSV.
- Skim Lab 03 to see the validation checks you should run before sharing.
