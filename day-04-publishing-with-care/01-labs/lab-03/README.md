# Lab 03: Optional Streamlit Handoff Interface

Goal: give colleagues a simple way to browse the curated data and see quality status without touching notebooks.

Inputs: `../lab-01/outputs/dataset-package/data/curated_collection.csv`; optional `validation_report.md`
Outputs: A running local Streamlit app
Time: ~20 minutes.

## Steps
1) **Do:** Ensure `curated_collection.csv` is in `../lab-01/outputs/dataset-package/data/`.  
   **Why:** The app reads directly from the packaged data.  
   **You should see:** The file present in that path.  
   **If it doesn't look right:** Re-run Lab 01 copy step; confirm the filename.

2) **Do:** (Optional) Place `validation_report.md` from Day 03 into this lab folder.  
   **Why:** Shows quality status in the app for colleagues.  
   **You should see:** The markdown file in `lab-03/`.  
   **If it doesn't look right:** Re-run Lab 03 to generate the report; copy it here.

3) **Do:** From `lab-03/`, run `pip install streamlit` once (if needed), then `streamlit run app.py`.  
   **Why:** Starts the local app; Streamlit is fast to spin up and easy for non-technical users.  
   **You should see:** Streamlit opening a local URL with the dashboard.  
   **If it doesn't look right:** Install Streamlit (`pip install streamlit`) or check that Python is available; be sure you’re running the command inside `lab-03/` so paths resolve.

4) **Do:** In the app, filter by rights or place and review the row counts.  
   **Why:** Lets colleagues explore without editing data.  
   **You should see:** Filtered tables and a row count updating.  
   **If it doesn't look right:** Confirm the column names match the dataset; refresh the app.

5) **Do:** View the “Data Quality Status” section.  
   **Why:** Surfaces validation evidence alongside the data.  
   **You should see:** The markdown report if provided; otherwise an info message.  
   **If it doesn't look right:** Ensure `validation_report.md` exists; check file permissions.

6) **Do:** Stop the app with Ctrl+C when finished.  
   **Why:** Clean shutdown frees your terminal.  
   **You should see:** The server stops and the prompt returns.  
   **If it doesn't look right:** Press Ctrl+C again; close the browser tab.
