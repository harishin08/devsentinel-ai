def check_server(server_name, cpu_usage, memory_usage):
    print("\nChecking server:", server_name)

    if cpu_usage > 80:
        cpu_status = "HIGH"
    else:
        cpu_status = "NORMAL"

    if memory_usage > 80:
        memory_status = "HIGH"
    else:
        memory_status = "NORMAL"

    print("CPU Usage:", str(cpu_usage) + "%")
    print("CPU Status:", cpu_status)
    print("Memory Usage:", str(memory_usage) + "%")
    print("Memory Status:", memory_status)

    if cpu_status == "HIGH" or memory_status == "HIGH":
        print("Overall Status: WARNING")
    else:
        print("Overall Status: HEALTHY")


check_server("web-server", 85, 60)
check_server("database-server", 45, 90)
check_server("app-server", 40, 50)
