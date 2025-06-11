from tkinter import simpledialog, messagebox, Toplevel, Entry, Label, Button, StringVar
from tkinter import ttk

class ProfileDialog(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Profile")
        self.result = None
        
        # Configure dialog style
        self.style = ttk.Style()
        self.style.configure(
            "Dialog.TButton",
            padding=4,  # Reduced padding
            relief="flat",
            background="#2196F3",
            foreground="white",
            font=("Helvetica", 9)  # Smaller font
        )
        self.style.map(
            "Dialog.TButton",
            background=[("active", "#1976D2"), ("disabled", "#BDBDBD")],
            foreground=[("disabled", "#757575")]
        )
        
        # Center dialog
        self.geometry("300x150")
        self.resizable(False, False)
        
        # Name field
        ttk.Label(self, text="Profile Name:", font=("Helvetica", 9)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_var = StringVar()
        ttk.Entry(self, textvariable=self.name_var, width=25).grid(row=0, column=1, padx=10, pady=5)
        
        # Description field
        ttk.Label(self, text="Description:", font=("Helvetica", 9)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.desc_var = StringVar()
        ttk.Entry(self, textvariable=self.desc_var, width=25).grid(row=1, column=1, padx=10, pady=5)
        
        # Button frame
        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Buttons
        ttk.Button(
            button_frame,
            text="OK",
            command=self._on_ok,
            style="Dialog.TButton",
            width=8  # Smaller width
        ).grid(row=0, column=0, padx=6)
        
        ttk.Button(
            button_frame,
            text="Cancel",
            command=self._on_cancel,
            style="Dialog.TButton",
            width=10
        ).grid(row=0, column=1, padx=10)
        
        # Make dialog modal
        self.transient(parent)
        self.grab_set()
        
        # Focus name field
        self.name_var.set("")
        self.desc_var.set("")
        self.focus_force()
        
    def _on_ok(self):
        name = self.name_var.get().strip()
        if name:
            self.result = (name, self.desc_var.get().strip())
            self.destroy()
        else:
            messagebox.showerror("Error", "Profile name is required!")
            
    def _on_cancel(self):
        self.destroy()

class DialogHandler:
    @staticmethod
    def get_profile_info():
        dialog = ProfileDialog(None)
        dialog.wait_window()
        return dialog.result if dialog.result else (None, None)

    @staticmethod
    def confirm_delete(profile_name):
        return messagebox.askyesno("Confirm", f"Delete profile '{profile_name}'?")

    @staticmethod
    def show_error(message):
        messagebox.showerror("Error", message)

    @staticmethod
    def show_success(message):
        messagebox.showinfo("Success", message)

    @staticmethod
    def confirm_save_cookies():
        return messagebox.askyesno("Save Cookies", "Do you want to save cookies now?")