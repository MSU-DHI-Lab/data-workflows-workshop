# Quick Reference

## Three keep-it-simple moves
- Keep processors explainable: if you cannot describe a box in one sentence, split it or remove it.
- Facet the flow: use the run record and queues like facets. Look before changing settings.
- Export artifacts: download the flow definition and record key properties alongside it.

## Core processors used today
- GetFile: watch a folder and ingest files.
- UpdateAttribute: attach small bits of metadata for routing.
- ReplaceText: light make-values-consistent step without code.
- RouteOnContent: branch based on content checks.
- PutFile: land outputs (clean and quarantine).

## Quarantine habit
- Always route uncertain files somewhere visible.
- Document why a file was quarantined in the run record narrative.

## Run record checkpoints
- RECEIVE → ATTRIBUTES MODIFIED → CONTENT MODIFIED → ROUTE → WRITE.
- Use the graph view when explaining the flow to colleagues.
