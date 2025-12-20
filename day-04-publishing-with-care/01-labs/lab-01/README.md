# Lab 01: Build a Publishable Data Package

Goal: assemble a ready-to-share package with data, documentation, and checks in one place.

Inputs: `inputs/curated_collection.csv`
Outputs: `outputs/dataset-package/` with `data/`, `docs/`, `checks/`
Time: ~20 minutes.

## Steps
1) **Do:** Copy `inputs/curated_collection.csv` into `outputs/dataset-package/data/`.  
   **Why:** Keeps the package self-contained; no external pointers needed.  
   **You should see:** The CSV inside `outputs/dataset-package/data/`.  
   **If it doesn't look right:** Check the path; ensure the file copied, not moved.

2) **Do:** Create `outputs/dataset-package/docs/README.md` using the guidance below and fill in purpose, source, and reuse notes.  
   **Why:** README tells future users what this is and how to handle it safely.  
   **You should see:** A README with purpose, notes on where the files came from and what changed, and reuse guidance saved in the docs folder.  
   **If it doesn't look right:** Make sure headings are present; keep it concise and friendly.

Create a README with these sections:
- Title
- Source and date
- Purpose
- Sensitive fields or redactions
- How to reuse safely

Example (edit values to match your dataset):
```
# Dataset README

## Title
Curated Collection Export (Practice Package)

## Source and date
Exported from the collection management system on 2025-12-20.

## Purpose
Share a cleaned, consistent set of collection records for analysis and reuse.

## Sensitive fields or redactions
No direct personal identifiers are included. Free-text description fields were reviewed for accidental personal data.

## How to reuse safely
Use the rights column to guide reuse. Cite this package using CITATION.cff. If you transform fields, update your notes on what changed and the validation report.
```

3) **Do:** Create `outputs/dataset-package/docs/data_dictionary.csv` with columns `Field,Definition,Type,Allowed/Notes`. Fill entries for id, title, creator, place, rights, date.  
   **Why:** Data dictionary preserves meaning so fields are not misread.  
   **You should see:** A CSV with six rows and definitions saved in docs.  
   **If it doesn't look right:** Ensure the header row exists; save as UTF-8.

4) **Do:** Write a short note on where the files came from and what changed in `outputs/dataset-package/docs/origins_and_changes.md` describing how the data was cleaned (reference Day 01–03 steps).  
   **Why:** This builds trust by making changes easy to review later.  
   **You should see:** A few sentences on source, cleaning, validation, and date saved in docs.  
   **If it doesn't look right:** Include the date and tools used; keep it plain-language.

5) **Do:** Save any validation reports or check outputs to `outputs/dataset-package/checks/` (reuse Day 03 outputs if available).  
   **Why:** Checks are evidence for downstream teams.  
   **You should see:** Markdown or text reports in the checks folder.  
   **If it doesn't look right:** Copy or export the report again; confirm file names are clear.

6) **Do:** Zip the `dataset-package` folder if you want a single bundle (practice path) and place it in `05-artifacts/` or keep as-is.  
   **Why:** Bundling reduces missing-file risk when handing off.  
   **You should see:** A zip file containing data, docs, and checks.  
   **If it doesn't look right:** Ensure the zip includes all subfolders; avoid double-nesting directories.
