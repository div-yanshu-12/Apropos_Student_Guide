import os
import subprocess
import time

files_to_run = [
    "chatbot.py",
    "events.py",
    "webpage.py",
    "webpages/admin/admin.py",
    "webpages/admin/admin2.py",
    "webpages/login/login.py"
]

processes = []

for file in files_to_run:
    print(f"Starting {file} in the background...")
    try:
        process = subprocess.Popen(["python", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append(process)
        print(f"Started {file} successfully.")
    except Exception as e:
        print(f"Failed to start {file}: {e}")

print("All scripts have been started in the background. Monitoring outputs...")

# Monitor processes for their initial outputs
time.sleep(10)  # Wait for 10 seconds to let scripts initialize

for process in processes:
    out, err = process.communicate(timeout=1)
    print(f"Output: {out.decode('utf-8')}\nError: {err.decode('utf-8')}")

print("Background script monitoring completed.")
