# Lab 03: Validate Basics in Colab

Goal: run quick checks on the cleaned CSV so you can share it confidently.

Inputs: `../lab-02/outputs/collection_cleaned.csv`
Outputs: Validation summary (copy into `05-artifacts/` or your notes)
Time: ~20 minutes.

## Why validate right after cleaning
Validation is different from cleaning: cleaning changes data; validation checks the results. Running checks immediately catches drop/miss issues before the file travels to someone else’s workflow.

## Steps
1) **Do:** Open `notebooks/day01_validation.ipynb` in Google Colab.  
   **Why:** Colab runs in the browser with no local installs, so everyone can follow along.  
   **You should see:** The notebook title and instructions.  
   **If it doesn't look right:** Upload the notebook to Colab via File → Upload notebook, or drag it into Colab if the direct link fails.

2) **Do:** Run the first code cell to upload your cleaned CSV when prompted.  
   **Why:** Colab needs the file in the session to run checks.  
   **You should see:** A file chooser followed by the filename listed.  
   **If it doesn't look right:** Re-export the CSV from OpenRefine, confirm it has headers, and retry the upload.

3) **Do:** Run the load-and-preview cell; confirm the filename matches your upload.  
   **Why:** Ensures the file reads correctly and columns appear as expected.  
   **You should see:** The first five rows with normalized `rights` and `place` values.  
   **If it doesn't look right:** Check for extra header rows; ensure the separator is a comma; re-upload if you see garbled text.

4) **Do:** Run the counts/missing-values cell.  
   **Why:** Confirms no rows vanished and highlights any empty fields to resolve.  
   **You should see:** Row count (8 for the sample) and near-zero missing values.  
   **If it doesn't look right:** Compare against the raw row count; if rows differ, re-export from OpenRefine without filters.

5) **Do:** Run the distinct rights/place cell.  
   **Why:** Verifies normalization stuck and no stray tokens remain.  
   **You should see:** Rights limited to `CC BY 4.0`, `Public Domain`, `Rights Reserved`; places limited to `New York City, NY` and `Albany, NY`.  
   **If it doesn't look right:** Reapply the operations JSON in OpenRefine, re-export, and rerun this notebook.

6) **Do:** Run the validation summary cell and copy the output into `05-artifacts/README.md` or your notes.  
   **Why:** Captures evidence for downstream teams and future reruns.  
   **You should see:** A short text block with row count, missing values, and distinct tokens.  
   **If it doesn't look right:** Ensure previous cells executed successfully; rerun from the top if needed.
