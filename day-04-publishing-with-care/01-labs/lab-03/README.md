# Lab 03: Optional Streamlit Handoff Interface

The goal of this lab is to give colleagues a simple way to browse the curated data and see quality status without touching notebooks. This is optional. If you skip it, you still complete Day 04 successfully.

This takes about 20 minutes.

**Inputs:**
- `../lab-01/outputs/dataset-package/data/curated_collection.csv`
- Optional: `validation_report.md` from Day 03

**Outputs:** A running local Streamlit app

## Before You Start

Streamlit is a Python tool that creates simple web apps from scripts. You do not need to know web development. You run a command, and a browser-based dashboard appears.

This lab is optional because not everyone needs an app. If you are handing off to colleagues who are comfortable with files and folders, the package from Lab 01 and Lab 02 is enough. The app is useful when you want a friendlier preview.

---

## Step 1: Confirm Data Is in Place

Check that `../lab-01/outputs/dataset-package/data/curated_collection.csv` exists.

The app reads directly from this path. If the file is missing, go back to Lab 01 and copy it.

---

## Step 2: Add the Validation Report (Optional)

This lab folder includes a sample `validation_report.md`. If you have your own `validation_report.md` from Day 03, copy it into this lab folder (`lab-03/`) and replace the sample.

The app can display this report in a "Data Quality Status" section. It shows colleagues that the data passed inspection.

If you do not have the report, the app will show an info message instead. This is fine for the practice path.

---

## Step 3: Install Streamlit

Open a terminal in the `lab-03/` folder and run:

```
pip install streamlit
```

You should see installation output ending without errors.

If installation fails, check your Python environment. Make sure you are using Python 3.9 or newer. Try running in a virtual environment if your system Python has restrictions.

---

## Step 4: Launch the App

From the `lab-03/` folder, run:

```
streamlit run app.py
```

Your browser should open automatically to a local URL like `http://localhost:8501`.

You should see a dashboard with your data displayed in a table. If you added the validation report, you should see it in the quality status section.

If the browser does not open, copy the URL from the terminal and paste it into your browser manually.

---

## Step 5: Explore the App

Try the filters. Select different values in the rights or place dropdowns and watch the table update.

Look at the row counts. They should match what you expect from your data.

If you included the validation report, find the "Data Quality Status" section and confirm it displays correctly.

---

## Step 6: Stop the App

When you are finished exploring, go back to your terminal and press **Ctrl+C** (hold the Control key and press C).

> **Note:** In a terminal, Ctrl+C means "stop the running program" — it is NOT copy/paste like in other applications.

The server stops and your terminal prompt returns (the blinking cursor waiting for your next command).

---

## Checkpoint

Before moving on, confirm:

- [ ] Streamlit installed without errors
- [ ] The app launched and displayed your data
- [ ] You could filter by rights or place
- [ ] (Optional) The validation report appeared in the app

If all items are checked, you have completed the optional Lab 03.

---

## If Something Went Wrong

**Module not found:** Run `pip install streamlit` again. Make sure you are in the same Python environment where you want to run the app.

**App cannot find the data file:** Run the app from the `lab-03/` folder. The script uses relative paths. If you run from a different folder, the paths break.

**Validation report not showing:** Confirm `validation_report.md` is in the `lab-03/` folder (not in a subfolder). Restart the app after adding the file.

**Browser did not open:** Copy the local URL from the terminal output and paste it into your browser.

**App crashes with an error:** Read the error message in the terminal. Common issues are missing dependencies (install them with pip) or file path errors (check that the data file exists where the app expects it).
