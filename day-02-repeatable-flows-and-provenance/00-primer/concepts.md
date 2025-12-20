# Primer Concepts

## What today is about
You will build a small, explainable flow in Apache NiFi that moves files from inbox to outbox, routes questionable records to quarantine, and captures a run record (NiFi calls this **Provenance**, meaning: a trace of what happened to a file) so you can show exactly what happened.

## Key concepts
- Repeatable flow: a sequence of steps that move and transform data. Analogy: a staged conservation workflow where an object moves from intake to cleaning to storage with logs at each station.
- Run record: recorded history of how a file moved and changed. Analogy: chain of custody for objects; knowing who handled it, when, and what was done.
- Lineage: NiFi’s graph view for one file. It lets you answer “where did this value come from?” without guessing.
- Quarantine routing: a deliberate path for suspect or invalid records so they do not mix with clean outputs. Analogy: pulling an object aside for condition concerns.

## Why NiFi fits today
- Strengths: drag-and-drop processors, built-in run record, back pressure on queues, easy routing for quarantine, and a rich set of file processors. Good for visual explainability.
- Limits: needs Docker/Java resources and uses address 8080; not ideal for heavy analytics. Use it for movement, light transforms, and traceability, then hand off to scripts if logic grows.

## Links to learn pages
- Repeatable flows and run record concepts connect to `learn/data_lakes_warehouses_lakehouses.md` for storage patterns.
- Documentation and publishing context connect to `learn/documentation_that_travels_with_data.md` and `learn/publishing_data_in_plain_language.md`.

## What success looks like today
- NiFi runs in Docker and UI is reachable at `http://localhost:8080/nifi/`.
- Inbox files flow to outbox with consistent rights text; questionable files land in quarantine.
- You can open the run record (NiFi Provenance view) for one file and explain each processor’s purpose.

## Where people get stuck
- Address conflicts on 8080: stop other services or change the mapped address.
- Forgetting to connect relationships: double-check RouteOnContent connections for quarantine and unmatched paths.
- Flow export confusion: use canvas right-click or top-right menu to download the flow definition.
- Quarantine not triggering: verify regex and attribute values; compare with `flow_blueprint.md`.
