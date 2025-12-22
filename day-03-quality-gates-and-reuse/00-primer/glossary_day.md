# Day 03 Glossary

- **Cleaning**: changing data values to fix issues (trim whitespace, standardize formats, correct typos).
- **Validation**: checking data against rules to confirm it meets expectations. Cleaning changes data; validation only checks it.
- **Quality check** (or quality gate): a set of tests data must pass before you treat it as ready to share or publish. If any test fails, you know something needs attention.
- **Validation rules** (or schema): the specific rules for fields, types, and allowed values. For example: "the rights column must not be empty" or "dates must follow YYYY-MM-DD format."
- **Quiet failure**: a data error that passes silently through a process without being caught. Validation rules prevent quiet failures by making problems visible.
- **Pandera**: a Python library for data validation. You define rules, and Pandera checks your data against them. It tells you exactly which rows and columns failed.
- **pandas**: a Python library for working with tabular data. It loads your CSV into a structure called a DataFrame so you can filter, transform, and analyze it.
- **DataFrame**: a table of data in Python, similar to a spreadsheet. It has rows and columns with labels. When you load a CSV with pandas, you get a DataFrame.
- **Check**: a Pandera rule applied to a column or the whole dataframe. For example, `Check.str_length(min_value=1)` checks that strings are not empty.
