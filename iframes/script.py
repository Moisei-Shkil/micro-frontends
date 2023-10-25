import subprocess

# Define the port numbers for each app
app_port = 3000
mf1_port = 3001
mf2_port = 3002

# Start the server for the 'app' directory on port 3000
app_server = subprocess.Popen(
    ["python3", "-m", "http.server", str(app_port)], cwd="app"
)

# Start the server for the 'mf1' directory on port 3001
mf1_server = subprocess.Popen(
    ["python3", "-m", "http.server", str(mf1_port)], cwd="mf1"
)

# Start the server for the 'mf2' directory on port 3002
mf2_server = subprocess.Popen(
    ["python3", "-m", "http.server", str(mf2_port)], cwd="mf2"
)

try:
    app_server.wait()
except KeyboardInterrupt:
    app_server.terminate()

try:
    mf1_server.wait()
except KeyboardInterrupt:
    mf1_server.terminate()

try:
    mf2_server.wait()
except KeyboardInterrupt:
    mf2_server.terminate()
