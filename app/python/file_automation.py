import os

project_directory = "."

print("DevSentinel AI - File Automation")
print("--------------------------------")

if os.path.exists(project_directory):
    print("Project directory exists.")

print("\nProject contents:")

for item in os.listdir(project_directory):
    if os.path.isdir(item):
        print("[DIR] ", item)
    else:
        print("[FILE]", item)

print("\nChecking important directories:")

for folder in ["app", "docs", "scripts", "config"]:
    if os.path.isdir(folder):
        print(folder, "- Found")
    else:
        print(folder, "- Missing")
