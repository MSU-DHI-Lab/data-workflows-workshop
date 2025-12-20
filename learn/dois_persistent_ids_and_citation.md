# DOIs, Persistent IDs, and Citation (Plain Language)
## What this is
Digital Object Identifiers (DOIs) and other persistent identifiers are stable references for digital objects. They provide a long-lived link and a metadata record that tell people how to cite and find a specific version of your dataset or artifact.
## Why it matters for collections and cultural heritage data
Collections teams rely on origin-and-changes information and attribution. A DOI keeps the link stable even if storage moves. It shows which version someone used and how to credit the creators. Without a persistent ID, people can cite the wrong file or lose trust in your release.
## A simple mental model
Analogy 1: A DOI is like an accession number for a digital object. Even if the storage location changes, the number still points to the item.  
Analogy 2: A DOI is like a stable catalog record URL. The shelving might change, but the record link remains the same.
## A concrete example (mini case study)
Mini case study: An archive publishes a cleaned metadata CSV and a small set of images. They register a DOI on Zenodo with version 1.0.0. Six months later they correct 50 creator names and release version 1.1.0 with a new DOI and links back to 1.0.0. Researchers can cite the exact version they used and understand what changed.
## How this shows up in this workshop
- Day 04 uses Zenodo metadata to prepare for DOI minting.
- CITATION.cff includes version, authors, and optionally a DOI so offline copies remain citable.
- README and data package docs remind you to record the DOI and version together.
## What “successful understanding” looks like
- You can explain why a DOI is more reliable than a plain URL.
- You can fill in key DOI metadata (title, creators, version, license, description).
- You can update CITATION.cff and README with a new DOI after a release.
- You can describe how to cite the dataset so others can attribute properly.
- You know when to mint a new DOI versus updating metadata on an existing one.
## Common misconceptions (and the gentle correction)
- Misconception: A DOI is only for articles. Correction: DOIs work for datasets, code, and other research objects.
- Misconception: One DOI forever. Correction: Each meaningful release should have its own DOI, linked through version notes.
- Misconception: If I have a DOI, I do not need documentation. Correction: The DOI record helps, but you still need README, license, and notes on what changed so people know what they are getting.
## Practical decision guide
- If your release is public and you want formal citation, then mint a DOI (Zenodo is a common choice).
- If your data changes frequently, then plan version numbers and release notes before minting.
- If your data contains sensitive elements, then ensure redactions are done before depositing.
- If you have multiple related files, then package them together and describe them in the DOI metadata.
- If collaborators need offline copies, then include the DOI and version inside README and CITATION.cff.
- If you release a minor correction, then decide whether to update metadata or mint a new DOI and document the choice.
## Troubleshooting and where people get stuck
- Problem: DOI metadata rejected. Fix: Ensure required fields (title, creators, description, license) are filled and valid JSON (a structured text format for storing data) if using the API (application programming interface).
- Problem: Wrong version cited. Fix: Maintain a changelog; link prior DOIs in the description; update README and CITATION.cff with the current DOI.
- Problem: License mismatch. Fix: Make license choices consistent across README, CITATION.cff, and the `.zenodo.json` file.
- Problem: Files too large. Fix: Check Zenodo size limits; compress or split; describe large external files in the DOI record.
- Problem: Sensitive data included. Fix: Redact before upload; document redactions in README and in your notes on what changed.
- Problem: Team forgets to record DOI offline. Fix: Add DOI and version to README, CITATION.cff, and package labels.
## Quick glossary (local to this page)
- DOI: Digital Object Identifier, a persistent ID with a resolvable link and metadata.
- Persistent ID: Any long-lived identifier that remains stable even if storage moves.
- Citation: The formal way to credit and reference a work, including authors, title, version, and DOI.
- Versioning: Assigning numbered releases (for example, 1.0.0) so changes are traceable.
- Metadata record: The descriptive fields attached to a DOI that tell others what the object is.
