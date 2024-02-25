import tkinter as tk
from tkinter import font
from tkinter import ttk

class FontViewerApp:

    def __init__(self, root):
        """
        Initializes application window.
        """
        self.root = root
        self.root.geometry("500x200")
        self.root.title("Tkinter Font Viewer")
        
        self.font_families = sorted(font.families())
        self.current_font_index = 0 
        self.sample_text = "The quick brown fox jumps over the lazy dog"

        self.fontdropdown = ttk.Combobox(root, values = self.font_families)
        self.fontdropdown.bind('<<ComboboxSelected>>', self.on_dragdown_select)
        self.fontdropdown.pack()

        self.label = tk.Label(root, text=self.sample_text, wraplength=400)
        self.label.pack(padx=10, pady=10)

        self.prev_button = ttk.Button(root, text="Previous", command=self.show_previous_font)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = ttk.Button(root, text="Next", command=self.show_next_font)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.update_font()  
    
    def on_dragdown_select(self, event):
        """
        Updates font to the selected font in the dragdown box.
        """
        selected_value = self.fontdropdown.get()
        self.current_font_index = self.font_families.index(selected_value)
        self.update_font()


    def update_font(self):
        """
        Updates font text to the current font index.
        """
        font_name = self.font_families[self.current_font_index]
        font_obj = font.Font(family=font_name, size=20)
        self.label.config(font=font_obj)
        self.label.config(text=f"{font_name}\n{self.sample_text}")

    def show_next_font(self):
        """
        Sets current font index to the next font and updates the font.
        """
        self.current_font_index = (self.current_font_index + 1) % len(self.font_families)
        self.update_font()

    def show_previous_font(self):
        """
        Sets current font index to the previous and updates the font.
        """
        self.current_font_index = (self.current_font_index - 1) % len(self.font_families)
        self.update_font()

root = tk.Tk()
app = FontViewerApp(root)
root.mainloop()
