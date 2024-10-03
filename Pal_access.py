import sys
print("Python Executable:", sys.executable)

import requests
import time

# URL and credentials
url = "http://10.200.11.19/login.html"
username = "admin"
password = "astro"

# Start time
time.sleep(5)  #add delay
start_time = time.time()

# Open the log file
with open("responses.log", "w") as log_file:
    while time.time() - start_time < 10:  # Run for 60 seconds
        # Send GET request with basic auth
        response = requests.get(url, auth=(username, password))
        
        # Write response to log file
        log_file.write(f"--- Response captured at {time.ctime()} ---\n")
        log_file.write(response.text)
        log_file.write("\n\n")

        # Wait for 1 second before the next request
        time.sleep(2)

print("Logging complete. Responses saved to 'responses.log'.")
