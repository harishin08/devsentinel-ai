report = """DevSentinel AI - Server Health Report
Server: web-server
Status: Running
CPU Usage: 75%
"""

# Write the report to a file
with open("server_report.txt", "w") as file:
    file.write(report)

print("Health report saved successfully.")

# Read the report from the file
with open("server_report.txt", "r") as file:
    content = file.read()

print("\nReport Contents:")
print(content)
