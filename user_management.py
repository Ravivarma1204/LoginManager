import hashlib
import logging
import sqlite3

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(database, username, password):
    """Register a new user with a hashed password."""
    hashed_password = hash_password(password)
    try:
        database.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        database.connection.commit()
        logging.info(f"User  registered: {username}")
        return True
    except sqlite3.IntegrityError:
        # This error occurs if the username already exists
        logging.warning(f"Registration failed for user: {username} (username may already exist)")
        return False

def verify_user(database, username, password):
    """Verify the provided username and password."""
    hashed_password = hash_password(password)
    database.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    if database.cursor.fetchone() is not None:
        logging.info(f"User  logged in: {username}")
        return True
    else:
        logging.warning(f"Failed login attempt for user: {username}")
        return False