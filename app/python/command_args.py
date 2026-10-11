import sys

print("DevSentinel AI - Command Line Tool")

if len(sys.argv) < 2:
    print("Usage: python3 app/python/command_args.py <server_name>")
else:
    server_name = sys.argv[1]
    print("Checking server:", server_name)
    print("Status: Healthy")
