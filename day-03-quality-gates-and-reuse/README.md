# Day 03: Quality Checks for Reuse

## Introduction
Today you turn cleaned data and repeatable flows into explicit quality gates. You will profile a dataset, write validation rules, and see how clear feedback builds trust. The goal is to make quality visible instead of hoping no surprises slip through.

These skills fit any real-world data pipeline. Cultural heritage examples anchor the exercises, but the same habits help labs, agencies, and community projects share data without fear of breakage. You will practice writing checks that others can read, rerun, and improve.

## What You Will Build Today
- A quick data profile that summarizes shape, missing values, and unique counts.
- A `validation_schema.py` file with 6 to 10 Pandera checks that encode the rules of trust.
- A set of notebook cells (Colab or local) that run the checks against clean and intentionally bad data.
- A short markdown report that explains which checks matter most and why.
- Saved outputs that show pass and fail cases for future reference.

## Why This Matters in a Real Data Workflow
Day 03 is where you make quality explicit and shareable. Checks catch drift before it spreads, and a readable schema keeps standards from living in one person’s head. This is what stops one unexpected value from silently polluting dashboards or public releases later.

## Today’s Toolbox (and why these tools matter beyond this workshop)
### Python and Google Colab: How to get it and run it
- What it is: A language and notebook environment that runs locally or in the browser.
- How you use it in this workshop: Profile data, write validation rules, and run checks.
- How you access it: Browser (Colab) or local install.
- Get it here: Python downloads at https://www.python.org/downloads/; Colab at https://colab.research.google.com.
- Open it like this: For Colab, open the notebook links in `01-labs/` and run the install cell. For local, install Python 3.9 or newer, create a virtual environment, install dependencies with `pip install pandera[pandas]`, then run the notebooks from this folder.
- Quick check: `python --version` shows 3.9 or newer locally, and the first import cell in Colab runs without errors.

### Pandera: How to get it and run it
- What it is: A Python library for declarative data validation on pandas dataframes.
- How you use it in this workshop: Define and run the validation schema in Lab 02 and Lab 03.
- How you access it: Install in your Python environment or Colab session.
- Get it here: https://pypi.org/project/pandera/ (install with `pip install pandera[pandas]`).
- Open it like this: After installing, import Pandera in the notebook (`import pandera as pa`) and load your schema from `validation_schema.py`.
- Quick check: Pandera imports with no errors and your schema runs on the sample data.

Both tools are open or low-cost, widely used, and worth keeping in your toolbox for any future data project.

## Setup and Getting Ready (download, install, configure)
- Begin with the shared checklist in `../TOOLBOX_SETUP.md` to confirm you have Python access or can use Colab.
- Colab path: follow the notebook link in `01-labs/lab-01/README.md`, then run the install cell included there. You should see Pandera import successfully in the first code cell.
- Local path: ensure Python 3.9 or newer is available. In a virtual environment, run `pip install pandera[pandas]` from the `day-03-quality-gates-and-reuse` folder. Open the lab notebooks or scripts and confirm `import pandera` succeeds.
- Common issues and fixes:
  - Pandera import fails: rerun the install, restart the kernel, and confirm you are using the right environment.
  - File paths break: run notebooks from this folder or adjust relative paths to the provided CSVs in `01-labs/`.
  - Type mismatches: cast columns before validation or enable coercion in your schema definitions.
  - Colab cannot access local files: upload the CSVs directly in the session or copy them to your drive for the session.
- If you cannot install locally, stay in Colab and use the provided datasets. For a full offline fallback, review expected outputs and schema examples in `02-job-aids/troubleshooting.md`.

## Suggested Timing (so you can plan your session)
- Plan for about 15 minutes in Lab 01 to profile the data and spot risk areas.
- Plan for about 30 minutes in Lab 02 to write and refine the validation schema.
- Plan for about 20 minutes in Lab 03 to run the checks, capture failures, and write the short report.

If time is tight, finish Lab 01 and Lab 02. You can skim Lab 03’s reporting steps and add them later.

## Navigation: Everything in this Day Folder
- `00-primer/concepts.md`: Primer on why explicit checks protect downstream work.
- `00-primer/glossary_day.md`: Definitions for validation terms and abbreviations used today.
- `01-labs/lab-01/README.md`: Lab 01 guides data profiling and risk spotting.
- `01-labs/lab-02/README.md`: Lab 02 walks through writing the Pandera schema and iterating on checks.
- `01-labs/lab-03/README.md`: Lab 03 runs the schema, interprets failures, and captures a short report.
- `02-job-aids/quick_reference.md`: Job aid with common Pandera patterns and code snippets.
- `02-job-aids/troubleshooting.md`: Troubleshooting steps for notebook, schema, and dependency issues.
- `03-assessments/knowledge_check.md`: Short questions to confirm understanding of validation concepts.
- `03-assessments/performance_task.md`: Applied task to design a validation schema for your own dataset.
- `03-assessments/rubric.md`: Criteria for judging whether checks are clear, sufficient, and reproducible.
- `05-artifacts/README.md`: Guidance on what outputs to save from the labs.

## If You Are Doing This Solo / If You Are Facilitating a Group
- **Solo:** Work through Lab 01 and Lab 02 to build the schema, then run Lab 03 to see failures and passes. Self-check by explaining what each rule protects and by running at least one intentional bad row.
- **Group:** Review the primer together, then split into pairs to draft schemas in Lab 02. Pause to compare rules and discuss which ones matter most. In Lab 03, project the failure output and have the group interpret it before fixing data or rules.

## What Success Looks Like
- A `validation_schema.py` (or notebook cell) that lists clear rules for key columns.
- Validation runs that produce readable pass or fail messages without crashing.
- A brief report or note that highlights the most important checks and why they exist.
- Examples saved for both passing data and intentional failures.
- If you only do one thing, save the validation schema and the report showing how it behaves on sample data.

## Troubleshooting at a Glance
- ImportError for Pandera or pandas: reinstall the package, restart the runtime, and confirm the environment matches the Python version requirement.
- Schema fails on unexpected columns: align column names between the dataset and the schema, or update the schema to match the cleaned data.
- Date or numeric parsing errors: convert columns before validation using pandas parsing helpers.
- Failing rows unclear: use `lazy=True` in Pandera to see all errors, then inspect the returned dataframe of failures.
- Colab session resets: rerun the install cell and re-upload data, then rerun the validation cells.
