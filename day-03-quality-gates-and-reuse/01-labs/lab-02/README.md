# Lab 02: Create Quality Checks with Pandera

Goal: codify 6–10 checks as Pandera validation rules, validate the clean dataset, and save the rules for reuse.

Inputs: `../lab-01/inputs/collection_cleaned.csv`
Outputs: Validation run, rules saved to `artifacts/validation_schema.py`
Time: ~30 minutes.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/watrall/data-workflows-workshop/blob/main/day-03-quality-gates-and-reuse/01-labs/lab-02/notebooks/lab02_pandera.ipynb)

## Steps
1) **Do:** Open `notebooks/lab02_pandera.ipynb` in Colab or locally and run the install cell.  
   **Why:** Ensures Pandera is available; Colab does not ship with it by default.  
   **You should see:** Install logs ending without errors.  
   **If it doesn't look right:** Rerun; check internet connectivity in Colab.

2) **Do:** Run the data load/import cell.  
   **Why:** Your validation rules must match column names and types; loading first avoids mismatches.  
   **You should see:** Dataframe preview with expected columns.  
   **If it doesn't look right:** Verify the CSV path and header row.

3) **Do:** Run the validation-rules definition cell (6–10 checks).  
   **Why:** Declares rules of trust in one place instead of scattered if-statements.  
   **You should see:** A rules object printed.  
   **If it doesn't look right:** Confirm column names; adjust allowed lists to match Lab 01 findings.

4) **Do:** Run the validation cell.  
   **Why:** Executes all checks and surfaces issues together.  
   **You should see:** Validated dataframe (same as input) if all checks pass.  
   **If it doesn't look right:** Read error messages; they tell you which column and value failed. Adjust data or checks.

5) **Do:** Save the rules to `artifacts/validation_schema.py` using the provided cell (this overwrites the existing file in this lab).  
   **Why:** Makes the checks portable and versionable for repeatable runs.  
   **You should see:** Confirmation message that the file was written to `artifacts/validation_schema.py`.  
   **If it doesn't look right:** Check path spelling; ensure the artifacts folder exists; run the notebook from inside `lab-02/` so the relative path resolves.

6) **Do:** Note for each check why it exists (e.g., `rights` allowed list prevents risky publishing).  
   **Why:** Captures intent so future maintainers keep or adjust checks with context.  
   **You should see:** Short notes you can drop into `05-artifacts/README.md`.  
   **If it doesn't look right:** Revisit Lab 01 profiling to anchor each check to an observed need.
