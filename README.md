# Data Workflows Workshop-in-a-Box

This repository is a complete, ready-to-run curriculum for learning practical data workflows without turning you into a full-time data engineer. You can work through it on your own, at your own pace, or you can run it with a group as four 60–90 minute sessions.

The big idea is simple. A lot of people who work with important data are not “data people” by training. They are domain experts who know their material deeply, but they are stuck at the edge of a very technical world of tools and jargon. That gap is real. It is also fixable.

Data science and analytics are not only for specialists. They are how you make messy information legible, how you make your work repeatable, how you catch mistakes before they spread, and how you publish outputs that other people can trust and reuse. If you have ever inherited a spreadsheet that nobody can explain, or tried to merge two exports that “should match” but do not, you already know why these skills matter.

This workshop does not dumb down the workflow. Instead, it brings you into the workflow with support. We meet in the middle. You will learn a small set of widely used tools and a way of thinking that travels. The goal is that you leave with a new toolbox, and the confidence to pull out the right tool the next time a new data problem shows up.

## Who this is for

This is designed for people who work with real-world data and want to get better at handling it.

Common examples:
- Cultural heritage practitioners: museums, archives, libraries, labs, repositories, collections teams, and research groups
- Anyone who understands their domain and their data, but does not want to be blocked by technical barriers
- Facilitators who want a complete curriculum they can run with a team, online or in person

You do not need a computer science background. You do need curiosity and a willingness to try things step by step.

## What you will learn

By the end, you will be able to:
- Clean and normalize messy data in a way you can explain and repeat
- Move data through a workflow that is visible, documented, and not dependent on one person’s memory
- Add quality checks so you can catch problems early and communicate what “good data” means
- Package and publish outputs so reuse is safe, attributable, and respectful

Just as importantly, you will understand why each step exists and what problem it solves.

## What this workflow is doing, in plain language

Think about the difference between a garage and a pantry.

A garage is where things land when life happens. Boxes show up. Old stuff gets stacked. You might label a few things so you can find them again. You keep it because it matters, even if it is not organized yet. A lot of real data starts its life like that. It arrives fast, in different shapes, with missing pieces, and with inconsistent naming.

A pantry is what you build when other people need to reliably find things. You put the same kinds of items together. You label shelves. You use consistent containers. The point is not perfection. The point is that someone else can walk in and find what they need without guessing.

This workshop teaches you how to move from garage to pantry. Not by magic, and not by hand-editing everything forever, but by building repeatable habits:
- Make your data legible
- Move it through steps you can see
- Check quality in ways that can travel with the dataset
- Publish with documentation so other people can trust what you made

## What is included

Each day is a self-contained 60–90 minute module with:
- A day overview (what you will do and why it matters)
- A short primer for key concepts in plain language
- Hands-on labs with expected outputs and troubleshooting
- Job aids and checklists you can reuse later
- Artifacts (datasets, notebooks, configuration files) needed to complete the work

You can run the days in order for a full arc, or you can jump directly to the day that matches your current needs.

## The four-day arc

The workshop follows a practical progression:
1) Make data legible
2) Make the process repeatable
3) Make quality explicit
4) Publish for safe reuse

That mirrors real work. First you clean enough to see clearly. Then you make it repeatable so you are not reinventing the same steps every time. Then you add quality checks so trust does not depend on memory. Then you publish with the context people need to reuse what you made.

## Day-by-day overview

### Day 01: Clean metadata and make values consistent
Read the Day 01 guide: [day-01-metadata-cleaning-and-normalization/README.md](day-01-metadata-cleaning-and-normalization/README.md)

Folder: [`day-01-metadata-cleaning-and-normalization/`](day-01-metadata-cleaning-and-normalization/)

What you will do:
- Use OpenRefine to clean messy fields and make values consistent
- Reconcile terms where appropriate
- Save a clear record of what you changed

What you will leave with:
- A cleaned dataset
- A saved OpenRefine operations file (a machine-readable record of every cleaning step)
- Short notes that explain what changed and why

Why this matters:
If the inputs are unclear, every downstream step becomes fragile. Day 01 is where you make your dataset readable to other humans and to tools.

### Day 02: Build a repeatable workflow for moving data
Read the Day 02 guide: [day-02-repeatable-flows-and-provenance/README.md](day-02-repeatable-flows-and-provenance/README.md)

Folder: [`day-02-repeatable-flows-and-provenance/`](day-02-repeatable-flows-and-provenance/)

What you will do:
- Build a visual workflow that moves data from an incoming folder to an outgoing folder
- Add a quarantine path for records that need review
- Capture simple “origin and changes” notes so the workflow is explainable later

What you will leave with:
- An exported workflow file you can reuse
- A simple run record you can keep with your outputs
- Routed outputs that show how records move through the process

Why this matters:
If your process only exists in someone’s head, it does not scale and it does not survive staff turnover. A visible workflow is also easier to teach, audit, and improve.

### Day 03: Add quality checks so reuse is safer
Read the Day 03 guide: [day-03-quality-gates-and-reuse/README.md](day-03-quality-gates-and-reuse/README.md)

Folder: [`day-03-quality-gates-and-reuse/`](day-03-quality-gates-and-reuse/)

What you will do:
- Write clear quality checks in Python using Pandera
- Run checks against your dataset and generate readable results
- Use Streamlit to present a simple review view so colleagues can understand failures without reading code

What you will leave with:
- A set of validation rules (a named set of checks that defines “what good looks like”)
- A pass/fail report that is easy to interpret
- A small review interface that supports human decision-making

Why this matters:
Quality is not vibes. It is criteria. When you make quality explicit, trust becomes repeatable and shareable.

### Day 04: Publish with care, documentation, and identifiers
Read the Day 04 guide: [day-04-publishing-with-care/README.md](day-04-publishing-with-care/README.md)

Folder: [`day-04-publishing-with-care/`](day-04-publishing-with-care/)

What you will do:
- Package your dataset and supporting materials so another person can reuse them responsibly
- Write documentation that explains what the dataset is and how it was produced
- (Optional) Deposit to a publishing platform like Zenodo and mint a DOI

What you will leave with:
- A deposit-ready publication bundle
- A documentation set that supports reuse (README, data dictionary, change notes)
- DOI-ready metadata if you choose the optional deposit path

Why this matters:
Publishing is not just uploading a file. Publishing is making something usable by someone who is not you, and doing it in a way that supports attribution, respect, and long-term access.

## Your toolbox for this workshop

I am calling this a toolbox on purpose. These are not “one special workflow” tools. These are general-purpose tools that show up across the broader data science and analytics world, and they are useful whenever you run into a new data challenge.

We also avoid expensive, proprietary platforms here. The point is portability. You should be able to use these tools on different machines, in different institutions, and in different contexts.

### OpenRefine
What it is:
- A point-and-click tool for cleaning messy data, especially metadata

Why we use it:
- It is fast to learn
- It keeps a clear history of changes
- It is excellent for making values consistent and untangling messy fields without writing code

### Apache NiFi
What it is:
- A visual way to move data through steps you can see

Why we use it:
- You can build repeatable flows without writing “glue code”
- It makes the process visible, which helps learning and auditing
- It encourages good habits around provenance and routing (including quarantine paths)

### Python and Google Colab
What it is:
- A way to run small scripts and notebooks in the browser

Why we use it:
- It reduces installation friction
- It is widely used and transferable
- It is ideal for transformations, checks, and documentation you can read like a narrative

### Pandera
What it is:
- A Python library for data validation, where you write rules that define what is acceptable

Why we use it:
- It turns “we should check this” into a repeatable set of rules
- It produces clear failures you can act on
- It supports a mindset shift from ad hoc cleaning to explicit quality standards

### Streamlit (open source)
What it is:
- A simple way to turn outputs into a small web interface

Why we use it:
- It helps colleagues review results without needing to run code
- It turns validation from a private technical step into a shared decision-making step
- It is a practical bridge between “code” and “team workflow”

### Zenodo and DOIs (optional)
What it is:
- A publishing platform and persistent identifiers for datasets

Why we use it:
- It gives your work a stable, citable home
- It supports versioning and attribution
- It encourages responsible publishing habits, including documentation and licensing

## Pace and expectations

This curriculum is designed around four sessions of 60–90 minutes. Each day includes suggested timing so you can plan, but the materials are also written so you can work through them on your own.

What success looks like here:
- You produce the outputs described in each day
- You can explain what changed and why
- You can repeat the process on a different dataset later

If you get stuck, use the troubleshooting sections in each lab. They are part of the curriculum, not an afterthought.

## Data handling, safety, and ethics

This matters. Especially in cultural heritage and adjacent domains, data is not just technical. It can involve people, communities, histories, harm, and power.

This workshop uses synthetic or safely anonymized datasets by default. When you adapt the workflow to your own data, keep these principles in view:
- Use the minimum data needed for the task
- Treat identifiers and sensitive fields as high-risk, even when they look harmless
- Document decisions, especially exclusions and transformations
- Respect rights, community protocols, and institutional constraints
- Design for responsible reuse, not maximum exposure

See [SECURITY_AND_DATA_HANDLING.md](SECURITY_AND_DATA_HANDLING.md) for practical guidance and a checklist you can use before publishing anything.

## Start here

If you are learning on your own:
1) Read [START_HERE.md](START_HERE.md)
2) Skim [TOOLBOX_SETUP.md](TOOLBOX_SETUP.md) to make sure you can access the tools
3) Start with Day 01 ([day-01-metadata-cleaning-and-normalization/README.md](day-01-metadata-cleaning-and-normalization/README.md)), or jump to the day that matches your immediate needs

If you are running this with a group:
- Use the Day overviews as your agenda (Day 01: [link](day-01-metadata-cleaning-and-normalization/README.md), Day 02: [link](day-02-repeatable-flows-and-provenance/README.md), Day 03: [link](day-03-quality-gates-and-reuse/README.md), Day 04: [link](day-04-publishing-with-care/README.md))
- Follow the suggested timing and pause at the “checkpoints” built into each day
- Pair participants when skill levels vary
- Encourage learners to narrate what they changed and why, not just click through steps

## Facilitator notes (optional)

If you are running this with participants, here are a few practical tips:
- Keep the goal visible: repeatable workflows and transferable skills, not perfection
- Narrate the why as much as the how
- When something breaks (and it will), treat troubleshooting as a learning moment
- If Docker or installs are blocked, use the provided fallback paths and focus on interpreting outputs together

This curriculum is designed to work in-person or online. It is also designed to work for individuals who want to build these skills quietly and steadily.

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

This workshop is published openly because these skills should be shareable. Please use it, adapt it, remix it, and run it in your own context.

If you improve something:
- Fix a confusing explanation
- Add a troubleshooting case you encountered
- Improve an example dataset
- Translate a section for a different audience

Contributions are welcome. Open a pull request with a clear description of what you changed and why. If you are unsure where to start, open an issue and describe the gap you found.
