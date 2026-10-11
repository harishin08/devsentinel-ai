servers = ["web-server", "database-server", "app-server"]

print("All servers:", servers)
print("First server:", servers[0])

servers.append("backup-server")

print("After adding a server:", servers)

servers.remove("app-server")

print("After removing a server:", servers)
