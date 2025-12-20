# Lab 02: Licensing, Citation, and Zenodo Metadata (Practice + Live Paths)

Goal: prepare legal and descriptive artifacts for publishing; optionally deposit to Zenodo.

Inputs: `../lab-01/outputs/dataset-package/`
Outputs: LICENSE, CITATION.cff, .zenodo.json, publishing checklist; optional DOI
Time: ~30 minutes.

## Steps
1) **Do:** Choose and confirm your license in `artifacts/LICENSE` (e.g., CC BY 4.0).  
   **Why:** Sets reuse expectations; avoids ambiguity.  
   **You should see:** Clear license text.  
   **If it doesn't look right:** Revisit license choice against data sensitivity; avoid adding terms beyond the license.

2) **Do:** Update `artifacts/CITATION.cff` with title, authors, version, and date.  
   **Why:** Provides a citable reference; DOIs and users rely on this.  
   **You should see:** YAML (a human-friendly text format for structured data) with your details, `cff-version: 1.2.0` intact.  
   **If it doesn't look right:** Check indentation and field names; keep strings quoted only if needed.

3) **Do:** Fill `artifacts/.zenodo.json` with your metadata (title, description, creators, keywords, license, version).  
   **Why:** Zenodo uses this to populate the deposit and DOI landing page.  
   **You should see:** Valid JSON (a structured text format for storing data) with your entries.  
   **If it doesn't look right:** Validate the JSON; ensure required fields are present.

4) **Do:** Walk through `publishing_checklist.md` and tick completed items.  
   **Why:** Ensures no artifact is missing before practice or live paths.  
   **You should see:** Checked boxes for docs, license, citation, metadata.  
   **If it doesn't look right:** Return to Lab 01 to fill gaps (README, dictionary, notes on what changed, checks).

5) **Do (Practice path):** Zip `dataset-package/` plus LICENSE, CITATION.cff, .zenodo.json; place the zip in `05-artifacts/`.  
   **Why:** Tests package completeness without an external deposit.  
   **You should see:** A zip containing data, docs, checks, and metadata files from Lab 01.  
   **If it doesn't look right:** Re-zip ensuring folder structure stays intact.

6) **Do (Live path, optional):** In Zenodo, create a new upload, add the package files, paste metadata from `.zenodo.json`, choose the license, and reserve/mint a DOI.  
   **Why:** A DOI makes the package citable and version-clear (skip this step if staying on the practice path).  
   **You should see:** A Zenodo draft or published record with a DOI link.  
   **If it doesn't look right:** Ensure required fields are filled; check file size limits; verify license selection.

7) **Do:** If you minted a DOI, add it to `CITATION.cff` (`doi:` field) and to your package `docs/README.md`.  
   **Why:** Keeps the DOI visible inside the package for offline readers.  
   **You should see:** DOI recorded in both files.  
   **If it doesn't look right:** Edit and save again; keep formatting consistent.
