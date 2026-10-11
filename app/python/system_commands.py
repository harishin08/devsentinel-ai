import subprocess

print("DevSentinel AI - System Command Runner")
print("--------------------------------------")

commands = [
    ["whoami"],
    ["hostname"],
    ["uptime"],
    ["df", "-h"]
]

for command in commands:
    print("\nCommand:", " ".join(command))

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
            check=True
        )

        print(result.stdout.strip())

    except subprocess.CalledProcessError:
        print("Command failed.")

    except subprocess.TimeoutExpired:
        print("Command timed out.")
