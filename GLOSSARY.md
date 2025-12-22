# Glossary

## File Formats

- **CSV (Comma-Separated Values)**: a plain text file where each line is a row of data and commas separate the columns. You can open CSV files in Excel, Google Sheets, or any text editor. Most data tools can read and write CSV.
- **JSON (JavaScript Object Notation)**: a structured text format that stores data as name-value pairs. It uses curly braces `{ }` and square brackets `[ ]` to organize information. Many tools use JSON for settings and data exchange. Example: `{"name": "Jane", "role": "curator"}`
- **YAML (YAML Ain't Markup Language)**: a human-readable text format often used for configuration files. It uses indentation (spaces) instead of brackets. The `docker-compose.yml` file is written in YAML. Example:
  ```
  name: Jane
  role: curator
  ```
- **UTF-8**: a way of encoding text that supports characters from all languages (accents, non-Latin scripts, symbols). When a file uses UTF-8 encoding, special characters display correctly. If you see garbled text (like Ã© instead of é), the file may have been opened with the wrong encoding.

## Web and Network Terms

- **localhost**: your own computer, accessed through a web browser. When you see `http://localhost:8080`, you are not visiting a website on the internet — you are connecting to software running on your own machine. The address `127.0.0.1` means the same thing.
- **Port**: a numbered door on your computer where software listens for connections. NiFi uses port 8080, OpenRefine uses port 3333. If a port is "already in use," another program is using that door.

## Data Concepts

- **Container**: a self-contained package that bundles software with everything it needs to run. Think of it like a shipping container for software: you can move it to any computer and it works the same way because everything is packed inside. Containers keep the software isolated from the rest of your computer.
- **Data lake**: storage for raw or varied files with minimal structure and tagging. Suited for intake and exploration.
- **Data warehouse**: structured tables designed for analysis with defined schemas and consistent joins.
- **Lakehouse**: combined pattern where raw files and structured tables live together with clear stewardship and performance features.
- **Data vault**: modeling approach with hubs (stable IDs), links (relationships), and satellites (changing details) that preserves history.
- **Schema** (meaning: a defined structure for a table): fields, types, and allowed values.
- **Lineage**: the record of where data came from and how it changed through steps.
- **Provenance**: descriptive history of origin, handling, and cleaning choices.
- **DataFrame**: a table of data in Python (rows and columns), similar to a spreadsheet. The pandas library creates and manipulates dataframes.

## Tools and Software

- **Docker**: a free program that creates and runs containers. You install Docker Desktop on your computer, and it handles the technical work of running containerized software like NiFi. Docker is like a universal delivery truck that can run any properly packaged software.
- **Docker Compose**: a helper tool that reads a simple recipe file (called `docker-compose.yml`) and uses Docker to start containers with the right settings. Instead of typing many commands, you just run `docker compose up` and the recipe handles the rest.
- **OpenRefine**: desktop tool for interactive cleaning, faceting, and exportable operations history.
- **Apache NiFi**: visual tool for building and running step-by-step flows with provenance and routing. In this workshop, NiFi runs inside a Docker container so you do not need to install it directly on your computer.
- **Pandera**: Python library for data validation. It checks whether your data meets rules you define (like "this column must not be empty").
- **pandas**: a Python library for working with tabular data. It loads CSV files into dataframes so you can filter, transform, and analyze them.
- **Streamlit (open source)**: Python framework to create simple web apps for sharing data views without heavy setup.
- **pip**: a tool that downloads and installs Python packages. The command `pip install pandera` downloads Pandera from the internet and installs it.
- **Virtual environment**: an isolated workspace for Python packages. It keeps packages for this workshop separate from other Python projects on your computer.

## Publishing and Citation

- **DOI (Digital Object Identifier)**: persistent ID with a resolvable link and metadata for citation.
- **Persistent ID**: any long-lived identifier that remains stable even if storage moves.
- **Citation**: formal reference to a work with authors, title, version, and persistent ID.
- **Versioning**: assigning numbered releases (for example, 1.0.0) so changes are traceable.
- **License**: permissions for reuse; examples include CC BY, CC0, and Rights Reserved.
- **Zenodo**: repository service that can mint DOIs for datasets and related files.
- **CITATION.cff**: citation file format describing how to reference a dataset or code package.
- **Rights token**: short statement describing reuse conditions (for example, Public Domain, CC BY 4.0).
