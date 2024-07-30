import tkinter as tk
from tkinter import ttk

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)

        self.label = tk.Label(self, text=message, wraplength=380)
        self.label.pack(pady=10)

        self.text = tk.Text(self, height=4, wrap="word")
        self.text.insert("1.0", message)
        self.text.pack(pady=10)
        self.text.config(state=tk.DISABLED)  # Make the text read-only

        self.copy_button = ttk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)

        self.ok_button = ttk.Button(self, text="OK", command=self.destroy)
        self.ok_button.pack(pady=10)

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.text.get("1.0", tk.END))
        self.update()  # Now it stays on the clipboard after the window is closed
