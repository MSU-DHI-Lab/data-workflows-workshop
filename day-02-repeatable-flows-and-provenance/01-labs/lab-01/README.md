# Lab 01: Run NiFi Locally and Orient

The goal of this lab is to start NiFi, load the interface in your browser, and learn what the main boxes and queues do. This takes about 15 minutes.

NiFi runs inside Docker, which is a program that packages software so it works the same way on any computer. You do not need to understand Docker deeply. You will run a few commands, and Docker will handle the rest.

**Inputs:** `docker-compose.yml` (a recipe file in this lab folder that tells Docker how to run NiFi)

**Outputs:** NiFi running at `http://localhost:8080/nifi/`

## Before You Start

This is your first time running NiFi. The interface might look complex, but you will only use a few features. Take it slow and focus on getting the environment running. Building the actual flow happens in Lab 02.

If you cannot run Docker on your machine (managed computer, restricted permissions), you can still follow along by reviewing the provided flow template and screenshots. Ask your facilitator to share their screen, or see the facilitator fallback in [troubleshooting.md](../../02-job-aids/troubleshooting.md).

---

## Step 1: Confirm Docker Desktop Is Running

Docker Desktop is a free program that runs containers (self-contained software packages) on your computer. You need it running before you can start NiFi.

Open Docker Desktop from your Applications folder (macOS) or Start menu (Windows). Once it opens, you should see the Docker whale icon in your menu bar (macOS) or system tray (Windows). The icon means Docker is running and ready.

If Docker is not installed, download it from https://www.docker.com/products/docker-desktop and follow the installation steps. The installer is straightforward. You may need to restart your computer after installing.

---

## Step 2: Open a Terminal in This Lab Folder

A terminal is a text-based way to talk to your computer. Instead of clicking icons, you type commands.

**Where to find a terminal:**
- **macOS**: Open the "Terminal" app (in Applications > Utilities, or search for "Terminal")
- **Windows**: Open "Command Prompt" or "PowerShell" (search in the Start menu)
- **VS Code**: View menu > Terminal (or press Ctrl+` on Windows, Cmd+` on Mac)

Once your terminal is open, you need to navigate to this lab folder. The command `cd` means "change directory" — it is like double-clicking a folder to go inside it.

Type this command (adjust the path if you downloaded the workshop to a different location):

```
cd Documents/data-workflows-workshop/day-02-repeatable-flows-and-provenance/01-labs/lab-01
```

**How to verify you are in the right place:**
- On macOS/Linux, type `ls` and press Enter
- On Windows, type `dir` and press Enter

You should see a file called `docker-compose.yml` in the list. This is the recipe file that tells Docker how to run NiFi.

If you see "file not found" or "No such file or directory" errors, you are not in the right folder. Double-check the path and try again. You need to be inside the `lab-01` folder.

---

## Step 3: Start NiFi

Run this command:

```
docker compose up
```

(On older Docker versions, you may need `docker-compose up` with a hyphen.)

**What happens when you run this command:**

1. Docker reads the recipe file (`docker-compose.yml`) in this folder
2. Docker downloads the NiFi software package (called an "image") if this is your first time. This download can take a few minutes depending on your internet speed.
3. Docker creates a container from that package and starts NiFi inside it
4. NiFi becomes available in your web browser

You will see logs scrolling in your terminal as NiFi starts up. The logs may look dense and technical. That is normal. Look for lines mentioning "Started" or "NiFi has started." This can take 1-2 minutes even after the download finishes.

If the command fails, check that Docker Desktop is running (look for the whale icon). Also check that nothing else is using port 8080 on your machine. On macOS/Linux, run `lsof -i :8080` to see what is using the port. On Windows, run `netstat -ano | find "8080"`.

**What is a port?** A port is like a numbered door on your computer. When NiFi runs, it listens on door 8080 for your browser to knock. If another program is already using door 8080, NiFi cannot open it.

---

## Step 4: Open the NiFi UI

Open your browser and go to:

```
http://localhost:8080/nifi/
```

You may see a certificate warning. This is normal for local development. Accept it and continue.

You should see the NiFi canvas: a large empty workspace with a toolbar on the left. The toolbar has icons for adding processors, input ports, output ports, and other components.

This is your first time seeing NiFi. The interface can look overwhelming, but you only need a few features today. The canvas is where you drag and connect processors. The toolbar on the left lets you add things. The top-right area shows status. Do not worry about understanding everything right now.

If the page does not load, wait another minute and refresh. NiFi takes a little while to fully start. If it still does not load, check your terminal for error messages.

---

## Step 5: Confirm Folders for Lab 02 Exist

NiFi runs inside a container, which is like a sealed box. By default, NiFi cannot see files on your computer. The recipe file (`docker-compose.yml`) creates small windows between the container and your computer so NiFi can read from and write to specific folders.

These "windows" connect three folders inside `lab-02/` (next door to this lab folder) to NiFi:

- `inputs/` (where you put files for NiFi to pick up)
- `outputs/` (where NiFi puts clean files)
- `quarantine/` (where NiFi puts questionable files)

Open `lab-02/` in your file browser or terminal. If these folders do not exist, create them now. NiFi cannot write to folders that do not exist on your machine.

You should see all three folders inside `lab-02/`. If any are missing, create them before continuing.

---

## Step 6: Seed the Inbox with a Sample File

Copy the sample file from this folder's `inputs/intake_sample.csv` into `lab-02/inputs/`.

In your terminal, from the `lab-01/` folder:

```
cp inputs/intake_sample.csv ../lab-02/inputs/
```

Or use your file browser to copy the file manually.

You should see `intake_sample.csv` inside `lab-02/inputs/`. This CSV is the data your flow will process in Lab 02. Having it ready means you can test the flow as soon as you build it.

---

## Step 7: Stop NiFi When Finished Exploring

When you are done looking around the NiFi UI, go back to your terminal and press **Ctrl+C** (hold the Control key and press C) to stop NiFi.

> **Note:** In a terminal, Ctrl+C means "stop the running program" — it is NOT copy/paste like in other applications.

You should see the logs stop and your terminal prompt return (the blinking cursor waiting for your next command).

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
