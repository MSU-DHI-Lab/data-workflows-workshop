# Data Workflows Workshop-in-a-Box

This is a four-day, already-run workshop packaged so you can reuse it with your own teams. Each day is a self-contained 60–90 minute mini-repo that blends hands-on labs, job aids, and assessments so cultural heritage professionals can move confidently between collections practice and the wider data and analytics world.

## Who this is for
- Museum, archive, library, lab, and repository teams who steward cultural collections.
- Folks who know their metadata but do not live inside data engineering tools.
- Facilitators who want a ready-to-run, low-friction learning arc for colleagues.

## Why this matters
Cultural data deserves the same care and clarity as any research dataset. This workshop bridges collections expertise with approachable data workflows: cleaning metadata, moving records through repeatable pipelines, adding quality checks, and publishing safely for reuse. The aim is confidence. You should feel ready to explain what changed, why it changed, and how others can build on your work.

## Toolchain: what each tool does and why it fits
- **OpenRefine** – What: interactive cleaning and reconciliation for messy metadata. Why: fast to learn, transparent change history, great for untangling controlled vocabularies without heavy coding.
- **Apache NiFi** – What: visual pipelines for moving and transforming data. Why: lets you sketch and run repeatable flows without writing glue code; easy to show provenance step by step.
- **Python / Google Colab** – What: lightweight scripting and notebooks in the browser. Why: no installs for participants, easy to share, and perfect for quick transformations or validations you can read like a story.
- **Pandera** – What: data validation library for Python that treats schema checks as code. Why: keeps quality gates living next to the data, with human-readable rules and clear failure messages.
- **Streamlit** – What: rapid app layer for sharing small tools or review UIs. Why: turns notebooks into friendly web views so collaborators can interact with outputs without touching code.
- **Zenodo / DOIs** – What: archiving and persistent identifiers for datasets and artifacts. Why: gives your outputs a citable home with clear versions, making reuse and attribution straightforward.

## Pace and expectations
- Four sessions, each 60–90 minutes, each standing on its own. You can run them in sequence or pick the day you need.
- Arrive with a modern browser and access to the listed tools (see `TOOLCHAIN_SETUP.md` for specifics).
- Success looks like producing the day’s artifacts, capturing what changed, and knowing how to repeat or adapt the steps later.

## Workshop flow: legibility → repeatability → quality → safe reuse/publishing
We start by making records legible (Day 01), then design repeatable movement (Day 02), add quality gates that travel with the data (Day 03), and finish with safe reuse and publishing patterns (Day 04). This order mirrors real cultural heritage work: you clean so others can read, you pipeline so others can depend on the flow, you test so others can trust, and you publish so others can cite and build.

## Day-by-day breakdown
- **Day 01: Metadata Cleaning and Normalization** (`day-01-metadata-cleaning-and-normalization/`)
  - Goals: tame messy fields, align vocabularies, and document changes.
  - What you will do: hands-on OpenRefine reconciliation and normalization labs.
  - What you will produce: cleaned datasets, change logs, and a day glossary.
  - Why this day matters: clear, normalized metadata is the foundation for every later step.

- **Day 02: Pipelines and Provenance** (`day-02-pipelines-and-provenance/`)
  - Goals: design a repeatable flow for moving records from source to workspace.
  - What you will do: build Apache NiFi pipelines and lightweight Colab scripts to capture transformations.
  - What you will produce: pipeline definitions, run notes, and provenance markers.
  - Why this day matters: a transparent path from input to output makes future updates dependable.

- **Day 03: Quality Gates and Reuse** (`day-03-quality-gates-and-reuse/`)
  - Goals: add checks that travel with the data and prep outputs for colleagues.
  - What you will do: write Pandera validations, adjust pipelines to enforce them, and surface results via Streamlit for review.
  - What you will produce: validation schemas, passing/failing reports, and a small review UI.
  - Why this day matters: portable quality gates keep trust high when data moves between teams.

- **Day 04: Governance and Publishing** (`day-04-governance-and-publishing/`)
  - Goals: package artifacts responsibly and assign persistent identifiers.
  - What you will do: assemble release bundles, document lineage, and register outputs with Zenodo/DOIs.
  - What you will produce: publication checklist results, deposit-ready bundles, and DOI metadata.
  - Why this day matters: publishing with provenance and stable links invites citation and respectful reuse.

## Start here
Ready to dive in? Read `START_HERE.md` for navigation and pacing, skim `TOOLCHAIN_SETUP.md` to ensure access, then open `day-01-metadata-cleaning-and-normalization/` to begin. Each day stands alone, so you can also jump to the topic you need most. If a concept is new, open the matching page in `learn/` for a quick primer.

## Ethics and data handling
The workshop uses synthetic or safely anonymized datasets. See `SECURITY_AND_DATA_HANDLING.md` for how to handle sample data and adapt the patterns to your own collections with care.

## Facilitator quick start
- Audience and timing: four sessions, each 60–90 minutes, for collections staff comfortable with metadata but new to data tooling.
- Agenda:  
  - Day 01 (legibility): facets and cleaning in OpenRefine; outputs = cleaned CSV + operations JSON + docs notes.  
  - Day 02 (repeatability): NiFi inbox → normalize → outbox with quarantine; outputs = flow definition JSON + blueprint notes + sample routed files.  
  - Day 03 (quality): Pandera checks in Colab/local; outputs = validation schema + report.  
  - Day 04 (publishing): package with README, dictionary, provenance, validation, LICENSE, CITATION.cff, .zenodo.json; optional Streamlit handoff.
- Prep checklist (day before): install OpenRefine; ensure Python 3.9+; Docker Desktop running and port 8080 free; confirm browser access to Colab; gather a Zenodo account only if running the live DOI path. Print or copy the agenda above and keep `TOOLCHAIN_SETUP.md` handy.
- Day-of checklist (30 minutes): open this README, `START_HERE.md`, and the Day 01 README; test OpenRefine at `http://127.0.0.1:3333`; if Docker is blocked, plan a facilitator screen-share run for NiFi and let learners observe outputs.
- Accessibility and pacing: keep instructions visible, narrate why each step matters, and pair participants if skill levels vary.

## Repo map
- `day-*/` – Four mini-repos, one per day, each with primer, labs, job aids, assessments, diagrams, and artifact drop zones.
- `learn/` – Plain-language explainers on data lakes, warehouses, lakehouses, data vaults, governance, provenance, DOIs, and publishing.
- `templates/` – Reusable templates for labs, rubrics, diagrams, datasets, and publication checklists.
- `shared_assets/` – Synthetic datasets, schemas, and examples used across days (see its README).
