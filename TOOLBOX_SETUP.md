# Toolbox Setup

This workshop uses lightweight tools. Each tool list includes what it does, why we use it, how to know it is working, and common fixes.

## Common prerequisites
- Modern browser and stable internet (for Colab and Zenodo practice).
- Python 3.9 or newer available locally (`python3 --version`).
- Git for downloading the workshop files (or you can download as a ZIP from GitHub).
- A terminal for running a few copy/paste commands (see "What is a terminal?" below).
- Docker Desktop for Day 02 flows (https://www.docker.com/products/docker-desktop). Docker is a free program that runs software packages called containers. You install Docker Desktop once, and it lets you run NiFi without complicated setup. See "What is Docker?" below for more details.

If you cannot install software locally (managed machines, restricted permissions), you can still run this workshop:
- Use Colab for Python work.
- Use the facilitator-run pathway for tools that require local installs (for example, NiFi via Docker). Learners can still interpret outputs, edit documentation, and complete the checks and packaging steps.

---

## Downloading the Workshop Files

### Option A: Download as ZIP (easiest)
1. Go to the workshop repository on GitHub
2. Click the green "Code" button
3. Select "Download ZIP"
4. Unzip the downloaded file to a location you can find (like your Documents folder)

### Option B: Use Git (if you have it installed)
Git is a tool for downloading and tracking code projects. If you have Git installed, open a terminal and run:
```
git clone https://github.com/MSU-DHI-Lab/data-workflows-workshop.git
```
This creates a folder called `data-workflows-workshop` with all the files.

**How to check if Git is installed:** Open a terminal and type `git --version`. If you see a version number, Git is installed. If not, use Option A or install Git from https://git-scm.com/downloads.

---

### What is a terminal?

A **terminal** (also called a command line) is a text-based way to talk to your computer. Instead of clicking icons, you type commands. It looks like a plain window with text.

**Where to find it:**
- **macOS**: Open the "Terminal" app (in Applications > Utilities, or search for "Terminal")
- **Windows**: Open "Command Prompt" or "PowerShell" (search for either in the Start menu)
- **VS Code**: If you use VS Code, there is a built-in terminal (View > Terminal or press Ctrl+` on Windows, Cmd+` on Mac)

**Common commands you will use:**
- `cd folder-name` — "Change directory." This moves you into a folder. Think of it like double-clicking a folder in Finder/File Explorer.
- `ls` (macOS/Linux) or `dir` (Windows) — List what is in the current folder
- `Ctrl+C` — Stop a running program (this is NOT copy/paste in the terminal)

**Example:** If you downloaded this workshop to your Documents folder, you would open a terminal and type:
```
cd Documents/data-workflows-workshop
```
Now you are "inside" the workshop folder and can run commands there.

---

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

### What is Docker?

Docker is a free program that runs self-contained software packages called **containers**. A container bundles software with everything it needs, so it works the same way on any computer. You do not install NiFi directly on your machine. Instead, Docker downloads a pre-built NiFi package (called an **image**) and runs it in an isolated container.

**Why use Docker?** Installing NiFi manually would require many steps and could conflict with other software on your computer. Docker handles all that complexity. You run one command, and Docker does the rest.

**Key terms you will see:**
- **Image**: A pre-built software package. Docker downloads the NiFi image once and reuses it.
- **Container**: A running instance of an image. When you run `docker compose up`, Docker creates a container from the NiFi image.
- **Port**: A numbered door on your computer. NiFi uses port 8080, so you access it at `http://localhost:8080/nifi/`.
- **Volume** or **mount**: A window between the container and your computer's folders. This lets NiFi read and write files on your machine.

### Apache NiFi (runs inside Docker)
- What it is: Visual, step-by-step flows with routing and a visible run record.
- How you use it in this workshop: Build the Day 02 inbox-to-outbox flow with quarantine and provenance.
- How you access it: Runs in a Docker container. You start it with one command and open it in your browser.
- Get it here: Docker downloads the NiFi image automatically when you run the start command. Docker Desktop download: https://www.docker.com/products/docker-desktop
- Open it like this: In `day-02-repeatable-flows-and-provenance/01-labs/lab-01/`, run `docker compose up`. Wait for logs to show NiFi started (look for \"Started\" messages), then open `http://localhost:8080/nifi/` in your browser.
- Quick check: NiFi canvas loads and shows a toolbar on the left.
- Common problems and fixes:
  - NiFi will not start: check Docker Desktop is running (look for the whale icon); ensure nothing else uses port 8080 (`lsof -i :8080` on macOS/Linux, `netstat -ano | find \"8080\"` on Windows); rerun `docker compose up`.
  - Cannot export flow: use the canvas right-click or top-right menu to download the flow definition.
  - Plan B if Docker is blocked: facilitator runs NiFi and screen-shares while learners review the blueprint and outputs.

### Python + Colab: How to get it and run it
- What it is: Notebook and scripting environment for profiling and validation.
- How you use it in this workshop: Run Day 01 and Day 03 notebooks to check cleaned data and validation rules.
- How you access it: Browser (Colab) or local install.
- Get it here: Python downloads at https://www.python.org/downloads/; Colab at https://colab.research.google.com.

**What is a notebook?** A notebook is a document that mixes text explanations with runnable code. The code lives in "cells" — small boxes you click and run one at a time. Results appear directly below each cell. Colab notebooks run in your browser, so you do not need to install Python.

**What is pip?** pip is a tool that downloads and installs Python add-ons (called "packages" or "libraries"). The command `pip install pandera[pandas]` tells pip to download Pandera and everything it needs.

**What is a virtual environment?** A virtual environment is an isolated workspace for Python. It keeps the packages you install for this workshop separate from other Python projects. This prevents conflicts.

**How to create a virtual environment (local install):**
1. Open a terminal and navigate to the workshop folder
2. Run: `python3 -m venv venv` (this creates a folder called `venv`)
3. Activate it:
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. You should see `(venv)` at the start of your terminal prompt
5. Now install packages: `pip install pandera[pandas]`

- Open it like this: For Colab, open the lab notebook links and run the install cell. For local, follow the virtual environment steps above, then run notebooks or scripts from the lab folder.
- Quick check: `python --version` shows 3.9 or newer locally, and the first import cell in Colab runs without errors.
- Common problems and fixes:
  - pandas or pandera not found: rerun the install cell; restart runtime (the "kernel" — the engine running your code) if needed.
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
