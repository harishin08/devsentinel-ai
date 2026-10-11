
# Day 8 - Reliable Python Automation

## Objectives
- Build a reusable server health checker.
- Validate CPU and memory values.
- Handle invalid input without crashing.
- Count and summarize server statuses.

## Concepts Learned
- Reusable Python functions
- Dictionaries and return values
- try/except error handling
- Numeric conversion using float()
- Validating metric ranges from 0 to 100
- The main() function
- The if __name__ == "__main__" pattern
- Counting results with dictionary values

## Project Files
- app/python/reliable_health_check.py
- docs/day-08-reliable-python-automation.md

## Test Results
- Healthy servers: 1
- Servers with warnings: 2
- Invalid server records: 2
- Negative CPU and memory values rejected
- Non-numeric input rejected
- Exactly 80% CPU and memory reported as HEALTHY

## Key Takeaway
Reliable automation validates its inputs, handles errors safely,
and produces consistent results.

## Day 8 Status
Completed: reusable health checks, error handling, and summaries.
