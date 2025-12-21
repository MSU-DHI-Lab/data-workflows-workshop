# Workshop Overview

## What this is
This repository is a four-part workshop-in-a-box for cultural heritage practitioners. Each day is a self-contained 60 to 90 minute session with a primer, labs, job aids, and optional assessments.

## Who it is for
- Learners: museum, archive, library, lab, and repository staff who work with metadata and collection records.
- Facilitators: instructors or trainers who want a reproducible curriculum with clear outputs.
- Teams: anyone who needs to clean, move, validate, and publish datasets with a clear record of what changed, plus reuse guidance.

## Prerequisites
- Comfort with CSV files and basic metadata concepts.
- A modern browser.
- If you will run everything locally: OpenRefine and Python 3.9+.
- If you will run Day 02 locally: Docker access for NiFi.

For setup and fallbacks, use `TOOLBOX_SETUP.md`.

## Session structure (60 to 90 minutes)
Each day follows the same shape:
1) Primer concepts (5 to 10 minutes)
2) Labs (50 to 70 minutes total)
3) Wrap-up (5 to 10 minutes): capture artifacts and a short reflection

## Day-by-day agenda and outputs

### Day 01: Metadata cleaning and making values consistent
- Suggested timing: 15 + 30 + 20 minutes
- Tools: OpenRefine, optional Colab
- Learner outputs:
	- Cleaned CSV export
	- OpenRefine operations file (a saved record of the cleaning steps)
	- Short notes: what changed, what was left as-is, and why

### Day 02: Repeatable flows and a run record
- Suggested timing: 15 + 30 + 20 minutes
- Tools: Apache NiFi (via Docker)
- Learner outputs:
	- NiFi flow export file (a `.json` file, a structured text format)
	- A written flow blueprint (settings and rationale)
	- Sample outputs and quarantined files, plus a brief walkthrough note of what happened

### Day 03: Quality checks for reuse
- Suggested timing: 15 + 30 + 20 minutes
- Tools: Python (local or Colab), Pandera
- Learner outputs:
	- A set of validation rules (code) and a markdown report (evidence)
	- A small set of clearly explained rules that protect downstream reuse

### Day 04: Publishing with care
- Suggested timing: 20 + 30 + 20 minutes
- Tools: documentation files, optional Zenodo path, optional Streamlit (open source)
- Learner outputs:
	- A single dataset package folder containing data, docs, and checks
	- LICENSE, CITATION.cff, and .zenodo.json that agree on title, version, and reuse terms
	- A completed publishing checklist

## Facilitator prep checklist (day before)
- Read the root README and `START_HERE.md`.
- Open each day README and confirm the suggested timing fits your schedule.
- Decide your environment path:
	- Full local path: learners run OpenRefine, Docker/NiFi, and Python.
	- Mixed path: learners use Colab for Python, facilitator runs NiFi.
- Test the key entry points:
	- OpenRefine launches and loads a CSV.
	- If using NiFi: `docker compose up` works and `http://localhost:8080/nifi/` loads.
	- Colab can install Pandera and run a simple cell.

## Facilitator day-of checklist (30 minutes)
- Open: root README, `TOOLBOX_SETUP.md`, and the current day README.
- Confirm file paths learners will use and where outputs should be saved.
- Set expectations: learners should write down what they did, what changed, and what success looks like.

## Restricted-environment pathways (no guessing)
If learners cannot install software:
- Use Colab for Day 03.
- For Day 02, run NiFi as the facilitator and share the flow definition and outputs. Learners can still complete the blueprint and a short explanation of what happened.
- For Day 01, if OpenRefine installs are blocked, run OpenRefine as the facilitator and have learners focus on the facet observations, “make values consistent” decisions, and documentation that accompanies exports.

## How to judge completion
A participant has completed the workshop when they can:
- Produce the day outputs.
- Explain, in plain language, what changed and why.
- Point to evidence that supports trust and reuse (OpenRefine operations file, notes on what changed, validation report, licensing and citation artifacts).

