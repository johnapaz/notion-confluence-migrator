import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = [
    "Flask==2.0.1",
    "requests==2.25.1",
    "python-dotenv==0.19.0",
    "Werkzeug==2.0.3",
    "tk",
    "customtkinter==5.2.2",
]

for package in required_packages:
    try:
        __import__(package.split("==")[0])
    except ImportError:
        print(f"Installing missing package: {package}")
        install(package)
