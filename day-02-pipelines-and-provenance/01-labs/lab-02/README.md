# Lab 02: Build a Minimal Flow (Inbox → Normalize → Outbox)

Goal: build an explainable NiFi flow that ingests files, normalizes rights text lightly, routes questionable files to quarantine, and writes clean files to an outbox.

Inputs: `../lab-02/inputs/` seeded with `intake_sample.csv`
Outputs: Cleaned files in `outputs/`, quarantined files in `quarantine/`, blueprint and settings in `artifacts/`
Time: ~30 minutes.

## Steps
1) **Do:** Start NiFi with `docker compose up` from `lab-01/` if not already running.  
   **Why:** Ensures the NiFi UI and mounted folders are available.  
   **You should see:** Logs showing NiFi started; UI reachable at `http://localhost:8080/nifi/`.  
   **If it doesn't look right:** Stop any previous run with `docker compose down`; retry `docker compose up`.

2) **Do:** On the canvas, drag a **GetFile** processor and set `Input Directory` to `/opt/nifi/inputs`, `Keep Source File` to `false`.  
   **Why:** Ingests from the shared inbox and avoids duplicates by removing picked-up files.  
   **You should see:** A green check on the processor after saving.  
   **If it doesn't look right:** Confirm the path exists inside the container; ensure the processor is enabled (right-click → Start).

3) **Do:** Add an **UpdateAttribute** processor; set a new attribute `rights.allowed` to `Public Domain,CC BY 4.0,Rights Reserved`.  
   **Why:** Stores the allowed tokens visibly for downstream checks; keeps policy in the flow, not someone’s head.  
   **You should see:** Processor turns valid after saving.  
   **If it doesn't look right:** Check for typos; ensure no required fields are empty; click Apply again.

4) **Do:** Connect GetFile → UpdateAttribute; configure the connection to drop nothing (default).  
   **Why:** Moves incoming FlowFiles into the metadata-enriched step.  
   **You should see:** A queue line between processors; status showing queued files after start.  
   **If it doesn't look right:** Make sure both processors are started; verify the connection is not self-looping.

5) **Do:** Add **ReplaceText**; set `Search Value` to `(?i)cc[- ]?by[- ]?4\.0`, `Replacement Value` to `CC BY 4.0`, `Evaluation Mode` to `Entire text`.  
   **Why:** Light normalization of rights variants without writing code; keeps content consistent.  
   **You should see:** Processor valid; no errors.  
   **If it doesn't look right:** Escape backslashes as shown; ensure Evaluation Mode is set.

6) **Do:** Add **RouteOnContent**; create a rule named `quarantine` with expression `^((?!Public Domain|CC BY 4.0|Rights Reserved).)*$` and enable `regex` match strategy.  
   **Why:** Any file lacking an allowed rights token is routed to quarantine instead of slipping through.  
   **You should see:** Processor valid with one relationship named `quarantine` plus `unmatched`.  
   **If it doesn't look right:** Check regex spelling; ensure the rule is enabled; look at the processor validation errors.

7) **Do:** Add two **PutFile** processors: one for `outputs` with Directory `/opt/nifi/outputs`, one for `quarantine` with Directory `/opt/nifi/quarantine`.  
   **Why:** Separate clean and suspect files; quarantine is a governance habit to make review explicit.  
   **You should see:** Both processors valid after setting directories.  
   **If it doesn't look right:** Confirm the directories exist (created in Lab 01 step 4); check permissions in Docker logs.

8) **Do:** Connect ReplaceText → RouteOnContent; RouteOnContent `unmatched` → PutFile (outputs); RouteOnContent `quarantine` → PutFile (quarantine).  
   **Why:** Directs clean files to the outbox and sends questionable ones to review.  
   **You should see:** Connections with labels showing relationships; queues showing counts when running.  
   **If it doesn't look right:** Edit connection settings to choose the right relationship; verify processors are running.

9) **Do:** Start all processors (select all → Start). Drop `intake_sample.csv` into `lab-02/inputs/` if not already there.  
   **Why:** Run the flow end-to-end to see routing and normalization in action.  
   **You should see:** FlowFiles moving; one file in outputs (normalized) and any non-matching files in quarantine.  
   **If it doesn't look right:** Check the bulletin board for processor errors; confirm the sample file exists and is not empty.

10) **Do:** Export a template/flow definition via the canvas menu: right-click the canvas or use the top-right global menu → “Download flow definition,” then save to `artifacts/flow_definition.json`.  
    **Why:** Captures the flow for reuse; pairs with the settings table in `flow_blueprint.md`.  
    **You should see:** A JSON file downloaded.  
    **If it doesn't look right:** Ensure you have permission to export; try both the canvas right-click and the global menu (nifi-logo dropdown) in newer NiFi versions.

11) **Do:** Record any adjustments to processor properties in `artifacts/flow_blueprint.md` so others can replay the exact setup.  
    **Why:** Written settings plus the flow file make the pipeline reproducible and auditable.  
    **You should see:** Updated notes reflecting your final configuration.  
    **If it doesn't look right:** Reopen processor configs and copy the values carefully; keep explanations short.
