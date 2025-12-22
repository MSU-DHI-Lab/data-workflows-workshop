# Troubleshooting

1) **Import looks garbled (strange characters like Ã© instead of é)**  
   - Fix: Re-import and ensure the format is CSV. Select UTF-8 encoding. UTF-8 is a way of storing text that supports all languages and special characters. If the encoding is wrong, accented letters and symbols appear as gibberish.

2) **Headers appeared as a row (first row of data is column names)**  
   - Fix: During import, check the box that says "Use first row as column headers" or similar.

3) **Facet shows no values (left panel is empty)**  
   - Fix: Clear any active filters first. Make sure you selected the right column. Switch the facet type to "Text facet" (not Timeline or Numeric).

4) **Too many rights variants remain after cleaning**  
   - Fix: Apply the OpenRefine operations file if you have one. Try trimming whitespace (Edit cells > Common transforms > Trim leading and trailing whitespace). Check case sensitivity by converting to lowercase first.

5) **Place names still inconsistent**  
   - Fix: Add a targeted text transform for the specific spelling. After fixing, re-export the operations file so your changes are saved.

6) **Creators reordered incorrectly**  
   - Fix: Use Undo (Edit > Undo or the Undo/Redo tab) to go back. Simplify to spacing fixes only. Avoid automatic reordering for names that might be ambiguous.

7) **Exported CSV has fewer rows than expected**  
   - Fix: Make sure no filters are active (look at the top of the screen for any active facet filters). Click "Remove All" on the facet panel, then re-export.

8) **Operations file is empty after export**  
   - Fix: Check the Undo/Redo tab on the left side. If no steps are recorded, your transforms were not saved. Redo the transforms and try the export again.

9) **Colab upload fails**  
   - Fix: Refresh the browser tab. Make sure the file is not too large (under 25MB for Colab). Try the upload cell again. In Colab, files need to be re-uploaded each time you restart the session.

10) **Validation shows unexpected missing values**  
    - Fix: Inspect the column in OpenRefine; confirm no cells were blanked during trimming; restore from the saved project if needed.
