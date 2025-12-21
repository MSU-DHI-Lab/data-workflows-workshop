# Day 02: Repeatable Flows and a Run Record with Apache NiFi

## Introduction
Today is about turning yesterday’s careful cleaning into a visible, repeatable flow. You will route files through Apache NiFi, see exactly how they move, and keep a run record you can show to any teammate. The goal is to make the process as clear as the data.

This work fits the middle of a data workflow. Cultural heritage examples guide the exercises, but the patterns apply to any team that needs to move files reliably between folders, systems, or people. By the end, you will know how to prove what happened to a file instead of hoping everyone trusts the output.

## What You Will Build Today
- A local NiFi instance running through Docker Compose.
- A basic flow that moves files from an inbox to an outbox with clear routing steps.
- Quarantine routing that safely holds files that do not meet expectations.
- A captured NiFi provenance view that shows the path one file took.
- An exported flow template and notes on processor settings for reuse.

## Why This Matters in a Real Data Workflow
Day 02 is where you make process repeatable and visible. Moving files by hand hides steps and invites mistakes. A documented flow with a run record stops one silent failure from spreading. This is what keeps a messy or partial export from becoming everyone’s problem later, and it sets up tomorrow’s quality checks to run in a predictable place.

## Today’s Toolbox (and why these tools matter beyond this workshop)
### Apache NiFi: How to get it and run it
- What it is: An open source visual tool for building and running data flows without code.
- How you use it in this workshop: Draw the Day 02 inbox-to-outbox flow, route files, and read provenance.
- How you access it: Runs in Docker using the provided Compose file.
- Get it here: NiFi Docker image pulls automatically; project downloads at https://nifi.apache.org/download.html.
- Open it like this: Install Docker Desktop or a Docker engine (https://www.docker.com/products/docker-desktop). In `01-labs/lab-01/`, run `docker compose up`. When logs say NiFi started, open `http://localhost:8080/nifi/` in your browser.
- Quick check: The NiFi canvas opens and you can drag processors from the left panel.

### Docker Compose: How to get it and run it
- What it is: A way to start containers with predictable settings from a simple YAML file.
- How you use it in this workshop: Launch NiFi with the provided `docker-compose.yml` so everyone shares the same ports and paths.
- How you access it: Install Docker Desktop (includes Compose) or Docker with the Compose plugin.
- Get it here: https://www.docker.com/products/docker-desktop
- Open it like this: From `01-labs/lab-01/`, run `docker compose up` in a terminal. Watch logs until NiFi reports it has started.
- Quick check: The terminal shows containers running and `http://localhost:8080/nifi/` loads the NiFi UI.

These tools stay in your toolbox after the workshop because they are open, widely adopted, and good for any team that needs traceable file movement.

## Setup and Getting Ready (download, install, configure)
- Start with the shared checklist in `../TOOLBOX_SETUP.md` to confirm Docker and a terminal are available.
- From this folder, run `docker compose up` in `01-labs/lab-01/` to start NiFi. You should see logs showing processors starting, and `http://localhost:8080/nifi/` should open the NiFi canvas.
- Check that the day’s input and output folders are present in `01-labs/lab-01/` and match the paths used in the lab instructions.
- Common issues and fixes:
  - Docker will not start containers: confirm Docker Desktop or your engine is running, then retry `docker compose up`.
  - Port 8080 already in use: stop the conflicting service or change the mapped port in `01-labs/lab-01/docker-compose.yml`, then relaunch.
  - Files are not moving: ensure each processor is started (green play icon) and connections are not paused or backpressured.
  - Provenance view is empty: confirm the flow processed a file and that provenance is enabled for the processors in use.
- If you cannot run Docker locally, follow the facilitator-run pathway described in `02-job-aids/troubleshooting.md`: watch a shared NiFi screen, review the exported template, and trace the provided provenance screenshots.

## Suggested Timing (so you can plan your session)
- Plan for about 15 minutes in Lab 01 to start NiFi and learn the canvas.
- Plan for about 30 minutes in Lab 02 to build the inbox-to-outbox flow with routing.
- Plan for about 20 minutes in Lab 03 to add quarantine handling and read the run record.

If time is tight, complete Lab 01 and Lab 02 through the outbox step, then skim the Lab 03 provenance walkthrough.

## Navigation: Everything in this Day Folder
- `00-primer/concepts.md`: Primer on why repeatable flows and provenance matter.
- `00-primer/glossary_day.md`: Definitions for NiFi terms used today.
- `01-labs/lab-01/README.md`: Lab 01 starts NiFi with Docker and orients you to the UI.
- `01-labs/lab-02/README.md`: Lab 02 builds the core flow from inbox to outbox with routing logic.
- `01-labs/lab-03/README.md`: Lab 03 adds quarantine handling and shows how to read the provenance view.
- `02-job-aids/quick_reference.md`: Job aid with key NiFi steps and processor tips.
- `02-job-aids/troubleshooting.md`: Day 02 troubleshooting guide with facilitator fallback steps.
- `03-assessments/knowledge_check.md`: Short questions to confirm you understand flow basics.
- `03-assessments/performance_task.md`: Applied task to design a small flow for your own context.
- `03-assessments/rubric.md`: Criteria to assess whether the flow is traceable and safe.
- `05-artifacts/README.md`: Checklist of outputs to save, including templates and run records.

## If You Are Doing This Solo / If You Are Facilitating a Group
- **Solo:** Start NiFi with Lab 01, then build and run the flow in Lab 02. Capture a provenance screenshot in Lab 03. Self-check by tracing one file from inbox to outbox and explaining each step aloud.
- **Group:** Demo the canvas in Lab 01, then have pairs build the flow in Lab 02 and compare routing choices. Pause before Lab 03 to discuss why quarantine matters. If laptops differ, one facilitator can run NiFi while others annotate the blueprint and provenance output together.

## What Success Looks Like
- NiFi runs locally and you can open the canvas without errors.
- A sample file moves from inbox to outbox through your processors.
- At least one file routes to quarantine when it does not meet the expected pattern.
- You export the flow template and save a provenance screenshot for a single run.
- If you only do one thing, build the inbox-to-outbox flow and capture the provenance for a single file.

## Troubleshooting at a Glance
- Containers fail to start: verify Docker resources (memory and CPU) are sufficient and retry after closing other heavy apps.
- Connection shows backpressure: right-click the queue, view queued files, and clear or increase backpressure limits before rerunning.
- Processors stuck in stopped state: check for missing controller services or invalid properties, fix them, then start the processor.
- Files land in the wrong folder: confirm absolute versus relative paths in processor settings match the paths in `01-labs/lab-02/README.md`.
- Provenance events missing details: ensure provenance is enabled for relevant processors and that you refresh the view after running data through the flow.
