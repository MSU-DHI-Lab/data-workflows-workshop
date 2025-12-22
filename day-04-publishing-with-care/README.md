# Day 04: Publishing with Care

## Introduction

This final day is about packaging your work so others can reuse it without guesswork. You will gather data, documentation, and quality evidence into a single folder, write clear reuse terms, and prepare citation details. If you choose, you will also stand up a small Streamlit handoff view for colleagues.

Publishing is the bridge from your workspace to someone else's. Cultural heritage collections provide the stories here, but any team that shares data needs the same habits: transparent licensing, clear versioning, and a stable landing place. You will see how to make your package easy to cite, easy to trust, and easy to maintain.

For term definitions used throughout this day, see [today's glossary](00-primer/glossary_day.md) and the [shared glossary](../GLOSSARY.md).

## What You Will Build Today

By the end of this session, you will have:

- A complete dataset package folder with data, docs, and validation outputs together
- A filled-in LICENSE, CITATION.cff, and `.zenodo.json` that agree on title, version, and reuse terms
- A concise README and data dictionary that explain what the data is and how to use it safely
- Zenodo-ready metadata for a draft or future deposit (no account required for practice)
- An optional Streamlit handoff app that previews the package for colleagues

## Why This Matters in a Real Data Workflow

Day 04 is where you publish for reuse with documentation and identifiers. Clear packages stop reuse from becoming risky improvisation, and stable references keep citations consistent over time. This is what prevents a half-documented folder from spreading confusion across teams or partners.

## Today's Toolbox

### Documentation Files

You will work with several standard file types that help others understand and reuse your data:

- **README** explains what the data is, where it came from, and how to use it safely
- **Data dictionary** defines each field so nobody has to guess what "rights" or "place" means
- **LICENSE** states what others can and cannot do with your data (for example, CC BY 4.0 allows reuse with attribution)
- **CITATION.cff** tells people how to cite your work in papers, projects, or other packages
- **.zenodo.json** provides structured metadata that Zenodo uses to create a DOI landing page

You will edit these files in any text editor. VS Code works well, but any editor that saves UTF-8 text is fine.

### Zenodo

Zenodo is a free service that hosts research outputs and can mint DOIs (Digital Object Identifiers). A DOI is a persistent link that stays stable even if you move files to a new server. It makes your work citable in a way that will not break.

**How to use Zenodo:**

1. Go to https://zenodo.org/ and create a free account (or sign in with your existing account)
2. Click "Upload" to start a new deposit
3. Fill in metadata (title, authors, description, license, version)
4. Upload your package files
5. Choose whether to publish immediately or save as a draft

For this workshop, you can complete everything locally without uploading. The practice path lets you prepare `.zenodo.json` and validate your metadata without needing an account.

### Streamlit (Optional)

Streamlit is a Python tool that creates simple web apps from scripts. In Lab 03, you can optionally run a small handoff app that lets colleagues browse your data and see quality status without touching notebooks.

**How to get Streamlit running:**

1. From the `01-labs/lab-03/` folder, run `pip install streamlit`
2. Run `streamlit run app.py`
3. Your browser opens to a local URL with the dashboard

This is optional. If you skip it, you still complete Day 04 successfully by finishing Labs 01 and 02.

## Setup Checklist

Before you begin the labs:

1. Review the shared checklist in [TOOLBOX_SETUP.md](../TOOLBOX_SETUP.md) to confirm you have a text editor ready
2. Open the template files in this folder and confirm you can edit and save them in UTF-8
3. **Optional app path:** If you want to run the Streamlit app, confirm Python 3.9+ is available and run `pip install streamlit`

**If you run into trouble:**

- **License or citation mismatch:** Make sure title, version, authors, and license text match across README, LICENSE, CITATION.cff, and `.zenodo.json`
- **YAML errors in CITATION.cff:** Check spacing (YAML is sensitive to indentation), use plain quotes, and compare against the examples in Lab 02
- **JSON errors in `.zenodo.json`:** Remove trailing commas and validate the file structure before saving. Online JSON validators can help spot problems.
- **Streamlit module not found:** Rerun `pip install streamlit` in your active environment, then retry the launch command
- **Local app cannot load files:** Run the app from `01-labs/lab-03/` so relative paths resolve correctly

If you cannot install locally or create accounts, complete the practice path: finish Labs 01 and 02, keep the package locally, and review `01-labs/lab-03/validation_report.md` to see expected app output.

## Suggested Timing

| Lab | Focus | Time |
|-----|-------|------|
| Lab 01 | Assemble the dataset package structure | ~20 minutes |
| Lab 02 | Complete licensing, citation, and Zenodo metadata | ~30 minutes |
| Lab 03 | Optional: Run the Streamlit handoff app | ~20 minutes |

If time is tight, finish Labs 01 and 02. You can review the Lab 03 report later without running the app.

## Navigation

| File | What it contains |
|------|------------------|
| [00-primer/concepts.md](00-primer/concepts.md) | Primer on why careful publishing and identifiers matter |
| [00-primer/glossary_day.md](00-primer/glossary_day.md) | Definitions for publishing and licensing terms |
| [01-labs/lab-01/README.md](01-labs/lab-01/README.md) | Lab 01: Build the package folder and organize files |
| [01-labs/lab-02/README.md](01-labs/lab-02/README.md) | Lab 02: Licensing, citation, and Zenodo metadata |
| [01-labs/lab-03/README.md](01-labs/lab-03/README.md) | Lab 03: Optional Streamlit handoff app |
| [02-job-aids/quick_reference.md](02-job-aids/quick_reference.md) | Publishing steps and required files summary |
| [02-job-aids/troubleshooting.md](02-job-aids/troubleshooting.md) | Troubleshooting for licensing, metadata, and app issues |
| [03-assessments/knowledge_check.md](03-assessments/knowledge_check.md) | Short questions to confirm publishing concepts |
| [03-assessments/performance_task.md](03-assessments/performance_task.md) | Applied task to package and document a dataset for reuse |
| [05-deliverables/README.md](05-deliverables/README.md) | Checklist of what to save and how to store final outputs |

## Working Solo vs. Facilitating a Group

**If you are working on your own:** Work through Labs 01 and 02 to complete the package, then decide if you want to run the optional app in Lab 03. Self-check by confirming the license, citation, and `.zenodo.json` all match, and that the README makes sense to a new reader.

**If you are leading a group:** Have participants pair up for Lab 01 to compare how they organize packages. In Lab 02, pause to align on licensing choices and citation details. Treat Lab 03 as optional show-and-tell if time allows or if installations vary.

## You Are Done When

Check your work against this list. You should have:

- [ ] `01-labs/lab-01/outputs/dataset-package/` containing:
  - [ ] `data/curated_collection.csv` (your cleaned data)
  - [ ] `docs/README.md` with purpose, source, and reuse guidance
  - [ ] `docs/data_dictionary.csv` defining each field
  - [ ] `docs/origins_and_changes.md` explaining how the data was cleaned
  - [ ] `checks/` folder with your validation report from Day 03
- [ ] `01-labs/lab-02/deliverables/LICENSE` with clear reuse terms (for example, CC BY 4.0)
- [ ] `01-labs/lab-02/deliverables/CITATION.cff` with title, authors, version, and date
- [ ] `01-labs/lab-02/deliverables/.zenodo.json` with matching metadata
- [ ] All four files (README, LICENSE, CITATION.cff, .zenodo.json) agreeing on title, version, and license

If you have a complete package folder with documentation and aligned metadata, you have completed the core work for Day 04. The package is ready to share, deposit, or hand off to a colleague.

## Troubleshooting at a Glance

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| License text unclear | Not sure which license fits | Review [quick_reference.md](02-job-aids/quick_reference.md) and keep the chosen license consistent |
| CITATION.cff will not parse | Indentation or syntax error | Check indentation, avoid tabs, validate against example keys |
| .zenodo.json rejected | Missing required fields or trailing commas | Ensure required fields are present, validate JSON structure |
| Streamlit app not launching | Module not installed | Run `pip install streamlit` and start from `lab-03/` |
| Package feels incomplete | Missing files | Compare against the checklist in [05-deliverables/README.md](05-deliverables/README.md) |

For more troubleshooting, see [02-job-aids/troubleshooting.md](02-job-aids/troubleshooting.md).

## Workshop Complete: What You Have Built

Over four days, you have:

1. **Day 01:** Cleaned messy metadata and exported a replayable operations file
2. **Day 02:** Built a visible flow with quarantine routing and captured a run record
3. **Day 03:** Written validation rules and produced a quality report
4. **Day 04:** Packaged everything with licensing, citation, and documentation

You now have a complete data workflow that is:

- **Legible:** Others can read what happened at every step
- **Repeatable:** Operations files, flow templates, and validation schemas can be rerun
- **Trustworthy:** Quality checks and provenance traces show the data passed inspection
- **Shareable:** The package has clear terms, citation details, and a stable structure

This is not the only way to do data work, but it is a solid foundation. The tools and habits here travel well to other projects, other teams, and other kinds of data.

## Take It Further

If you want to explore beyond the workshop:

- **Deposit to Zenodo:** If you have real data you can share, create a Zenodo deposit and mint a DOI
- **Automate with GitHub Actions:** Set up a GitHub repository that runs validation automatically when you push new data
- **Add a data catalog entry:** If your institution has a data catalog, register your package there
- **Teach someone else:** Walk a colleague through the workflow. Teaching is one of the best ways to solidify what you learned.
- **Connect to a larger pipeline:** Explore how NiFi flows can feed into data warehouses or visualization tools

## Reflection Prompts

Take a moment to think about the full workshop arc:

- What part of this workflow would have the biggest impact on your current data practices?
- If you had to explain this workshop to a skeptical colleague in two sentences, what would you say?
- What is one thing you will do differently the next time you receive a messy data export?

These questions do not have right answers. They help you connect what you learned to the work waiting for you when you return.

## Thank You

You made it through the workshop. That took effort, curiosity, and patience. The skills you practiced here, making data legible, processes visible, quality explicit, and packages trustworthy, are valuable in any context where data matters.

Keep the toolbox. Use it when the next messy export arrives.
