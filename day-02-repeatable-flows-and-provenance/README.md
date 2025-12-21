# Day 02: Repeatable Flows and a Run Record with Apache NiFi

Welcome back. Today you build a small, explainable NiFi flow that moves a file from an inbox, makes a couple of values consistent, and lands it in an outbox while capturing a run record you can explain.

## Why NiFi today
- Visual flows make the work legible to colleagues who do not read code; each processor box is an explainable move.
- Built-in run record (NiFi calls this **Provenance**, meaning: a trace of what happened to a file) shows exactly how data moved and changed, which builds trust like a chain of custody.
- Back pressure, queues, and routing keep you from quietly losing data. A quarantine folder makes review explicit.
- Tradeoffs: NiFi needs Java and memory; flows can get messy if you add too much. We stay minimal to keep it teachable.

## What you'll do and produce
- Run NiFi locally via Docker Compose for a predictable setup.
- Build a minimal flow: inbox → update attributes → simple make-values-consistent step → outbox.
- Add quarantine routing and trace one file through the run record.
- Export a flow blueprint and capture processor settings for replay.

## Suggested timing (so you can plan your session)
- Lab 01 (run NiFi + orient): ~15 minutes
- Lab 02 (build minimal flow): ~30 minutes
- Lab 03 (quarantine + run record walkthrough): ~20 minutes

## Navigation
- Primer: `00-primer/concepts.md`, `00-primer/glossary_day.md`
- Labs: `01-labs/`
- Job aids: `02-job-aids/`
- Assessments: `03-assessments/`
- Diagrams: `04-diagrams/`
- Files created: `05-artifacts/`

If you're short on time: run Lab 01, then Lab 02 through the outbox step, and read the run record walkthrough notes in Lab 03.

## What success looks like
- NiFi opens in your browser and stays responsive.
- A sample input file moves through the flow into outputs.
- A non-conforming file routes to quarantine instead of slipping through.
- You can open the run record (NiFi Provenance view) for one run and explain the path from inbox to outbox.

## Where people get stuck (and quick fixes)
- Docker is blocked: use the facilitator-run pathway and focus learners on reading the blueprint, outputs, and a short run record walkthrough note.
- Address 8080 in use: stop the conflicting service or change the mapped address in docker compose.
- Nothing moves through the flow: confirm processors are started and connections are not backpressured.
- Paths look wrong: verify the paths NiFi uses (for example, `/opt/nifi/inputs`) versus the paths in your repo folder.
