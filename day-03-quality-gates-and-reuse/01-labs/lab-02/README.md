# Lab 02: Create Quality Checks with Pandera

The goal of this lab is to codify 6-10 checks as Pandera validation rules, run them against your cleaned dataset, and save the rules for reuse. This takes about 30 minutes.

**Inputs:** `../lab-01/inputs/collection_cleaned.csv` (the cleaned data from Lab 01, or your own cleaned CSV from Day 01)

**Outputs:**
- Validation run confirming the data passes
- Rules saved to `deliverables/validation_schema.py`

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MSU-DHI-Lab/data-workflows-workshop/blob/main/day-03-quality-gates-and-reuse/01-labs/lab-02/notebooks/lab02_pandera.ipynb)

## Before You Start

Pandera is a library that checks whether your data meets the rules you define. Instead of writing scattered if-statements, you describe what "good data" looks like in one place. Pandera then checks every row against those rules.

Think of it like a checklist that runs automatically. You say "this column must have these values" and Pandera tells you which rows break that rule.

---

## Step 1: Install Pandera

Open the notebook and run the install cell:

```python
!pip install pandera[pandas]
```

You should see installation logs ending without errors.

If installation fails, check your internet connection. In Colab, try Runtime > Restart runtime, then run the install cell again.

---

## Step 2: Load Your Data

Run the data load/import cell. It reads your cleaned CSV and shows a preview.

You should see the same columns from Lab 01: `id`, `title`, `creator`, `place`, `rights`, `date`.

If the load fails, check the file path. In Colab, upload the CSV if prompted. The notebook expects the file to be named `collection_cleaned.csv`.

---

## Step 3: Define Your Validation Schema

Run the validation-rules definition cell. This cell creates a Pandera schema with 6-10 checks.

A schema is a Python object that describes your data's structure. It lists each column, what type it should be, and what rules it must follow.

The sample schema includes checks like:
- `id` must be an integer greater than 0
- `rights` must be one of the allowed values
- `title` must not be blank

You should see the schema object printed without errors.

If you see a NameError, make sure you ran the import cell first. If you see column name errors, adjust the schema to match your actual column names.

---

## Step 4: Run Validation

Run the validation cell. It applies the schema to your data.

If all checks pass, you will see the validated dataframe (same as your input data) printed without error messages. This is your first time running a validation schema. A passing result means your data matches the rules you defined. It is a good feeling.

If any checks fail, you will see an error listing which column, which check, and which values failed. This is expected if your data does not match the rules. Read the error message to understand what went wrong.

For example, if you see "Check failed: isin" on the rights column, it means some rights values are not in your allowed list. Either fix the data or update the allowed list in your schema.

---

## Step 5: Save the Schema

Run the cell that saves the schema to `deliverables/validation_schema.py`.

This creates a Python file you can import in other projects. The schema is now portable and version-controllable.

You should see a confirmation message that the file was written.

If the save fails, check the file path. Make sure the `deliverables/` folder exists. Run the notebook from inside `lab-02/` so relative paths resolve correctly.

---

## Step 6: Document Why Each Check Exists

For each check in your schema, write a brief note explaining why it matters.

Examples:
- `rights in [...]` prevents publishing data with unclear reuse terms
- `id > 0` catches placeholder or error values
- `title not blank` ensures every record has a human-readable label

Save these notes alongside your schema or in the day’s `../../05-deliverables/README.md`. Documentation makes the checks understandable to future maintainers.

---

## Checkpoint

Before moving on, confirm:

- [ ] Pandera installed without errors
- [ ] Your validation schema has 6-10 checks
- [ ] Validation ran successfully on your cleaned data
- [ ] `deliverables/validation_schema.py` exists with your saved schema
- [ ] You have notes explaining why each check matters

If all five are checked, you are ready for Lab 03.

---

## If Something Went Wrong

**Pandera import fails:** Rerun the install cell, then restart the runtime (Runtime > Restart runtime in Colab), and run cells from the top.

**Schema fails on unexpected columns:** Your column names must match exactly. Check for trailing spaces or capitalization differences. Update either the data or the schema.

**All rows fail validation:** Your allowed lists or ranges may be too strict. Check Lab 01 profiling results and adjust the schema to match what the data actually contains.

**Type errors:** If a column is the wrong type (for example, dates stored as strings), add `coerce=True` to that column in the schema, or cast the column in pandas before validation.

**File not saved:** Check that you are running the notebook from the `lab-02/` folder and that `deliverables/` exists. Create the folder if missing.
