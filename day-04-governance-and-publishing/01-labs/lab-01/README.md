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

2) **Do:** Create `outputs/dataset-package/docs/README.md` using the template below and fill in purpose, source, and reuse notes.  
   **Why:** README tells future users what this is and how to handle it safely.  
   **You should see:** A README with purpose, provenance, and reuse guidance saved in the docs folder.  
   **If it doesn't look right:** Make sure headings are present; keep it concise and friendly.

Template:
```
# Dataset README
- Title:
- Source and date:
- Purpose of this package:
- Sensitive fields or redactions:
- How to reuse safely:
```

3) **Do:** Create `outputs/dataset-package/docs/data_dictionary.csv` with columns `Field,Definition,Type,Allowed/Notes`. Fill entries for id, title, creator, place, rights, date.  
   **Why:** Data dictionary preserves meaning so fields are not misread.  
   **You should see:** A CSV with six rows and definitions saved in docs.  
   **If it doesn't look right:** Ensure the header row exists; save as UTF-8.

4) **Do:** Write a short provenance note in `outputs/dataset-package/docs/provenance.md` describing how the data was cleaned (reference Day 01–03 steps).  
   **Why:** Provenance is the chain of custody for data; it builds trust.  
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
