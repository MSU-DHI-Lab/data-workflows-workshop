# Data Workflows Workshop-in-a-Box

This repository is a complete, ready-to-run curriculum for learning practical data workflows without turning you into a full-time data engineer. You can work through it on your own, at your own pace, or you can run it with a group as four 60–90 minute sessions.

A lot of people who work with important data are not “data people” by training. They are domain experts who know their material deeply, but they are stuck at the edge of a very technical world of tools and jargon. That gap is real. It is also fixable.

Data science and analytics are not only for specialists. They are how you make messy information legible, how you make work repeatable, how mistakes get caught before they spread, and how outputs get published so other people can trust and reuse them. If you have ever inherited a spreadsheet that nobody can explain, or tried to merge two exports that “should match” but do not, you already know why these skills matter.

This curriculum does not dumb down the workflow. Instead, it brings people into the workflow with support. The aim is to meet in the middle. The tools and habits here travel well. The goal is to leave with a toolbox and the confidence to pull out the right tool the next time a new data problem shows up.

**Jump to:** [At a glance](#at-a-glance) · [Quick start](#quick-start) · [Day-by-day overview](#day-by-day-overview) · [Workflow map](#workflow-map) · [Your toolbox](#your-toolbox-for-this-workshop) · [Start here](#start-here) · [Use, reuse, and contribute](#use-reuse-and-contribute)

## At a glance

| Item | What it means |
|---|---|
| Format | Workshop-in-a-box (solo or facilitated) |
| Time | 4 modules, 60 to 90 minutes each |
| Outcome | Clean data, repeatable workflow, quality checks, publishable package |
| Tools | OpenRefine, NiFi, Python, Colab, Pandera, Streamlit, Zenodo (optional) |
| Skill level | Domain expertise helpful; no computer science background required |
| Cost | Free and low-cost tools; avoids expensive proprietary platforms |
| What remains | Reusable workflows, checklists, and a publication-ready bundle |

## Quick start

If you want the simplest path:

1) Read [START_HERE.md](START_HERE.md)  
2) Set up tools using [TOOLBOX_SETUP.md](TOOLBOX_SETUP.md)  
3) Begin with [Day 01](day-01-metadata-cleaning-and-normalization/README.md) and follow the Navigation section inside each day

If this is being run with a group, the same path works. The day READMEs are written so they can act as an agenda.

## Who this is for

This is designed for people who work with real-world data and want to get better at handling it.

Common examples:
- Cultural heritage practitioners: museums, archives, libraries, labs, repositories, collections teams, and research groups
- Anyone who understands their domain and their data, but does not want to be blocked by technical barriers
- Facilitators who want a complete curriculum they can run with a team, online or in person

A computer science background is not required. Curiosity and a willingness to try things step by step are enough.

## What you will learn

By the end, learners will be able to:
- Clean and normalize messy data in a way that can be explained and repeated
- Move data through a workflow that is visible, documented, and not dependent on one person’s memory
- Add quality checks so problems get caught early and “good data” can be described clearly
- Package and publish outputs so reuse is safe, attributable, and respectful

Just as importantly, the work will make sense. Each step exists for a reason, and those reasons are explained along the way.

## What this workflow is doing, in plain language

Think about the difference between a garage and a pantry.

A garage is where things land when life happens. Boxes show up. Old stuff gets stacked. A few labels get added so things can be found again. A lot of real data starts its life like that. It arrives quickly, in different shapes, with missing pieces, and with inconsistent naming.

A pantry is what gets built when other people need to reliably find things. Similar items go together. Shelves are labeled. Containers are consistent. The point is not perfection. The point is that someone else can walk in and find what they need without guessing.

This curriculum shows how to move from garage to pantry. Not by magic, and not by hand-editing forever, but by building repeatable habits:
- Make data legible
- Move it through steps that can be seen
- Check quality in ways that can travel with the dataset
- Publish with documentation so other people can trust what was made

## Workflow map

Messy export → Clean and normalize → Repeatable workflow → Quality checks → Publishable package

## What is included

Each day is a self-contained 60–90 minute module with:
- A day overview (what will be done and why it matters)
- A short primer for key concepts in plain language
- Hands-on labs with expected outputs and troubleshooting
- Job aids and checklists that can be reused later
- Artifacts (datasets, notebooks, configuration files) needed to complete the work

The days can be run in order for a full arc, or used independently based on what is needed right now.

## Day-by-day overview

| Day | Focus | What gets produced | Link |
|---|---|---|---|
| Day 01 | Cleaning and normalization | Clean dataset plus replayable cleaning steps | [Day 01 README](day-01-metadata-cleaning-and-normalization/README.md) |
| Day 02 | Repeatable workflow | A visible flow that can be reused plus simple run notes | [Day 02 README](day-02-repeatable-flows-and-provenance/README.md) |
| Day 03 | Quality checks and review | Validation rules plus readable pass/fail outputs | [Day 03 README](day-03-quality-gates-and-reuse/README.md) |
| Day 04 | Publishing for reuse | A deposit-ready package plus documentation and identifiers | [Day 04 README](day-04-publishing-with-care/README.md) |

## Your toolbox for this workshop

We’re calling this a toolbox on purpose. These are not “one special workflow” tools. These are general-purpose tools that show up across the broader data science and analytics world, and they are useful whenever a new data challenge shows up.

Expensive, proprietary platforms are intentionally avoided here. The point is portability. These tools can be used on different machines, in different institutions, and in different contexts.

### OpenRefine (desktop app)

![OpenRefine](https://img.shields.io/badge/OpenRefine-cleaning-informational)

OpenRefine is a point-and-click tool for cleaning messy data, especially metadata. It shines when the problem is not “big data,” but “real data,” meaning inconsistent values, typos, mixed formats, and fields that were never standardized in the first place.

It is used here because it is fast to learn and it keeps a clear record of what changed. In the wider analytics world, that replayable history matters. It means cleaning steps can be reviewed, reused, and explained.

- Get it here: https://openrefine.org/download.html  
- How you access it: Install on your computer  
- Open it like this:
  1) Download and unzip the package for your operating system  
  2) Run the OpenRefine application  
  3) A browser tab should open automatically with the OpenRefine interface  
- Quick check: The OpenRefine home screen appears in the browser and a new project can be created

### Apache NiFi (workflow tool, typically run with Docker)

![Apache%20NiFi](https://img.shields.io/badge/Apache%20NiFi-workflows-informational)

NiFi is a visual way to move data through steps that can be seen. If there has ever been a wish to point to a process and say, “This is exactly what happens to our data,” NiFi supports that kind of clarity.

It is used here because it makes workflows visible and repeatable without requiring a lot of glue code. In the broader data world, this is a core idea. A workflow that can be seen can be taught, audited, improved, and handed off.

- Get it here: https://nifi.apache.org/download.html  
- How you access it: Usually runs locally via Docker for this workshop  
- Open it like this:
  1) Follow the NiFi setup steps in [TOOLBOX_SETUP.md](TOOLBOX_SETUP.md)  
  2) Start the NiFi environment as described there  
  3) Open the NiFi web interface in a browser (the exact address is listed in the setup guide)  
- Quick check: The NiFi canvas loads in the browser and the toolbar appears without errors

### Python and Google Colab (browser-based notebooks)

![Python](https://img.shields.io/badge/Python-analysis-informational)
![Google%20Colab](https://img.shields.io/badge/Google%20Colab-notebooks-informational)

Python is one of the most widely used languages in data work, and notebooks are a common way to combine code, explanation, and outputs in one place.

Google Colab is used because it reduces setup friction. Notebooks can run in the browser, which helps when learning or when installation is difficult. In the wider analytics world, notebooks are also a standard way to share methods and reasoning, not just results.

- Get it here: https://colab.research.google.com/  
- How you access it: Web-based (runs in your browser)  
- Open it like this:
  1) Click an “Open in Colab” badge when it appears in the day materials  
  2) Run cells from top to bottom, reading the notes as you go  
- Quick check: A cell runs and output appears directly below it

### Pandera (data validation rules)

![Pandera](https://img.shields.io/badge/Pandera-validation-informational)

Pandera is a Python library that lets quality checks be written as explicit rules. Instead of “someone should probably check this column,” it becomes “this is the rule, and it can be run every time.”

It is used here because quality is not a vibe. It is criteria. In the wider analytics world, this is how teams prevent small issues from quietly becoming big issues, especially when data moves between people and systems.

- Get it here: https://pandera.readthedocs.io/  
- How you access it: Runs inside Python (installed as a package)  
- Open it like this:
  1) In Colab, the notebook installs what it needs, if required  
  2) If running locally, follow the Python setup steps in [TOOLBOX_SETUP.md](TOOLBOX_SETUP.md)  
- Quick check: A validation cell runs and produces a clear pass or a clear failure message

### Streamlit (open source review interface)

![Streamlit](https://img.shields.io/badge/Streamlit-review%20UI-informational)

Streamlit is a simple way to turn results into a small web interface. It is useful when colleagues need to review outcomes without needing to read code or run a notebook.

It is used here because it turns validation into a shared step instead of a private technical step. In the wider analytics world, this matters. Good data work is rarely solo work, and review needs to be understandable.

- Get it here: https://streamlit.io/  
- How you access it: Runs locally in Python, or via the provided workflow for this workshop  
- Open it like this:
  1) Follow the Streamlit steps in the Day 03 materials  
  2) Start the app using the exact command shown there  
  3) Open the local URL that Streamlit prints in the terminal  
- Quick check: A simple page loads in the browser with the expected review elements

### Zenodo and DOIs (optional publishing step)

![Zenodo](https://img.shields.io/badge/Zenodo-publishing-informational)

Zenodo is a publishing platform that supports datasets and research outputs. A DOI is a persistent identifier that makes something citable and trackable over time.

This is included as an optional step because publishing is not just uploading a file. Publishing is packaging work so someone who is not you can reuse it responsibly. In the wider analytics world, this supports reproducibility and attribution.

- Get it here: https://zenodo.org/  
- How you access it: Web-based  
- Open it like this:
  1) Create an account (or log in)  
  2) Follow the Day 04 publishing guide to prepare a deposit bundle  
- Quick check: A new upload can be started and the metadata fields appear for describing the deposit

## Pace and expectations

This curriculum is designed around four sessions of 60–90 minutes. Each day includes suggested timing so sessions can be planned, but the materials are also written so they can be completed independently.

What success looks like here:
- The outputs described in each day are produced
- Changes can be explained in plain language
- The process can be repeated on a different dataset later

If something goes wrong, the troubleshooting sections are part of the curriculum, not an afterthought.

## Data handling, safety, and ethics

This matters. Especially in cultural heritage and adjacent domains, data is not just technical. It can involve people, communities, histories, harm, and power.

This workshop uses synthetic or safely anonymized datasets by default. When adapting the workflow to real data, keep these principles in view:
- Use the minimum data needed for the task
- Treat identifiers and sensitive fields as high-risk, even when they look harmless
- Document decisions, especially exclusions and transformations
- Respect rights, community protocols, and institutional constraints
- Design for responsible reuse, not maximum exposure

See [SECURITY_AND_DATA_HANDLING.md](SECURITY_AND_DATA_HANDLING.md) for practical guidance and a checklist to use before publishing anything.

## Start here

If learning independently:
1) Read [START_HERE.md](START_HERE.md)  
2) Set up tools using [TOOLBOX_SETUP.md](TOOLBOX_SETUP.md)  
3) Begin with Day 01: [day-01-metadata-cleaning-and-normalization/README.md](day-01-metadata-cleaning-and-normalization/README.md)

If running this with a group:
- Use the Day READMEs as the agenda:
  - Day 01: [link](day-01-metadata-cleaning-and-normalization/README.md)
  - Day 02: [link](day-02-repeatable-flows-and-provenance/README.md)
  - Day 03: [link](day-03-quality-gates-and-reuse/README.md)
  - Day 04: [link](day-04-publishing-with-care/README.md)
- Follow the suggested timing and pause at the checkpoints built into each day
- Pair participants when skill levels vary
- Encourage learners to narrate what changed and why, not just click through steps

## Repo map

- `day-*/`  
  Four day folders, one per day:
  - Day 01: [day-01-metadata-cleaning-and-normalization/](day-01-metadata-cleaning-and-normalization/)
  - Day 02: [day-02-repeatable-flows-and-provenance/](day-02-repeatable-flows-and-provenance/)
  - Day 03: [day-03-quality-gates-and-reuse/](day-03-quality-gates-and-reuse/)
  - Day 04: [day-04-publishing-with-care/](day-04-publishing-with-care/)

- `learn/`  
  Plain-language explainers for core concepts: [learn/](learn/)

- `shared_assets/`  
  Synthetic datasets and shared examples used across days: [shared_assets/](shared_assets/)

## Use, reuse, and contribute

This workshop is published openly because these skills should be shareable. Use it, adapt it, remix it, and run it in any context.

If something gets improved:
- Fix a confusing explanation
- Add a troubleshooting case that came up
- Improve an example dataset
- Translate a section for a different audience

Contributions are welcome. Open a pull request with a clear description of what changed and why. If unsure where to start, open an issue and describe the gap.
