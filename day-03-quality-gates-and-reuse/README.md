# Day 03: Quality Checks for Reuse

## Introduction

Today you will turn cleaned data and repeatable flows into explicit quality gates. You will profile a dataset, write validation rules, and see how clear feedback builds trust. The goal is to make quality visible instead of hoping no surprises slip through.

These skills fit any real-world data pipeline. Cultural heritage examples anchor the exercises, but the same habits help labs, agencies, and community projects share data without fear of breakage. You will practice writing checks that others can read, rerun, and improve.

For term definitions used throughout this day, see [today's glossary](00-primer/glossary_day.md) and the [shared glossary](../GLOSSARY.md).

## What You Will Build Today

By the end of this session, you will have:

- A quick data profile that summarizes shape, missing values, and unique counts
- A `validation_schema.py` file with 6 to 10 Pandera checks that encode the rules of trust
- A set of notebook cells (Colab or local) that run the checks against clean and intentionally bad data
- A short markdown report that explains which checks matter most and why
- Saved outputs that show pass and fail cases for future reference

## Why This Matters in a Real Data Workflow

Day 03 is where you make quality explicit and shareable. Checks catch drift before it spreads, and a readable schema (a defined structure for what your data should look like) keeps standards from living in one person's head. This is what stops one unexpected value from silently polluting dashboards or public releases later.

## Today's Toolbox

### Python and Google Colab

Python is a programming language, and Colab is a free browser-based notebook environment from Google that lets you run Python without installing anything. You will use these to profile data, write validation rules, and run checks.

**Colab path (recommended if you are new to Python):** Open the notebook links in the labs and run the install cell. No local setup needed.

**Local path:** Install Python 3.9 or newer from https://www.python.org/downloads/, create a virtual environment, then run `pip install pandera[pandas]`.

### Pandera

Pandera is a Python library for declarative data validation. "Declarative" means you describe what the data should look like, and Pandera checks whether it matches. Instead of writing lots of if-statements scattered through your code, you define your rules in one place.

Think of Pandera like a checklist that runs automatically. You say "the rights column must contain only these three values" and Pandera tells you which rows break that rule.

**How to get it running:**

1. In Colab or your local Python environment, run `pip install pandera[pandas]`
2. In your notebook, run `import pandera as pa` to load the library
3. Use the provided schema examples in Lab 02 as a starting point

You should see the import succeed without errors. If you see a ModuleNotFoundError, rerun the install command and restart your notebook kernel.

Both tools are open or low-cost, widely used, and worth keeping in your toolbox for any future data project.

## Setup Checklist

Before you begin the labs:

1. Review the shared checklist in [TOOLBOX_SETUP.md](../TOOLBOX_SETUP.md) to confirm you have Python access or can use Colab
2. **Colab path:** Open the notebook link in [Lab 01](01-labs/lab-01/README.md) and run the install cell. You should see Pandera import successfully
3. **Local path:** Confirm Python 3.9+ is available, create a virtual environment, run `pip install pandera[pandas]`, and confirm `import pandera` succeeds

**If you run into trouble:**

- **Pandera import fails:** Rerun the install command, restart your notebook kernel, and confirm you are in the right environment
- **File paths break:** Run notebooks from the day-03 folder or adjust relative paths to point to the provided CSVs
- **Type mismatches:** Cast columns before validation or enable coercion in your schema definitions (the labs show how)
- **Colab cannot access local files:** Upload the CSVs directly in the session or copy them to your Google Drive

If you cannot install locally, stay in Colab and use the provided datasets. For a full offline fallback, review expected outputs and schema examples in [troubleshooting.md](02-job-aids/troubleshooting.md).

## Suggested Timing

| Lab | Focus | Time |
|-----|-------|------|
| Lab 01 | Profile the data and spot risk areas | ~15 minutes |
| Lab 02 | Write and refine the validation schema | ~30 minutes |
| Lab 03 | Run checks, capture failures, write the report | ~20 minutes |

If time is tight, finish Lab 01 and Lab 02. You can skim Lab 03's reporting steps and add them later.

## Navigation

| File | What it contains |
|------|------------------|
| [00-primer/concepts.md](00-primer/concepts.md) | Primer on why explicit checks protect downstream work |
| [00-primer/glossary_day.md](00-primer/glossary_day.md) | Definitions for validation terms used today |
| [01-labs/lab-01/README.md](01-labs/lab-01/README.md) | Lab 01: Data profiling and risk spotting |
| [01-labs/lab-02/README.md](01-labs/lab-02/README.md) | Lab 02: Writing the Pandera schema and iterating on checks |
| [01-labs/lab-03/README.md](01-labs/lab-03/README.md) | Lab 03: Running the schema, interpreting failures, and writing a report |
| [02-job-aids/quick_reference.md](02-job-aids/quick_reference.md) | Common Pandera patterns and code snippets |
| [02-job-aids/troubleshooting.md](02-job-aids/troubleshooting.md) | Troubleshooting for notebook, schema, and dependency issues |
| [03-assessments/knowledge_check.md](03-assessments/knowledge_check.md) | Short questions to confirm understanding of validation concepts |
| [03-assessments/performance_task.md](03-assessments/performance_task.md) | Applied task to design a validation schema for your own dataset |
| [05-deliverables/README.md](05-deliverables/README.md) | What outputs to save from the labs |

## Working Solo vs. Facilitating a Group

**If you are working on your own:** Work through Lab 01 and Lab 02 to build the schema, then run Lab 03 to see failures and passes. Self-check by explaining what each rule protects and by running at least one intentional bad row.

**If you are leading a group:** Review the primer together, then split into pairs to draft schemas in Lab 02. Pause to compare rules and discuss which ones matter most. In Lab 03, project the failure output and have the group interpret it before fixing data or rules.

## You Are Done When

Check your work against this list. You should have:

- [ ] `01-labs/lab-02/deliverables/validation_schema.py` with 6 to 10 checks for key columns
- [ ] A validation run on clean data that passes without errors
- [ ] A validation run on intentionally bad data that surfaces failures
- [ ] `01-labs/lab-03/validation_report.md` explaining which checks matter and why
- [ ] Notes connecting each check to a real risk (like unsafe publishing or broken joins)

If you have the validation schema and a report showing how it behaves on sample data, you have completed the core work for Day 03. The schema is your codified standard, and the report is evidence you can share with teammates.

## Troubleshooting at a Glance

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| ImportError for Pandera or pandas | Package not installed or wrong environment | Reinstall the package, restart runtime, confirm environment |
| Schema fails on unexpected columns | Column name mismatch | Align column names between dataset and schema |
| Date or numeric parsing errors | Wrong data type | Convert columns using pandas before validation |
| Failing rows unclear | Validation stops at first error | Use `lazy=True` to see all failures at once |
| Colab session resets | Session timeout | Rerun install cell, re-upload data, rerun validation |

For more troubleshooting, see [02-job-aids/troubleshooting.md](02-job-aids/troubleshooting.md).

## What Comes Next

Tomorrow in Day 04, you will package your validated data for sharing. You will gather the cleaned CSV, the validation report, licensing information, and citation details into a single folder. The goal is to make your work easy to cite, easy to trust, and easy to reuse.

The validation report you created today becomes part of that package. It shows downstream users that the data passed inspection and explains what "trustworthy" means in concrete terms.

## Take It Further

If you want to explore beyond today's labs:

- **Add a cross-column check:** Write a Pandera check that compares two columns, like "if rights is CC BY 4.0, then creator cannot be blank"
- **Try hypothesis testing:** Pandera can generate test data. Explore the hypothesis integration to see how it creates edge cases
- **Validate your own data:** Export a CSV from your collection system and write 5 checks based on what you know should be true
- **Compare schemas:** If you work with a partner, compare your schemas. Did you prioritize the same fields?
- **Read more about data contracts:** Explore how validation schemas fit into broader "data contract" practices in the data engineering world

## Reflection Prompts

Before you move on, take a moment to think about what you learned:

- What did validation catch that you would have missed by eyeballing the spreadsheet?
- Which check would you add first to your own collection data, and why?
- How would you explain a validation failure to a colleague who is not technical?

These questions do not have right answers. They help you connect today's practice to future situations in your own work.
