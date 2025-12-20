# Lab 01: Import and Inspect with Facets

Goal: spot inconsistencies before changing anything. You will import a messy export, facet key columns, and write down three cleaning targets.

Inputs: `inputs/collection_export_raw.csv`
Outputs: Three written cleaning targets in your notes (or `05-artifacts/` if you want to capture them).
Time: ~15 minutes.

## Why facets first
Facets show you how many distinct values live in a column. They make patterns and outliers obvious without editing data. Starting with facets prevents accidental over-normalization and helps you focus on the highest-impact fixes.

## Steps
1) **Do:** Open OpenRefine and create a new project from `collection_export_raw.csv` (choose comma-separated).  
   **Why:** Importing sets the workspace and preserves the header row so facets map to the right columns.  
   **You should see:** The table preview with columns `id`, `title`, `creator`, `place`, `rights`, `description`, `date`.  
   **If it doesn't look right:** Re-import and ensure you selected CSV, not TSV; confirm the first row is treated as headers.

2) **Do:** Add a text facet on the `rights` column (Facet → Text facet).  
   **Why:** Rights statements often block reuse; seeing variants early shows how much normalization is needed.  
   **You should see:** A facet box with several variants like `CC BY-4.0`, `cc by 4.0`, `Public domain`.  
   **If it doesn't look right:** Make sure you selected the `rights` column; if the facet is empty, check that the column is not set to blank or filtered out.

3) **Do:** Add a text facet on the `place` column.  
   **Why:** Place names drive search and aggregation; facets reveal casing and punctuation differences.  
   **You should see:** Variants such as `NYC`, `New york City`, `Albany, N.Y.`.  
   **If it doesn't look right:** Clear any active filters; ensure the facet type is Text facet, not Timeline.

4) **Do:** Add a text facet on the `creator` column.  
   **Why:** Creator formatting affects attribution; facets reveal spacing issues and ordering differences.  
   **You should see:** Values like `Jane  Doe`, `Doe, Jane`, `Smith, A.`.  
   **If it doesn't look right:** Check the column name; remove other filters that might hide rows.

5) **Do:** Note three cleaning targets based on what you see (e.g., "Normalize rights to three allowed statements").  
   **Why:** Writing targets keeps scope realistic in a 60–90 minute window and guards against meaning loss.  
   **You should see:** A short list of priorities tied to the facets.  
   **If it doesn't look right:** Revisit facets to confirm the biggest variants; avoid making up changes you cannot justify.

6) **Do:** Save the project in OpenRefine (Project menu → Export → OpenRefine project archive) if you want a backup.  
   **Why:** Preserves the raw state before edits for easy rollback.  
   **You should see:** A downloaded `.tar.gz` project archive.  
   **If it doesn't look right:** Check browser download permissions; try a different browser if the save stalls.
