
# Day 6 - Python Health Checks and Logging

## Objectives
- Improve server health-check automation.
- Validate CPU and memory usage.
- Handle invalid inputs safely.
- Record health-check results in a log file.

## Concepts Learned
- Python functions
- Input validation using try/except
- CPU and memory thresholds
- Healthy and warning statuses
- Creating directories with os.makedirs()
- Writing timestamped log entries
- Appending to files using open() with mode "a"

## Project Files
- app/python/health_checker.py
- logs/health-check.log

## Test Results
- Web server: WARNING because CPU usage is 85%.
- Database server: WARNING because memory usage is 90%.
- App server: HEALTHY.
- Test server: Invalid CPU usage rejected.
- Invalid server: Non-numeric input rejected.
- Repeated runs successfully append results to the log.

## Key Takeaway
Logging creates a record of health checks that can help investigate
server problems later.

## Day 6 Status
Completed: health-check validation and timestamped logging.
