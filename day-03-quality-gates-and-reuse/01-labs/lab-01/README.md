# Lab 01: Profile the Dataset (exploratory data analysis, sometimes called EDA)

Goal: practice professional curiosity before writing checks. You will load the cleaned CSV, inspect structure, missingness, and unique values.

Inputs: `inputs/collection_cleaned.csv`
Outputs: Notes on shape, missingness, and allowed lists (keep in `05-artifacts/` if you like)
Time: ~15 minutes.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/watrall/data-workflows-workshop/blob/main/day-03-quality-gates-and-reuse/01-labs/lab-01/notebooks/lab01_profile.ipynb)

## Steps
1) **Do:** Open `notebooks/lab01_profile.ipynb` in Colab or locally and run the first cell to load the CSV.  
   **Why:** Trust begins with a clean load; you need to see columns as the code will.  
   **You should see:** A 4-row preview with columns `id, title, creator, place, rights, date`.  
   **If it doesn't look right:** Check the file path; confirm the CSV has headers; re-upload in Colab if needed.

2) **Do:** Run the shape and dtypes cell.  
   **Why:** Confirms expected structure before you write validation rules.  
   **You should see:** `(4, 6)` and string types for text, integers for `id`/`date` if coercible.  
   **If it doesn't look right:** Look for extra header rows; ensure date is numeric or convertible.

3) **Do:** Run the missingness scan cell.  
   **Why:** Tells you which fields must be non-null in your checks.  
   **You should see:** Zero missing values in this sample.  
   **If it doesn't look right:** Note columns with missing values and plan checks accordingly.

4) **Do:** Run the unique values cell for `rights` and `place`.  
   **Why:** Informs allowed lists for validation.  
   **You should see:** Rights tokens `Public Domain`, `CC BY 4.0`, `Rights Reserved`; places `Albany`, `New York City`.  
   **If it doesn't look right:** Check for trailing spaces; consider trimming upstream; update allowed lists later in validation.

5) **Do:** Write 3–4 candidate checks based on what you saw (e.g., `id` not null and >0, rights in allowed list).  
   **Why:** Keeps the checks focused on highest-risk issues.  
   **You should see:** A short list of checks ready for Lab 02.  
   **If it doesn't look right:** Revisit the notebook outputs; prioritize checks that prevent publishing or join failures.
