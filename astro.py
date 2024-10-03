import requests
import time

# Configuration
device_url = "http://10.200.11.19"  # Device IP
login_endpoint = "/login.html"  # Login endpoint
username = "admin"  # Username
password = "astro"  # Password

# Construct the login URL with parameters
login_url = f"{device_url}{login_endpoint}?user={username}&pass={password}&submit=Submit"

# Start a session
session = requests.Session()

# Step 1: Access the device URL to initiate the session
initial_response = session.get(device_url)

# Add a delay to allow for the login page to load
time.sleep(2)  # Sleep for 300 seconds (5 minutes)

# Step 2: Log in to the device
login_response = session.get(login_url)

# Check if login was successful
if "You have successfully logged in" in login_response.text:  # Change this based on the response indicating a successful login
    print("Login successful!")
else:
    print("Login failed. Check your credentials.")
