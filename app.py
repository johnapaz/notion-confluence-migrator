import subprocess
import sys
import tkinter as tk
from src.gui.main_screen import MainScreen
from callback_server import start_server, stop_server

def install_requirements():
    subprocess.check_call([sys.executable, "dependency_checker.py"])

def on_closing():
    stop_server()  # Stop the server when the application is closed
    root.destroy()

def main():
    global root
    install_requirements()  # Install required packages

    start_server()  # Start the server when the application starts

    root = tk.Tk()
    app = MainScreen(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)  # Handle window close event
    root.mainloop()

if __name__ == "__main__":
    main()
