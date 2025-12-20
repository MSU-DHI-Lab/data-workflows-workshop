# Troubleshooting

1) **Import looks garbled**  
   - Fix: Re-import and ensure the format is CSV; confirm UTF-8 encoding.

2) **Headers appeared as a row**  
   - Fix: During import, select "Use first row as column headers".

3) **Facet shows no values**  
   - Fix: Clear filters; make sure you selected the right column; switch facet type to Text facet.

4) **Too many rights variants remain**  
   - Fix: Apply the operations JSON; trim whitespace; check case sensitivity with a lowercase transform.

5) **Place normalization missed a spelling**  
   - Fix: Add a targeted text transform for that spelling; re-export the operations JSON.

6) **Creators reordered incorrectly**  
   - Fix: Undo the step; simplify to spacing fixes only; avoid automatic reordering for ambiguous names.

7) **Exported CSV has fewer rows**  
   - Fix: Ensure no filters are active; re-export with all rows; confirm row count before and after.

8) **Operations JSON is empty**  
   - Fix: Check the Undo/Redo tab for recorded steps; if empty, redo transforms and extract again.

9) **Colab upload fails**  
   - Fix: Refresh the notebook session; ensure the file is under size limits; retry the upload cell.

10) **Validation shows unexpected missing values**  
    - Fix: Inspect the column in OpenRefine; confirm no cells were blanked during trimming; restore from the saved project if needed.
