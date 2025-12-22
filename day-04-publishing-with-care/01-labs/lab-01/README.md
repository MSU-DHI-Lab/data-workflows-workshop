# Lab 01: Build a Publishable Data Package

The goal of this lab is to assemble a ready-to-share package with data, documentation, and checks in one place. This takes about 20 minutes.

**Inputs:** `inputs/curated_collection.csv`

**Outputs:** `outputs/dataset-package/` folder containing `data/`, `docs/`, and `checks/` subfolders

## Before You Start

A "package" here means a folder structure that contains everything someone needs to understand and use your data. When you hand off a package, the recipient should not need to ask follow-up questions.

Good packages are self-contained. The data, the documentation, and the quality evidence all travel together.

---

## Step 1: Copy the Data File

Create the folder structure for your package:

```
outputs/dataset-package/
    data/
    docs/
    checks/
```

Copy `inputs/curated_collection.csv` into `outputs/dataset-package/data/`.

You should see the CSV inside the `data/` folder.

Keep the package self-contained. No external pointers, no links to files outside the folder. Someone who downloads this folder should have everything they need.

---

## Step 2: Create the README

Create `outputs/dataset-package/docs/README.md` with the following sections:

**Title:** Give your dataset a clear name.

**Source and date:** Where did this data come from? When was it exported?

**Purpose:** What is this dataset for? Who might use it?

**Sensitive fields or redactions:** Are there any columns with personal information? Were any values removed or obscured?

**How to reuse safely:** What should someone know before using this data? Point them to the rights column and citation file.

Here is an example you can adapt:

```markdown
# Dataset README

## Title
Curated Collection Export (Practice Package)

## Source and date
Exported from the collection management system on 2025-12-20.

## Purpose
Share a cleaned, consistent set of collection records for analysis and reuse.

## Sensitive fields or redactions
No direct personal identifiers are included. Free-text description fields were reviewed for accidental personal data.

## How to reuse safely
Use the rights column to guide reuse. Cite this package using CITATION.cff. If you transform fields, update your notes and the validation report.
```

Keep it concise. A good README answers the questions a new user would ask in their first five minutes with the data.

---

## Step 3: Create the Data Dictionary

Create `outputs/dataset-package/docs/data_dictionary.csv` with columns:
- Field
- Definition
- Type
- Allowed/Notes

Fill entries for each column in your dataset: id, title, creator, place, rights, date.

Example:

```csv
Field,Definition,Type,Allowed/Notes
id,Unique record identifier,integer,Must be greater than 0
title,Human-readable name for the record,string,Cannot be blank
creator,Person or organization that created the item,string,Last, First format preferred
place,Geographic location associated with the item,string,City, State format
rights,Reuse permissions for the item,string,Public Domain | CC BY 4.0 | Rights Reserved
date,Year associated with the item,integer,4-digit year
```

Save this file in `docs/`. It preserves field meanings so nobody has to guess what "rights" or "place" really means.

---

## Step 4: Document Origins and Changes

Create `outputs/dataset-package/docs/origins_and_changes.md` describing:
- Where the data originally came from
- What cleaning steps were applied (reference Day 01)
- What validation checks were run (reference Day 03)
- When this package was assembled

Keep it brief. A few sentences on each point is enough. The goal is trust: a reader can see the chain of custody.

---

## Step 5: Add Quality Evidence

Copy your validation reports from Day 03 into `outputs/dataset-package/checks/`.

If you have `validation_report.md` from Day 03 Lab 03, put it here. If you have other outputs like pass/fail summaries, include those too.

Quality evidence shows downstream teams that the data passed inspection. It is not just your word; it is documentation.

---

## Step 6: Review Your Package Structure

Your folder should now look like:

```
outputs/dataset-package/
    data/
        curated_collection.csv
    docs/
        README.md
        data_dictionary.csv
        origins_and_changes.md
    checks/
        validation_report.md
```

Walk through each file and make sure it makes sense. Imagine you are receiving this package for the first time. Would you know what to do with it?

---

## Step 7: Bundle the Package (Optional)

If you want a single file to hand off, zip the `dataset-package` folder.

Place the zip in `05-deliverables/` or wherever you store final outputs.

Bundling reduces the risk of missing files when you share the package by email or file transfer.

---

## Checkpoint

Before moving on, confirm:

- [ ] `outputs/dataset-package/data/` contains your CSV
- [ ] `outputs/dataset-package/docs/README.md` explains the dataset
- [ ] `outputs/dataset-package/docs/data_dictionary.csv` defines each field
- [ ] `outputs/dataset-package/docs/origins_and_changes.md` documents the data's history
- [ ] `outputs/dataset-package/checks/` contains your validation report

If all five are checked, you are ready for Lab 02.

---

## If Something Went Wrong

**Folder structure looks wrong:** Delete and recreate. The structure should match the example above exactly.

**README is too long or too short:** Aim for one page. If you find yourself writing paragraphs, break them into bullet points.

**Data dictionary is confusing:** Each row should answer "what does this column mean?" Keep definitions short and specific.

**Missing validation report:** Go back to Day 03 Lab 03 and generate it. If you skipped Day 03, note that in your package and explain what checks you would run in the future.
