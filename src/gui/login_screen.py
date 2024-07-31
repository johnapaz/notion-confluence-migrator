import customtkinter as ctk
from PIL import Image, ImageTk
import os

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Login Screen")

        self.setup_ui()

    def setup_ui(self):
        # Load Notion and Confluence logos
        notion_logo_path = os.path.join('assets', 'notion.png')
        confluence_logo_path = os.path.join('assets', 'confluence.png')

        notion_logo = Image.open(notion_logo_path)
        confluence_logo = Image.open(confluence_logo_path)

        # Convert logos to PhotoImage
        notion_logo_tk = ImageTk.PhotoImage(notion_logo)
        confluence_logo_tk = ImageTk.PhotoImage(confluence_logo)

        # Create Notion login button
        self.notion_button = ctk.CTkButton(
            self.root,
            image=notion_logo_tk,
            text="Notion",
            corner_radius=10,
            width=200,
            height=200,
            command=self.notion_login
        )
        self.notion_button.image = notion_logo_tk  # Keep a reference to avoid garbage collection
        self.notion_button.place(relx=0.25, rely=0.5, anchor='center')

        # Create Confluence login button
        self.confluence_button = ctk.CTkButton(
            self.root,
            image=confluence_logo_tk,
            text="Confluence",
            corner_radius=10,
            width=200,
            height=200,
            command=self.confluence_login
        )
        self.confluence_button.image = confluence_logo_tk  # Keep a reference to avoid garbage collection
        self.confluence_button.place(relx=0.75, rely=0.5, anchor='center')

    def notion_login(self):
        # Implement Notion login logic
        pass

    def confluence_login(self):
        # Implement Confluence login logic
        pass

if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginScreen(root)
    root.mainloop()
