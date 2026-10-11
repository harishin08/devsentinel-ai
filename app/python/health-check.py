cpu_usage = 45.5

print("DevSentinel AI Server Health Check")
print("CPU Usage:", cpu_usage, "%")

if cpu_usage > 80:
    print("WARNING: High CPU usage!")
else:
    print("Server CPU usage is normal.")

