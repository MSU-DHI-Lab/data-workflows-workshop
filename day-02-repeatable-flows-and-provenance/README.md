# Day 02: Repeatable Flows and a Run Record with Apache NiFi

## Introduction

Today you will turn yesterday's careful cleaning into a visible, repeatable flow. You will route files through Apache NiFi, see exactly how they move, and keep a run record you can show to any teammate. The goal is to make the process as clear as the data.

This work fits the middle of a data workflow. Cultural heritage examples guide the exercises, but the patterns apply to any team that needs to move files reliably between folders, systems, or people. By the end, you will know how to prove what happened to a file instead of hoping everyone trusts the output.

For term definitions used throughout this day, see [today's glossary](00-primer/glossary_day.md) and the [shared glossary](../GLOSSARY.md).

## What You Will Build Today

By the end of this session, you will have:

- A local NiFi instance running through Docker Compose
- A basic flow that moves files from an inbox to an outbox with clear routing steps
- Quarantine routing that safely holds files that do not meet expectations
- A captured NiFi provenance view (the run record) showing the path one file took
- An exported flow template and notes on processor settings for reuse

## Why This Matters in a Real Data Workflow

Day 02 is where you make process repeatable and visible. Moving files by hand hides steps and invites mistakes. A documented flow with a run record stops one silent failure from spreading. This is what keeps a messy or partial export from becoming everyone's problem later, and it sets up tomorrow's quality checks to run in a predictable place.

## Today's Toolbox

### Apache NiFi

NiFi is a visual tool for building and running data flows without writing code. You drag boxes (called processors) onto a canvas and connect them to show how files move. NiFi keeps a detailed run record called "provenance" that shows exactly what happened to each file.

A **container** is a lightweight, isolated environment that runs software with all its dependencies bundled together. Think of it as a shipping container for software: everything the program needs is packed inside, so it runs the same way on any computer. Docker is the tool that creates and runs these containers.

**How to get NiFi running:**

1. Make sure Docker Desktop is installed and running (download from https://www.docker.com/products/docker-desktop)
2. Open a terminal and navigate to `01-labs/lab-01/`
3. Run `docker compose up`
4. Wait for the logs to show NiFi has started (look for messages about processors being available)
5. Open `http://localhost:8080/nifi/` in your browser

You should see the NiFi canvas with a toolbar on the left. If you see a certificate warning, that is expected for local development. Accept it and continue.

This is your first time running NiFi, so do not worry if it takes a moment to load. The interface might look complex at first, but you will only use a handful of features today.

### Docker Compose

Docker Compose is a tool that starts containers with predictable settings from a simple configuration file. The `docker-compose.yml` file in Lab 01 tells Docker exactly how to run NiFi so everyone gets the same setup.

**Why this matters:** You do not need to configure NiFi manually. The compose file handles ports, folders, and settings. You just run one command and the environment is ready.

These tools stay in your toolbox after the workshop because they are open, widely adopted, and good for any team that needs traceable file movement.

## Setup Checklist

Before you begin the labs:

1. Review the shared checklist in [TOOLBOX_SETUP.md](../TOOLBOX_SETUP.md) to confirm Docker and a terminal are available
2. From the `01-labs/lab-01/` folder, run `docker compose up` to start NiFi
3. Open `http://localhost:8080/nifi/` and confirm you see the NiFi canvas
4. Check that the day's input and output folders are present in `01-labs/lab-01/` and match the paths used in the lab instructions

**If you run into trouble:**

- **Docker will not start containers:** Confirm Docker Desktop (or your Docker engine) is running, then retry `docker compose up`
- **Port 8080 already in use:** Another application is using that port. Stop the other service, or change the mapped port in `docker-compose.yml` and relaunch
- **Files are not moving:** Make sure each processor is started (green play icon) and connections are not paused or backed up
- **Provenance view is empty:** Confirm the flow processed a file and that you selected the right FlowFile

If you cannot run Docker locally, follow the facilitator-run pathway described in [troubleshooting.md](02-job-aids/troubleshooting.md). You can watch a shared NiFi screen, review the exported template, and trace the provided provenance screenshots.

## Suggested Timing

| Lab | Focus | Time |
|-----|-------|------|
| Lab 01 | Start NiFi and learn the canvas | ~15 minutes |
| Lab 02 | Build the inbox-to-outbox flow with routing | ~30 minutes |
| Lab 03 | Add quarantine handling and read the run record | ~20 minutes |

If time is tight, complete Lab 01 and Lab 02 through the outbox step. You can skim the Lab 03 provenance walkthrough and return later.

## Navigation

| File | What it contains |
|------|------------------|
| [00-primer/concepts.md](00-primer/concepts.md) | Primer on why repeatable flows and provenance matter |
| [00-primer/glossary_day.md](00-primer/glossary_day.md) | Definitions for NiFi terms used today |
| [01-labs/lab-01/README.md](01-labs/lab-01/README.md) | Lab 01: Start NiFi with Docker and orient to the UI |
| [01-labs/lab-02/README.md](01-labs/lab-02/README.md) | Lab 02: Build the core flow from inbox to outbox |
| [01-labs/lab-03/README.md](01-labs/lab-03/README.md) | Lab 03: Quarantine handling and reading the provenance view |
| [02-job-aids/quick_reference.md](02-job-aids/quick_reference.md) | Key NiFi steps and processor tips |
| [02-job-aids/troubleshooting.md](02-job-aids/troubleshooting.md) | Day 02 troubleshooting with facilitator fallback steps |
| [03-assessments/knowledge_check.md](03-assessments/knowledge_check.md) | Short questions to confirm you understand flow basics |
| [03-assessments/performance_task.md](03-assessments/performance_task.md) | Applied task to design a small flow for your own context |
| [05-artifacts/README.md](05-artifacts/README.md) | Checklist of outputs to save |

## Working Solo vs. Facilitating a Group

**If you are working on your own:** Start NiFi with Lab 01, then build and run the flow in Lab 02. Capture a provenance screenshot in Lab 03. Self-check by tracing one file from inbox to outbox and explaining each step aloud.

**If you are leading a group:** Demo the canvas in Lab 01, then have pairs build the flow in Lab 02 and compare routing choices. Pause before Lab 03 to discuss why quarantine matters. If laptops differ, one facilitator can run NiFi while others annotate the blueprint and provenance output together.

## You Are Done When

Check your work against this list. You should have:

- [ ] NiFi running locally at `http://localhost:8080/nifi/` without errors
- [ ] A sample file that moved from `inputs/` to `outputs/` through your flow
- [ ] At least one file routed to `quarantine/` because it did not meet the expected pattern
- [ ] `01-labs/lab-02/artifacts/flow_definition.json` containing your exported flow
- [ ] `01-labs/lab-02/artifacts/flow_blueprint.md` with notes on processor settings
- [ ] A provenance screenshot or narrative for a single file's journey

If you have the flow definition and a provenance trace for one file, you have completed the core work for Day 02. The flow definition is your recipe for repeatable movement, and the provenance trace is your proof of what happened.

## Troubleshooting at a Glance

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Containers fail to start | Not enough memory or CPU | Check Docker resource settings, close heavy apps, and retry |
| Connection shows backpressure | Queue is full | Right-click the queue, view queued files, clear or increase limits |
| Processors stuck in stopped state | Missing settings or controller services | Open the processor, fill required properties, apply, and start |
| Files land in the wrong folder | Path mismatch | Check absolute vs relative paths in processor settings |
| Provenance events missing details | Provenance not enabled or time window too narrow | Enable provenance on relevant processors and widen the time range |

For more troubleshooting, see [02-job-aids/troubleshooting.md](02-job-aids/troubleshooting.md).

## What Comes Next

Tomorrow in Day 03, you will add explicit quality checks to your workflow. Instead of hoping the data is correct, you will write validation rules that confirm it. The cleaned and routed files from today become the input for those checks.

The provenance trace you captured today shows how a file moved. Tomorrow's validation report will show whether the file's contents are trustworthy. Together, they form a complete picture: where the data went and whether it passed inspection.

## Take It Further

If you want to explore beyond today's labs:

- **Add a second routing rule:** Create another branch in RouteOnContent for a different pattern, like files missing a required field
- **Try a different processor:** Explore the UpdateRecord or ConvertRecord processors for transforming CSV to JSON
- **Connect to a remote folder:** If you have access to a shared drive, configure GetFile to watch a network path instead of a local folder
- **Export and import a template:** Practice exporting your flow as a template and importing it into a fresh NiFi canvas
- **Read more about NiFi provenance:** See the Apache NiFi documentation on provenance events and how to query them

## Reflection Prompts

Before you move on, take a moment to think about what you learned:

- What does the provenance view tell you that you could not see by just looking at the output folder?
- If a colleague asked "what happened to that file?" how would you answer using NiFi?
- What kind of files would you quarantine in your own work, and what would you check before releasing them?

These questions do not have right answers. They help you connect today's practice to future situations in your own work.
