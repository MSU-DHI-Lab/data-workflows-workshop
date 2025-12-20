# Troubleshooting

1) **NiFi container won't start**  
   - Fix: Check Docker is running; ensure port 8080 is free; retry `docker compose up`.

2) **Cannot reach UI / certificate warning**  
   - Fix: Accept the local cert warning (expected); confirm container is healthy in Docker Desktop.

3) **GetFile not picking up files**  
   - Fix: Confirm path `/opt/nifi/inputs`; ensure files exist; set `Keep Source File` to false.

4) **Processor shows invalid state**  
   - Fix: Open the processor; fill required properties; apply and retry start.

5) **Regex in ReplaceText not matching**  
   - Fix: Use `(?i)` for case-insensitive; escape dots; test with a simple pattern first.

6) **Files not routing to quarantine**  
   - Fix: Verify RouteOnContent expression; confirm connection for `quarantine` relationship exists and is started.

7) **PutFile fails to write**  
   - Fix: Ensure mounted directories exist; check container logs for permission errors.

8) **Provenance empty**  
   - Fix: Expand the time window; ensure processors are running; look at queued FlowFiles and select provenance.

9) **Flow too chatty / cluttered**  
   - Fix: Pause processors; simplify; remove unused processors. If you cannot explain a box, do not ship it.
