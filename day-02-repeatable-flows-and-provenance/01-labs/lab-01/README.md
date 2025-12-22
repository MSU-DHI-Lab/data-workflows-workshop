# Lab 01: Run NiFi Locally and Orient

The goal of this lab is to start NiFi in Docker, load the UI, and learn what the main boxes and queues do. This takes about 15 minutes.

**Inputs:** `docker-compose.yml` (a configuration file in this lab folder that tells Docker how to run NiFi)

**Outputs:** NiFi running at `http://localhost:8080/nifi/`

## Before You Start

This is your first time running NiFi. The interface might look complex, but you will only use a few features. Take it slow and focus on getting the environment running. Building the actual flow happens in Lab 02.

If you cannot run Docker on your machine (managed computer, restricted permissions), you can still follow along by reviewing the provided flow template and screenshots. Ask your facilitator to share their screen, or see the facilitator fallback in [troubleshooting.md](../../02-job-aids/troubleshooting.md).

---

## Step 1: Confirm Docker Is Running

Open Docker Desktop (or check your Docker engine) and make sure it is running. You should see the Docker whale icon in your menu bar or system tray.

If Docker is not installed, download it from https://www.docker.com/products/docker-desktop and follow the installation steps. You may need to restart your computer.

---

## Step 2: Open a Terminal in This Lab Folder

Open a terminal (Terminal on macOS, Command Prompt or PowerShell on Windows, or the built-in terminal in VS Code) and navigate to this folder:

```
cd day-02-repeatable-flows-and-provenance/01-labs/lab-01
```

You should see the `docker-compose.yml` file when you list the directory contents (`ls` on macOS/Linux, `dir` on Windows).

If you see "file not found" errors, check your path. You need to be inside the `lab-01` folder.

---

## Step 3: Start NiFi with Docker Compose

Run this command:

```
docker compose up
```

(On older Docker versions, you may need `docker-compose up` with a hyphen.)

Docker will pull the Apache NiFi image if this is your first time. That download can take a few minutes. After that, you will see logs scrolling in your terminal as NiFi starts up.

Wait until you see messages about processors being available or the web server starting. This can take 1-2 minutes even after the download finishes.

If the command fails, check that Docker is running. Also check that nothing else is using port 8080 on your machine. On macOS/Linux, run `lsof -i :8080` to see what is using the port. On Windows, run `netstat -ano | find "8080"`.

---

## Step 4: Open the NiFi UI

Open your browser and go to:

```
http://localhost:8080/nifi/
```

You may see a certificate warning. This is normal for local development. Accept it and continue.

You should see the NiFi canvas: a large empty workspace with a toolbar on the left. The toolbar has icons for adding processors, input ports, output ports, and other components.

If the page does not load, wait another minute and refresh. NiFi takes a little while to fully start. If it still does not load, check your terminal for error messages.

---

## Step 5: Create Folders for Lab 02

Before you build a flow, you need folders for the flow to watch. In the `lab-02/` folder (next door to this one), create three folders if they do not already exist:

- `inputs/`
- `outputs/`
- `quarantine/`

These folders map to volume mounts that NiFi can access. The flow will pick up files from `inputs/`, process them, and write to `outputs/` or `quarantine/`.

---

## Step 6: Seed the Inbox with a Sample File

Copy the sample file `inputs/intake_sample.csv` from this lab folder into `../lab-02/inputs/`.

This CSV is the data your flow will process in Lab 02. Having it ready means you can test the flow as soon as you build it.

---

## Step 7: Stop NiFi When Finished Exploring

When you are done looking around the NiFi UI, go back to your terminal and press Ctrl+C to stop the container.

You should see Docker logs stop and your terminal prompt return.

If the container does not stop cleanly, run `docker compose down` in the same directory to force a shutdown.

---

## Checkpoint

Before moving on, confirm:

- [ ] Docker is installed and running
- [ ] NiFi started successfully and you saw the canvas at `http://localhost:8080/nifi/`
- [ ] `lab-02/inputs/`, `lab-02/outputs/`, and `lab-02/quarantine/` folders exist
- [ ] The sample CSV is in `lab-02/inputs/`

If all four are checked, you are ready for Lab 02.

---

## If Something Went Wrong

**Docker will not start:** Make sure Docker Desktop is running. On some systems, you need to enable virtualization in your BIOS settings.

**Port 8080 already in use:** Another application is using that port. Stop the other service, or edit the port mapping in `docker-compose.yml` (change `8080:8080` to something like `8081:8080`) and access NiFi at the new port.

**NiFi takes forever to start:** The first run downloads the image and initializes data. This is normal. Subsequent starts will be faster.

**Certificate warning in browser:** This is expected for local development. Accept the warning and continue.

**Cannot reach UI even after waiting:** Check the terminal for error messages. If NiFi crashed, try restarting with `docker compose down` followed by `docker compose up`.
