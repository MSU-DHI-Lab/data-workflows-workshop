# Performance Task

## Scenario
A partner sends you weekly CSVs. You need a small pipeline that normalizes rights strings, routes questionable files to quarantine, and leaves a clear trail for colleagues.

## Your task
1) Build the inbox → normalize → outbox flow with quarantine, using the Day 02 pattern.
2) Ingest a sample file, confirm routing, and capture a provenance trace for one FlowFile.
3) Export the flow definition and update `artifacts/flow_blueprint.md` with any property tweaks.
4) Write a short note on why you chose quarantine rules and how someone else should review quarantined files.

## Submission
- Place the exported flow definition, updated blueprint, and your provenance note in `05-artifacts/submissions/`.
- Include any sample input/output files you used for testing.
