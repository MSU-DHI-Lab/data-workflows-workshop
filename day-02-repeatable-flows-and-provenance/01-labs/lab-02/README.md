# Lab 02: Build a Minimal Flow (Inbox to Outbox with Routing)

The goal of this lab is to build an explainable NiFi flow that ingests files, makes rights text consistent, routes questionable files to quarantine, and writes clean files to an outbox. This takes about 30 minutes.

**Inputs:** `inputs/` folder seeded with `intake_sample.csv` from Lab 01

**Outputs:**
- Cleaned files in `outputs/`
- Quarantined files in `quarantine/`
- Blueprint and settings in `artifacts/`

## Before You Start

This lab involves dragging processors onto a canvas and configuring them. Each processor does one job. You connect processors with lines to show how data flows.

Do not worry about making mistakes. NiFi lets you undo, delete, and reconfigure. The goal is to understand the pattern, not to build something perfect on the first try.

---

## Step 1: Start NiFi

If NiFi is not already running, open a terminal in the `lab-01/` folder and run:

```
docker compose up
```

Wait for the logs to show NiFi has started, then open `http://localhost:8080/nifi/` in your browser.

You should see the NiFi canvas with a toolbar on the left.

If NiFi does not start, run `docker compose down` first to clean up any old state, then try `docker compose up` again.

---

## Step 2: Add a GetFile Processor

Drag a processor from the toolbar (the first icon that looks like a box) onto the canvas. A dialog opens asking which processor type to add.

Search for `GetFile` and select it. Click Add.

Double-click the GetFile processor to configure it:
- Set **Input Directory** to `/opt/nifi/inputs`
- Set **Keep Source File** to `false`

Click Apply, then OK.

The GetFile processor watches a folder and picks up any files that appear. Setting Keep Source File to false means it removes the file after picking it up, preventing duplicate processing.

If the processor shows an error icon, check that you filled in the required fields. The Input Directory path must match the Docker volume mount.

---

## Step 3: Add an UpdateAttribute Processor

Drag another processor onto the canvas and search for `UpdateAttribute`. Add it.

Double-click to configure. Click the plus sign to add a new property:
- Property name: `rights.allowed`
- Property value: `Public Domain,CC BY 4.0,Rights Reserved`

Click Apply, then OK.

This stores the allowed rights tokens as an attribute on each file. Downstream processors can use this to decide what is valid.

---

## Step 4: Connect GetFile to UpdateAttribute

Hover over the GetFile processor until you see an arrow icon. Click and drag to the UpdateAttribute processor.

A dialog opens asking which relationship to connect. Select `success` and click Add.

You should see a line connecting the two processors with a small queue icon in the middle.

If you connected to the wrong processor, right-click the connection and delete it, then try again.

---

## Step 5: Add a ReplaceText Processor

Add another processor and search for `ReplaceText`. This processor cleans up text content.

Configure it:
- **Search Value:** `(?i)cc[- ]?by[- ]?4\.0`
- **Replacement Value:** `CC BY 4.0`
- **Evaluation Mode:** `Entire text`

Click Apply, then OK.

The search value is a regular expression (a pattern for matching text). The `(?i)` makes it case-insensitive. This catches variants like `cc by 4.0`, `CC-BY-4.0`, and normalizes them.

If you see a validation error, check that you typed the backslash correctly (`\.0` not just `.0`).

---

## Step 6: Connect UpdateAttribute to ReplaceText

Connect UpdateAttribute to ReplaceText using the `success` relationship.

---

## Step 7: Add a RouteOnContent Processor

Add a `RouteOnContent` processor. This routes files based on what they contain.

Configure it:
- Click the plus sign to add a new property
- Property name: `quarantine`
- Property value: `^((?!Public Domain|CC BY 4.0|Rights Reserved).)*$`
- In the Settings tab, set **Match Requirement** to `content must contain match`

Click Apply, then OK.

This regex matches files that do NOT contain any of the allowed rights tokens. Those files get routed to quarantine instead of the outbox.

If the processor shows invalid, check the regex for typos. The vertical bars (`|`) separate alternatives.

---

## Step 8: Connect ReplaceText to RouteOnContent

Connect ReplaceText to RouteOnContent using the `success` relationship.

---

## Step 9: Add Two PutFile Processors

Add two `PutFile` processors and position them to the right of RouteOnContent.

Configure the first one:
- **Directory:** `/opt/nifi/outputs`

Configure the second one:
- **Directory:** `/opt/nifi/quarantine`

These are the destinations for clean and questionable files.

---

## Step 10: Connect RouteOnContent to Both Destinations

Connect RouteOnContent to the outputs PutFile:
- In the connection dialog, select the `unmatched` relationship (files that passed the allowed-rights check)

Connect RouteOnContent to the quarantine PutFile:
- Select the `quarantine` relationship (files that failed the check)

You should now have a complete flow from GetFile through to two PutFile destinations.

---

## Step 11: Start the Flow and Test

Select all processors (Ctrl+A or Cmd+A), right-click, and select Start.

Check that `intake_sample.csv` is in the `lab-02/inputs/` folder. If the file has valid rights content, it should move to `outputs/`. If the rights are invalid, it should move to `quarantine/`.

Watch the queues between processors. You should see numbers briefly appear as files flow through.

If files are not moving, check that all processors are started (green play icon). Look at the bulletin board (top right bell icon) for error messages.

---

## Step 12: Export the Flow Definition

Right-click on an empty area of the canvas and look for "Download flow definition" or check the top-right menu (the NiFi logo dropdown) for an export option.

Save the file as `artifacts/flow_definition.json`.

This captures your entire flow so others can import it and get the same setup.

---

## Step 13: Document Your Settings

Open `artifacts/flow_blueprint.md` and record the key processor settings you configured. Include:
- GetFile input directory
- Allowed rights tokens
- ReplaceText regex
- RouteOnContent routing rule

This written documentation helps when the JSON file is not enough to explain why you made certain choices.

---

## Checkpoint

Before moving on, confirm:

- [ ] All processors are running without errors
- [ ] A test file moved from `inputs/` to `outputs/` or `quarantine/`
- [ ] `artifacts/flow_definition.json` exists
- [ ] `artifacts/flow_blueprint.md` has your settings documented

If all four are checked, you are ready for Lab 03.

---

## If Something Went Wrong

**Processor shows invalid state:** Open the processor configuration and look for red text indicating which property is wrong. Fix it and apply again.

**Files not moving:** Check that all processors are started. Look for backpressure warnings on queues. Check the bulletin board for errors.

**Files land in the wrong folder:** Verify the directory paths in PutFile match `/opt/nifi/outputs` and `/opt/nifi/quarantine`. These are paths inside the Docker container, not on your local machine.

**Regex not matching:** Test your regex with a simple pattern first. Check for missing parentheses or vertical bars.

**Cannot export flow:** Try both the canvas right-click menu and the top-right NiFi logo dropdown. Different NiFi versions put the export option in different places.
