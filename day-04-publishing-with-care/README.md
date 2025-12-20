# Day 04: Publishing with Care

Welcome. This final day focuses on packaging your work so others can reuse it safely. You will assemble the key documentation files, prepare Zenodo metadata, and optionally stand up a small Streamlit (open source) handoff view for colleagues.

## Why publishing needs care
Publishing is different from sharing. It adds clear rights and reuse terms, a short history of what changed, and a stable reference (a DOI) so people can cite and build on your work without guessing.

## Why publishing artifacts matter
Each artifact carries a piece of the trust story:
- README: what this is, where it came from, how to use it safely.
- Data dictionary: what each field means so meaning doesn’t drift.
- LICENSE: how others may reuse the work.
- CITATION.cff: how to credit the creators and version.
- Zenodo metadata: the structured record that powers the DOI landing page.

## What you'll do and produce
- Build a publishable data package with data, docs, and checks in one folder.
- Draft licensing, citation, and Zenodo metadata (practice path requires no account).
- Optionally deploy a simple Streamlit handoff app for colleagues.

## Suggested timing (so you can plan your session)
- Lab 01 (package the dataset): ~20 minutes
- Lab 02 (licensing + citation + Zenodo metadata): ~30 minutes
- Lab 03 (optional Streamlit handoff): ~20 minutes

## Two paths
- **Practice path:** prepare all artifacts locally without depositing anywhere. No accounts required.
- **Live path:** if you have a Zenodo account, deposit, mint a DOI, and record it in the package.

## Navigation
- Primer: `00-primer/concepts.md`, `00-primer/glossary_day.md`
- Labs: `01-labs/`
- Job aids: `02-job-aids/`
- Assessments: `03-assessments/`
- Diagrams: `04-diagrams/`
- Artifacts: `05-artifacts/`

## What success looks like
- You produce a single package folder that contains data, docs, and checks.
- LICENSE, CITATION.cff, and .zenodo.json agree on title, version, and reuse terms.
- You can hand the package to someone else and they can understand it without a separate meeting.

## Where people get stuck (and quick fixes)
- License uncertainty: use the licensing explainer in `learn/` and choose a license that matches your risk level.
- CITATION.cff formatting errors: check indentation and keep keys exactly as written.
- JSON errors in .zenodo.json: validate JSON and avoid trailing commas.
- Restricted accounts: complete the practice path and keep the deposit steps as an optional follow-on.
