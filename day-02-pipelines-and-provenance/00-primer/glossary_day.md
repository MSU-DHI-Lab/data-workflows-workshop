# Day 02 Glossary

- **Processor**: a NiFi component that performs one action on flow files.
- **FlowFile**: NiFi's unit of data plus attributes moving through the flow.
- **Provenance**: the recorded history of FlowFile events (receive, route, modify, drop).
- **Lineage**: the traced path of a FlowFile through processors and queues.
- **Back pressure**: NiFi setting that slows upstream processors when queues fill.
- **Quarantine**: an explicit route for problematic FlowFiles to separate storage for review.
- **Connection**: the link between processors that also holds queued FlowFiles.
