# Day 01: Metadata Cleaning and Making Values Consistent for Reuse

## Introduction

Messy metadata slows every downstream step. Today you will make records legible, consistent, and ready for teams who need to trust what they see. You will tidy values, keep meaning intact, and capture the exact moves you made so others can replay them.

This work sits at the front door of any data workflow. Cultural heritage collections provide the examples, but the same habits apply to spreadsheets from a lab, a municipal office, or a community archive. Careful cleaning keeps later analysis and publishing from becoming a guessing game.

For term definitions used throughout this day, see [today's glossary](00-primer/glossary_day.md) and the [shared glossary](../GLOSSARY.md).

## What You Will Build Today

By the end of this session, you will have:

- A cleaned CSV with consistent values for rights, places, and creator fields
- An OpenRefine project with saved facets and transformations
- An OpenRefine operations file (a JSON file that captures your exact cleaning steps so anyone can replay them)
- A short note explaining any normalization decisions that could affect meaning
- A quick validation run in Python or Colab that confirms the cleaned file is ready to hand off

## Why This Matters in a Real Data Workflow

Day 01 is where you make data legible. Clear, consistent fields keep one messy export from becoming everyone's problem later. A replayable recipe turns manual cleanup into a small piece of process, not a heroic one-time effort. Everything you do today sets up the repeatable flows, checks, and publishing work that follows.

## Today's Toolbox

### OpenRefine

OpenRefine is a free desktop tool for exploring, faceting, and cleaning tabular data. You will use it to clean the Day 01 dataset and export an operations file others can replay.

**How to get it running:**

1. Download OpenRefine from https://openrefine.org/download.html
2. Unzip the downloaded file
3. Run `refine` (on macOS or Linux) or `openrefine.exe` (on Windows)
4. Your browser opens automatically to `http://127.0.0.1:3333`

You should see the OpenRefine home screen. If the page does not load, check that nothing else is using port 3333, then try launching OpenRefine again.

### Python and Google Colab

Python is a programming language, and Colab is a free browser-based notebook environment from Google that lets you run Python without installing anything. You will use these for quick validation checks on cleaned data.

**Colab path (recommended if you are new to Python):** Open the notebook link in [Lab 03](01-labs/lab-03/README.md) and run the install cell. No local setup needed.

**Local path:** Install Python 3.9 or newer from https://www.python.org/downloads/, create a virtual environment, then run `pip install pandera[pandas]`.

### Pandera

Pandera is a Python library that checks whether your data meets the rules you define. Think of it as a spell-checker for your dataset's structure. You will use it in Lab 03 to confirm your cleaned data is ready to share.

These tools are open or low-cost, widely used, and valuable beyond this single workflow.

## Setup Checklist

Before you begin the labs:

1. Review the shared checklist in [TOOLBOX_SETUP.md](../TOOLBOX_SETUP.md) to confirm you have access to the basics
2. Install and launch OpenRefine. You should see the OpenRefine home screen at `http://127.0.0.1:3333`
3. Choose your validation path for Lab 03:
   - **In-browser:** Open the Colab link in [Lab 03](01-labs/lab-03/README.md)
   - **Local:** Confirm Python 3.9+ is available and run `pip install pandera[pandas]`

**If you run into trouble:**

- **OpenRefine page will not load:** Stop anything using port 3333, then relaunch OpenRefine
- **Memory errors with large files:** Split the file or increase the OpenRefine memory setting in its configuration file
- **Python import errors:** Rerun the install command, restart the notebook kernel, and confirm you are in the right environment
- **File not found in validation:** Make sure you run notebooks from the `day-01-metadata-cleaning-and-normalization` folder, or upload the CSV in Colab

If you cannot install software locally, use the Colab path for validation. You can also review the provided OpenRefine screenshots and operations file in [troubleshooting.md](02-job-aids/troubleshooting.md) to see expected steps and outputs.

## Suggested Timing

| Lab | Focus | Time |
|-----|-------|------|
| Lab 01 | Explore facets and spot problems | ~15 minutes |
| Lab 02 | Clean values and export the operations file | ~30 minutes |
| Lab 03 | Run validation and note results | ~20 minutes |

If time is tight, finish Lab 01 and the operations export in Lab 02. You can skim the validation steps and return later.

## Navigation

| File | What it contains |
|------|------------------|
| [00-primer/concepts.md](00-primer/concepts.md) | Primer on why legibility matters before automation |
| [00-primer/glossary_day.md](00-primer/glossary_day.md) | Quick definitions for today's terms |
| [01-labs/lab-01/README.md](01-labs/lab-01/README.md) | Lab 01: Exploring facets and spotting problems |
| [01-labs/lab-02/README.md](01-labs/lab-02/README.md) | Lab 02: Cleaning, normalizing values, exporting the operations file |
| [01-labs/lab-03/README.md](01-labs/lab-03/README.md) | Lab 03: Light validation pass in Python or Colab |
| [02-job-aids/quick_reference.md](02-job-aids/quick_reference.md) | Concise steps you can keep open while you work |
| [02-job-aids/troubleshooting.md](02-job-aids/troubleshooting.md) | Common errors and fixes for Day 01 tools |
| [03-assessments/knowledge_check.md](03-assessments/knowledge_check.md) | Short questions to confirm you grasp the concepts |
| [03-assessments/performance_task.md](03-assessments/performance_task.md) | Applied task to practice the skills on your own data |
| [05-deliverables/README.md](05-deliverables/README.md) | What to save from each lab and how to organize outputs |

## Working Solo vs. Facilitating a Group

**If you are working on your own:** Start with the primer, complete Lab 01 and Lab 02, and save the operations file. Use Lab 03 to sanity-check your cleaned CSV. Self-check by explaining what changed and why in two sentences.

**If you are leading a group:** Demonstrate facets live in Lab 01, then have pairs tackle Lab 02 and compare their normalization choices. Pause before Lab 03 to discuss how to document cleaning decisions. If laptops vary, one facilitator can drive while others observe the operations export and validation outputs.

## You Are Done When

Check your work against this list. You should have:

- [ ] `01-labs/lab-02/outputs/collection_cleaned.csv` with consistent rights and place values
- [ ] `01-labs/lab-02/deliverables/openrefine_operations.json` capturing your cleaning steps
- [ ] Notes in `05-deliverables/` explaining your normalization decisions
- [ ] A validation summary from Lab 03 showing row counts and distinct values

If you have the cleaned CSV and the operations file saved together, you have completed the core work for Day 01. The operations file is the most important artifact because it lets anyone replay your exact steps on future exports.

## Troubleshooting at a Glance

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| OpenRefine keeps redirecting or shows blank | Browser cache issue | Clear browser cache for `127.0.0.1:3333` and relaunch |
| Values did not change as expected | Wrong column selected or filter active | Check you applied the transformation to the correct column and clear any filters |
| Non-UTF-8 characters after export | Encoding mismatch | Export using UTF-8 and reopen in a UTF-8 aware editor |
| Pandera errors about missing columns | Column name mismatch | Verify column names match the schema in Lab 03 |
| Colab cannot see the uploaded file | File not uploaded in current session | Re-upload the file and check the filename matches |

For more troubleshooting, see [02-job-aids/troubleshooting.md](02-job-aids/troubleshooting.md).

## What Comes Next

Tomorrow in Day 02, you will take your cleaned CSV and build a repeatable flow in Apache NiFi. The flow will move files from an inbox to an outbox, route questionable records to quarantine, and keep a visible record of what happened to each file. Your `collection_cleaned.csv` becomes the starting point for that work.

The operations file you exported today is your first piece of provenance. It shows exactly what changed and makes your cleaning repeatable. That same principle of "show your work" continues through the rest of the workshop.

## Take It Further

If you want to explore beyond today's labs:

- **Try clustering:** OpenRefine's clustering feature suggests similar strings that might mean the same thing. Try it on the creator column and see what it finds.
- **Experiment with GREL:** OpenRefine has a small expression language called GREL. Try writing a custom transform like `value.trim().toLowercase()` on a test column.
- **Profile your own data:** Export a CSV from your own collection system and facet the messiest columns. What cleaning targets would you set?
- **Compare operations files:** If you work with a partner, compare your operations files. Did you make the same normalization choices?
- **Read more about controlled vocabularies:** See how rights statement standardization works in projects like RightsStatements.org or Creative Commons.

## Reflection Prompts

Before you move on, take a moment to think about what you learned:

- What did faceting reveal that you would have missed by scrolling through the spreadsheet?
- Which normalization decision felt the hardest, and why?
- If you had to clean a much larger dataset, what would you do differently to save time while keeping the work auditable?

These questions do not have right answers. They help you connect today's practice to future situations in your own work.
