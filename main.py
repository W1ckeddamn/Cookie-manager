import tkinter as tk
from src.ui.main_window import MainWindow
import os

def main():
    root = tk.Tk()
    # Set default font for better appearance
    root.option_add("*Font", "Helvetica 10")
    
    # Set window icon
    icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.png")
    if os.path.exists(icon_path):
        icon = tk.PhotoImage(file=icon_path)
        root.iconphoto(True, icon)
    
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()