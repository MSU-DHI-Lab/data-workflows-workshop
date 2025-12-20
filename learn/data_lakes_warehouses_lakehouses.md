# Data Lakes, Warehouses, and Lakehouses (Plain Language)
## What this is
Data lakes, warehouses, and lakehouses are storage patterns for organizing data. A data lake holds raw or mixed-format files with light tagging. A warehouse holds modeled tables that follow a defined schema. A lakehouse combines both in one system so raw files and structured tables live together with governance.
## Why it matters for collections and cultural heritage data
Collections data arrives messy, then gets cleaned and published. Choosing the right pattern protects provenance, rights, and meaning. If you over-structure too early, you risk discarding context. If you never add structure, teams struggle to search, join, and cite. Knowing these patterns helps you plan how records travel from intake to public reuse without losing trust.
## A simple mental model
Analogy 1: A data lake is like a back room where boxes arrive as-is. You label the boxes with source and date but do not re-box them yet.  
Analogy 2: A warehouse is like the main stacks with cataloged shelves and consistent call numbers so anyone can find items.  
Lakehouse: Think of a well-run back room with some shelves installed. You can keep raw boxes and also arrange frequently used items on labeled shelves without moving to a different building.
## A concrete example (mini case study)
Mini case study: A museum digitization team receives mixed CSVs and TIFFs every month. They place raw files in a lake folder with tags for source system, ingest date, and rights. Once a quarter, they standardize the CSVs into tidy tables for public search (warehouse-style) and convert heavy-use files into columnar formats for faster queries (lakehouse-style). They keep raw and curated versions together with manifests that show which raw files fed which tables.
## How this shows up in this workshop
- Day 01–02: You act like a lake intake, receiving raw exports and moving them through a pipeline.
- Day 03: You apply quality gates that mirror warehouse expectations such as types, required fields, and allowed lists.
- Day 04: You package and publish with provenance so others can reuse or cite, similar to a lakehouse where governance and access sit next to raw and modeled data.
## What “successful understanding” looks like
- You can explain when to keep data raw and when to model it for reuse.
- You can point to where provenance and rights are recorded in each pattern.
- You can map workflow steps to lake (ingest and tag), warehouse (modeled tables), or lakehouse (mixed storage with governance).
- You can caution teammates about over-modeling early or skipping structure when consistent queries are needed.
- You can describe how a manifest or lineage note links raw files to curated tables.
## Common misconceptions (and the gentle correction)
- Misconception: A lake is a dumping ground. Correction: A good lake uses tags, folder structure, and readme files to keep context visible.
- Misconception: A warehouse is rigid forever. Correction: Warehouses evolve; you model what is stable and revisit when fields change.
- Misconception: Lakehouse is only marketing. Correction: It is a practical pattern that keeps raw and curated data together with table formats and governance so you avoid duplicating storage.
- Misconception: Small teams do not need patterns. Correction: Even small teams benefit from light tagging for lakes and a couple of modeled tables for recurring queries.
## Practical decision guide
- If files arrive in many formats and you are exploring fields, start lake-style: store raw files with tags for source, date, and rights.
- If you need reliable joins and reporting, add warehouse-style tables with clear schemas and data dictionaries.
- If you want one home for raw and curated files, consider a lakehouse approach with manifests and table formats that support governance.
- If auditors or partners need traceability, keep manifests or lineage notes that connect raw to curated outputs.
- If performance is an issue, convert frequently used datasets to structured tables or columnar formats while keeping raw files.
- If resources are limited, prioritize tagging and a few high-value tables rather than modeling everything.
## Troubleshooting and where people get stuck
- Problem: Losing context in a lake. Fix: Add minimal tags (source, ingest date, rights) and a README per folder; keep a manifest of raw files.
- Problem: Over-modeling early. Fix: Keep a raw zone; model only stable fields; note assumptions in a data dictionary.
- Problem: Too many warehouse tables to maintain. Fix: Focus on tables that serve public search or reporting; archive less-used tables as lake files with notes.
- Problem: Unclear lineage between raw and curated. Fix: Keep pointers (file names, checksums, ingest dates) in a manifest stored next to both raw and modeled outputs.
- Problem: Access confusion. Fix: Write access rules per zone (raw vs curated); label sensitive fields and rights tokens in the glossary and README.
- Problem: Performance pain querying ad hoc files. Fix: Convert high-use data to columnar formats (for example, Parquet) or small warehouse tables while retaining raw files.
## Quick glossary (local to this page)
- Data lake: storage for raw or varied files with minimal structure and tagging.
- Data warehouse: structured tables designed for analysis with defined schemas.
- Lakehouse: combined pattern where raw files and structured tables live together with governance and performance features.
- Schema: a defined structure for a table including fields, types, and allowed values.
- Lineage: the record of where data came from and how it changed.
