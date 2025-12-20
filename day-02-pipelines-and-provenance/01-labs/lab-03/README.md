# Lab 03: Add Quarantine and Walk Provenance

Goal: add a quarantine path for suspect files and trace one record through provenance to explain what happened.

Inputs: Flow from Lab 02, sample file(s) in `lab-02/inputs/`
Outputs: Quarantined files (if any), provenance notes in `artifacts/provenance_narrative_template.md`
Time: ~20 minutes.

## Steps
1) **Do:** In NiFi, select the **RouteOnContent** processor and confirm the `quarantine` relationship is connected to the quarantine PutFile.  
   **Why:** Ensures suspect files have a clear, separate destination.  
   **You should see:** A connection labeled `quarantine` leading to the quarantine PutFile.  
   **If it doesn't look right:** Reconfigure RouteOnContent rules; reconnect the relationship to the quarantine PutFile.

2) **Do:** Start all processors if they are stopped. Drop a file with an unexpected rights string (e.g., `Rights Unknown`) into `lab-02/inputs/`.  
   **Why:** Forces the quarantine path to demonstrate governance in action.  
   **You should see:** The file lands in `quarantine/`; the outbox remains unchanged for this file.  
   **If it doesn't look right:** Check the RouteOnContent regex (`^((?!Public Domain|CC BY 4.0|Rights Reserved).)*$`); confirm the quarantine PutFile directory exists and is writable; compare settings to `lab-02/artifacts/flow_blueprint.md`.

3) **Do:** In the NiFi UI, right-click the quarantined FlowFile in the queue and choose View provenance.  
   **Why:** Provenance shows the exact path and transformations. This is your trust story.  
   **You should see:** Events like RECEIVE, ATTRIBUTES MODIFIED, CONTENT MODIFIED, ROUTE, WRITE with timestamps.  
   **If it doesn't look right:** Ensure the flow is running; verify the file actually queued in quarantine; refresh provenance.

4) **Do:** Click the lineage graph for that FlowFile.  
   **Why:** Visual lineage makes it easy to explain the journey to stakeholders.  
   **You should see:** A simple chain from GetFile through each processor to quarantine PutFile.  
   **If it doesn't look right:** Confirm you selected the correct FlowFile; widen the time window in provenance search.

5) **Do:** Open `artifacts/provenance_narrative_template.md` and fill it out for this record.  
   **Why:** Captures the story of what happened and why quarantine fired. Key for governance and future audits.  
   **You should see:** A completed narrative with events and reasons.  
   **If it doesn't look right:** Revisit provenance to confirm the event order; keep notes brief but clear.

6) **Do:** Stop processors and `docker compose down` when finished.  
   **Why:** Clean shutdown avoids leftover state and frees resources.  
   **You should see:** Containers stop and the terminal prompt returns.  
   **If it doesn't look right:** Run `docker compose ps` to confirm status; rerun `docker compose down` if needed.
