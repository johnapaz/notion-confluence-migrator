import tkinter as tk
from tkinter import ttk
from ..auth import authenticate_notion, authenticate_confluence

class LoginScreen:
    def __init__(self, root, source, url):
        self.root = root
        self.source = source
        self.url = url
        self.root.geometry("600x400")
        self.create_login_screen()

    def create_login_screen(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Login").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(frame, text="Username:").grid(row=1, column=0, sticky=tk.W)
        self.username_entry = ttk.Entry(frame, width=50)
        self.username_entry.grid(row=2, column=0, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="API Token:").grid(row=3, column=0, sticky=tk.W)
        self.token_entry = ttk.Entry(frame, width=50, show="*")
        self.token_entry.grid(row=4, column=0, sticky=(tk.W, tk.E))

        ttk.Button(frame, text="Login", command=self.authenticate).grid(row=5, column=0, sticky=tk.W)
        ttk.Button(frame, text="Back", command=self.go_back).grid(row=6, column=0, sticky=tk.W)

    def authenticate(self):
        try:
            username = self.username_entry.get()
            token = self.token_entry.get()
        except tk.TclError as e:
            tk.messagebox.showerror("Error", f"Error retrieving input values: {e}")
            return

        if not username or not token:
            tk.messagebox.showerror("Error", "Username and API Token cannot be empty")
            return

        try:
            if self.source == "Notion":
                if authenticate_notion(token):
                    self.show_content_selection(username, token)
                else:
                    tk.messagebox.showerror("Error", "Failed to authenticate with Notion")
            elif self.source == "Confluence":
                if authenticate_confluence(username, token):
                    self.show_content_selection(username, token)
                else:
                    tk.messagebox.showerror("Error", "Failed to authenticate with Confluence")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Authentication error: {e}")

    def show_content_selection(self, username, token):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .content_selection_screen import ContentSelectionScreen
        ContentSelectionScreen(self.root, self.source, self.url, username, token)

    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .url_screen import URLScreen
        URLScreen(self.root, self.source)
