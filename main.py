from flask import Flask, request, jsonify, render_template
import subprocess
import os

def run_selenium_script(device_ip,action):
     # Define the base directories for Mardan and Haripur
    mardan_directory = r"G:\coding\python\TVN\Webpage selenium script\Production Files\Mardan"
    haripur_directory = r"G:\coding\python\TVN\Webpage selenium script\Production Files\Haripur"

        # Determine the parent directory based on the device IP
    if device_ip.startswith("10.235"):  # Mardan devices
        base_directory = mardan_directory
    elif device_ip.startswith("10.233"):  # Haripur devices
        base_directory = haripur_directory
    else:
        raise ValueError(f"Invalid device IP: {device_ip}")
    print(base_directory)
    
    # Determine the script directory based on the action
    if action == "switch":
        script_directory = base_directory
    elif action == "revert":
        script_directory = os.path.join(base_directory, "RevertToHyt")
    else:
        raise ValueError(f"Invalid action: {action}")

    # Construct the script path
    script_name = f"{device_ip}.py"
    script_path = os.path.join(script_directory, script_name)
    print(script_path)

    if os.path.exists(script_path):
        # Use subprocess to execute the script
        subprocess.run(["python", script_path], check=True)
    else:
        raise FileNotFoundError(f"No script found for device: {device_ip}")
    
app = Flask(__name__)
@app.route("/")
def index():
    # Renders the `index.html` file
    return render_template("index.html")


@app.route('/run_script', methods=["POST"])
def run_script():
    device_name = request.form.get("device_ip")
    action = request.form.get("action")
    try:
        run_selenium_script(device_name,action)
        return ("script executed successfully")
    except FileNotFoundError as e:
        return (str(e), 404)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    