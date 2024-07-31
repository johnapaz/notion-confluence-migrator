import customtkinter as ctk
from tkinter import Listbox, END

class SiteSelectionScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label = ctk.CTkLabel(self, text="Select a Confluence Site")
        self.label.pack(pady=10)

        # Use a standard Listbox
        self.site_listbox = Listbox(self)
        self.site_listbox.pack(pady=10, padx=20, fill="both", expand=True)

        self.confirm_button = ctk.CTkButton(self, text="Confirm", command=self.confirm_selection)
        self.confirm_button.pack(pady=10)

        self.pack(fill="both", expand=True)

        # Example sites, replace with actual data
        sites = ["Site 1", "Site 2", "Site 3"]
        for site in sites:
            self.site_listbox.insert(END, site)

    def confirm_selection(self):
        selected_site = self.site_listbox.get(self.site_listbox.curselection())
        print(f"Selected site: {selected_site}")
        self.show_space_selection_screen(selected_site)

    def show_space_selection_screen(self, selected_site):
        from src.gui.space_selection_screen import SpaceSelectionScreen
        self.space_selection_screen = SpaceSelectionScreen(self.master, selected_site)
        self.space_selection_screen.pack(fill="both", expand=True)
        self.pack_forget()
