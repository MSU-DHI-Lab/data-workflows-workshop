# Security and Data Handling

## Principles
- Use synthetic or safely anonymized data for exercises. Do not place live sensitive records in this repo.
- Protect rights and donor restrictions. Keep rights tokens and licenses visible in README and data dictionaries.
- Keep provenance: note sources, redactions, and cleaning steps so others understand what changed.

## Handling guidance
- Redaction: remove or mask personally identifiable information and sensitive location details before sharing. Note redactions in README and provenance notes.
- Access: store working files locally or in approved institutional storage. Avoid public links for sensitive drafts.
- Retention: delete temporary working files after packaging the final artifacts. Keep the published bundle and its documentation together.
- Attribution: include CITATION.cff and license details with every shared bundle to set reuse expectations.

## Checks before sharing
- Verify rights tokens and licenses match across README, data dictionary, LICENSE, and .zenodo.json (if used).
- Confirm validation reports are included so downstream teams see quality status.
- Ensure no uncontrolled PII or sensitive coordinates remain. Re-run facets for likely identifiers and locations.
- Include a short “how to handle this data” note in the package README.

## If something goes wrong
- If sensitive data leaks into a working file, stop sharing, remove the file, re-run redaction, and document the fix in provenance.
- If rights are unclear, pause publishing and confirm with the rights holder or policy team.
- If a bundle was shared without documentation, issue an updated bundle with README, dictionary, license, and citation information.
