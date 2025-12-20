# Day 02: Pipelines and Provenance with Apache NiFi

Welcome back. Today we build a small, honest NiFi flow that moves a file from an inbox, normalizes a couple of fields, and lands it in an outbox while capturing provenance you can explain. Everything here ran in a live session and is packaged for reuse.

## Why NiFi today
- Visual pipelines make the work legible to colleagues who do not read code; each processor box is an explainable move.
- Built-in provenance shows exactly how data moved and changed, which builds trust like a chain of custody.
- Back pressure, queues, and routing keep you from quietly losing data; quarantine is a governance habit.
- Tradeoffs: NiFi needs Java and memory; flows can get messy if you add too much. We stay minimal to keep it teachable.

## What you'll do and produce
- Run NiFi locally via Docker Compose for a predictable setup.
- Build a minimal flow: inbox → update attributes → simple content normalize → outbox.
- Add quarantine routing and trace a record through provenance.
- Export a flow blueprint and capture processor settings for replay.

## Timebox
- Lab 01 (run NiFi + orient): ~15 minutes
- Lab 02 (build minimal flow): ~30 minutes
- Lab 03 (quarantine + provenance walkthrough): ~20 minutes

## Navigation
- Primer: `00-primer/concepts.md`, `00-primer/glossary_day.md`
- Labs: `01-labs/`
- Job aids: `02-job-aids/`
- Assessments: `03-assessments/`
- Diagrams: `04-diagrams/`
- Artifacts: `05-artifacts/`

If you're short on time: run Lab 01, then Lab 02 through the outbox step, and read the provenance walkthrough notes in Lab 03.
