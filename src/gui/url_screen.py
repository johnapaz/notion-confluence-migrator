import tkinter as tk
from tkinter import ttk

class URLScreen:
    def __init__(self, root, source):
        self.root = root
        self.source = source
        self.root.geometry("600x400")
        self.create_url_screen()

    def create_url_screen(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Enter URL:").grid(row=0, column=0, sticky=tk.W)
        self.url_entry = ttk.Entry(frame, width=50)
        self.url_entry.grid(row=1, column=0, sticky=(tk.W, tk.E))

        ttk.Button(frame, text="Next", command=self.show_login_screen).grid(row=2, column=0, sticky=tk.W)
        ttk.Button(frame, text="Back", command=self.go_back).grid(row=3, column=0, sticky=tk.W)

    def show_login_screen(self):
        url = self.url_entry.get()
        if not url:
            tk.messagebox.showerror("Error", "URL cannot be empty")
            return
        for widget in self.root.winfo_children():
            widget.destroy()
        from .login_screen_old import LoginScreen
        LoginScreen(self.root, self.source, url)

    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        from .main_screen import MainScreen
        MainScreen(self.root)
