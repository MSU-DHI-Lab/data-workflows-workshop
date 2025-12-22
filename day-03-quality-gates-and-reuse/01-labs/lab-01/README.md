# Lab 01: Profile the Dataset

The goal of this lab is to practice professional curiosity before writing checks. You will load the cleaned CSV, inspect its structure, look for missing values, and note unique values in key columns. This takes about 15 minutes.

Profiling is sometimes called "exploratory data analysis" or EDA. The idea is simple: look at your data before you make assumptions about it.

**Inputs:** `inputs/collection_cleaned.csv`

**Outputs:** Notes on shape, missingness, and allowed lists (save in `05-artifacts/` if you like)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MSU-DHI-Lab/data-workflows-workshop/blob/main/day-03-quality-gates-and-reuse/01-labs/lab-01/notebooks/lab01_profile.ipynb)

## Before You Start

This is your first time writing validation rules in Python. Do not worry if notebooks are new to you. The cells are pre-written, and you will run them one at a time to see what they do.

If something breaks, read the error message. Most errors in this lab come from file paths or missing uploads. The fixes are usually straightforward.

---

## Step 1: Open the Notebook

Click the "Open in Colab" badge above, or open `notebooks/lab01_profile.ipynb` in Google Colab manually.

Run the first cell to load the CSV. If you are using Colab, you may need to upload the file when prompted.

You should see a 4-row preview (or however many rows your sample has) with columns `id`, `title`, `creator`, `place`, `rights`, `date`.

If the load fails, check the file path. In Colab, make sure you uploaded the file during this session. The file should be named exactly `collection_cleaned.csv`.

---

## Step 2: Check Shape and Data Types

Run the shape and dtypes cell.

You should see something like `(4, 6)` meaning 4 rows and 6 columns. Data types should show `object` for text columns and `int64` for numeric columns like `id` or `date` (if they are integers).

If the shape is different from what you expect, check whether extra rows were introduced during cleaning, or whether some rows were dropped by mistake.

---

## Step 3: Scan for Missing Values

Run the missingness scan cell.

You should see zero missing values for all columns in this sample. If your real data has missing values, note which columns they are in.

Missing values matter because downstream processes may fail or produce wrong results if required fields are blank. Knowing which columns have gaps helps you write targeted checks.

---

## Step 4: Check Unique Values in Key Columns

Run the unique values cell for `rights` and `place`.

You should see:
- Rights tokens like `Public Domain`, `CC BY 4.0`, `Rights Reserved`
- Place values like `Albany`, `New York City` (or whatever standardized forms you used in Day 01)

These unique values become your allowed lists for validation. If you see unexpected values, you may need to go back to Day 01 and clean further, or accept them as valid and update your expectations.

If you see extra whitespace (like `"CC BY 4.0 "` with a trailing space), consider trimming upstream in OpenRefine.

---

## Step 5: Write Candidate Checks

Based on what you saw, write 3-4 candidate checks. These are plain-language rules you will turn into code in Lab 02.

Examples:
- `id` must not be null and must be greater than 0
- `rights` must be one of: Public Domain, CC BY 4.0, Rights Reserved
- `place` must not be blank
- `date` must be a 4-digit year between 1800 and 2030

Keep your checks focused on the highest-risk issues. What would break downstream work if it were wrong? What would embarrass you if it were published?

---

## Checkpoint

Before moving on, confirm:

- [ ] The notebook loaded your data successfully
- [ ] You know the shape (rows and columns) of your dataset
- [ ] You identified which columns have missing values (if any)
- [ ] You have a list of 3-4 candidate checks ready for Lab 02

If all four are checked, you are ready for Lab 02.

---

## If Something Went Wrong

**Notebook will not load the CSV:** Check the file path. In Colab, files must be uploaded each session. Make sure the filename matches exactly.

**Shape looks wrong:** Look for extra header rows or merged cells from the original export. Re-export from OpenRefine if needed.

**Columns have unexpected types:** Pandas guesses types based on content. If a column you expect to be numeric shows as `object`, the data may contain non-numeric values. Note this for validation.

**Unique values have extra whitespace:** This is common. You can trim in pandas (`df['column'].str.strip()`) or go back to OpenRefine and apply a trim transform.
