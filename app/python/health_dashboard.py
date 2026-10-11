
import os
import platform
import shutil
from datetime import datetime

import psutil


LOG_DIR = "logs"
REPORT_FILE = os.path.join(LOG_DIR, "health-dashboard.txt")


def collect_metrics():
    """Collect CPU, memory, and disk usage."""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = shutil.disk_usage(".")

    disk_percent = (disk.total - disk.free) / disk.total * 100

    return {
        "cpu": cpu,
        "memory": memory.percent,
        "disk": disk_percent,
    }


def determine_status(metrics):
    """Determine overall system health."""
    if any(value > 80 for value in metrics.values()):
        return "WARNING"
    return "HEALTHY"


def generate_report():
    os.makedirs(LOG_DIR, exist_ok=True)

    metrics = collect_metrics()
    status = determine_status(metrics)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = [
        "=" * 45,
        "       DEVSENTINEL AI HEALTH DASHBOARD",
        "=" * 45,
        f"Timestamp: {timestamp}",
        f"Hostname: {platform.node()}",
        f"Operating System: {platform.system()}",
        "",
        f"CPU Usage: {metrics['cpu']:.1f}%",
        f"Memory Usage: {metrics['memory']:.1f}%",
        f"Disk Usage: {metrics['disk']:.2f}%",
        "",
        f"Overall Status: {status}",
        "=" * 45,
    ]

    report_text = "\n".join(report)

    print(report_text)

    with open(REPORT_FILE, "a", encoding="utf-8") as file:
        file.write(report_text + "\n\n")

    print(f"\nReport saved to: {REPORT_FILE}")


if __name__ == "__main__":
    generate_report()
