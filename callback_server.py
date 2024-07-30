from flask import Flask, request, jsonify, redirect
import threading
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
AUTH_URL = os.getenv('AUTH_URL')
TOKEN_URL = os.getenv('TOKEN_URL')
SCOPES = os.getenv('SCOPES')

access_token = None  # Global variable to store the access token

@app.route('/callback')
def callback():
    global access_token
    code = request.args.get('code')
    if code:
        data = {
            'grant_type': 'authorization_code',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'code': code,
            'redirect_uri': REDIRECT_URI
        }
        response = requests.post(TOKEN_URL, data=data)
        if response.status_code == 200:
            access_token = response.json()['access_token']
            return redirect("/success")
        else:
            return jsonify({"error": "Failed to authenticate with Atlassian"}), 400
    else:
        return jsonify({"error": "Missing authorization code"}), 400

@app.route('/success')
def success():
    return "Authentication successful. You can now close this window and return to the application."

@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

def run_server():
    app.run(host='0.0.0.0', port=8000)

def start_server():
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True  # Allow server to be killed when main thread exits
    server_thread.start()

def stop_server():
    # Send a request to the shutdown endpoint
    try:
        requests.post('http://localhost:8000/shutdown')
    except requests.exceptions.RequestException as e:
        print(f"Error shutting down server: {e}")

def get_access_token():
    global access_token
    return access_token

if __name__ == '__main__':
    start_server()
