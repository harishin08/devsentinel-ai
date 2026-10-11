import os
import platform

print("DevSentinel AI - System Information")
print("-----------------------------------")

print("Operating System:", platform.system())
print("OS Version:", platform.release())
print("Python Version:", platform.python_version())
print("Current Directory:", os.getcwd())

print("\nProject Files and Folders:")

for item in os.listdir("."):
    print("-", item)
