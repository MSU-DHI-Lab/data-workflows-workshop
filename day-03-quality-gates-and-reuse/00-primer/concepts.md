# Primer Concepts

## What today is about
You will add quality gates to cleaned data so it can travel safely. Cleaning fixes values; validation proves they meet expectations. Both matter for trust.

## Key concepts
- Cleaning vs validation: cleaning changes data (trim, normalize). Validation checks data against rules (types, allowed lists) to prove readiness.
- Quality gate: a defined set of checks that data must pass before moving forward. Analogy: a condition report before an object goes on loan.
- Schema: a structured set of rules about fields, types, ranges, and allowed values. It makes expectations explicit and versioned.
- Quiet failure: when data breaks expectations silently and flows onward. It erodes trust because downstream teams inherit issues without warning.

## Why we start small (6–10 checks)
Small sets are explainable and runnable in session time. They cover the highest-risk issues first. You can add more once core rules of trust are solid.

## Collections examples
- Rights token restricted to an allowed list so publishing stays safe.
- Identifier required and positive so records do not collapse into each other.
- Date field constrained to realistic years to avoid malformed timelines.

## Why Pandera fits today
- Declarative rules read like documentation; no hunting for scattered if-statements.
- Clear failure messages show rows and checks, good for handoff.
- Runs in Colab with a single install and can be saved as a reusable module.
- Tradeoff: Python-based; keep checks readable for non-coders and document them alongside the data.

## Links to learn pages
- Validation and publishing connect to `learn/publishing_data_in_plain_language.md` and `learn/dois_persistent_ids_and_citation.md`.
- Documentation practices connect to `learn/documentation_that_travels_with_data.md`.

## What success looks like today
- A Pandera schema with 6–10 checks runs and either passes clean data or surfaces clear failure cases.
- Validation report saved and ready to share.
- You can explain each check and the risk it prevents.

## Where people get stuck
- Type casting: fix with `coerce=True` or by casting in pandas first.
- Missing files: upload or point to the correct CSV path before running.
- Overly strict checks: start with core fields (id, rights, place, date) and loosen if needed with documented rationale.
- Forgetting to share evidence: save the failure cases or summary so stakeholders see what was tested.
