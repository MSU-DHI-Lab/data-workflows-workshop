# Lab 03: Add Quarantine and Review the Run Record

The goal of this lab is to verify quarantine routing works and trace one file through NiFi's run record (called "provenance") to explain what happened. This takes about 20 minutes.

**Inputs:** Your flow from Lab 02, sample files in `inputs/`

**Outputs:** Quarantined files (if any), run record notes in `deliverables/provenance_narrative_template.md`

## Key Terms

**Provenance** is NiFi's built-in run record. It logs every event that happens to a file: when it was received, how it was modified, where it was routed, and when it was written.

**Lineage** is NiFi's graph view for one file. It shows the chain of events visually, making it easy to explain a file's journey to colleagues.

---

## Step 1: Confirm Quarantine Routing Is Connected

Open the NiFi canvas and find the RouteOnContent processor.

Check that the `quarantine` relationship is connected to the quarantine PutFile processor. You set this up in Lab 02, but it is worth confirming.

You should see a line from RouteOnContent to the quarantine PutFile, labeled with the quarantine relationship.

If the connection is missing, create it now: drag from RouteOnContent, select the `quarantine` relationship, and connect to the quarantine PutFile.

---

## Step 2: Test Quarantine with a Bad File

Create a test file with an unexpected rights string. You can copy `intake_sample.csv` and edit the rights value to something invalid like `Rights Unknown`.

Save the modified file into `inputs/`.

Start all processors if they are not already running. Wait a moment for the file to process.

You should see the file appear in the `quarantine/` folder, not the `outputs/` folder. This confirms the routing rule is working.

If the file went to outputs instead, check your RouteOnContent regex. The pattern should match files that do NOT contain any allowed rights token.

---

## Step 3: View Provenance for the Quarantined File

Right-click on the queue leading into the quarantine PutFile (or right-click on the quarantine PutFile itself) and look for "View provenance" or "View data provenance."

A list of events appears. Find the events for your test file.

You should see a sequence like:
- RECEIVE (file picked up by GetFile)
- ATTRIBUTES_MODIFIED (UpdateAttribute added the allowed list)
- CONTENT_MODIFIED (ReplaceText tried to normalize)
- ROUTE (RouteOnContent decided this file goes to quarantine)
- SEND or DROP (PutFile wrote the file)

If you do not see events, make sure the flow processed a file recently. Provenance events have timestamps, so you may need to adjust the time filter.

---

## Step 4: View the Lineage Graph

Select one provenance event and click the lineage icon (it may look like a small graph or flowchart).

A visual graph appears showing the file's path through each processor.

You should see a chain from GetFile through each step to the quarantine PutFile. This is your trust story: you can point to this graph and say "here is exactly what happened to that file."

If the lineage looks incomplete, try widening the time window or selecting a different event for the same file.

---

## Step 5: Write a Provenance Narrative

Open `deliverables/provenance_narrative_template.md` and fill it out for the file you traced.

Document:
- What file did you trace?
- What events appeared in the provenance view?
- Why did the file end up in quarantine?
- What would you tell a colleague who asked what happened?

This narrative captures the story in plain language. The provenance graph is evidence, and the narrative explains what it means.

---

## Step 6: Stop NiFi

When you are finished, go to your terminal and press Ctrl+C to stop NiFi. Then run:

```
docker compose down
```

This shuts down the containers cleanly and frees resources.

---

## Checkpoint

Before moving on, confirm:

- [ ] At least one file landed in `quarantine/` based on your routing rule
- [ ] You viewed the provenance for that file and saw the event sequence
- [ ] You viewed the lineage graph for a single file
- [ ] `deliverables/provenance_narrative_template.md` is filled out

If all four are checked, you have completed Day 02.

---

## If Something Went Wrong

**Provenance view is empty:** Check that the flow actually processed a file. Provenance only shows events that happened. If nothing moved, there is nothing to trace.

**Lineage graph is confusing:** Focus on one file at a time. If you processed many files, filter by filename or narrow the time window.

**Quarantine not triggering:** Double-check the RouteOnContent regex. The pattern `^((?!Public Domain|CC BY 4.0|Rights Reserved).)*$` matches files that do NOT contain any of those strings. If your file contains one of them, it will not match.

**Cannot find the View provenance option:** Right-click on different parts of the canvas. Some NiFi versions put the option on queues, some on processors. You can also access global provenance from the menu bar.

**Docker will not stop:** If Ctrl+C does not work, open another terminal and run `docker compose down` in the lab folder. As a last resort, use Docker Desktop to stop the containers manually.
