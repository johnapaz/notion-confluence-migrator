import tkinter as tk
from tkinter import ttk, messagebox
from .progress_screen import ProgressScreen

class ConfirmationScreen:
    def __init__(self, root, source, url, username, token, selected_content, dest_username, dest_token, selected_space):
        self.root = root
        self.source = source
        self.url = url
        self.username = username
        self.token = token
        self.selected_content = selected_content
        self.dest_username = dest_username
        self.dest_token = dest_token
        self.selected_space = selected_space
        self.root.geometry("600x400")
        self.create_confirmation_screen()

    def create_confirmation_screen(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Confirm Migration").grid(row=0, column=0, sticky=tk.W)
        content_text = f"Content: {', '.join(self.selected_content)}"
        ttk.Label(frame, text=content_text).grid(row=1, column=0, sticky=tk.W)
        space_text = f"Space: {self.selected_space}"
        ttk.Label(frame, text=space_text).grid(row=2, column=0, sticky=tk.W)

        ttk.Button(frame, text="Execute", command=self.execute_migration).grid(row=3, column=0, sticky=tk.W)
        ttk.Button(frame, text="Back", command=self.go_back).grid(row=4, column=0, sticky=tk.W)

    def execute_migration(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        ProgressScreen(self.root, self.source, self.url, self.username, self.token, self.selected_content, self.dest_username, self.dest_token, self.selected_space)

    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .space_selection_screen import SpaceSelectionScreen
        SpaceSelectionScreen(self.root, self.source, self.url, self.username, self.token, self.selected_content, self.dest_username, self.dest_token)
