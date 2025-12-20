# Primer Concepts

## What today is about
You will build a small, explainable pipeline in Apache NiFi that moves files from inbox to outbox, routes questionable records to quarantine, and captures provenance so you can show exactly what happened.

## Key concepts
- Pipeline: a sequence of automated steps that move and transform data. Analogy: a staged conservation workflow where an object moves from intake to cleaning to storage with logs at each station.
- Provenance: recorded history of how data moved and changed. Analogy: chain of custody for objects; knowing who handled it, when, and what was done.
- Lineage: the path a specific record took through the pipeline. It lets you answer “where did this value come from?” without guessing.
- Quarantine routing: a deliberate path for suspect or invalid records so they do not mix with clean outputs. Analogy: pulling an object aside for condition concerns.

## Why NiFi fits today
- Strengths: drag-and-drop processors, built-in provenance, back pressure on queues, easy routing for quarantine, and a rich set of file processors. Good for visual explainability.
- Limits: needs Docker/Java resources and port 8080; not ideal for heavy analytics. Use it for movement, light transforms, and traceability, then hand off to scripts if logic grows.

## Links to learn pages
- Pipelines and provenance concepts connect to `learn/data_lakes_warehouses_lakehouses.md` for storage patterns.
- Documentation and publishing context connect to `learn/documentation_that_travels_with_data.md` and `learn/publishing_data_in_plain_language.md`.

## What success looks like today
- NiFi runs in Docker and UI is reachable at `http://localhost:8080/nifi/`.
- Inbox files flow to outbox with normalized rights text; questionable files land in quarantine.
- You can view provenance for a record and explain each processor’s purpose.

## Where people get stuck
- Port conflicts on 8080: stop other services or change the mapped port.
- Forgetting to connect relationships: double-check RouteOnContent connections for quarantine and unmatched paths.
- Flow export confusion: use canvas right-click or top-right menu to download the flow definition.
- Quarantine not triggering: verify regex and attribute values; compare with `flow_blueprint.md`.
