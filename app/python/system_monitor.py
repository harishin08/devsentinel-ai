
import os
import shutil
import platform
import psutil
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "system-monitor.log")


def write_log(message):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


def check_system():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = shutil.disk_usage(".")

    disk_used = (disk.total - disk.free) / disk.total * 100

    if cpu_usage > 80 or memory.percent > 80 or disk_used > 80:
        status = "WARNING"
    else:
        status = "HEALTHY"

    print("=" * 45)
    print("       DEVSENTINEL AI SYSTEM MONITOR")
    print("=" * 45)
    print("Time:", timestamp)
    print("Operating System:", platform.system())
    print("Hostname:", platform.node())
    print(f"\nCPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Available Memory: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Disk Usage: {disk_used:.2f}%")
    print(f"Disk Free: {disk.free / (1024 ** 3):.2f} GB")
    print("\nOverall Status:", status)
    print("=" * 45)

    message = (
        f"Host: {platform.node()} | CPU: {cpu_usage}% | "
        f"Memory: {memory.percent}% | Disk: {disk_used:.2f}% | "
        f"Status: {status}"
    )

    write_log(message)
    print(f"Log saved to: {LOG_FILE}")


if __name__ == "__main__":
    check_system()

