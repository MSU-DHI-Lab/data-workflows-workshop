# Lab 02: Clean, Make Values Consistent, and Export a Reproducible Recipe

The goal of this lab is to apply targeted fixes to rights, place, and creator fields, then export both the cleaned CSV and the OpenRefine operations file. The operations file is the most important artifact because it captures your exact steps for future reruns.

This takes about 30 minutes.

**Inputs:**
- `../lab-01/inputs/collection_export_raw.csv`
- Optional: your saved OpenRefine project from Lab 01

**Outputs:**
- Cleaned CSV saved to `outputs/collection_cleaned.csv`
- Operations file saved to `deliverables/openrefine_operations.json`
- Data dictionary and dataset README starter files in `deliverables/`

## Why These Fields, and Why Keep Changes Small

**Rights:** High impact for reuse. Ambiguous rights statements block sharing. You will make values consistent with a short allowed list without inventing new statements.

**Place:** Common search facet. Small differences break aggregation. You will standardize names (city/state) while keeping the original intent.

**Creator:** Attribution needs consistency. You will tidy spacing and apply a light Last, First pattern without pretending to do full authority control.

The operations file matters because it lets anyone replay your exact steps on future exports. A CSV can be shared, but the operations file explains how you got there.

---

## Step 1: Open Your Project

Open your Day 01 project in OpenRefine. If you saved it from Lab 01, it should appear in your recent projects. If not, reimport the raw CSV from `../lab-01/inputs/collection_export_raw.csv`.

You should see the same rows and facets from Lab 01. If the data looks different, reimport the raw CSV and recreate the three facets from Lab 01 to confirm the starting state matches your notes.

---

## Step 2: Apply the Provided Operations File

OpenRefine can replay a saved set of transformations. A sample operations file is provided in `deliverables/openrefine_operations.json`. Applying it shows you how reproducibility works in practice.

Go to the Undo/Redo tab (top left of the screen), click Apply, and paste the contents of `deliverables/openrefine_operations.json`. Click Perform Operations.

You should see changes happen immediately. Rights values collapse to three options. Place values normalize. Creator spacing cleans up.

If something goes wrong, check that you pasted the JSON correctly and that the column names in the file match your dataset. Look at the Undo/Redo tab for error messages and try again.

---

## Step 3: Verify Rights Cleanup

Add a text facet on the `rights` column if one is not already visible.

You should see only three values: `CC BY 4.0`, `Public Domain`, `Rights Reserved`. No other variants should remain.

If you still see variants, reapply the operations file. Check for trailing spaces by running a trim transform: click the rights column dropdown, select Edit cells, then Common transforms, then Trim leading and trailing whitespace.

---

## Step 4: Verify Place Cleanup

Add a text facet on the `place` column.

You should see standardized values like `New York City, NY` and `Albany, NY`. No variants like `NYC` or `New york City` should remain.

If variants remain, look at the capitalization. You may need to reapply the place transforms or add a manual fix for a missed case. After fixing, re-export the recipe (Step 7) to capture your adjustment.

---

## Step 5: Spot-Check Creator Values

Look at 5 to 10 rows to confirm creator values have consistent spacing and a light Last, First format where that format already existed.

You should see values like `Doe, Jane` without double spaces. Avoid reordering names that were ambiguous in the original. Keep changes minimal.

If you see problems, undo the last step and simplify the creator transform. Small, conservative changes are better than aggressive cleanup that distorts meaning.

---

## Step 6: Export the Cleaned CSV

Go to the Export menu (top right), select Comma-separated value, and save the file as `outputs/collection_cleaned.csv`.

You should see a downloaded CSV with normalized rights and places. Open it briefly to confirm headers are present and rows look correct.

If rows are missing, check that no filters are active. Go back to OpenRefine, click "Remove All" on the facet panel to clear filters, then re-export.

---

## Step 7: Export Your Updated Operations File

Go to the Undo/Redo tab, click Extract, and copy the JSON. Save it to `deliverables/openrefine_operations.json`, replacing the sample file with your own version.

This captures the exact steps you applied. Anyone can replay this file on a new export to get the same results.

If the extracted JSON is empty, check the Undo/Redo tab for recorded steps. If nothing is there, your transforms may not have applied. Redo them and extract again.

---

## Step 8: Start the Documentation Files

Open `deliverables/data_dictionary_template.md` and `deliverables/dataset_readme_template.md`. Fill them with your cleaned field definitions and notes about what changed.

Save your completed versions into `05-deliverables/` or keep them alongside your cleaned CSV.

Documentation alongside the data preserves meaning and helps others understand your decisions. Even brief notes are valuable.

If you edited heavily and want a clean start, copy fresh templates from `deliverables/`.

---

## Checkpoint

Before moving on, confirm:

- [ ] `outputs/collection_cleaned.csv` exists and has consistent values
- [ ] `deliverables/openrefine_operations.json` contains your cleaning steps
- [ ] You started notes on your normalization decisions

If all three are checked, you are ready for Lab 03.

---

## If Something Went Wrong

**Values did not change as expected:** Check whether you applied the transformation to the correct column or had a filter active. Use Undo to step back and try again.

**Operations file will not apply:** Verify the JSON syntax. Check that column names in the file match your dataset exactly. Look for typos.

**Exported CSV has fewer rows:** Clear all filters before exporting. Compare the row count in OpenRefine to the exported file.

**Operations file is empty after extract:** Confirm you made changes. If the Undo/Redo list is empty, your transforms did not apply. Redo them manually.

**Non-UTF-8 characters after export:** Export using UTF-8 encoding. Reopen the file in a UTF-8 aware editor to confirm special characters display correctly.
