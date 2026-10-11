# Day 4 — Python Fundamentals

## 1. Introduction to Python

Python is a programming language used for automation, scripting, application development, and AI.

Check the installed version:

```bash
python3 --version
```

## 2. Printing Output

The `print()` function displays information.

```python
print("Hello from DevSentinel AI!")
```

## 3. Variables

Variables store data.

```python
project_name = "DevSentinel AI"
environment = "Development"
version = 1

print(project_name)
print(environment)
print(version)
```

## 4. Data Types

Common Python data types:

- `str` — text
- `int` — whole numbers
- `float` — decimal numbers
- `bool` — `True` or `False`
- `list` — collection of items
- `dict` — key-value pairs

Example:

```python
project = "DevSentinel AI"
version = 1
cpu_usage = 45.5
is_running = True

print(type(project))
print(type(version))
print(type(cpu_usage))
print(type(is_running))
```

## 5. Conditions

Use `if`, `elif`, and `else` to make decisions.

```python
cpu_usage = 85

if cpu_usage > 80:
    print("High CPU usage!")
elif cpu_usage > 60:
    print("Moderate CPU usage.")
else:
    print("CPU usage is normal.")
```

## 6. Comparison Operators

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `==` | Equal to |
| `!=` | Not equal to |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

## 7. Logical Operators

- `and` — both conditions must be true.
- `or` — at least one condition must be true.
- `not` — reverses a Boolean value.

```python
cpu_usage = 85
memory_usage = 90

print(cpu_usage > 80 and memory_usage > 80)
print(cpu_usage > 80 or memory_usage > 80)
```

## 8. For Loops

A `for` loop processes items in a collection.

```python
servers = ["web-server", "database-server", "app-server"]

for server in servers:
    print("Checking:", server)
```

## 9. While Loops

A `while` loop repeats while its condition is true.

```python
attempt = 1

while attempt <= 5:
    print("Health check:", attempt)
    attempt += 1
```

## 10. The range() Function

`range()` generates a sequence of numbers.

```python
for number in range(1, 6):
    print("Health check:", number)
```

This prints numbers from 1 through 5.

## 11. Functions

Functions organize reusable code.

```python
def check_server(server_name):
    print("Checking server:", server_name)
    print("Status: Healthy")

check_server("web-server")
check_server("database-server")
```

## 12. Return Values

A function can return a result.

```python
def check_cpu(cpu_usage):
    if cpu_usage > 80:
        return "HIGH"
    return "NORMAL"

print(check_cpu(85))
print(check_cpu(45))
```

## 13. Lists

Lists store multiple items and can be modified.

```python
servers = ["web-server", "database-server", "app-server"]

servers.append("backup-server")
servers.remove("app-server")

print(servers)
```

## 14. Dictionaries

Dictionaries store key-value pairs.

```python
server = {
    "name": "web-server",
    "status": "Running",
    "cpu_usage": 75
}

print(server["name"])

server["cpu_usage"] = 85
print(server["cpu_usage"])
```

## 15. File Handling

Python can write and read files.

```python
with open("server_report.txt", "w") as file:
    file.write("Server Status: Running")

with open("server_report.txt", "r") as file:
    print(file.read())
```

`w` writes or overwrites a file. `r` reads a file.

## 16. Exception Handling

`try` and `except` handle errors gracefully.

```python
try:
    cpu_usage = int(input("Enter CPU usage: "))
    print("CPU usage:", cpu_usage)
except ValueError:
    print("Please enter a valid number.")
```

## 17. Python Modules

Modules provide reusable functionality.

```python
import os
import platform

print(platform.system())
print(platform.python_version())
print(os.getcwd())
print(os.listdir("."))
```

- `os` — interacts with the operating system.
- `platform` — provides system and Python version information.

## 18. Server Health Checker

The following utility combines functions, conditions, variables, and logical operators.

```python
def check_server(server_name, cpu_usage, memory_usage):
    print("\nChecking server:", server_name)

    cpu_status = "HIGH" if cpu_usage > 80 else "NORMAL"
    memory_status = "HIGH" if memory_usage > 80 else "NORMAL"

    print("CPU Usage:", str(cpu_usage) + "%")
    print("CPU Status:", cpu_status)
    print("Memory Usage:", str(memory_usage) + "%")
    print("Memory Status:", memory_status)

    if cpu_status == "HIGH" or memory_status == "HIGH":
        print("Overall Status: WARNING")
    else:
        print("Overall Status: HEALTHY")


check_server("web-server", 85, 60)
check_server("database-server", 45, 90)
check_server("app-server", 40, 50)
```

## 19. Files Created

- `app/python/hello.py`
- `app/python/variables.py`
- `app/python/data_types.py`
- `app/python/conditions.py`
- `app/python/comparison.py`
- `app/python/logical_operators.py`
- `app/python/loops.py`
- `app/python/while_loop.py`
- `app/python/range_loop.py`
- `app/python/functions.py`
- `app/python/return_values.py`
- `app/python/lists.py`
- `app/python/dictionaries.py`
- `app/python/file_handling.py`
- `app/python/exception_handling.py`
- `app/python/os_automation.py`
- `app/python/health_checker.py`

## 20. Day 4 Summary

**Completed:** Python fundamentals and a basic server health checker.

**Key takeaway:** Python can automate repetitive DevOps tasks, inspect system information, process data, and identify potential server issues.

**Next:** Day 5 — continue the foundations phase with Python scripting and practical automation.
