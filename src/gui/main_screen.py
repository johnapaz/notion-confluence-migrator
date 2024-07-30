import tkinter as tk
from tkinter import ttk
from src.gui.url_screen import URLScreen

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Notion to Confluence Migration")
        self.root.geometry("600x400")
        self.create_main_screen()

    def create_main_screen(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.source_var = tk.StringVar()
        ttk.Label(frame, text="Select Source:").grid(row=0, column=0, sticky=tk.W)
        ttk.Radiobutton(frame, text="Notion", variable=self.source_var, value="Notion").grid(row=1, column=0, sticky=tk.W)
        ttk.Radiobutton(frame, text="Confluence", variable=self.source_var, value="Confluence").grid(row=2, column=0, sticky=tk.W)

        ttk.Button(frame, text="Next", command=self.show_url_screen).grid(row=3, column=0, sticky=tk.W)

    def show_url_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        URLScreen(self.root, self.source_var.get())
