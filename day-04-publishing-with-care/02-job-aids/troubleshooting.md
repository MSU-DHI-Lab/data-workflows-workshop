# Troubleshooting

1) **Not sure which license to choose**  
   - Fix: If you want others to reuse your data freely with credit, CC BY 4.0 is a common choice. If you want no restrictions at all, use CC0 (public domain). If data cannot be shared, note "Rights Reserved." Document your choice in the LICENSE file and README.

2) **CITATION.cff shows errors or will not validate**  
   - Fix: CITATION.cff uses YAML format, which is sensitive to spacing. Keep `cff-version: 1.2.0` at the top. Use spaces (not tabs) for indentation. Make sure each field has a value after the colon. Compare your file against the example in Lab 02.

3) **Invalid .zenodo.json (Zenodo rejects the file)**  
   - Fix: JSON files need exact syntax. Common mistakes: trailing commas after the last item, missing quotes around text, mismatched brackets. Use an online JSON validator (search "JSON validator") to check for errors. Required fields: title, upload_type, description, creators, license, version.

4) **Package missing documentation files**  
   - Fix: Go back to Lab 01 and make sure you created all the files: README, data dictionary, notes on what changed (provenance), and validation checks. These should all be in your dataset-package folder.

5) **Zenodo upload problems**  
   - Fix: Check that your files are not too large (Zenodo has a 50GB limit per file, but uploads can be slow for large files). Fill in all required metadata fields in the Zenodo form. Make sure you selected a license from the dropdown. Save as a draft first, then publish when everything looks correct.

6) **Streamlit app cannot find the data file**  
   - Fix: The app looks for files in specific locations relative to where you run it. Make sure `curated_collection.csv` is in the `dataset-package/data/` folder. Run the app from inside the `lab-03/` folder, not from elsewhere. Check the file path in `app.py` matches your folder structure.

7) **Validation report not showing in the Streamlit app**  
   - Fix: The app looks for `validation_report.md` in a specific location. Check where the app expects it (look at the `report_path` in `app.py`). Save your report file there. Stop the app (Ctrl+C in the terminal) and restart it to reload files.

8) **Colleagues confused by technical terms**  
   - Fix: Add a "How to read this" section at the top of your README explaining key terms. Replace jargon with plain language where possible. In validation reports, explain what each check means and what a failure indicates.
