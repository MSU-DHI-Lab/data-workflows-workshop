# Primer Concepts

## What today is about
You will make messy metadata legible without losing meaning. The goal is to normalize values, document changes, and prepare for repeatable flows.

## Key concepts
- Normalization: making values consistent in format and wording without changing their meaning. Analogy: shelving books so all authors are filed the same way even if labels were printed differently.
- Controlled vocabularies: agreed lists of terms for subjects, places, or rights. Analogy: using a shared subject heading list so two catalogers do not invent new terms.
- Identifiers: stable labels that point to a record across systems. Analogy: an accession number that always refers to the same object.
- Provenance: the record of how data was sourced and changed. Keep it visible so others can trust the results.

## Why meaning can be lost
Meaning drifts when we over-normalize or merge near matches without context. Trimming spaces is safe; collapsing two different rights statements is not. Treat every change as reversible and documented.

## Why facet before changing values
Facets surface the spread of values so you do not guess. They show whether a variant is common or an outlier and keep you from collapsing meaningful differences.

## Why OpenRefine fits today
- Strengths: fast facets, clustering suggestions, undo/redo history, and exportable operations JSON for reproducibility.
- Limits: not an authority control system, not ideal for very large datasets. Use it for human-in-the-loop fixes before pipelines.
- Fit: quick wins in a 60–90 minute session with a clear history you can hand off.

## Links to learn pages
- Data lakes, warehouses, lakehouses: see `learn/data_lakes_warehouses_lakehouses.md`.
- Documentation that travels with data: see `learn/documentation_that_travels_with_data.md`.
- Licensing and rights: see `learn/licensing_for_datasets_and_media.md`.

## What success looks like today
- You identify high-impact fields (rights, place, creator) and normalize them without losing meaning.
- You export operations JSON and a cleaned CSV.
- You capture notes for data dictionary and README updates.

## Where people get stuck
- Over-merging similar values: use facets and check context before merging.
- Forgetting to record steps: export operations JSON and write brief notes.
- Losing rows on export: clear filters before exporting; verify row counts.
- Misreading controlled vocabularies: keep the allowed list visible while cleaning.
