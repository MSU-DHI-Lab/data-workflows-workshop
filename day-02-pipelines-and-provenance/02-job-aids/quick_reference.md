# Quick Reference

## Three keep-it-simple moves
- Keep processors explainable: if you cannot describe a box in one sentence, split it or remove it.
- Facet the flow: use provenance and queues like facets. Look before changing settings.
- Export artifacts: download the flow definition and record key properties alongside it.

## Core processors used today
- GetFile: watch a folder and ingest files.
- UpdateAttribute: attach small bits of metadata for routing.
- ReplaceText: light normalization without code.
- RouteOnContent: branch based on content checks.
- PutFile: land outputs (clean and quarantine).

## Quarantine habit
- Always route uncertain files somewhere visible.
- Document why a file was quarantined in the provenance narrative.

## Provenance checkpoints
- RECEIVE → ATTRIBUTES MODIFIED → CONTENT MODIFIED → ROUTE → WRITE.
- Use lineage view when explaining the flow to stakeholders.
