
# Day 9 - System Monitoring Automation

## Objectives
- Monitor CPU usage.
- Check memory and disk usage.
- Determine overall system health.
- Save monitoring results to a log file.

## Concepts Learned
- Python third-party libraries
- Installing psutil in a virtual environment
- CPU monitoring with psutil.cpu_percent()
- Memory monitoring with psutil.virtual_memory()
- Disk monitoring with shutil.disk_usage()
- Conditional health status checks
- Timestamped logging
- Creating directories with os.makedirs()
- Appending log entries to files

## Project Files
- app/python/system_monitor.py
- logs/system-monitor.log

## Test Results
- CPU usage: 0.1%
- Memory usage: 13.3%
- Disk usage: 54.98%
- Overall status: HEALTHY
- Log entry successfully created.

## Key Takeaway
System monitoring helps identify resource usage and potential
problems before they affect applications.

## Day 9 Status
Completed: CPU, memory, disk monitoring, and logging.
