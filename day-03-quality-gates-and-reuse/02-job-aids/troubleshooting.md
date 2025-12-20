# Troubleshooting

1) **Pandas can't read the CSV**  
   - Fix: Check path and encoding; ensure headers exist; re-upload in Colab if needed.

2) **Schema errors about missing columns**  
   - Fix: Ensure column names match exactly; adjust schema or rename columns in the data.

3) **Pandera import fails**  
   - Fix: Rerun the install cell; restart runtime if needed; ensure internet in Colab.

4) **All rows fail validation**  
   - Fix: Confirm allowed lists and ranges; check for leading/trailing spaces; adjust checks to match cleaned data realities.

5) **Validation stops on first error**  
   - Fix: Use `lazy=True` in `schema.validate` to collect all failures.

6) **Date column read as string**  
   - Fix: Add `coerce=True` in Column definitions or cast in pandas before validating.

7) **Report file not saved**  
   - Fix: Check working directory; ensure you have write access; rerun the report cell.

8) **Stakeholder can't read errors**  
   - Fix: Add plain-language notes next to failures (what it means, what to do next); share the markdown report.
