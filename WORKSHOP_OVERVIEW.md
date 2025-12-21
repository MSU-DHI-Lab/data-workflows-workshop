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

### OpenRefine: How to get it and run it
- What it is: Desktop tool for faceting and cleaning tabular data.
- How you use it in this workshop: Clean Day 01 data and export an operations file.
- How you access it: Install on your computer; opens in your browser locally.
- Get it here: https://openrefine.org/download.html
- Open it like this: Download, unzip, run `refine` (macOS/Linux) or `openrefine.exe` (Windows). Browser opens `http://127.0.0.1:3333`.
- Quick check: OpenRefine home screen appears at `http://127.0.0.1:3333`.

### Apache NiFi (Docker): How to get it and run it
- What it is: Visual flow tool with routing and provenance.
- How you use it in this workshop: Day 02 inbox-to-outbox flow with quarantine.
- How you access it: Runs in Docker via the provided Compose file.
- Get it here: Docker Desktop at https://www.docker.com/products/docker-desktop (pulls `apache/nifi` automatically).
- Open it like this: From `day-02-repeatable-flows-and-provenance/01-labs/lab-01/`, run `docker compose up`, then open `http://localhost:8080/nifi/`.
- Quick check: NiFi canvas loads in the browser and shows processors to drag.

### Python and Google Colab: How to get it and run it
- What it is: Language and notebook environment running locally or in the browser.
- How you use it in this workshop: Day 01 and Day 03 validation and profiling.
- How you access it: Browser (Colab) or local install.
- Get it here: Python at https://www.python.org/downloads/; Colab at https://colab.research.google.com.
- Open it like this: For Colab, open the notebook links and run the install cell. For local, install Python 3.9+, create a virtual environment, install dependencies with `pip install pandera[pandas]`, then run notebooks from the lab folder.
- Quick check: `python --version` shows 3.9 or newer locally; Colab import cells run without errors.

### Pandera: How to get it and run it
- What it is: Python library for declarative data validation on pandas dataframes.
- How you use it in this workshop: Define and run rules in Day 03 labs.
- How you access it: Install in your Python environment or Colab session.
- Get it here: https://pypi.org/project/pandera/ (install with `pip install pandera[pandas]`).
- Open it like this: Import Pandera in the notebook and load the schema file. Run validation cells.
- Quick check: Imports succeed and validation outputs appear without errors.

### Streamlit (optional): How to get it and run it
- What it is: Lightweight Python framework for small web apps.
- How you use it in this workshop: Optional Day 04 handoff app.
- How you access it: Install in your Python environment.
- Get it here: https://streamlit.io/
- Open it like this: In `day-04-publishing-with-care/01-labs/lab-03/`, run `pip install streamlit` then `streamlit run app.py`. Browser opens to a local URL.
- Quick check: Streamlit dashboard opens and shows the handoff view.

### Zenodo (optional): How to get it and run it
- What it is: Free hosting with persistent identifiers (DOIs).
- How you use it in this workshop: Prepare `.zenodo.json` and, if desired, create a draft deposit.
- How you access it: Web-based.
- Get it here: https://zenodo.org/
- Open it like this: Sign in, start a new upload, or complete `.zenodo.json` locally for practice.
- Quick check: A draft record is viewable in Zenodo or your `.zenodo.json` validates locally.

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
