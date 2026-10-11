cpu_usage = 85
memory_usage = 90
server_running = True

print("Both CPU and memory are high:",
      cpu_usage > 80 and memory_usage > 80)

print("CPU or memory is high:",
      cpu_usage > 80 or memory_usage > 80)

print("Server is not running:",
      not server_running)
