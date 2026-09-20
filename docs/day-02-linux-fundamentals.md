# Day 2 — Linux Fundamentals & Shell Scripting

## DevSentinel AI — 90-Day AI + DevOps Project

### 🎯 Day 2 Goal

Learn the Linux fundamentals required for DevOps and start using Linux commands and shell scripts to automate system-related tasks.

---

# 1. What is Linux?

Linux is an open-source operating system widely used in DevOps, cloud computing, servers, containers, and CI/CD systems.

Many DevOps tools run on Linux, including:

* Jenkins
* Docker
* Kubernetes
* Terraform
* Ansible
* Prometheus
* Grafana

### Why Linux is important for DevOps

DevOps engineers commonly work with:

* Linux servers
* Cloud virtual machines
* Containers
* CI/CD servers
* Monitoring systems
* Shell scripts
* Application deployment

Therefore, Linux is one of the most important foundations of DevOps.

---

# 2. WSL — Windows Subsystem for Linux

WSL allows us to run a Linux environment directly inside Windows.

Our DevSentinel AI project is stored in Windows:

```text
C:\Users\gandu\devsentinel-ai
```

Inside WSL, the same location is accessed as:

```text
/mnt/c/Users/gandu/devsentinel-ai
```

### Important

First enter WSL:

```bash
wsl
```

Then navigate to the project:

```bash
cd /mnt/c/Users/gandu/devsentinel-ai
```

---

# 3. Linux Filesystem

Linux has a single filesystem hierarchy that starts from:

```text
/
```

This is called the root directory.

Important directories:

| Directory | Purpose                            |
| --------- | ---------------------------------- |
| `/`       | Root of the Linux filesystem       |
| `/home`   | User home directories              |
| `/etc`    | System configuration               |
| `/var`    | Logs and changing application data |
| `/tmp`    | Temporary files                    |
| `/usr`    | User programs and utilities        |
| `/opt`    | Optional software                  |
| `/bin`    | Essential commands                 |
| `/dev`    | Devices                            |
| `/mnt`    | Mounted filesystems                |

### Our WSL home directory

Our Linux username is:

```text
hari
```

Therefore the home directory is:

```text
/home/hari
```

---

# 4. Important Linux Commands

## pwd

`pwd` means **Print Working Directory**.

It shows the directory where we currently are.

```bash
pwd
```

Example:

```text
/home/hari
```

---

## ls

`ls` lists files and directories.

```bash
ls
```

For detailed information:

```bash
ls -l
```

To show hidden files:

```bash
ls -la
```

---

## cd

`cd` means **Change Directory**.

Example:

```bash
cd /home/hari
```

Go to the parent directory:

```bash
cd ..
```

Go to the home directory:

```bash
cd ~
```

---

# 5. Creating Directories

Use:

```bash
mkdir directory-name
```

Example:

```bash
mkdir scripts
```

We created the Linux scripts directory:

```text
scripts/linux
```

---

# 6. Creating Files

Use:

```bash
touch filename
```

Example:

```bash
touch commands.txt
```

---

# 7. Writing to Files

Use `echo` with `>`:

```bash
echo "Hello Linux" > file.txt
```

This creates the file and writes the text.

### Append

Use `>>`:

```bash
echo "Another line" >> file.txt
```

The `>>` operator adds content without removing existing content.

---

# 8. Reading Files

Use:

```bash
cat filename
```

Example:

```bash
cat commands.txt
```

---

# 9. Copying Files

Use:

```bash
cp source destination
```

Example:

```bash
cp file.txt backup.txt
```

---

# 10. Moving or Renaming Files

Use:

```bash
mv old-name new-name
```

Example:

```bash
mv file.txt new-file.txt
```

The same command can move files between directories.

---

# 11. Removing Files

Use:

```bash
rm filename
```

Example:

```bash
rm file.txt
```

### Important

`rm` permanently removes files in the normal Linux command-line environment, so use it carefully.

---

# 12. File Permissions

Linux controls who can read, write, or execute a file.

Example:

```text
-rw-r--r--
```

The permissions are divided into:

```text
Owner
Group
Others
```

Permissions:

```text
r = read
w = write
x = execute
```

---

# 13. chmod

`chmod` changes file permissions.

Example:

```bash
chmod +x test.sh
```

`+x` adds execute permission.

Before:

```text
-rw-r--r--
```

After:

```text
-rwxr-xr-x
```

The file can now be executed:

```bash
./test.sh
```

---

# 14. Shell Scripts

A shell script is a file containing Linux commands that can be executed together.

Shell scripts are useful for automation.

Example:

```bash
#!/bin/bash

echo "DevSentinel Linux test"
```

The first line:

```bash
#!/bin/bash
```

tells Linux to use Bash to execute the script.

---

# 15. Shell Variables

Variables store values.

Example:

```bash
NAME="DevSentinel"
```

To use the variable:

```bash
echo "$NAME"
```

Output:

```text
DevSentinel
```

Another example:

```bash
ENVIRONMENT="Development"

echo "$ENVIRONMENT"
```

---

# 16. Command Substitution

Command substitution allows the output of one command to be used inside another command.

Syntax:

```bash
$(command)
```

Example:

```bash
echo "Current user: $(whoami)"
```

Example:

```bash
echo "Current directory: $(pwd)"
```

Example:

```bash
echo "System: $(uname -s)"
```

### Important

This:

```bash
$(whoami)
```

is not normally used by itself.

Instead, place it inside another command:

```bash
echo "$(whoami)"
```

---

# 17. Important System Commands

## whoami

Shows the current Linux user.

```bash
whoami
```

Our user:

```text
hari
```

---

## hostname

Shows the computer/WSL hostname.

```bash
hostname
```

Our hostname:

```text
Harishin
```

---

## uname

Shows system information.

```bash
uname -s
```

Shows the operating system.

```bash
uname -r
```

Shows the kernel version.

```bash
uname -m
```

Shows the system architecture.

Our architecture:

```text
x86_64
```

---

## uptime

Shows how long the system has been running.

```bash
uptime
```

Human-readable version:

```bash
uptime -p
```

---

# 18. Process Management

A process is a running program.

Linux assigns every process a unique number called a:

```text
PID
```

PID means:

**Process ID**

---

## ps

Shows currently running processes.

```bash
ps
```

For more detailed information:

```bash
ps aux
```

---

## grep

`grep` searches text.

Example:

```bash
ps aux | grep bash
```

This searches running processes for `bash`.

The `|` symbol is called a **pipe**.

It sends the output of one command to another command.

---

# 19. top

`top` provides real-time system monitoring.

Run:

```bash
top
```

It can show:

* CPU usage
* Memory usage
* Processes
* Process IDs
* System load

Press:

```text
q
```

to exit `top`.

---

# 20. Memory Monitoring

Use:

```bash
free -h
```

The `-h` means human-readable.

It displays:

* Total memory
* Used memory
* Free memory
* Available memory
* Swap

---

# 21. Disk Monitoring

Use:

```bash
df -h
```

This shows disk usage.

For the root filesystem:

```bash
df -h /
```

It shows:

* Filesystem
* Size
* Used space
* Available space
* Usage percentage
* Mount point

---

# 22. DevSentinel Basic Shell Script

We created:

```text
scripts/linux/basic-script.sh
```

Contents:

```bash
#!/bin/bash

NAME="DevSentinel"
ENVIRONMENT="Development"

echo "Project: $NAME"
echo "Environment: $ENVIRONMENT"

echo "Current user: $(whoami)"
echo "Current directory: $(pwd)"
echo "System: $(uname -s)"
```

We made it executable:

```bash
chmod +x scripts/linux/basic-script.sh
```

Then executed it.

---

# 23. DevSentinel System Information Script

We created our first useful DevSentinel automation script:

```text
scripts/linux/system-info.sh
```

Contents:

```bash
#!/bin/bash

echo "========================================"
echo "        DevSentinel AI"
echo "        System Information"
echo "========================================"

echo "Hostname       : $(hostname)"
echo "User           : $(whoami)"
echo "Operating System: $(uname -s)"
echo "Kernel         : $(uname -r)"
echo "Architecture   : $(uname -m)"
echo "Uptime         : $(uptime -p)"

echo ""
echo "------------- Memory -------------------"
free -h

echo ""
echo "------------- Disk ---------------------"
df -h /

echo "========================================"
```

We made it executable:

```bash
chmod +x scripts/linux/system-info.sh
```

Run it using:

```bash
./scripts/linux/system-info.sh
```

---

# 24. What Our Script Does

The script automatically collects system information.

### Hostname

```bash
hostname
```

Identifies the machine.

### Current user

```bash
whoami
```

Shows the Linux user running the script.

### Operating system

```bash
uname -s
```

Shows the operating system.

### Kernel

```bash
uname -r
```

Shows the Linux kernel version.

### Architecture

```bash
uname -m
```

Shows CPU architecture.

### Uptime

```bash
uptime -p
```

Shows how long the system has been running.

### Memory

```bash
free -h
```

Shows memory usage.

### Disk

```bash
df -h /
```

Shows root filesystem disk usage.

---

# 25. Why This Matters in DevOps

DevOps engineers need to monitor servers.

For example, before deploying an application we may want to know:

```text
Is the server running?
How much memory is available?
How much disk space is available?
Which operating system is running?
Which user is executing the deployment?
How long has the server been running?
```

Our `system-info.sh` script starts automating these checks.

Later, DevSentinel AI will collect much more information and eventually use AI to analyze system conditions.

---

# 26. Git Workflow

After completing our work, we checked the project:

```bash
git status
```

We found the new Linux scripts.

We added them:

```bash
git add scripts/linux
```

Created a commit:

```bash
git commit -m "Add Linux fundamentals and system monitoring scripts"
```

Then pushed to GitHub:

```bash
git push
```

---

# 27. Day 2 Git Commit

Our Day 2 commit was:

```text
1afbd3c Add Linux fundamentals and system monitoring scripts
```

GitHub branch:

```text
main
```

The working tree was clean after the push:

```text
nothing to commit, working tree clean
```

---

# 28. Day 2 Project Files

At the end of Day 2, we have:

```text
devsentinel-ai/
│
├── README.md
│
├── app/
│
├── config/
│
├── docs/
│
└── scripts/
    └── linux/
        ├── basic-script.sh
        ├── commands.txt
        └── system-info.sh
```

---

# 29. Important Commands Learned

```bash
pwd
ls
ls -l
ls -la
cd
cd ..
cd ~
mkdir
touch
echo
cat
cp
mv
rm
chmod
whoami
hostname
uname
uptime
ps
ps aux
grep
top
free
df
```

---

# 30. Important Concepts Learned

### Linux

Operating system widely used in DevOps.

### Filesystem

Linux organizes files starting from `/`.

### Permissions

Linux controls read, write, and execute access.

### Processes

Running programs are represented as processes with PIDs.

### Shell

The command-line environment used to interact with Linux.

### Shell scripting

Combines commands into automated scripts.

### Git

Tracks changes in our project.

### GitHub

Stores and shares our project repository remotely.

---

# 31. Day 2 Practical Achievement

Today we progressed from manually running Linux commands to creating automation.

We built:

```text
Linux commands
      ↓
Shell scripting
      ↓
System information
      ↓
DevSentinel automation
```

This is the beginning of the DevSentinel AI platform.

---

# 32. Day 2 Summary

Today I learned:

* What Linux is
* Why Linux is important for DevOps
* How WSL works
* Linux filesystem structure
* Basic Linux commands
* Creating and managing files
* File permissions
* `chmod`
* Processes
* PIDs
* `ps`
* `top`
* Memory monitoring
* Disk monitoring
* Shell variables
* Command substitution
* Bash scripts
* Git commit
* Git push
* Basic DevOps automation

---

# 33. Day 2 Status

**Day 2 — COMPLETED ✅**

Project:

**DevSentinel AI**

GitHub:

`harishin08/devsentinel-ai`

Day 2 Git commit:

```text
1afbd3c Add Linux fundamentals and system monitoring scripts
```

Next:

**Day 3 — Git & GitHub Advanced**
