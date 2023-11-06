import subprocess
from cors_script import cors_server_script

# Define the port numbers for each app
app_port = 3010
mf1_port = 3011
mf2_port = 3012


# Start the server for the 'app' directory on port 3000
app_server = subprocess.Popen(
    ["python3", "-m", "http.server", str(app_port)], cwd="app"
)

# Start the server for the 'mf1' directory on port 3001
mf1_server = subprocess.Popen(
    ["python3", "-c", cors_server_script.format(port=mf1_port)], cwd="mf1"
)

# Start the server for the 'mf2' directory on port 3002
mf2_server = subprocess.Popen(
    ["python3", "-c", cors_server_script.format(port=mf2_port)], cwd="mf2"
)

try:
    app_server.wait()
    mf1_server.wait()
    mf2_server.wait()
except KeyboardInterrupt:
    app_server.terminate()
    mf1_server.terminate()
    mf2_server.terminate()
