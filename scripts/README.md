# Workshop Validation Scripts

These are maintainer utilities for quick sanity checks.

## Validate notebooks and sample CSVs

Runs two lightweight checks:

- All `*.ipynb` code cells compile as Python (ignoring notebook magics like `!pip` and `%`).
- All `*.csv` files have consistent column counts on every row (catches unquoted commas like `Doe, Jane`).

From the repo root:

```bash
python3 scripts/validate_workshop.py
```

