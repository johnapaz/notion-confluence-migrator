import tkinter as tk
from tkinter import ttk, messagebox
from src.migration import migrate_content
from src.api import NotionAPI, ConfluenceAPI

class ProgressScreen:
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
        self.create_progress_screen()

    def create_progress_screen(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Migration in Progress...").grid(row=0, column=0, sticky=tk.W)
        self.progress_bar = ttk.Progressbar(frame, mode='indeterminate')
        self.progress_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.progress_bar.start()

        self.root.after(100, self.run_migration)

    def run_migration(self):
        notion_api = NotionAPI(token=self.token)
        confluence_api = ConfluenceAPI(username=self.dest_username, token=self.dest_token)
        success = True
        for content in self.selected_content:
            response = migrate_content(notion_api, confluence_api, content, self.selected_space)
            if not response:
                success = False
                break

        self.progress_bar.stop()
        if success:
            messagebox.showinfo("Success", "Migration completed successfully")
        else:
            messagebox.showerror("Error", "Migration failed")

        self.root.quit()
