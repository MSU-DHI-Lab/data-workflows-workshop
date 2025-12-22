# Troubleshooting

1) **Pandas cannot read the CSV (FileNotFoundError or parsing error)**  
   - Fix: Check that the file path is correct. The path is like an address telling Python where to find the file. If you are in Colab, you may need to re-upload the file (files disappear when the session ends). Make sure the file has headers in the first row and uses UTF-8 encoding.

2) **Validation rules report missing columns**  
   - Fix: Column names must match exactly, including capitalization and spaces. Check your data's column names and update either the data or the validation rules to match.

3) **Pandera import fails (ModuleNotFoundError)**  
   - Fix: Run the install cell again: `pip install pandera[pandas]`. Then restart the runtime (in Colab: Runtime > Restart runtime). Make sure you have internet access. Run cells from the top after restarting.

4) **All rows fail validation**  
   - Fix: Your validation rules may be too strict, or the data has unexpected values. Check for leading/trailing spaces in text columns (use `.strip()` to remove them). Review your allowed lists and ranges.

5) **Validation stops on first error (you only see one failure)**  
   - Fix: Add `lazy=True` when running validation. This tells Pandera to collect all failures instead of stopping at the first one. Example: `schema.validate(df, lazy=True)`

6) **Date column read as string (not recognized as dates)**  
   - Fix: Add `coerce=True` in your Column definition. This tells Pandera to try converting the values to the expected type. Or convert the column in pandas before validating: `df['date_column'] = pd.to_datetime(df['date_column'])`

7) **Report file not saved (file not appearing)**  
   - Fix: Check which folder you are running the notebook from. The file saves relative to that location. Make sure you have write permission. Try running the save cell again.

8) **Colleague cannot read the error messages**  
   - Fix: Add plain-language notes next to technical errors. Explain what each failure means and what to do about it. Share the markdown report file, not just the raw error output.
