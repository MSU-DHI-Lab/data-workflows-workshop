# Troubleshooting

1) **License uncertainty**  
   - Fix: Choose the least restrictive license that fits the data; CC BY 4.0 is common for metadata. Document your choice.

2) **CITATION.cff errors**  
   - Fix: Keep `cff-version: 1.2.0`; check indentation; use simple strings for fields like title and authors.

3) **Invalid .zenodo.json**  
   - Fix: Validate JSON; ensure required fields (title, upload_type, description, creators, license, version).

4) **Package missing docs**  
   - Fix: Re-run Lab 01; ensure README, data dictionary, provenance note, and checks are present.

5) **Zenodo upload issues**  
   - Fix: Check file size limits; fill all required metadata; ensure license is selected; retry after saving as draft.

6) **Streamlit app cannot find data**  
   - Fix: Place `curated_collection.csv` in `dataset-package/data/`; run the app from `lab-03/` so relative paths resolve.

7) **Validation report not showing in app**  
   - Fix: Save `validation_report.md` in `lab-03/`; restart the app to reload files.

8) **Stakeholders confused by jargon**  
   - Fix: Add plain-language notes in README and reports; include a short "how to read this" section.
