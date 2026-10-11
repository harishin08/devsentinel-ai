
def check_server(server_name, cpu_usage, memory_usage):
    """Validate server metrics and return a health result."""

    try:
        cpu = float(cpu_usage)
        memory = float(memory_usage)
    except (TypeError, ValueError):
        return {
            "server": server_name,
            "status": "INVALID",
            "message": "CPU and memory must be numbers."
        }

    if not 0 <= cpu <= 100 or not 0 <= memory <= 100:
        return {
            "server": server_name,
            "status": "INVALID",
            "message": "CPU and memory must be between 0 and 100."
        }

    if cpu > 80 or memory > 80:
        status = "WARNING"
        message = "High CPU or memory usage."
    else:
        status = "HEALTHY"
        message = "All metrics are within limits."

    return {
        "server": server_name,
        "status": status,
        "message": message
    }


def display_result(result):
    print(f"\nServer: {result['server']}")
    print(f"Status: {result['status']}")
    print(f"Message: {result['message']}")



def main():
    servers = [
        ("web-server", 85, 60),
        ("database-server", 45, 90),
        ("app-server", 40, 50),
        ("test-server", 150, 50),
        ("invalid-server", "abc", 50)
    ]

    counts = {
        "HEALTHY": 0,
        "WARNING": 0,
        "INVALID": 0
    }

    for server in servers:
        result = check_server(*server)
        display_result(result)
        counts[result["status"]] += 1

    print("\n" + "=" * 35)
    print("SERVER HEALTH SUMMARY")
    print("=" * 35)
    print("Healthy servers:", counts["HEALTHY"])
    print("Servers with warnings:", counts["WARNING"])
    print("Invalid server records:", counts["INVALID"])
    print("Total servers:", len(servers))


if __name__ == "__main__":
    main()

