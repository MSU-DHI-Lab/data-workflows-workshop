# Toolchain Setup

This workshop uses lightweight tools. Each tool list includes what it does, why we use it, how to know it is working, and common fixes.

## Common prerequisites
- Modern browser and stable internet (for Colab and Zenodo practice).
- Python 3.9 or newer available locally (`python3 --version`).
- Git and a terminal (or built-in VS Code terminal) for running a few copy/paste commands.

If you cannot install software locally (managed machines, restricted permissions), you can still run this workshop:
- Use Colab for Python work.
- Use the facilitator-run pathway for tools that require local installs (for example, NiFi via Docker). Learners can still interpret outputs, edit documentation, and complete the checks and packaging steps.

## OpenRefine (Day 01)
- What it does: desktop tool for interactive cleaning, faceting, and exporting an operations history.
- Why we use it: fast pattern-spotting and reversible transforms before you automate anything. Tradeoff: not ideal for very large datasets.
- Success looks like: reaching `http://127.0.0.1:3333` and seeing the OpenRefine UI.
- Common problems and fixes: 
  - Problem: UI will not load (Windows/macOS). Fix: restart OpenRefine; ensure no other app is using address 3333.
  - Problem: memory errors on large files. Fix: split the file or increase OpenRefine memory settings in the OpenRefine config.

## Apache NiFi in Docker (Day 02)
- What it does: visual, step-by-step flows with routing and a visible run record (a trace of what happened).
- Why we use it: lets you draw a repeatable file-moving flow with visible history. Tradeoff: needs Docker and a free browser address at `http://localhost:8080/`.
- Success looks like: `docker compose up` in `day-02-repeatable-flows-and-provenance/01-labs/lab-01/` followed by reaching `http://localhost:8080/nifi/`.
- Common problems and fixes:
  - Problem: NiFi will not start. Fix: check Docker is running; make sure nothing else is using address 8080 (`lsof -i :8080` on macOS/Linux, `netstat -ano | find "8080"` on Windows); rerun `docker compose up`.
  - Problem: cannot export flow. Fix: use the canvas right-click or top-right menu to download flow definition.
  - Plan B if Docker is blocked: facilitator runs NiFi and screen-shares the flow while learners review the blueprint and outputs.

## Python + Colab (Day 03)
- What it does: runs notebooks for profiling and validation.
- Why we use it: no local setup in Colab; easy to read code and outputs. Tradeoff: needs internet if using Colab.
- Success looks like: notebooks run cells without import errors after `pip install pandera[pandas]`.
- Common problems and fixes:
  - Problem: pandas or pandera not found. Fix: rerun the install cell; restart runtime if needed.
  - Problem: file not found. Fix: ensure CSV is uploaded or paths point to repo files when running locally. Use Colab if local Python is restricted.

## Pandera (Day 03)
- What it does: declarative data validation for pandas dataframes.
- Why we use it: readable rules of trust next to the data. Tradeoff: Python-only; needs pandas.
- Success looks like: running the validation function returns your table when it passes, or prints a clear list of what failed.
- Common problems and fixes:
  - Problem: validation stops after one error. Fix: use `lazy=True` to see all failures.
  - Problem: type errors. Fix: set `coerce=True` in columns or cast types before validation.

## Streamlit (Day 04 optional)
- What it does: builds a simple web app to share a data view without heavy setup.
- Why we use it: quick handoff for browsing data and quality status. Tradeoff: local install required if not using Colab.
- Success looks like: `streamlit run app.py` in `day-04-publishing-with-care/01-labs/lab-03/` opens a local URL with the dashboard.
- Common problems and fixes:
  - Problem: module not found. Fix: run `pip install streamlit`.
  - Problem: file path errors. Fix: run the app from `lab-03/` so relative paths resolve.

## Zenodo / DOIs (Day 04)
- What it does: hosts datasets and can mint DOIs for citation.
- Why we use it: provides a persistent identifier and landing page for the package. Tradeoff: live deposit requires an account; size limits apply.
- Success looks like: the Zenodo metadata file (named `.zenodo.json`) is filled in, LICENSE and CITATION.cff agree on title/version/license, and (optionally) a Zenodo draft or DOI is created.
- Common problems and fixes:
  - Problem: metadata rejected. Fix: ensure required fields (title, creators, description, license, version) are filled.
  - Problem: size limits. Fix: compress or split files; describe large external files in README.
  - Problem: license mismatch. Fix: align LICENSE, README, CITATION.cff, and .zenodo.json.
  - Plan B if accounts are restricted: complete the practice path locally, keep the bundle in `05-artifacts/`, and include a note for future deposit.

## What success looks like overall
- OpenRefine UI loads locally. NiFi UI loads at `http://localhost:8080/nifi/`. Colab notebooks run with dependencies installed. Pandera checks pass or fail with clear messages. Optional Streamlit app launches from `day-04-publishing-with-care/01-labs/lab-03/`. Zenodo metadata is complete and consistent.
