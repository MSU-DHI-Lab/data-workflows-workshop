# Primer Concepts

## What today is about
You will package cleaned data with documentation, rights, and citation details so it can be reused and cited safely. The focus is publishing artifacts, careful reuse, and an optional handoff app.

## Key concepts
- Publishing with care: practices that keep data safe, explainable, and respectful of rights and context. Think of packing a fragile item for shipping: you add padding, clear labels, and a note on how to handle it so it arrives intact.
- Publish package: a bundle with data, documentation, and checks ready for partners or the public. It lets the work travel without you in the room.
- DOI: a persistent, citable link with versioning that provides continuity about which version someone used.
- Versioning: tagging releases so changes are trackable and citable.
- Licensing: permissions and restrictions on reuse (for example, CC BY, CC0, Rights Reserved) matched to the data and media.

## Links to learn pages
- Publishing and DOIs: `learn/publishing_data_in_plain_language.md` and `learn/dois_persistent_ids_and_citation.md`.
- Documentation: `learn/documentation_that_travels_with_data.md`.
- Licensing: `learn/licensing_for_datasets_and_media.md`.

## Why this toolset fits today
- Publishing artifacts (LICENSE, CITATION.cff, .zenodo.json) make the package citable and clear.
- Streamlit offers a simple handoff for colleagues to view data and quality status without code. Tradeoff: requires a local install if you run it.

## What success looks like today
- A dataset package with data, README, data dictionary, notes on where the files came from and what changed, validation report, LICENSE, CITATION.cff, and .zenodo.json.
- Practice path bundle stored locally; live path ready for Zenodo if you choose to deposit.
- Optional Streamlit app runs and shows the curated data and quality status.

## Where people get stuck
- License mismatch across files: align LICENSE, README, CITATION.cff, and .zenodo.json.
- DOI not recorded locally: add DOI and version to README and CITATION.cff after minting.
- Sensitive content: ensure redactions before bundling; note them in README and in the notes on what changed.
- Streamlit paths: run the app from `day-04-publishing-with-care/01-labs/lab-03/` so relative paths resolve.
