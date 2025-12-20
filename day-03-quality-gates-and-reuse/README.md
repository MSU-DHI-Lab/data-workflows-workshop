# Day 03: Quality Gates and Reuse at Scale

Welcome. Today we add trust signals to your data with lightweight, readable validation. You will profile a dataset, write Pandera checks, and produce a shareable report. This is the same flow we used in the live run.

## Why quality gates today
- Cleaning fixes data; validation proves it meets expectations. You need both so surprises do not creep in later.
- Quality gates are kindness: they stop quiet failures before they reach colleagues and make your standards explicit.

## Why Pandera
- Declarative checks read like “rules of trust” instead of scattered if-statements.
- Schemas live next to the data and can be versioned, replayed, and explained to non-coders.
- Great fit for Colab: installable in one line, runs in-browser, and outputs friendly error reports.

## What you'll do and produce
- Profile the dataset to see shape, missingness, and uniques.
- Define a Pandera schema (Python + Colab) that encodes 6–10 clear checks.
- Run validation against clean and intentionally bad data to see how failures are reported.
- Capture a markdown report and a reusable `validation_schema.py` artifact.

## Timebox
- Lab 01 (profile / EDA): ~15 minutes
- Lab 02 (write quality gates): ~30 minutes
- Lab 03 (run report + failures): ~20 minutes

## Navigation
- Primer: `00-primer/concepts.md`, `00-primer/glossary_day.md`
- Labs: `01-labs/`
- Job aids: `02-job-aids/`
- Assessments: `03-assessments/`
- Diagrams: `04-diagrams/`
- Artifacts: `05-artifacts/`

If you're short on time: run Lab 01 to understand the data, then Lab 02 with the provided schema, and skim the Lab 03 report output to see how failures surface.
