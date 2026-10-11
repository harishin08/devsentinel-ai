import os

environment = os.getenv("APP_ENV", "Development")
server_name = os.getenv("SERVER_NAME", "web-server")

print("DevSentinel AI - Environment Configuration")
print("Environment:", environment)
print("Server Name:", server_name)
