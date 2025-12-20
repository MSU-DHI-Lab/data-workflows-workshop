# Quick Reference

## Mindset
- Tests are kindness: they prevent surprises for the next person.
- Checks encode shared expectations; write them so a teammate can nod and agree.

## Pandera essentials
- Define your validation rules once; reuse them everywhere (`DataFrameSchema` with `Check`s).
- Use `lazy=True` to gather all failures at once instead of failing fast.
- Keep checks explainable: each rule should map to a real risk (e.g., rights list prevents unsafe publishing).

## Common checks to start with
- Required fields: ids, titles, rights.
- Allowed lists: rights tokens, place names.
- Ranges: dates within collection scope.
- Types: integers where needed, strings for text.

## Reporting
- Save the failure cases table or markdown report for colleagues.
- Pair the report with next steps (fix data vs adjust checks vs quarantine).
