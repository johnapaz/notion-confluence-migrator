import subprocess
import sys
import pkg_resources

required_packages = [
    'Flask==2.0.1',
    'requests==2.25.1',
    'python-dotenv==0.19.0',
    'Werkzeug==2.0.3',
    'tk'
]

def install_packages():
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    missing_packages = [pkg for pkg in required_packages if pkg.split('==')[0] not in installed_packages]

    if missing_packages:
        try:
            print("Installing missing packages...")
            result = subprocess.run([sys.executable, '-m', 'pip', 'install', *missing_packages],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                print("All packages installed successfully.")
            else:
                print("Failed to install some packages.")
                print(result.stderr.decode())
                sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Failed to install packages: {e}")
            sys.exit(1)
    else:
        print("All required packages are already installed.")

if __name__ == "__main__":
    install_packages()
