# Toolbox Setup

This workshop uses lightweight tools. Each tool list includes what it does, why we use it, how to know it is working, and common fixes.

## Common prerequisites
- Modern browser and stable internet (for Colab and Zenodo practice).
- Python 3.9 or newer available locally (`python3 --version`).
- Git and a terminal (or built-in VS Code terminal) for running a few copy/paste commands.
- Docker Desktop or a Docker engine for Day 02 flows (https://www.docker.com/products/docker-desktop).

If you cannot install software locally (managed machines, restricted permissions), you can still run this workshop:
- Use Colab for Python work.
- Use the facilitator-run pathway for tools that require local installs (for example, NiFi via Docker). Learners can still interpret outputs, edit documentation, and complete the checks and packaging steps.

### OpenRefine: How to get it and run it
- What it is: Desktop tool for interactive cleaning, faceting, and exporting an operations history.
- How you use it in this workshop: Clean the Day 01 dataset and export an operations file others can replay.
- How you access it: Install on your computer (launches locally, uses your browser).
- Get it here: https://openrefine.org/download.html
- Open it like this: Download the ZIP or tarball, unzip, then run `refine` (macOS/Linux) or `openrefine.exe` (Windows). Your browser opens to `http://127.0.0.1:3333`.
- Quick check: You should see the OpenRefine home screen at `http://127.0.0.1:3333`.
- Common problems and fixes:
  - UI will not load: restart OpenRefine and make sure nothing else uses port 3333.
  - Memory errors on large files: split the file or increase OpenRefine memory settings in its config.

### Apache NiFi in Docker: How to get it and run it
- What it is: Visual, step-by-step flows with routing and a visible run record.
- How you use it in this workshop: Build the Day 02 inbox-to-outbox flow with quarantine and provenance.
- How you access it: Runs in Docker via the provided Compose file.
- Get it here: Docker pulls the `apache/nifi` image automatically; Docker Desktop download: https://www.docker.com/products/docker-desktop
- Open it like this: In `day-02-repeatable-flows-and-provenance/01-labs/lab-01/`, run `docker compose up`. Wait for logs to show NiFi started, then open `http://localhost:8080/nifi/` in your browser.
- Quick check: NiFi canvas loads and shows processors in the left panel.
- Common problems and fixes:
  - NiFi will not start: check Docker is running; ensure nothing else uses port 8080 (`lsof -i :8080` on macOS/Linux, `netstat -ano | find \"8080\"` on Windows); rerun `docker compose up`.
  - Cannot export flow: use the canvas right-click or top-right menu to download the flow definition.
  - Plan B if Docker is blocked: facilitator runs NiFi and screen-shares while learners review the blueprint and outputs.

### Python + Colab: How to get it and run it
- What it is: Notebook and scripting environment for profiling and validation.
- How you use it in this workshop: Run Day 01 and Day 03 notebooks to check cleaned data and validation rules.
- How you access it: Browser (Colab) or local install.
- Get it here: Python downloads at https://www.python.org/downloads/; Colab at https://colab.research.google.com.
- Open it like this: For Colab, open the lab notebook links and run the install cell. For local, install Python 3.9+, create and activate a virtual environment, install dependencies with `pip install -r requirements.txt` if provided or `pip install pandera[pandas]`, then run notebooks or scripts from the lab folder.
- Quick check: `python --version` shows 3.9 or newer locally, and the first import cell in Colab runs without errors.
- Common problems and fixes:
  - pandas or pandera not found: rerun the install cell; restart runtime if needed.
  - File not found: ensure CSV is uploaded or paths point to repo files; in Colab, re-upload the file each session.

### Pandera: How to get it and run it
- What it is: Declarative data validation for pandas dataframes.
- How you use it in this workshop: Write Day 03 validation schemas and run them on clean and intentionally bad data.
- How you access it: Install inside your Python environment or Colab session.
- Get it here: https://pypi.org/project/pandera/ (install with `pip install pandera[pandas]`).
- Open it like this: After installing, run `python -c \"import pandera\"` or import in a notebook to confirm. Use the provided schema examples in the labs.
- Quick check: Pandera imports with no errors and validation functions run.
- Common problems and fixes:
  - Validation stops after one error: use `lazy=True` to see all failures.
  - Type errors: set `coerce=True` in columns or cast types before validation.

### Streamlit (Day 04 optional): How to get it and run it
- What it is: Builds a simple web app to share a data view without heavy setup.
- How you use it in this workshop: Optional handoff app in Day 04 Lab 03 to preview package contents.
- How you access it: Install in your Python environment.
- Get it here: https://streamlit.io/
- Open it like this: In `day-04-publishing-with-care/01-labs/lab-03/`, run `pip install streamlit` then `streamlit run app.py`. Your browser opens to a local URL.
- Quick check: The Streamlit dashboard opens in your browser and shows the handoff view.
- Common problems and fixes:
  - Module not found: run `pip install streamlit`.
  - File path errors: run the app from `lab-03/` so relative paths resolve.

### Zenodo / DOIs (Day 04): How to get it and run it
- What it is: Hosts datasets and can mint DOIs for citation.
- How you use it in this workshop: Fill `.zenodo.json`, align it with README, LICENSE, and CITATION.cff, and optionally create a draft deposit.
- How you access it: Web-based.
- Get it here: https://zenodo.org/
- Open it like this: Sign in or create an account, click Upload, and start a new upload. For practice, complete `.zenodo.json` locally without uploading.
- Quick check: You can view or edit a draft record in Zenodo, or validate `.zenodo.json` locally with required fields present.
- Common problems and fixes:
  - Metadata rejected: ensure required fields (title, creators, description, license, version) are filled.
  - Size limits: compress or split files; describe large external files in README.
  - License mismatch: align LICENSE, README, CITATION.cff, and `.zenodo.json`.
  - Plan B if accounts are restricted: complete the practice path locally, keep the bundle in `05-deliverables/`, and include a note for future deposit.

## What success looks like overall
- OpenRefine UI loads locally. NiFi UI loads at `http://localhost:8080/nifi/`. Colab notebooks run with dependencies installed. Pandera checks pass or fail with clear messages. Optional Streamlit app launches from `day-04-publishing-with-care/01-labs/lab-03/`. Zenodo metadata is complete and consistent.
