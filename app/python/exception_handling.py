try:
    cpu_usage = int(input("Enter CPU usage (0-100): "))

    if cpu_usage < 0 or cpu_usage > 100:
        print("Error: CPU usage must be between 0 and 100.")
    elif cpu_usage > 80:
        print("WARNING: High CPU usage!")
    else:
        print("CPU usage is normal.")

except ValueError:
    print("Error: Please enter a valid number.")
