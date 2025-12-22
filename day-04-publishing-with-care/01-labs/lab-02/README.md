# Lab 02: Licensing, Citation, and Zenodo Metadata

The goal of this lab is to prepare legal and descriptive artifacts for publishing. You will choose a license, fill out citation details, and prepare Zenodo metadata. Optionally, you can deposit to Zenodo and mint a DOI.

This takes about 30 minutes.

**Inputs:** `../lab-01/outputs/dataset-package/`

**Outputs:**
- LICENSE file with clear reuse terms
- CITATION.cff with citation details
- .zenodo.json with repository metadata
- Completed publishing checklist

## Before You Start

This lab deals with legal and administrative details. It may feel less hands-on than the earlier labs, but it matters a lot. Without clear licensing, others cannot legally reuse your data. Without citation details, they cannot give you credit. Without stable identifiers, links break over time.

Take your time with this lab. The files you create will outlive the project.

---

## Step 1: Choose and Confirm Your License

Open `artifacts/LICENSE` and review the contents.

A common choice for data is **CC BY 4.0** (Creative Commons Attribution 4.0). This allows others to share and adapt your data as long as they give credit.

If your institution has specific requirements, follow those. If you are unsure, CC BY 4.0 is a safe default for non-sensitive data.

You should see clear license text that matches your choice.

Make sure the license you put in this file matches what you say in the README, CITATION.cff, and .zenodo.json. Inconsistency creates confusion.

---

## Step 2: Update CITATION.cff

Open `artifacts/CITATION.cff` and fill in the details.

CITATION.cff is a YAML file (YAML is a text format for structured data, similar to JSON but more human-readable). It tells tools and people how to cite your work.

Required fields:
- `cff-version: 1.2.0` (keep this as-is)
- `title:` Your dataset title
- `message:` A short instruction like "If you use this dataset, please cite it as below."
- `authors:` A list of contributors with name and optionally ORCID
- `version:` Your version number (for example, 1.0.0)
- `date-released:` The release date (YYYY-MM-DD format)
- `license:` The license identifier (for example, CC-BY-4.0)

Example:

```yaml
cff-version: 1.2.0
title: Curated Collection Export
message: If you use this dataset, please cite it as below.
authors:
  - family-names: Smith
    given-names: Jane
version: 1.0.0
date-released: 2025-12-22
license: CC-BY-4.0
```

Save the file. If you see YAML errors, check indentation (use spaces, not tabs) and make sure strings do not have unescaped special characters.

---

## Step 3: Fill Out .zenodo.json

Open `artifacts/.zenodo.json` and fill in the metadata.

This file tells Zenodo how to populate your deposit and DOI landing page. JSON (JavaScript Object Notation) is a structured text format. Each field has a name and a value.

Required fields:
- `title`
- `description`
- `creators` (array of objects with `name` and optionally `orcid` and `affiliation`)
- `license` (use a license identifier like "cc-by-4.0")
- `upload_type` (for datasets, use "dataset")
- `version`

Example:

```json
{
  "title": "Curated Collection Export",
  "description": "A cleaned and validated set of collection records for reuse.",
  "creators": [
    {
      "name": "Smith, Jane",
      "affiliation": "Example Museum"
    }
  ],
  "license": "cc-by-4.0",
  "upload_type": "dataset",
  "version": "1.0.0"
}
```

Save the file. JSON is strict about syntax: no trailing commas, use double quotes, match brackets carefully. Use an online JSON validator if you are unsure.

---

## Step 4: Walk Through the Publishing Checklist

Open `publishing_checklist.md` (if provided) or create a simple checklist:

- [ ] Data file is present in package
- [ ] README explains the dataset
- [ ] Data dictionary defines fields
- [ ] Origins and changes are documented
- [ ] Validation report is included
- [ ] LICENSE file is present
- [ ] CITATION.cff is complete
- [ ] .zenodo.json is valid
- [ ] Title, version, and license match across all files

Go through each item. If something is missing, go back and fix it.

---

## Step 5: Bundle for Practice Path

If you are not depositing to Zenodo, create a zip of the `dataset-package/` folder plus LICENSE, CITATION.cff, and .zenodo.json.

Place the zip in `05-artifacts/`.

This is your practice package. It is complete and ready to share even without a DOI.

---

## Step 6: Deposit to Zenodo (Optional Live Path)

If you want to mint a DOI:

1. Go to https://zenodo.org/ and sign in
2. Click "Upload" and start a new upload
3. Upload your package files
4. Fill in metadata from your `.zenodo.json` (copy values manually or use Zenodo's form)
5. Select your license
6. Click "Reserve DOI" to get a draft DOI, or "Publish" to make it live

You should see a DOI assigned to your deposit.

If Zenodo rejects your upload, check that required fields are filled and file sizes are within limits.

---

## Step 7: Record the DOI (If You Minted One)

If you published to Zenodo and received a DOI:

1. Add the DOI to `CITATION.cff` in a `doi:` field
2. Add the DOI to your package README

This ensures the DOI is visible inside the package, not just on Zenodo.

---

## Checkpoint

Before moving on, confirm:

- [ ] LICENSE file is present and matches your choice
- [ ] CITATION.cff is complete with title, authors, version, date, and license
- [ ] .zenodo.json is valid JSON with required fields
- [ ] Title, version, and license are consistent across all files
- [ ] (Optional) You have a DOI recorded if you deposited to Zenodo

If all items are checked, you are ready for Lab 03 (optional) or you have completed Day 04.

---

## If Something Went Wrong

**License uncertainty:** Choose CC BY 4.0 for most non-sensitive data. Consult your institution if you have restrictions.

**CITATION.cff errors:** YAML is sensitive to indentation. Use spaces, not tabs. Check that colons have a space after them. Compare against the example.

**Invalid .zenodo.json:** Remove trailing commas. Use double quotes around strings. Validate with an online JSON checker.

**Zenodo upload fails:** Check file size limits. Ensure all required fields are filled. Save as draft before publishing to catch errors.

**Mismatch across files:** Open all four files (README, LICENSE, CITATION.cff, .zenodo.json) side by side and verify title, version, and license match exactly.
