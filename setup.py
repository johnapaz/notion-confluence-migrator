import subprocess
import sys

def install_packages():
    try:
        import pip
    except ImportError:
        print("Pip is not installed. Please install pip first.")
        sys.exit(1)

    required_packages = [
        'Flask==2.0.1',
        'requests==2.25.1',
        'python-dotenv==0.19.0',
        'Werkzeug==2.0.3'
    ]

    for package in required_packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_packages()
