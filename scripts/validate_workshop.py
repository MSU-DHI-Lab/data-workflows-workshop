#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def iter_notebooks() -> list[Path]:
    return sorted(REPO_ROOT.rglob("*.ipynb"))


def iter_csv_files() -> list[Path]:
    return sorted(REPO_ROOT.rglob("*.csv"))


def compile_notebook_code_cells(notebook_path: Path) -> list[str]:
    nb = json.loads(notebook_path.read_text(encoding="utf-8"))
    errors: list[str] = []

    for idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue

        src = "".join(cell.get("source", ""))
        lines: list[str] = []
        for line in src.splitlines():
            stripped = line.lstrip()
            if stripped.startswith("!") or stripped.startswith("%"):
                continue
            lines.append(line)

        py = "\n".join(lines).strip()
        if not py:
            continue

        try:
            compile(py, f"{notebook_path}#cell{idx}", "exec")
        except SyntaxError as exc:
            errors.append(
                f"{notebook_path} cell {idx}: {exc.msg} (line {exc.lineno})"
            )

    return errors


def validate_csv_shape(csv_path: Path) -> list[str]:
    errors: list[str] = []

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return [f"{csv_path}: empty CSV"]

        expected = len(header)
        for line_no, row in enumerate(reader, start=2):
            if len(row) != expected:
                errors.append(
                    f"{csv_path}: line {line_no} has {len(row)} columns; expected {expected}"
                )
                break

    return errors


def main() -> int:
    all_errors: list[str] = []

    for nb_path in iter_notebooks():
        all_errors.extend(compile_notebook_code_cells(nb_path))

    for csv_path in iter_csv_files():
        all_errors.extend(validate_csv_shape(csv_path))

    if all_errors:
        print("Validation failed:\n")
        for err in all_errors:
            print("-", err)
        return 1

    print("OK: notebooks compile (excluding magics) and CSVs are well-formed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

