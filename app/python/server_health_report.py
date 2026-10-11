import os
from datetime import datetime


def check_server(server_name, cpu_usage, memory_usage):
    if not 0 <= cpu_usage <= 100 or not 0 <= memory_usage <= 100:
        return {
            "server": server_name,
            "cpu": cpu_usage,
            "memory": memory_usage,
            "status": "INVALID"
        }

    if cpu_usage > 80 or memory_usage > 80:
        status = "WARNING"
    else:
        status = "HEALTHY"

    return {
        "server": server_name,
        "cpu": cpu_usage,
        "memory": memory_usage,
        "status": status
    }


def generate_report(servers):
    print("=" * 45)
    print("       DEVSENTINEL AI HEALTH REPORT")
    print("=" * 45)
    print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    healthy = 0
    warnings = 0
    invalid = 0

    for server in servers:
        result = check_server(
            server["name"],
            server["cpu"],
            server["memory"]
        )

        print(f"\nServer: {result['server']}")
        print(f"CPU Usage: {result['cpu']}%")
        print(f"Memory Usage: {result['memory']}%")
        print(f"Status: {result['status']}")

        if result["status"] == "HEALTHY":
            healthy += 1
        elif result["status"] == "WARNING":
            warnings += 1
        else:
            invalid += 1

    print("\n" + "=" * 45)
    print("SUMMARY")
    print("Healthy servers:", healthy)
    print("Servers with warnings:", warnings)
    print("Invalid server records:", invalid)
    print("Total servers:", len(servers))
    print("=" * 45)


servers = [
    {"name": "web-server", "cpu": 85, "memory": 60},
    {"name": "database-server", "cpu": 45, "memory": 90},
    {"name": "app-server", "cpu": 40, "memory": 50},
    {"name": "test-server", "cpu": 150, "memory": 50}
]

generate_report(servers)
