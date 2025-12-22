# Lab 03: Validate Basics in Colab

The goal of this lab is to run quick checks on the cleaned CSV so you can share it confidently. Validation is different from cleaning: cleaning changes data, validation checks the results.

This takes about 20 minutes.

**Inputs:** `../lab-02/outputs/collection_cleaned.csv`

**Outputs:** Validation summary (copy into `05-deliverables/` or your notes)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MSU-DHI-Lab/data-workflows-workshop/blob/main/day-01-metadata-cleaning-and-normalization/01-labs/lab-03/notebooks/day01_validation.ipynb)

## Why Validate Right After Cleaning

Running checks immediately catches drop/miss issues before the file travels to someone else's workflow. You want to confirm that the cleaning did what you expected and nothing unexpected happened along the way.

This is also your first time running Python code in this workshop. Do not worry if the notebook environment is new to you. You will run pre-written cells and read the output, not write code from scratch.

---

## Step 1: Open the Notebook in Colab

Click the "Open in Colab" badge above, or open `notebooks/day01_validation.ipynb` in Google Colab manually by going to https://colab.research.google.com and uploading the file.

You should see the notebook title and instructions at the top. Colab runs in your browser, so no local installation is needed.

If the direct link does not work, go to Colab, click File, then Upload notebook, and select the file from this lab folder.

---

## Step 2: Upload Your Cleaned CSV

Run the first code cell. It will prompt you to upload a file. Select your `collection_cleaned.csv` from Lab 02.

You should see a file chooser dialog, then the filename listed after upload completes.

If the upload fails, check that your file is under 25MB and try again. You can also try re-exporting the CSV from OpenRefine if the file seems corrupted.

Colab sessions are temporary. If you close the browser or the session times out, you will need to re-upload the file.

---

## Step 3: Load and Preview the Data

Run cell 2 (the cell under "Load the CSV and preview"). It reads your CSV into a table and shows the first few rows.

You should see the first five rows with consistent `rights` and `place` values reflecting your Lab 02 cleanup.

If the data looks garbled, check that the file has headers and uses comma separators. If you see extra header rows, the file may have been exported incorrectly. Re-export from OpenRefine with the correct settings.

---

## Step 4: Check Counts and Missing Values

Run cell 3 (under "Check counts and missing values"). It reports how many rows are in the file and whether any columns have blank values.

You should see a row count (8 for the sample) and near-zero missing values. If your cleaned data has more rows, the count will be higher.

If the row count is lower than expected, compare against the original raw file. Rows may have been filtered out during export. Go back to Lab 02 and re-export with filters cleared.

---

## Step 5: Check Distinct Values

Run cell 4 (under "Check distinct rights and place values"). It lists the unique values in those columns.

You should see:
- Rights limited to `CC BY 4.0`, `Public Domain`, `Rights Reserved`
- Places limited to the standardized values from your cleanup (for example, `New York City, NY` and `Albany, NY`)

If you see unexpected values, your cleaning may not have applied completely. Go back to Lab 02, reapply the operations file, re-export the CSV, and re-upload it here.

---

## Step 6: Copy the Validation Summary

Run cell 5 (the final code cell, under "Validation summary"). It prints a short text block with row count, missing values, and distinct tokens.

Copy this output into `05-deliverables/README.md` or your notes. This captures evidence for downstream teams and future reruns.

If the summary is empty, make sure the previous cells ran successfully. Rerun from the top of the notebook if needed.

---

## Checkpoint

Before moving on, confirm:

- [ ] The notebook ran without errors
- [ ] Row count matches your expected cleaned data
- [ ] Distinct values for rights and place match your Lab 02 targets
- [ ] You copied the validation summary to your deliverables

If all four are checked, you have completed Day 01.

---

## If Something Went Wrong

**Colab cannot see the uploaded file:** Confirm you uploaded the file in the current session. Colab sessions are temporary, so files disappear when the session ends. Re-upload if needed.

**Import errors for pandas or pandera:** Run the install cell at the top of the notebook, then restart the runtime (Runtime menu, then Restart runtime) and run cells from the top.

**Validation shows unexpected missing values:** Inspect the column in OpenRefine. Confirm no cells were blanked during trimming. If needed, restore from the saved project and re-clean.

**Notebook will not run at all:** Check your internet connection. Colab requires an active connection. If Colab is down, try again later or switch to a local Python environment.
