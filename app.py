from logging_config import setup_logging
from user_management import verify_credentials, register_user
import tkinter as tk
from tkinter import messagebox

# Set up logging
setup_logging()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("User  Login and Registration")
        self.root.geometry("300x300")

        # Create frames
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Username label and entry
        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password label and entry
        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login button
        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        # Register button
        self.register_button = tk.Button(self.root, text="Register", command=self.register)
        self.register_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if verify_credentials(username, password):
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Login", "Invalid credentials. Please try again.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if register_user(username, password):
            messagebox.showinfo("Registration", "Registration successful!")
        else:
            messagebox.showerror("Registration", "Registration failed. User may already exist.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()