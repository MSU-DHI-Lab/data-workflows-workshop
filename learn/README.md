# Data World Explainers (Plain Language)
## What this is
This folder gathers plain-language explainers that connect collections work to broader data concepts. Each page follows a consistent structure with examples, decision guides, and troubleshooting.
## Why it matters for collections and cultural heritage data
Collections teams often meet data-engineering terms when cleaning, validating, or publishing. These explainers reduce guesswork so you can adapt the workshop patterns back at your institution.
## A simple mental model
Analogy 1: Think of these pages as gallery labels for data practices. They tell you what you are looking at and why it matters.  
Analogy 2: Treat them like a field guide you carry on a survey. They give quick IDs and “what to do next” tips.
## A concrete example (mini case study)
Mini case study: A library team wants to publish a cleaned CSV with rights notes. They read the DOI and licensing explainers, choose CC BY for metadata, prepare .zenodo.json, and add the DOI to CITATION.cff. The team avoids conflicting licenses and keeps the package citable.
## How this shows up in this workshop
You will refer to these explainers when making tool choices (lakes vs warehouses), adding validation (schemas and checks), and publishing (DOIs, licensing, documentation).
## What “successful understanding” looks like
- You can explain core terms to a colleague without jargon.
- You can choose patterns (lake, warehouse, lakehouse) that fit your data stage.
- You can set up licenses and DOIs consistently across files.
- You can bundle documentation so data travels with meaning intact.
## Common misconceptions (and the gentle correction)
- Misconception: “These are just definitions.” Correction: Each page includes examples, decision guides, and fixes for common problems.
- Misconception: “I have to learn everything at once.” Correction: Use the pages as needed for the day you are on.
## Practical decision guide
- If you are cleaning: read the lake/warehouse/lakehouse and documentation pages.
- If you are validating: read the data vaults and documentation pages for history and trust concepts.
- If you are publishing: read the licensing, DOI, and publishing pages together.
- If you are designing pipelines: read the lake/warehouse/lakehouse page for storage choices.
- If you are sharing with partners: ensure your bundle follows the publishing and documentation pages.
## Troubleshooting and where people get stuck
- Problem: Jargon overload. Fix: use the local glossary at the end of each page and the root GLOSSARY.md.
- Problem: Conflicting definitions. Fix: align with GLOSSARY.md and the linked pages; avoid mixing terms.
- Problem: Unsure which page to read first. Fix: start with the topic that matches your current day’s task (cleaning, pipelines, validation, publishing).
- Problem: Time pressure. Fix: skim the “What this is,” “Why it matters,” and “Decision guide” sections first.
- Problem: Missing links. Fix: use relative paths in this folder; all referenced pages live here.
## Quick glossary (local to this page)
- Explainer: a focused, plain-language guide on one concept.
- Decision guide: a short set of if/then bullets to choose an approach.
- Provenance: record of origin and changes to data.
- License: permissions for reuse.
- DOI: persistent identifier for citation.
