# Day 04: Publishing with Care

## Introduction
This final day is about packaging your work so others can reuse it without guesswork. You will gather data, documentation, and quality evidence into a single folder, write clear reuse terms, and prepare citation details. If you choose, you will also stand up a small open source Streamlit handoff view for colleagues.

Publishing is the bridge from your workspace to someone else’s. Cultural heritage collections provide the stories here, but any team that shares data needs the same habits: transparent licensing, clear versioning, and a stable landing place. You will see how to make your package easy to cite, easy to trust, and easy to maintain.

## What You Will Build Today
- A complete dataset package folder with data, docs, and validation outputs together.
- A filled-in LICENSE, CITATION.cff, and `.zenodo.json` that agree on title, version, and reuse terms.
- A concise README and data dictionary that explain what the data is and how to use it safely.
- Zenodo-ready metadata for a draft or future deposit (no account required for practice).
- An optional Streamlit (open source) handoff app that previews the package for colleagues.

## Why This Matters in a Real Data Workflow
Day 04 is where you publish for reuse with documentation and identifiers. Clear packages stop reuse from becoming risky improvisation, and stable references keep citations consistent over time. This is what prevents a half-documented folder from spreading confusion across teams or partners.

## Today’s Toolbox (and why these tools matter beyond this workshop)
### Documentation files: How to get them and run them
- What it is: README, data dictionary, LICENSE, and CITATION.cff files that explain content, rights, and attribution.
- How you use it in this workshop: Fill and align these files so the package is understandable and legally usable.
- How you access it: Edit in a text editor such as VS Code or any Markdown editor.
- Get it here: VS Code download at https://code.visualstudio.com/ (or use your preferred editor).
- Open it like this: Open this repository folder in your editor, then open each markdown or YAML file in Day 04 labs to edit.
- Quick check: Files save in UTF-8 and show updated text when you reopen them.

### Zenodo: How to get it and run it
- What it is: A free service for hosting research outputs and minting DOIs.
- How you use it in this workshop: Prepare `.zenodo.json`, then optionally create a draft deposit for your package.
- How you access it: Web-based.
- Get it here: https://zenodo.org/
- Open it like this: Sign in or create an account, click Upload, and start a new upload. For practice, fill `.zenodo.json` locally without uploading.
- Quick check: You can view or edit a draft record in Zenodo, or validate that `.zenodo.json` has required fields locally.

### Streamlit (open source): How to get it and run it
- What it is: A lightweight Python framework for simple web apps.
- How you use it in this workshop: Optional handoff app in Lab 03 to preview the package for colleagues.
- How you access it: Install in your Python environment.
- Get it here: https://streamlit.io/
- Open it like this: In `day-04-publishing-with-care/01-labs/lab-03/`, run `pip install streamlit` then `streamlit run app.py`. Your browser opens to a local URL.
- Quick check: A Streamlit dashboard opens and shows the handoff view from Lab 03.

### Python: How to get it and run it (for the optional app)
- What it is: A language and runtime for the optional Streamlit app.
- How you use it in this workshop: Run the optional Day 04 Streamlit handoff.
- How you access it: Install locally.
- Get it here: https://www.python.org/downloads/
- Open it like this: Install Python 3.9 or newer, create and activate a virtual environment in `day-04-publishing-with-care/01-labs/lab-03/`, run `pip install streamlit`, then run `streamlit run app.py`.
- Quick check: `python --version` shows 3.9 or newer and the Streamlit command opens a local URL.

These tools are open or low-cost, widely used, and worth keeping in your toolbox whenever you share data.

## Setup and Getting Ready (download, install, configure)
- Start with the shared checklist in `../TOOLBOX_SETUP.md` to confirm you have a text editor and, if using the optional app, Python access.
- Documentation path: open the template files in this folder and confirm you can edit and save them in UTF-8.
- Optional app path:
  - In-browser: you can read the `01-labs/lab-03/README.md` and review the screenshots without running the app.
  - Local: ensure Python 3.9 or newer, then run `pip install streamlit` in this folder. Launch with `streamlit run 01-labs/lab-03/app.py` and confirm it opens a local URL with the dashboard.
- Common issues and fixes:
  - License or citation mismatch: align title, version, authors, and license text across README, LICENSE, CITATION.cff, and `.zenodo.json`.
  - YAML errors in CITATION.cff: check spacing, use plain quotes, and validate keys against the examples in `01-labs/lab-02/README.md`.
  - JSON errors in `.zenodo.json`: remove trailing commas and validate the file structure before saving.
  - Streamlit module not found: rerun `pip install streamlit` in the active environment, then retry the launch command.
  - Local app cannot load files: run the app from `01-labs/lab-03/` so relative paths resolve, or adjust file paths inside the app configuration.
- If you cannot install locally or create accounts, complete the practice path: finish Labs 01 and 02, keep the package locally, and review the `01-labs/lab-03/validation_report.md` to see expected app output.

## Suggested Timing (so you can plan your session)
- Plan for about 20 minutes in Lab 01 to assemble the dataset package structure.
- Plan for about 30 minutes in Lab 02 to complete licensing, citation, and Zenodo metadata.
- Plan for about 20 minutes in Lab 03 if you choose to run the Streamlit handoff app.

If time is tight, finish Labs 01 and 02. You can review the Lab 03 report later without running the app.

## Navigation: Everything in this Day Folder
- `00-primer/concepts.md`: Primer on why careful publishing and identifiers matter.
- `00-primer/glossary_day.md`: Definitions for publishing and licensing terms used today.
- `01-labs/lab-01/README.md`: Lab 01 builds the package folder and organizes required files.
- `01-labs/lab-02/README.md`: Lab 02 guides you through licensing, citation, and Zenodo metadata.
- `01-labs/lab-03/README.md`: Lab 03 walks through the optional Streamlit app and how to share a quick preview.
- `01-labs/lab-03/validation_report.md`: Example report showing expected validation outputs for the app path.
- `02-job-aids/quick_reference.md`: Job aid summarizing publishing steps and required files.
- `02-job-aids/troubleshooting.md`: Troubleshooting guide for licensing, metadata, and app issues.
- `03-assessments/knowledge_check.md`: Short questions to confirm publishing concepts.
- `03-assessments/performance_task.md`: Applied task to package and document a dataset for reuse.
- `03-assessments/rubric.md`: Criteria to judge whether the package is ready to share.
- `05-artifacts/README.md`: Checklist of what to save and how to store final outputs.

## If You Are Doing This Solo / If You Are Facilitating a Group
- **Solo:** Work through Labs 01 and 02 to complete the package, then decide if you want to run the optional app in Lab 03. Self-check by confirming the license, citation, and `.zenodo.json` all match and that the README makes sense to a new reader.
- **Group:** Have participants pair up for Lab 01 to compare how they organize packages. In Lab 02, pause to align on licensing choices and citation details. Treat Lab 03 as optional show-and-tell if time allows or if installations vary.

## What Success Looks Like
- A single folder contains data, README, data dictionary, validation outputs, LICENSE, CITATION.cff, and `.zenodo.json`.
- License, citation, and metadata agree on the title, version, creators, and reuse terms.
- You can explain to a colleague how to cite and use the package safely without a follow-up meeting.
- Optional: the Streamlit app runs locally and shows the same information as your documentation.
- If you only do one thing, finish the documentation and metadata files so the package is trustworthy to share.

## Troubleshooting at a Glance
- License text unclear: use the guidance in `02-job-aids/quick_reference.md` and keep the chosen license consistent across files.
- CITATION.cff will not parse: check indentation, avoid tabs, and validate against the example keys in the lab instructions.
-.zenodo.json rejected by a validator: ensure required fields are present, remove trailing commas, and verify string quoting.
- Streamlit app not launching: confirm you ran `pip install streamlit`, then start from `01-labs/lab-03/` to keep paths correct.
- Package feels incomplete: compare your folder to the checklist in `05-artifacts/README.md` and add any missing documents or outputs.
