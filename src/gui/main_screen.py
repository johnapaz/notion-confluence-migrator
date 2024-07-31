import customtkinter as ctk
from tkinter import messagebox
from src.gui.site_selection_screen import SiteSelectionScreen

class MainScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Notion-Confluence Integration")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Choose a service to log in")
        self.label.pack(pady=20)

        self.notion_button = ctk.CTkButton(self, text="Login with Notion", command=self.notion_login, width=200, height=40, corner_radius=10)
        self.notion_button.pack(pady=20)

        self.confluence_button = ctk.CTkButton(self, text="Login with Confluence", command=self.confluence_login, width=200, height=40, corner_radius=10)
        self.confluence_button.pack(pady=20)

    def notion_login(self):
        messagebox.showinfo("Notion Login", "Redirecting to Notion login...")
        # Replace this with actual login logic for Notion
        self.show_site_selection_screen()

    def confluence_login(self):
        messagebox.showinfo("Confluence Login", "Redirecting to Confluence login...")
        # Replace this with actual login logic for Confluence
        self.show_site_selection_screen()

    def show_site_selection_screen(self):
        self.site_selection_screen = SiteSelectionScreen(self)
        self.site_selection_screen.pack(fill="both", expand=True)
        self.pack_forget()

if __name__ == "__main__":
    app = MainScreen()
    app.mainloop()
