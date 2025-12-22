# Day 02 Glossary

- **Processor**: a NiFi building block that performs one action. Think of processors as stations on an assembly line — each one does a specific job (read a file, check a value, write to a folder). You drag processors onto the canvas and connect them.
- **FlowFile**: NiFi's name for a piece of data moving through your flow. A FlowFile includes the actual content (like your CSV) plus extra information (attributes) like filename and timestamp. Think of it as an envelope carrying your data.
- **Provenance**: NiFi's detailed record of what happened to each FlowFile. It logs events like "received," "routed," "modified," and "dropped." You can open the provenance view to trace exactly where a file went and what happened at each step.
- **Lineage**: the traced path of a FlowFile through processors and queues. If provenance is the full history book, lineage is the map showing the journey.
- **Back pressure**: a safety setting that slows down processors when queues fill up. It prevents NiFi from getting overwhelmed. If you see yellow warning colors on a connection, that is back pressure at work.
- **Quarantine**: a separate destination for problematic FlowFiles. Instead of mixing bad records with good ones, you route them to a quarantine folder for review. This keeps your output clean.
- **Connection**: the arrow linking two processors. Connections also hold a queue of FlowFiles waiting to be processed. You can click a connection to see how many files are waiting.
- **Canvas**: the main NiFi work area where you drag, drop, and connect processors. It is the visual representation of your data flow.
