# Primer Concepts

## What today is about
You will make messy metadata legible without losing meaning. The goal is to normalize values, document changes, and prepare for repeatable flows.

## Key concepts
- Normalization: making values consistent in format and wording without changing their meaning. Think of sorting a box of cables: you group and label them so anyone can grab the right one without guessing.
- Controlled vocabularies: agreed lists of terms for subjects, places, or rights. Picture a toolbox with labeled compartments so everyone reaches for the same label instead of inventing new ones.
- Identifiers: stable labels that point to a record across systems. Imagine naming your home Wi-Fi network uniquely so every device knows exactly which one to join.
- Provenance: the record of how data was sourced and changed. Keep it visible so others can trust the results.

## Why meaning can be lost
Meaning drifts when we over-normalize or merge near matches without context. Trimming spaces is safe; collapsing two different rights statements is not. Treat every change as reversible and documented.

## Why facet before changing values
Facets surface the spread of values so you do not guess. They show whether a variant is common or an outlier and keep you from collapsing meaningful differences.

## Why OpenRefine fits today
- Strengths: fast facets, clustering suggestions, undo/redo history, and an exportable operations file (a saved record of the steps) for reproducibility.
- Limits: not an authority control system, not ideal for very large datasets. Use it for human-in-the-loop fixes before you move to repeatable steps.
- Fit: quick wins in a 60–90 minute session with a clear history you can hand off.

## Links to learn pages
- Data lakes, warehouses, lakehouses: see `learn/data_lakes_warehouses_lakehouses.md`.
- Documentation that travels with data: see `learn/documentation_that_travels_with_data.md`.
- Licensing and rights: see `learn/licensing_for_datasets_and_media.md`.

## What success looks like today
- You identify high-impact fields (rights, place, creator) and normalize them without losing meaning.
- You export an OpenRefine operations file and a cleaned CSV.
- You capture notes for data dictionary and README updates.

## Where people get stuck
- Over-merging similar values: use facets and check context before merging.
- Forgetting to record steps: export the OpenRefine operations file and write brief notes.
- Losing rows on export: clear filters before exporting; verify row counts.
- Misreading controlled vocabularies: keep the allowed list visible while cleaning.
