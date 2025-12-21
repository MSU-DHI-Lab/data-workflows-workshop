# Lab 02: Clean, Make Values Consistent, and Export a Reproducible Recipe

Goal: apply targeted fixes to rights, place, and creator fields, then export both the cleaned CSV and the OpenRefine operations file (a saved record of the steps).

Inputs:
- `../lab-01/inputs/collection_export_raw.csv`
- Optional: your saved OpenRefine project from Lab 01

Outputs:
- Cleaned CSV saved to `outputs/collection_cleaned.csv`
- Operations file saved to `artifacts/openrefine_operations.json` (a `.json` file meaning a structured text format; already provided; update with your own if you add steps)
- Data dictionary and dataset README starter files in `artifacts/`

Time: ~30 minutes.

## Why these fields and why we keep changes small
- **Rights:** high-impact for reuse; ambiguity blocks sharing. We make values consistent with a short allowed list without inventing new statements.
- **Place:** common search facet; small differences break aggregation. We make names consistent (city/state) while keeping the original intent.
- **Creator:** attribution needs consistency; we tidy spacing and a light Last, First pattern without pretending to do full authority control.
- The OpenRefine operations file is the most important outcome because it lets anyone replay your exact steps on future exports.

## Steps
1) **Do:** Open your Day 01 project in OpenRefine (or import the raw CSV again).  
   **Why:** Starts from the inspected data so your edits trace back to known issues.  
   **You should see:** The same rows and facets from Lab 01.  
   **If it doesn't look right:** Re-import the raw CSV and recreate the three facets to confirm the state matches your notes.

2) **Do:** Apply the provided operations file (`artifacts/openrefine_operations.json`) via Undo/Redo → Apply.  
   **Why:** Reusing a recipe speeds work and keeps changes reproducible.  
   **You should see:** Rights values collapse to three options; place values normalize; creator spacing cleans up.  
   **If it doesn't look right:** Ensure you selected `openrefine_operations.json`, not the CSV; check the Undo/Redo tab for errors and reapply.

3) **Do:** Add a text facet on `rights` to confirm only the allowed tokens remain.  
   **Why:** Quick validation that the rights cleanup stuck.  
   **You should see:** Only `CC BY 4.0`, `Public Domain`, `Rights Reserved`.  
   **If it doesn't look right:** Reapply the operations file; check for trailing spaces and run a trim transform on `rights` if needed.

4) **Do:** Add a text facet on `place` to confirm variants collapsed.  
   **Why:** Ensures place cleanup did not leave stray variants.  
   **You should see:** `New York City, NY` and `Albany, NY`.  
   **If it doesn't look right:** Look for capitalization differences; reapply the place transforms or adjust the expression and re-export the recipe.

5) **Do:** Spot-check `creator` values (5–10 rows) for spacing and order.  
   **Why:** Light formatting reduces duplicates, but we avoid heavy merging to prevent meaning loss.  
   **You should see:** Consistent `Last, First` or tidy versions of existing strings without invented names.  
   **If it doesn't look right:** Undo and adjust the creator transform to avoid reordering ambiguous names; keep changes minimal.

6) **Do:** Export the cleaned data as CSV to `outputs/collection_cleaned.csv` (Export → Comma-separated value).  
   **Why:** Creates the shareable file your colleagues will use.  
   **You should see:** A downloaded CSV with normalized rights and places.  
   **If it doesn't look right:** Confirm the export included headers; ensure no filters are active that might hide rows.

7) **Do:** Export your updated operations file (Undo/Redo → Extract → Save to `artifacts/openrefine_operations.json`).  
   **Why:** Captures the exact steps for reruns and makes future repeats much easier.  
   **You should see:** A file downloaded; it should list your transforms.  
   **If it doesn't look right:** Reopen the Undo/Redo tab to confirm steps exist; re-export and check that the file is not empty.

8) **Do:** Open `artifacts/data_dictionary_template.md` and `artifacts/dataset_readme_template.md`; fill them with your cleaned field definitions and notes, then save into `05-artifacts/` if desired.  
   **Why:** Documentation alongside the data preserves meaning and reuse context.  
   **You should see:** Completed files with every field described, rights guidance noted, and notes on where the file came from and what changed, saved alongside your cleaned CSV.  
   **If it doesn't look right:** Make sure you opened the markdown files, not the CSV; copy them afresh from `artifacts/` if you edited heavily.
