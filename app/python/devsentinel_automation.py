import os
import platform
import shutil
import subprocess


def check_project():
    print("\n--- Project Directory Check ---")

    for folder in ["app", "docs", "scripts", "config"]:
        if os.path.isdir(folder):
            print(f"[OK] {folder} exists")
        else:
            print(f"[MISSING] {folder}")


def check_system():
    print("\n--- System Information ---")
    print("Operating System:", platform.system())
    print("Hostname:", platform.node())
    print("Python Version:", platform.python_version())

    disk = shutil.disk_usage("/")
    total_gb = disk.total / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)

    print(f"Root Disk Size: {total_gb:.2f} GB")
    print(f"Root Disk Free: {free_gb:.2f} GB")


def check_command():
    print("\n--- Command Check ---")

    try:
        result = subprocess.run(
            ["uptime"],
            capture_output=True,
            text=True,
            timeout=10,
            check=True
        )
        print(result.stdout.strip())
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        print("Unable to check uptime:", error)


print("===================================")
print("       DevSentinel AI")
print("       Automation Utility")
print("===================================")

check_project()
check_system()
check_command()

print("\nAutomation completed.")
