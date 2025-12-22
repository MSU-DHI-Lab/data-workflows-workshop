# Performance Task

## Scenario
You need to ship a dataset to a downstream team. They trust your cleaning but want proof it meets agreed rules of trust.

## Your task
1) Profile the dataset (shape, missingness, uniques) and note the top 6–10 risks.
2) Create Pandera validation rules with checks for those risks and validate the dataset.
3) Run validation on both the clean file and an intentionally flawed file; capture the failure cases.
4) Produce a markdown report summarizing results and recommended next actions (fix data, adjust checks, quarantine).

## Submission
- Place your validation rules file (`validation_schema.py`), validation report, and any notes in `05-deliverables/submissions/`.
- Include the inputs and outputs you used for testing.
