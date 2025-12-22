# Primer Concepts

## What today is about
You will build a small, explainable flow in Apache NiFi that moves files from inbox to outbox, routes questionable records to quarantine, and captures a run record (NiFi calls this **Provenance**, meaning: a trace of what happened to a file) so you can show exactly what happened.

## Key concepts
- Repeatable flow: a sequence of steps that move and transform data. Imagine a kitchen prep line: ingredients move from wash to chop to cook with a label at each station so nothing is missed.
- Run record: recorded history of how a file moved and changed. Think of a delivery tracking log that shows every handoff and timestamp so you can explain where a package went.
- Lineage: NiFi’s graph view for one file. It lets you answer “where did this value come from?” without guessing.
- Quarantine routing: a deliberate path for suspect or invalid records so they do not mix with clean outputs. Picture setting a questionable item aside on a separate shelf until you can inspect it.

## Why NiFi fits today
- Strengths: drag-and-drop processors, built-in run record, back pressure on queues, easy routing for quarantine, and a rich set of file processors. Good for visual explainability.
- Limits: NiFi runs inside Docker (a program that packages software). It uses port 8080 (a numbered door on your computer where your browser connects). Not ideal for heavy analytics. Use it for movement, light transforms, and traceability, then hand off to scripts if logic grows.

## Links to learn pages
- Repeatable flows and run record concepts connect to `learn/data_lakes_warehouses_lakehouses.md` for storage patterns.
- Documentation and publishing context connect to `learn/documentation_that_travels_with_data.md` and `learn/publishing_data_in_plain_language.md`.

## What success looks like today
- NiFi runs inside a Docker container and the interface is reachable at `http://localhost:8080/nifi/`.
- Inbox files flow to outbox with consistent rights text; questionable files land in quarantine.
- You can open the run record (NiFi Provenance view) for one file and explain each processor’s purpose.

## Where people get stuck
- Port 8080 already in use: another program is using that port (numbered door). Stop the other program or change the port in the recipe file (`docker-compose.yml`).
- Forgetting to connect relationships: double-check RouteOnContent connections for quarantine and unmatched paths.
- Flow export confusion: use canvas right-click or top-right menu to download the flow definition.
- Quarantine not triggering: verify regex and attribute values; compare with `flow_blueprint.md`.
