import tkinter as tk
from tkinter import ttk, messagebox
import requests
from .custom_dialog import CustomDialog

class SiteSelectionScreen:
    def __init__(self, root, source, url, username, token, selected_content, access_token):
        self.root = root
        self.source = source
        self.url = url
        self.username = username
        self.token = token
        self.selected_content = selected_content
        self.access_token = access_token

        self.create_site_selection_screen()

    def create_site_selection_screen(self):
        self.root.geometry("600x400")
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Select a Confluence Site").grid(row=0, column=0, sticky=tk.W)

        self.site_var = tk.StringVar()
        sites = self.fetch_sites()
        site_options = [site['name'] for site in sites]
        
        if site_options:
            self.site_menu = ttk.OptionMenu(frame, self.site_var, site_options[0], *site_options)
            self.site_menu.grid(row=1, column=0, sticky=tk.W)
            ttk.Button(frame, text="Next", command=self.confirm_selection).grid(row=2, column=0, sticky=tk.W)
        else:
            ttk.Label(frame, text="No sites available").grid(row=1, column=0, sticky=tk.W)
        
        ttk.Button(frame, text="Back", command=self.go_back).grid(row=3, column=0, sticky=tk.W)

    def fetch_sites(self):
        url = "https://api.atlassian.com/oauth/token/accessible-resources"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            CustomDialog(self.root, "HTTP Error", f"HTTP error occurred: {http_err}")
        except Exception as err:
            CustomDialog(self.root, "Error", f"An error occurred: {err}")
        return []

    def confirm_selection(self):
        selected_site_name = self.site_var.get()
        selected_site = next(site for site in self.fetch_sites() if site['name'] == selected_site_name)
        selected_site_id = selected_site['id']
        self.show_space_selection_screen(selected_site_id)

    def show_space_selection_screen(self, selected_site_id):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .space_selection_screen import SpaceSelectionScreen
        SpaceSelectionScreen(self.root, self.source, selected_site_id, self.username, self.token, self.selected_content, self.access_token)

    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .destination_login_screen import DestinationLoginScreen
        DestinationLoginScreen(self.root, self.source, self.url, self.username, self.token, self.selected_content)
