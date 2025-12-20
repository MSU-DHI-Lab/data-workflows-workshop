# Data Lakes, Warehouses, and Lakehouses (Plain Language)
## What this is
Data lakes, warehouses, and lakehouses are storage patterns for organizing data. A data lake holds raw or mixed-format files with light tagging. A warehouse holds modeled tables that follow a schema (meaning: a defined table structure). A lakehouse combines both in one system so raw files and structured tables live together with clear stewardship and access rules.
## Why it matters for collections and cultural heritage data
Collections data arrives messy, then gets cleaned and published. Choosing the right pattern protects origin-and-changes context, rights, and meaning. If you over-structure too early, you risk discarding context. If you never add structure, teams struggle to search, join, and cite. Knowing these patterns helps you plan how records travel from intake to public reuse without losing trust.
## A simple mental model
Picture your garage on a busy weekend. New boxes arrive, you mark them with a quick note, and set them on a shelf until you know what to do next. That is the lake stage: raw, labeled just enough, nothing thrown away too soon.

Now think about your kitchen pantry. Staples are in clear containers with labels so you can grab what you need without hunting. That is the warehouse stage: structured, consistent, and easy to use. Between the two is a tidy workbench where you keep both raw boxes and the tools you reach for often. That blended space is the lakehouse idea. The point is not that one stage is always better. You move between them as your data matures. In this workshop you will feel the garage stage in Day 01–02 intake and movement, the pantry mindset in Day 03 checks, and the blended bench when you publish with both raw traces and curated tables in Day 04.
## A concrete example (mini case study)
Mini case study: A museum digitization team receives mixed CSVs and TIFFs every month. They place raw files in a lake folder with tags for source system, ingest date, and rights. Once a quarter, they standardize the CSVs into tidy tables for public search (warehouse-style) and convert heavy-use files into columnar formats for faster queries (lakehouse-style). They keep raw and curated versions together with manifests that show which raw files fed which tables.
## How this shows up in this workshop
- Day 01–02: You act like a lake intake, receiving raw exports and moving them through a repeatable set of steps.
- Day 03: You apply quality checks that mirror warehouse expectations such as types, required fields, and allowed lists.
- Day 04: You package and publish with origin-and-changes notes so others can reuse or cite, similar to a lakehouse where access rules and stewardship notes sit next to raw and modeled data.
## What “successful understanding” looks like
- You can explain when to keep data raw and when to model it for reuse.
- You can point to where origin-and-changes notes and rights are recorded in each pattern.
- You can map workflow steps to lake (ingest and tag), warehouse (modeled tables), or lakehouse (mixed storage with clear access rules).
- You can caution teammates about over-modeling early or skipping structure when consistent queries are needed.
- You can describe how a manifest or linking note connects raw files to curated tables.
## Common misconceptions (and the gentle correction)
- Misconception: A lake is a dumping ground. Correction: A good lake uses tags, folder structure, and readme files to keep context visible.
- Misconception: A warehouse is rigid forever. Correction: Warehouses evolve; you model what is stable and revisit when fields change.
- Misconception: Lakehouse is only marketing. Correction: It is a practical pattern that keeps raw and curated data together with table formats and clear access and stewardship rules so you avoid duplicating storage.
- Misconception: Small teams do not need patterns. Correction: Even small teams benefit from light tagging for lakes and a couple of modeled tables for recurring queries.
## Practical decision guide
- If files arrive in many formats and you are exploring fields, then start lake-style and store raw files with tags for source, date, and rights.
- If you need reliable joins and reporting, then add warehouse-style tables with clear table structures (sometimes called schemas) and data dictionaries.
- If you want one home for raw and curated files, then consider a lakehouse approach with manifests, table formats, and clear access rules.
- If auditors or partners need traceability, then keep manifests or linking notes that connect raw to curated outputs.
- If performance is an issue, then convert frequently used datasets to structured tables or columnar formats while keeping raw files.
- If resources are limited, then prioritize tagging and a few high-value tables rather than modeling everything.
## Troubleshooting and where people get stuck
- Problem: Losing context in a lake. Fix: Add minimal tags (source, ingest date, rights) and a README per folder; keep a manifest of raw files.
- Problem: Over-modeling early. Fix: Keep a raw zone; model only stable fields; note assumptions in a data dictionary.
- Problem: Too many warehouse tables to maintain. Fix: Focus on tables that serve public search or reporting; archive less-used tables as lake files with notes.
- Problem: Unclear connection between raw and curated. Fix: Keep pointers (file names, checksums, ingest dates) in a manifest stored next to both raw and modeled outputs.
- Problem: Access confusion. Fix: Write access rules per zone (raw vs curated); label sensitive fields and rights tokens in the glossary and README.
- Problem: Performance pain querying ad hoc files. Fix: Convert high-use data to columnar formats (for example, Parquet) or small warehouse tables while retaining raw files.
## Quick glossary (local to this page)
- Data lake: storage for raw or varied files with minimal structure and tagging.
- Data warehouse: structured tables designed for analysis with defined table structures (sometimes called schemas).
- Lakehouse: combined pattern where raw files and structured tables live together with clear stewardship and performance features.
- Schema (meaning: a defined structure for a table): fields, types, and allowed values.
