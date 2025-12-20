# Lab 01: Run NiFi Locally and Orient

Goal: start NiFi in Docker, load the UI, and learn what the main boxes and queues do.

Inputs: `docker-compose.yml` (a small configuration file Docker reads, in this lab folder)
Outputs: Running NiFi UI at `http://localhost:8080/nifi/`
Time: ~15 minutes.

## Steps
1) **Do:** Ensure Docker Desktop is running, then open a terminal in this lab folder.  
   **Why:** Docker gives everyone the same NiFi version and settings, reducing "works on my machine" issues.  
   **You should see:** A shell prompt inside `lab-01/`.  
   **If it doesn't look right:** Install/start Docker Desktop; re-run the terminal in this folder.

2) **Do:** Run `docker-compose up` (or `docker compose up`) in this directory.  
   **Why:** Starts NiFi with the provided configuration.  
   **You should see:** Docker pulling `apache/nifi` then logs showing NiFi starting; health checks passing.  
   **If it doesn't look right:** Retry with `docker compose up` if your Docker uses the newer syntax; check that address 8080 is free.

3) **Do:** Visit `http://localhost:8080/nifi/` in your browser.  
   **Why:** Access the canvas to build and inspect flows.  
   **You should see:** The NiFi UI; your browser may warn about certificates.  
   **If it doesn't look right:** Accept the local certificate warning (expected in local dev); confirm NiFi is still running in Docker.

4) **Do:** Create local folders `inputs/`, `outputs/`, and `quarantine/` inside `lab-02/` if they are not present.  
   **Why:** These map to volume mounts for the flow to watch and write files.  
   **You should see:** Three folders in `lab-02/`.  
   **If it doesn't look right:** Make sure you are in the repo root when creating folders; check permissions.

5) **Do:** Place the sample CSV `lab-01/inputs/intake_sample.csv` into `lab-02/inputs/`.  
   **Why:** Seeds the inbox with data the flow will pick up in Lab 02.  
   **You should see:** The CSV file present in `lab-02/inputs/`.  
   **If it doesn't look right:** Copy the file again; verify the path is correct.

6) **Do:** Stop NiFi when finished observing (Ctrl+C in the terminal).  
   **Why:** Frees resources before building the flow in Lab 02.  
   **You should see:** Docker logs stop and the prompt return.  
   **If it doesn't look right:** Run `docker compose down` in the same directory.
