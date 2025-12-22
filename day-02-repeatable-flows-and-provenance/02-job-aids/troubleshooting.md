# Troubleshooting

1) **NiFi will not start**  
   - Fix: Check that Docker Desktop is running (look for the whale icon in your menu bar). Make sure port 8080 is free (no other program using that numbered door). Then retry `docker compose up`.

2) **Cannot reach NiFi in browser / certificate warning**  
   - Fix: Accept the certificate warning (this is expected for local development). If the page still does not load, open Docker Desktop and confirm NiFi shows as running. Wait another minute and refresh.

3) **GetFile not picking up files**  
   - Fix: Confirm the path is `/opt/nifi/inputs` (this is where NiFi looks inside the container). Make sure files actually exist in `lab-02/inputs/` on your computer. Set `Keep Source File` to false.

4) **Processor shows invalid state**  
   - Fix: Open the processor configuration; fill in the required properties (shown with red text); click Apply and try starting again.

5) **Regex in ReplaceText not matching**  
   - Fix: Use `(?i)` at the start for case-insensitive matching; escape dots with backslash (`\.`); test with a simple pattern first.

6) **Files not routing to quarantine**  
   - Fix: Verify the RouteOnContent expression matches what you expect; confirm the connection for the `quarantine` relationship exists and is started.

7) **PutFile fails to write**  
   - Fix: Ensure the folders (`lab-02/outputs/` and `lab-02/quarantine/`) exist on your computer. Open Docker Desktop and click on the NiFi container to view logs for permission errors.

8) **Run record (Provenance view) is empty**  
   - Fix: Expand the time window in the provenance viewer; ensure processors are running (green play icon); confirm files actually moved through the flow.

9) **Flow looks too complex or cluttered**  
   - Fix: Pause processors; simplify by removing unused ones; remember that if you cannot explain what a processor does, you probably do not need it.
