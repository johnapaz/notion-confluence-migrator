import tkinter as tk
from tkinter import ttk, messagebox

class ContentSelectionScreen:
    def __init__(self, root, source, url, username, token):
        self.root = root
        self.source = source
        self.url = url
        self.username = username
        self.token = token
        self.root.geometry("600x400")
        self.create_content_selection_screen()

    def create_content_selection_screen(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Select Content to Export").grid(row=0, column=0, sticky=tk.W)
        # Fetch and display content (mockup here)
        self.content_var = tk.StringVar(value=["Page 1", "Page 2", "Page 3"])
        self.content_listbox = tk.Listbox(frame, listvariable=self.content_var, selectmode=tk.MULTIPLE)
        self.content_listbox.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Button(frame, text="Next", command=self.show_destination_login_screen).grid(row=2, column=0, sticky=tk.W)
        ttk.Button(frame, text="Back", command=self.go_back).grid(row=3, column=0, sticky=tk.W)

    def show_destination_login_screen(self):
        selected_content = [self.content_listbox.get(i) for i in self.content_listbox.curselection()]
        if not selected_content:
            messagebox.showerror("Error", "No content selected")
            return
        for widget in self.root.winfo_children():
            widget.destroy()
        from .destination_login_screen import DestinationLoginScreen
        DestinationLoginScreen(self.root, self.source, self.url, self.username, self.token, selected_content)

    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .login_screen_old import LoginScreen
        LoginScreen(self.root, self.source, self.url)
