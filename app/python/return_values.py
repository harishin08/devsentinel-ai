def check_cpu(cpu_usage):
    if cpu_usage > 80:
        return "HIGH"
    else:
        return "NORMAL"


status = check_cpu(85)
print("CPU Status:", status)

status = check_cpu(45)
print("CPU Status:", status)
