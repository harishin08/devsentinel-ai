# Day 5 — Python Scripting and DevOps Automation

**Project:** DevSentinel AI  
**Phase:** 1 — Foundations  
**Status:** Completed

## 1. Command-Line Arguments

The `sys` module allows Python scripts to receive input from the terminal.

```python
import sys

if len(sys.argv) < 2:
    print("Usage: python3 script.py <server_name>")
else:
    print("Checking server:", sys.argv[1])
```

Example:

```bash
python3 app/python/command_args.py web-server
```

## 2. Environment Variables

Environment variables configure applications without hardcoding settings.

```python
import os

environment = os.getenv("APP_ENV", "Development")
server_name = os.getenv("SERVER_NAME", "web-server")

print("Environment:", environment)
print("Server:", server_name)
```

Example:

```bash
APP_ENV=Production SERVER_NAME=database-server python3 app/python/environment_variables.py
```

## 3. File and Directory Automation

Python can inspect project files and directories using the `os` module.

```python
import os

print(os.getcwd())
print(os.listdir("."))

if os.path.isdir("app"):
    print("App directory exists.")
```

Useful functions:
- `os.getcwd()` — current working directory.
- `os.listdir()` — lists directory contents.
- `os.path.exists()` — checks whether a path exists.
- `os.path.isdir()` — checks whether a path is a directory.

## 4. Running Linux Commands

The `subprocess` module allows Python to execute system commands.

```python
import subprocess

result = subprocess.run(
    ["uptime"],
    capture_output=True,
    text=True,
    timeout=10,
    check=True
)

print(result.stdout)
```

Important options:
- `capture_output=True` captures output.
- `text=True` returns text instead of bytes.
- `timeout=10` limits execution time.
- `check=True` raises an exception for a nonzero exit status.

Prefer fixed command argument lists and avoid executing untrusted input.

## 5. System Information

The `platform` module provides system details.

```python
import platform

print(platform.system())
print(platform.node())
print(platform.python_version())
```

The `shutil` module provides disk usage information.

```python
import shutil

disk = shutil.disk_usage("/")

print("Total bytes:", disk.total)
print("Used bytes:", disk.used)
print("Free bytes:", disk.free)
```

## 6. Final DevSentinel AI Automation Utility

File: `app/python/devsentinel_automation.py`

The utility combines:
- Project directory checks.
- Operating-system information.
- Hostname and Python version.
- Root filesystem capacity.
- Linux uptime command execution.

### Successful Test Results

- `app` — found.
- `docs` — found.
- `scripts` — found.
- `config` — found.
- Operating system — Linux (WSL2).
- Python version — 3.14.4.
- Disk information — displayed successfully.
- Uptime command — executed successfully.

## Key Takeaways

1. Command-line arguments make scripts reusable.
2. Environment variables support configurable applications.
3. Python can inspect files and directories.
4. `subprocess.run()` connects Python automation to Linux commands.
5. `platform` and `shutil` provide useful system information.
6. Error handling and command timeouts make automation safer.

## Day 5 Completion

**Status:** Completed — Python scripting and basic DevOps automation.

**Next:** Day 6 — Python automation practice and a more robust DevSentinel utility.
