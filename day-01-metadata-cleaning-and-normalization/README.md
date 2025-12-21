# Day 01: Metadata Cleaning and Making Values Consistent for Reuse

## Introduction
Messy metadata slows every downstream step. Today is about making records legible, consistent, and ready for teams who need to trust what they see. You will tidy values, keep meaning intact, and capture the exact moves you made so others can replay them.

This work sits at the front door of any data workflow. Cultural heritage collections provide the examples, but the same habits apply to spreadsheets from a lab, a municipal office, or a community archive. You will see how careful cleaning keeps later analysis and publishing from becoming a guessing game.

## What You Will Build Today
- A cleaned CSV with consistent values for rights, places, and creator fields.
- An OpenRefine project with saved facets and transformations.
- An OpenRefine operations file that anyone can replay to reproduce your steps.
- A short note explaining any normalization decisions that could affect meaning.
- A quick validation run in Python or Colab that confirms the cleaned file is ready to hand off.

## Why This Matters in a Real Data Workflow
Day 01 is where you make data legible. Clear, consistent fields keep one messy export from becoming everyone’s problem later. A replayable recipe turns manual cleanup into a small piece of process, not a one-off heroic effort. Everything you do today sets up the repeatable flows, checks, and publishing work that follows.

## Today’s Toolbox (and why these tools matter beyond this workshop)
### OpenRefine: How to get it and run it
- What it is: A free desktop tool for exploring, faceting, and cleaning tabular data.
- How you use it in this workshop: Clean the Day 01 dataset and export an operations file others can replay.
- How you access it: Install on your computer; it opens in your browser locally.
- Get it here: https://openrefine.org/download.html
- Open it like this: Download the ZIP or tarball, unzip, then run `refine` (macOS/Linux) or `openrefine.exe` (Windows). Your browser opens to `http://127.0.0.1:3333`.
- Quick check: You should see the OpenRefine home screen at `http://127.0.0.1:3333`.

### Python and Google Colab: How to get it and run it
- What it is: A language and notebook environment that runs locally or in the browser.
- How you use it in this workshop: Run quick validation checks on cleaned data.
- How you access it: Browser (Colab) or local install.
- Get it here: Python downloads at https://www.python.org/downloads/; Colab at https://colab.research.google.com.
- Open it like this: For Colab, open the notebook link in `01-labs/lab-03/README.md` and run the install cell. For local, install Python 3.9 or newer, create a virtual environment, run `pip install pandera[pandas]`, then run the notebook or script from this folder.
- Quick check: The first import cells in the notebook run without errors and `python --version` shows 3.9 or newer locally.

### Pandera: How to get it and run it
- What it is: A Python library for declarative data validation on pandas dataframes.
- How you use it in this workshop: Power the light validation checks in Lab 03.
- How you access it: Install in your Python environment or Colab session.
- Get it here: https://pypi.org/project/pandera/ (install with `pip install pandera[pandas]`).
- Open it like this: After installing, import Pandera in the notebook (`import pandera as pa`). Use the provided schema examples in Lab 03.
- Quick check: The import succeeds and the validation cells run without errors.

These tools are open or low-cost, widely used, and valuable beyond this single workflow.

## Setup and Getting Ready (download, install, configure)
- Start with the shared checklist in `../TOOLBOX_SETUP.md` to confirm you have access to the basics.
- Install OpenRefine and launch it. You should reach `http://127.0.0.1:3333` in your browser and see the OpenRefine home screen.
- Choose your validation path:
  - In-browser: open the provided Colab link in `01-labs/lab-03/README.md`.
  - Local: ensure Python 3.9 or newer is available, then run `pip install pandera[pandas]` inside your environment.
- Common issues and fixes:
  - OpenRefine page will not load: stop anything using port 3333, then relaunch OpenRefine.
  - Memory errors with large files: split the file or increase the OpenRefine memory setting in its configuration file.
  - Python import errors: rerun the install command, restart the notebook kernel, and confirm you are in the right environment.
  - File not found in validation: check that you run notebooks from the `day-01-metadata-cleaning-and-normalization` folder or upload the CSV in Colab.
- If you cannot install locally, use the Colab path and review the provided OpenRefine screenshots and operations file in `02-job-aids/troubleshooting.md` to see the expected steps and outputs.

## Suggested Timing (so you can plan your session)
- Plan for about 15 minutes in Lab 01 to explore facets.
- Plan for about 30 minutes in Lab 02 to clean values and export the operations file.
- Plan for about 20 minutes in Lab 03 to run validation and note results.

If time is tight, finish Lab 01 and the operations export in Lab 02. You can skim the validation steps and return later.

## Navigation: Everything in this Day Folder
- `00-primer/concepts.md`: Primer on why legibility matters before automation.
- `00-primer/glossary_day.md`: Quick definitions for today’s terms.
- `01-labs/lab-01/README.md`: Lab 01 guides you through exploring facets and spotting problems.
- `01-labs/lab-02/README.md`: Lab 02 covers cleaning, normalizing values, and exporting the operations file.
- `01-labs/lab-03/README.md`: Lab 03 walks through a light validation pass in Python or Colab.
- `02-job-aids/quick_reference.md`: Job aid with concise steps you can keep open while you work.
- `02-job-aids/troubleshooting.md`: Common errors and fixes specific to Day 01 tools.
- `03-assessments/knowledge_check.md`: Short questions to confirm you grasp the concepts.
- `03-assessments/performance_task.md`: Applied task to practice the skills on your own data.
- `03-assessments/rubric.md`: Criteria to judge whether the work meets the goals.
- `05-artifacts/README.md`: What to save from each lab and how to organize outputs.

## If You Are Doing This Solo / If You Are Facilitating a Group
- **Solo:** Start with the primer, complete Lab 01 and Lab 02, and save the operations file. Use Lab 03 to sanity-check your cleaned CSV. Self-check by explaining what changed and why in two sentences.
- **Group:** Demonstrate facets live in Lab 01, then have pairs tackle Lab 02 and compare their normalization choices. Pause before Lab 03 to discuss how to document cleaning decisions. If laptops vary, one facilitator can drive while others observe the operations export and validation outputs.

## What Success Looks Like
- A cleaned CSV that removes obvious inconsistencies without losing meaning.
- An OpenRefine operations file saved alongside the data so others can rerun the steps.
- Notes that explain any normalization rules that might change interpretation.
- A validation pass that completes without missing-file errors and surfaces any lingering issues.
- If you only do one thing, export the OpenRefine operations file and the cleaned CSV together.

## Troubleshooting at a Glance
- OpenRefine keeps redirecting or blank page shows: clear your browser cache for `127.0.0.1:3333` and relaunch.
- Values did not change as expected: check whether you applied the transformation to the correct column or had a filter active.
- Non-UTF-8 characters after export: ensure you export using UTF-8 and re-open the file in a UTF-8 aware editor.
- Pandera errors about missing columns: verify column names match the schema in `01-labs/lab-03/README.md`.
- Colab cannot see the uploaded file: confirm you uploaded during the session and referenced the correct filename.
