import tkinter as tk
from ui import UserInterface
from session_manager import SessionManager
from database import Database
import logging
from logging_config import setup_logging

def main():
    # Set up logging
    setup_logging()

    # Initialize the main application window
    root = tk.Tk()
    root.title("User  Authentication System")
    
    # Initialize the database
    database = Database('users.db')
    database.create_user_table()  # Ensure the user table exists
    database.create_session_table()  # Ensure the sessions table exists

    # Initialize the session manager with the database
    session_manager = SessionManager(database)

    # Create the user interface
    ui = UserInterface(root, session_manager, database)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()