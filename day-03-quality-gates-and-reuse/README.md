# Day 03: Quality Checks for Reuse

Welcome. Today we add trust signals to your data with lightweight, readable validation. You will profile a dataset, write Pandera checks, and produce a shareable report.

## Why quality checks today
- Cleaning fixes data; validation proves it meets expectations. You need both so surprises do not creep in later.
- Quality checks are kindness: they stop quiet failures before they reach colleagues and make your standards explicit.

## Why Pandera
- Declarative checks read like “rules of trust” instead of scattered if-statements.
- Validation rules live next to the data and can be versioned, replayed, and explained to non-coders.
- Great fit for Colab: installable in one line, runs in-browser, and outputs friendly error reports.

## What you'll do and produce
- Profile the dataset to see shape, missingness, and uniques.
- Define a Pandera set of validation rules (Python + Colab) that encodes 6–10 clear checks.
- Run validation against clean and intentionally bad data to see how failures are reported.
- Capture a markdown report and a reusable `validation_schema.py` file.

## Suggested timing (so you can plan your session)
- Lab 01 (first look at the data): ~15 minutes
- Lab 02 (write the checks): ~30 minutes
- Lab 03 (run checks and write a short report): ~20 minutes

## Navigation
- Primer: `00-primer/concepts.md`, `00-primer/glossary_day.md`
- Labs: `01-labs/`
- Job aids: `02-job-aids/`
- Assessments: `03-assessments/`
- Diagrams: `04-diagrams/`
- Files created: `05-artifacts/`

If you're short on time: run Lab 01 to understand the data, then Lab 02 with the provided rules file, and skim the Lab 03 report output to see how failures surface.

## What success looks like
- You can point to a small set of checks and explain what each one protects.
- Your validation run produces a readable pass/fail report.
- When you introduce a known-bad row, the checks fail in an understandable way.

## Where people get stuck (and quick fixes)
- Pandera will not import: rerun the install cell and restart the notebook runtime.
- A check fails unexpectedly: print failing rows and confirm whether the rule is correct or the data needs cleaning.
- Type issues: cast columns before validation or enable coercion in your rules.
- File not found: confirm the working directory and relative paths, or use Colab upload.
