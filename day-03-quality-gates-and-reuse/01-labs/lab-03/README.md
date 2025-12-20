# Lab 03: Generate Quality Report and Practice with Known Failures

Goal: run your Pandera schema against a dataset with intentional issues, read the failures, and produce a markdown report stakeholders can understand.

Inputs: `inputs/collection_with_failures.csv`, `artifacts/validation_schema.py`
Outputs: `validation_report.md` plus your notes
Time: ~20 minutes.

## Steps
1) **Do:** Open `notebooks/lab03_report.ipynb` in Colab or locally (run it from `lab-03/`) and run the install cell.  
   **Why:** Ensures Pandera is available in this session and paths resolve to the schema and inputs.  
   **You should see:** Successful install logs.  
   **If it doesn't look right:** Rerun the cell; verify internet access; confirm you are running from `lab-03/` so imports find `../lab-02/artifacts/validation_schema.py`.

2) **Do:** Run the schema import and data load cell.  
   **Why:** Uses the same rules on a dataset with known issues to see real failures.  
   **You should see:** A preview with some suspect values (missing id, bad rights token, far future date).  
   **If it doesn't look right:** Check paths; ensure `validation_schema.py` exists in `artifacts/` and you are running the notebook from `lab-03/` so the relative import works.

3) **Do:** Run the validation try/except cell.  
   **Why:** Collects all failures (`lazy=True`) so you see the full picture.  
   **You should see:** A table of failure cases showing column, check, and failing value.  
   **If it doesn't look right:** Confirm the schema imported; ensure the dataset columns match the schema.

4) **Do:** Run the report generation cell to create `validation_report.md`.  
   **Why:** Reports are artifacts for stakeholders. They are clear, portable evidence of what failed.  
   **You should see:** Printed report text and a saved `validation_report.md`.  
   **If it doesn't look right:** Verify `validation_errors` is populated; rerun validation with `lazy=True`.

5) **Do:** Add a short reflection in your notes: which checks caught what, and what you would do next (fix data, adjust checks, quarantine).  
   **Why:** Connects failures to actions; shows governance, not just tooling.  
   **You should see:** A few bullet points you can share with teammates.  
   **If it doesn't look right:** Re-read the failure cases; tie each to a specific check and risk prevented.
