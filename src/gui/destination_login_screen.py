import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from urllib.parse import urlencode
import requests
import os
from dotenv import load_dotenv
from callback_server import start_server, stop_server, get_access_token

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
AUTH_URL = os.getenv('AUTH_URL')
TOKEN_URL = os.getenv('TOKEN_URL')
SCOPES = os.getenv('SCOPES')

class DestinationLoginScreen:
    def __init__(self, root, source, url, username, token, selected_content):
        self.root = root
        self.source = source
        self.url = url
        self.username = username
        self.token = token
        self.selected_content = selected_content

        start_server()  # Start the server when the screen is initialized
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event

        self.create_destination_login_screen()

    def create_destination_login_screen(self):
        self.root.geometry("600x400")
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Login to Destination").grid(row=0, column=0, sticky=tk.W)
        self.login_button = ttk.Button(frame, text="Login with Atlassian", command=self.redirect_to_atlassian_login)
        self.login_button.grid(row=1, column=0, sticky=tk.W)
        ttk.Button(frame, text="Back", command=self.go_back).grid(row=2, column=0, sticky=tk.W)

        # Check if already authenticated
        self.check_authentication()

    def redirect_to_atlassian_login(self):
        params = {
            'audience': 'api.atlassian.com',
            'client_id': CLIENT_ID,
            'scope': SCOPES,
            'redirect_uri': REDIRECT_URI,
            'response_type': 'code',
            'prompt': 'consent'
        }
        url = f"{AUTH_URL}?{urlencode(params)}"
        webbrowser.open(url)

    def check_authentication(self):
        self.root.after(1000, self.update_access_token)

    def update_access_token(self):
        access_token = get_access_token()
        if access_token:
            self.login_button.destroy()
            self.show_site_selection_screen(access_token)
        else:
            self.check_authentication()

    def show_site_selection_screen(self, access_token):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .site_selection_screen import SiteSelectionScreen
        SiteSelectionScreen(self.root, self.source, self.url, self.username, self.token, self.selected_content, access_token)

    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .content_selection_screen import ContentSelectionScreen
        ContentSelectionScreen(self.root, self.source, self.url, self.username, self.token)

    def on_closing(self):
        stop_server()  # Stop the server when the window is closed
        self.root.destroy()
