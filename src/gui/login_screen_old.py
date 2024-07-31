import customtkinter as ctk
from tkinter import PhotoImage

class LoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login Screen")
        self.geometry("400x300")

        # Load images using PhotoImage
        notion_logo = PhotoImage(file="path/to/notion_logo.png")
        confluence_logo = PhotoImage(file="path/to/confluence_logo.png")

        # Create buttons with logos
        self.notion_button = ctk.CTkButton(self, image=notion_logo, text="Login with Notion", command=self.notion_login)
        self.notion_button.pack(pady=20)

        self.confluence_button = ctk.CTkButton(self, image=confluence_logo, text="Login with Confluence", command=self.confluence_login)
        self.confluence_button.pack(pady=20)

    def notion_login(self):
        print("Notion login clicked")

    def confluence_login(self):
        print("Confluence login clicked")

if __name__ == "__main__":
    app = LoginScreen()
    app.mainloop()
