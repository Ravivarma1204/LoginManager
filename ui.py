import tkinter as tk
from tkinter import messagebox
from user_management import register_user, verify_user  # Import the functions

class UserInterface:
    def __init__(self, root, session_manager, database):
        self.root = root
        self.session_manager = session_manager
        self.database = database
        self.setup_ui()

    def setup_ui(self):
        self.root.title("User  Authentication System")
        self.root.geometry("300x200")

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

        # Session info button
        self.session_info_button = tk.Button(self.root, text="Show Session Info", command=self.show_session_info)
        self.session_info_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Verify user credentials using user_management
        if verify_user(self.database, username, password):
            # Create a session for the user
            session_id = self.session_manager.create_session(username)
            messagebox.showinfo("Login", f"Login successful! Session ID: {session_id}")
        else:
            messagebox.showerror("Login", "Invalid credentials. Please try again.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Attempt to register the user using user_management
        if register_user(self.database, username, password):
            messagebox.showinfo("Registration", "Registration successful!")
        else:
            messagebox.showerror("Registration", "Registration failed. User may already exist.")

    def show_session_info(self):
        """Display the current session information."""
        session_id = self.session_manager.get_active_session_id()  # Assuming you have a method to get the active session ID
        if session_id:
            messagebox.showinfo("Session Info", f"Current Session ID: {session_id}")
        else:
            messagebox.showinfo("Session Info", "No active session.")