cpu_usage = 85

if cpu_usage > 80:
    print("WARNING: High CPU usage!")
elif cpu_usage > 60:
    print("NOTICE: CPU usage is moderate.")
else:
    print("CPU usage is normal.")
