import tkinter as tk
from tkinter import ttk
import requests
from .custom_dialog import CustomDialog

class SpaceSelectionScreen:
    def __init__(self, root, source, site_id, username, token, selected_content, access_token):
        self.root = root
        self.source = source
        self.site_id = site_id
        self.username = username
        self.token = token
        self.selected_content = selected_content
        self.access_token = access_token

        self.create_space_selection_screen()

    def create_space_selection_screen(self):
        self.root.geometry("600x600")
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Choose where this content goes").grid(row=0, column=0, columnspan=2, sticky=tk.W)

        # Section for adding content to an existing space
        ttk.Label(frame, text="Add to space").grid(row=1, column=0, columnspan=2, sticky=tk.W)
        ttk.Label(frame, text="Add content to an existing space in Confluence.").grid(row=2, column=0, columnspan=2, sticky=tk.W)

        self.space_var = tk.StringVar()
        spaces = self.fetch_spaces()
        self.space_options = [space['name'] for space in spaces]

        if self.space_options:
            self.space_menu = ttk.OptionMenu(frame, self.space_var, self.space_options[0], *self.space_options)
            self.space_menu.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        else:
            ttk.Label(frame, text="No spaces available").grid(row=3, column=0, columnspan=2, sticky=tk.W)

        # Section for creating a new space
        ttk.Label(frame, text="Create a space").grid(row=4, column=0, columnspan=2, sticky=tk.W)
        ttk.Label(frame, text="Create a new space in Confluence for this content.").grid(row=5, column=0, columnspan=2, sticky=tk.W)
        
        ttk.Label(frame, text="Space Name:").grid(row=6, column=0, sticky=tk.W)
        self.new_space_name = tk.Entry(frame)
        self.new_space_name.grid(row=6, column=1, sticky=tk.W)

        ttk.Label(frame, text="Space Key:").grid(row=7, column=0, sticky=tk.W)
        self.new_space_key = tk.Entry(frame)
        self.new_space_key.grid(row=7, column=1, sticky=tk.W)

        ttk.Button(frame, text="Create Space", command=self.create_space).grid(row=8, column=0, columnspan=2, sticky=tk.W)
        ttk.Button(frame, text="Confirm", command=self.confirm_selection).grid(row=9, column=0, columnspan=2, sticky=tk.W)
        ttk.Button(frame, text="Back", command=self.go_back).grid(row=10, column=0, columnspan=2, sticky=tk.W)

    def fetch_spaces(self):
        url = f"https://api.atlassian.com/ex/confluence/{self.site_id}/wiki/rest/api/space"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json().get('results', [])
        except requests.exceptions.HTTPError as http_err:
            CustomDialog(self.root, "HTTP Error", f"HTTP error occurred: {http_err}")
        except Exception as err:
            CustomDialog(self.root, "Error", f"An error occurred: {err}")
        return []

    def create_space(self):
        space_name = self.new_space_name.get()
        space_key = self.new_space_key.get().upper()
        if not space_name or not space_key:
            CustomDialog(self.root, "Error", "Space name and key cannot be empty")
            return

        url = f"https://api.atlassian.com/ex/confluence/{self.site_id}/wiki/rest/api/space"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "key": space_key,
            "name": space_name
        }
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            new_space = response.json()
            self.space_options.append(new_space['name'])
            self.space_menu['menu'].add_command(label=new_space['name'], command=tk._setit(self.space_var, new_space['name']))
            self.space_var.set(new_space['name'])
            CustomDialog(self.root, "Success", f"Space '{new_space['name']}' created successfully")
        except requests.exceptions.HTTPError as http_err:
            CustomDialog(self.root, "HTTP Error", f"HTTP error occurred: {http_err}")
        except Exception as err:
            CustomDialog(self.root, "Error", f"An error occurred: {err}")

    def confirm_selection(self):
        selected_space = self.space_var.get()
        # TODO: Implement confirmation logic to import content into the selected space
        tk.messagebox.showinfo("Success", f"Content imported successfully into {selected_space}!")
        self.root.destroy()

    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .site_selection_screen import SiteSelectionScreen
        SiteSelectionScreen(self.root, self.source, self.site_id, self.username, self.token, self.selected_content, self.access_token)
