
import os
from datetime import datetime


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "health-check.log")


def write_log(message):
    os.makedirs(LOG_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


def check_server(server_name, cpu_usage, memory_usage):
    print("\nChecking server:", server_name)

    try:
        cpu_usage = float(cpu_usage)
        memory_usage = float(memory_usage)
    except (TypeError, ValueError):
        message = f"{server_name}: Invalid CPU or memory value."
        print("ERROR:", message)
        write_log("ERROR - " + message)
        return

    if not 0 <= cpu_usage <= 100:
        message = f"{server_name}: CPU usage must be between 0 and 100."
        print("ERROR:", message)
        write_log("ERROR - " + message)
        return

    if not 0 <= memory_usage <= 100:
        message = f"{server_name}: Memory usage must be between 0 and 100."
        print("ERROR:", message)
        write_log("ERROR - " + message)
        return

    cpu_status = "HIGH" if cpu_usage > 80 else "NORMAL"
    memory_status = "HIGH" if memory_usage > 80 else "NORMAL"

    overall_status = (
        "WARNING"
        if cpu_status == "HIGH" or memory_status == "HIGH"
        else "HEALTHY"
    )

    print(f"CPU Usage: {cpu_usage:g}%")
    print("CPU Status:", cpu_status)
    print(f"Memory Usage: {memory_usage:g}%")
    print("Memory Status:", memory_status)
    print("Overall Status:", overall_status)

    message = (
        f"{server_name} | CPU: {cpu_usage:g}% ({cpu_status}) | "
        f"Memory: {memory_usage:g}% ({memory_status}) | "
        f"Overall: {overall_status}"
    )
    write_log(message)


check_server("web-server", 85, 60)
check_server("database-server", 45, 90)
check_server("app-server", 40, 50)
check_server("test-server", 150, 50)
check_server("invalid-server", "abc", 50)
