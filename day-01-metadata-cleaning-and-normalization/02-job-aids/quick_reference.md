# Quick Reference

## OpenRefine three moves
- Facet first: Text facets on key columns to see variants before editing.
- Transform carefully: Use simple GREL like `value.trim()` and clear replace rules; avoid irreversible merges.
- Export the recipe: Undo/Redo → Extract saves an operations file you can replay for the next data pull.

## Clustering in a nutshell
- What it is: Suggested groups of similar strings (e.g., `NYC` vs `New York City`).
- How to use: Review each cluster, merge only when meaning is clearly the same, and document decisions.
- Why it matters: Reduces duplicates without manual row-by-row edits.

## Operations export
- Path: Undo/Redo → Extract → Save. This is the most important artifact for reproducibility.
- Reuse: Apply the operations file to new projects via Undo/Redo → Apply.

## Common pitfalls to avoid
- Over-normalizing rights: Do not invent new statements; stick to allowed tokens.
- Hiding rows with filters: Clear filters before exporting so you do not drop data.
- Losing provenance: Capture your decisions in the artifacts README along with the operations file.
