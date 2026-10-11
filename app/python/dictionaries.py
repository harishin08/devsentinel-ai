server = {
    "name": "web-server",
    "status": "Running",
    "cpu_usage": 75,
    "environment": "Development"
}

print("Server Name:", server["name"])
print("Server Status:", server["status"])
print("CPU Usage:", server["cpu_usage"], "%")

server["cpu_usage"] = 85

print("Updated CPU Usage:", server["cpu_usage"], "%")
