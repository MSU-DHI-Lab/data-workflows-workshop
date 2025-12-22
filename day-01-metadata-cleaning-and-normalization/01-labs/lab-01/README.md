# Lab 01: Import and Inspect with Facets

The goal of this lab is to spot inconsistencies before changing anything. You will import a messy export, facet key columns, and write down three cleaning targets. This takes about 15 minutes.

**Inputs:** `inputs/collection_export_raw.csv`

**Outputs:** Three written cleaning targets in your notes (save them in `05-deliverables/` if you want to keep them)

## Why Facets First

Facets show you how many distinct values live in a column. They make patterns and outliers obvious without editing data. Starting with facets prevents accidental over-editing and helps you focus on the highest-impact fixes.

Think of facets like sorting a messy drawer: you see what you actually have before deciding what to combine or throw away.

---

## Step 1: Create a New Project

Open OpenRefine and create a new project from `inputs/collection_export_raw.csv`. When the import dialog asks about format, choose comma-separated. Make sure the first row is treated as headers.

You should see a table preview with columns `id`, `title`, `creator`, `place`, `rights`, `description`, and `date`. Each column should have a meaningful header, not data values.

If something looks wrong, go back and reimport. Check that you selected CSV (not TSV) and that the header row option is enabled.

This is your first time using OpenRefine if you are new to the tool. Take a moment to look around the interface. The main area shows your data in rows and columns. The column headers have dropdown arrows that give you access to transforms and facets. The left side panel will show facets once you create them. The Undo/Redo tab at the top left tracks everything you do.

---

## Step 2: Facet the Rights Column

Click the dropdown arrow on the `rights` column header, then select Facet, then Text facet.

A facet box appears on the left side of the screen. It shows every distinct value in the rights column and how many rows have each value.

You should see several variants like `CC BY-4.0`, `cc by 4.0`, `Public domain`, and others. The exact variants depend on your sample file, but you will probably see inconsistent capitalization and punctuation.

If the facet box is empty, check that you selected the `rights` column and that no filters are hiding rows. Close any other facets that might be active.

Rights statements often determine whether data can be shared, so catching these variants early matters a lot.

---

## Step 3: Facet the Place Column

Now add a text facet on the `place` column using the same method: click the dropdown arrow, select Facet, then Text facet.

You should see variants like `NYC`, `New york City`, `Albany, N.Y.`, or similar. Place names drive search and aggregation, so small differences break grouping later.

If the facet looks wrong, clear any active filters first. Make sure the facet type is Text facet, not Timeline or another option.

---

## Step 4: Facet the Creator Column

Add a text facet on the `creator` column.

You should see values like `Jane  Doe` (with extra spaces), `Doe, Jane`, `Smith, A.`, or other formatting differences. Creator formatting affects attribution and deduplication.

If you do not see the facet, confirm the column name is correct and remove any filters hiding rows.

---

## Step 5: Identify Three Cleaning Targets

Look at all three facets and decide which problems to fix. Write down three cleaning targets based on what you see.

Good targets are specific and achievable. For example:
- "Normalize rights to three allowed statements: CC BY 4.0, Public Domain, Rights Reserved"
- "Standardize place names to City, State format"
- "Fix double spaces in creator names"

Writing targets keeps scope realistic in a 60-90 minute window and helps you avoid changing things that do not need to change.

If you are not sure what to prioritize, focus on fields that block downstream work. Rights affect sharing. Places affect search. Creators affect attribution.

---

## Step 6: Save a Backup (Optional)

If you want to save the raw state before making any changes, export a backup. Go to the Project menu, then Export, then OpenRefine project archive. This saves a `.tar.gz` file you can reimport later.

You should see the file download to your computer.

If the download stalls, check browser download permissions or try a different browser.

---

## Checkpoint

Before moving on, confirm:

- [ ] OpenRefine is running and shows your imported data
- [ ] You have facets visible for rights, place, and creator
- [ ] You have written down three cleaning targets

If all three are checked, you are ready for Lab 02.

---

## If Something Went Wrong

**Import looks garbled:** Reimport and confirm you selected CSV format with UTF-8 encoding.

**Headers appear as a data row:** During import, check the option to use the first row as column headers.

**Facets show no values:** Clear any filters, confirm you selected the right column, and switch the facet type to Text facet.

**Too many variants to read:** That is expected. Facets reveal the mess. You do not need to fix everything, just identify the highest-priority targets.
