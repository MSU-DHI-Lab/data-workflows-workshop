# Lab 03: Generate Quality Report and Practice with Known Failures

The goal of this lab is to run your Pandera validation rules against a dataset with intentional issues, read the failures, and produce a markdown report colleagues can understand. This takes about 20 minutes.

**Inputs:**
- `inputs/collection_with_failures.csv` (a dataset with intentional problems)
- `../lab-02/deliverables/validation_schema.py`

**Outputs:**
- `validation_report.md` in this lab folder
- Notes on what you would do next (fix data, adjust checks, or quarantine)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MSU-DHI-Lab/data-workflows-workshop/blob/main/day-03-quality-gates-and-reuse/01-labs/lab-03/notebooks/lab03_report.ipynb)

## Before You Start

Lab 02 validated clean data. This lab validates intentionally bad data to see what failure looks like.

Seeing failures is important. In real work, you will encounter problems. Knowing how to read error messages and explain them to others is a core skill.

---

## Step 1: Open the Notebook and Install Dependencies

Open `notebooks/lab03_report.ipynb` in Colab or locally.

Run the install cell if prompted. You should see Pandera install successfully.

In Colab, the notebook will clone this repo into `/content/data-workflows-workshop` so it can read the lab files.

In Colab, you can also upload `validation_schema.py` (from Lab 02) and `collection_with_failures.csv` directly into the Colab Files panel, and the notebook will use those instead.

---

## Step 2: Load the Schema and Bad Data

Run the rules import and data load cell.

The notebook loads your validation schema from Lab 02 and reads `collection_with_failures.csv`, a dataset with known issues. It will prefer uploaded files in Colab, otherwise it uses the repo versions.

You should see a preview of the data. Look for suspicious values: a missing id, a bad rights token, a date far in the future.

If the schema import fails, check the file path. Make sure `validation_schema.py` exists in `../lab-02/deliverables/` and that you are running from `lab-03/`.

---

## Step 3: Run Validation with lazy=True

Run the validation try/except cell. The `lazy=True` option tells Pandera to collect all failures instead of stopping at the first one.

You should see a table of failure cases. Each row shows:
- Which column failed
- Which check failed
- What value caused the failure

Read through the failures. Can you connect each one to a rule in your schema?

If no failures appear, the test data may not actually violate your rules. Check that the bad file has genuinely invalid values.

---

## Step 4: Generate the Markdown Report

Run the report generation cell. It creates `validation_report.md` with a summary of failures.

You should see the report text printed in the notebook and a message confirming the file was saved.

The report should be readable by someone who does not know Pandera. It explains what failed, why it matters, and what to do next.

If the file does not save, check your working directory and write permissions.

---

## Step 5: Reflect on What You Would Do Next

For each failure, decide:
- **Fix the data:** The value is wrong and should be corrected
- **Adjust the check:** The rule is too strict and the value is actually valid
- **Quarantine:** The record is problematic and should be set aside for review

Write a few bullet points connecting failures to actions. This shows careful review, not just running tools.

Add your notes to the report or keep them in the day’s `../../05-deliverables/README.md`.

---

## Checkpoint

Before moving on, confirm:

- [ ] Validation ran against the bad data and found failures
- [ ] You can explain what each failure means in plain language
- [ ] `validation_report.md` exists with a clear summary
- [ ] You have notes on what you would do next for each failure type

If all four are checked, you have completed Day 03.

---

## If Something Went Wrong

**Schema import fails:** Check the file path. The notebook expects the schema at `../lab-02/deliverables/validation_schema.py`. Run from `lab-03/` so relative paths work.

**No failures found:** The test data may accidentally pass your rules. Check that `collection_with_failures.csv` has genuinely invalid values (wrong rights tokens, missing ids, bad dates).

**Failure messages are confusing:** Use `lazy=True` to see all errors at once. Each failure row includes the column name, check name, and failing value. Match these to your schema rules.

**Report file not saving:** Check write permissions and working directory. Try saving to a different location or copying the output manually.

**Colab session reset:** Rerun the install cell, re-upload data files, and rerun from the top.
