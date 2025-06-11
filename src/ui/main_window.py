from tkinter import ttk
import tkinter as tk
from src.managers.cookie_manager import CookieManager
from src.ui.dialogs import DialogHandler

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Manager")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        # Configure button style
        self.style = ttk.Style()
        # Create custom style using clam theme for better color support
        self.style.theme_use('clam')
        self.style.configure(
            "Custom.TButton",
            padding=(4, 2),  # (left/right, top/bottom)
            relief="flat",
            background="#2196F3",
            foreground="white",
            font=("Helvetica", 9, "bold")
        )
        # Configure button colors properly
        self.style.map(
            "Custom.TButton",
            background=[("pressed", "#1976D2"), ("active", "#2196F3")],
            foreground=[("pressed", "white"), ("active", "white")]
        )

        self.cookie_manager = CookieManager()
        self.dialog_handler = DialogHandler()
        self.current_profile = None  # Track current profile


        self.setup_ui()
        self.load_profiles()

    def setup_ui(self):
        # Configure grid weights to center the content
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

        # Create frame for tree with padding
        tree_frame = ttk.Frame(self.root, padding="20 10 20 10")  # left top right bottom
        tree_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")
        
        # Create the tree view inside frame
        self.tree = ttk.Treeview(tree_frame, columns=("Name", "Description"), 
                               show="headings", height=10)
        self.tree.heading("Name", text="NAME")
        self.tree.heading("Description", text="DESCRIPTION")
        self.tree.column("Name", width=150)
        self.tree.column("Description", width=200)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Create buttons with custom style and different widths
        buttons = [
            ("ADD", self.add_profile, 8),
            ("REMOVE", self.remove_profile, 8),
            ("SETTINGS", self.settings, 8),
            ("BROWSER", self.open_browser, 10)  # Changed text to be shorter
        ]
        
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=4, pady=20)
        
        for col, (text, command, width) in enumerate(buttons):
            btn = ttk.Button(
                button_frame, 
                text=text, 
                command=command,
                style="Custom.TButton",
                width=width
            )
            btn.grid(row=0, column=col, padx=5)  # Reduced padding from 8 to 5

    def load_profiles(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        profiles = self.cookie_manager.load_profiles()
        for name, desc in profiles:
            self.tree.insert("", tk.END, values=(name, desc))

    def add_profile(self):
        name, desc = self.dialog_handler.get_profile_info()
        if name:
            if self.cookie_manager.add_profile(name, desc):
                # Обновляем список профилей
                self.load_profiles()
                
                # Находим и выделяем новый профиль
                for item in self.tree.get_children():
                    if str(self.tree.item(item)["values"][0]) == name:
                        self.tree.selection_set(item)
                        self.tree.focus(item)
                        self.tree.see(item)
                        
                        try:
                            # Явно открываем браузер для нового профиля
                            self.cookie_manager.open_browser(name)
                        except Exception as e:
                            self.dialog_handler.show_error(f"Failed to open browser: {str(e)}")
                        break
            else:
                self.dialog_handler.show_error(f"Profile '{name}' already exists!")

    def remove_profile(self):
        selected = self.tree.selection()
        if selected:
            # Get profile name and convert to string
            profile_name = str(self.tree.item(selected[0])["values"][0])
            
            if self.cookie_manager.remove_profile(profile_name):
                # Close browser if it's open
                self.cookie_manager.close_browser(profile_name)
                # Refresh the profile list
                self.load_profiles()
            else:
                self.dialog_handler.show_error(f"Failed to remove profile '{profile_name}'")
        else:
            self.dialog_handler.show_error("Please select a profile first")

    def settings(self):
        pass  # Placeholder for future implementation

    def open_browser(self):
        """Open browser for selected profile"""
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])["values"]
            profile_name = str(values[0]) if values else None
            
            if profile_name:
                try:
                    self.cookie_manager.open_browser(profile_name)
                except Exception as e:
                    self.dialog_handler.show_error(f"Failed to open browser: {str(e)}")
            else:
                self.dialog_handler.show_error("Invalid profile name")
        else:
            self.dialog_handler.show_error("Please select a profile first")