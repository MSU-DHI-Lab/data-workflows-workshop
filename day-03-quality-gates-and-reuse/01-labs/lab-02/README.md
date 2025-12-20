# Lab 02: Implement Quality Gates with Pandera

Goal: codify 6–10 checks as a Pandera schema, validate the clean dataset, and save the schema for reuse.

Inputs: `../lab-01/inputs/collection_cleaned.csv`
Outputs: Validation run, schema saved to `artifacts/validation_schema.py`
Time: ~30 minutes.

## Steps
1) **Do:** Open `notebooks/lab02_pandera.ipynb` in Colab or locally and run the install cell.  
   **Why:** Ensures Pandera is available; Colab does not ship with it by default.  
   **You should see:** Install logs ending without errors.  
   **If it doesn't look right:** Rerun; check internet connectivity in Colab.

2) **Do:** Run the data load/import cell.  
   **Why:** Schema must match column names and types; loading first avoids mismatches.  
   **You should see:** Dataframe preview with expected columns.  
   **If it doesn't look right:** Verify the CSV path and header row.

3) **Do:** Run the schema definition cell (6–10 checks).  
   **Why:** Declares rules of trust in one place instead of scattered if-statements.  
   **You should see:** A schema object printed.  
   **If it doesn't look right:** Confirm column names; adjust allowed lists to match Lab 01 findings.

4) **Do:** Run the validation cell.  
   **Why:** Executes all checks and surfaces issues together.  
   **You should see:** Validated dataframe (same as input) if all checks pass.  
   **If it doesn't look right:** Read error messages; they tell you which column and value failed. Adjust data or checks.

5) **Do:** Save the schema to `artifacts/validation_schema.py` using the provided cell (this overwrites the existing file in this lab).  
   **Why:** Makes the gate portable and versionable for pipelines.  
   **You should see:** Confirmation message that the file was written to `artifacts/validation_schema.py`.  
   **If it doesn't look right:** Check path spelling; ensure the artifacts folder exists; run the notebook from inside `lab-02/` so the relative path resolves.

6) **Do:** Note for each check why it exists (e.g., `rights` allowed list prevents risky publishing).  
   **Why:** Captures intent so future maintainers keep or adjust checks with context.  
   **You should see:** Short notes you can drop into `05-artifacts/README.md`.  
   **If it doesn't look right:** Revisit Lab 01 profiling to anchor each check to an observed need.
