import uuid

class SessionManager:
    def __init__(self, database):
        self.database = database  # Pass the database instance
        self.sessions = {}  # In-memory storage for active sessions

    def create_session(self, username):
        """Create a new session for the user and store it in the database."""
        session_id = str(uuid.uuid4())  # Generate a unique session ID
        self.sessions[session_id] = username  # Store in memory
        
        # Store in the database
        self.database.cursor.execute("INSERT INTO sessions (session_id, username) VALUES (?, ?)", (session_id, username))
        self.database.connection.commit()
        
        return session_id

    def validate_session(self, session_id):
        """Check if the session ID is valid."""
        return session_id in self.sessions

    def logout(self, session_id):
        """Log out the user by invalidating the session ID."""
        if session_id in self.sessions:
            del self.sessions[session_id]  # Remove from memory
            
            # Remove from the database
            self.database.cursor.execute("DELETE FROM sessions WHERE session_id=?", (session_id,))
            self.database.connection.commit()

    def get_active_session_id(self):
        """Return the current active session ID if it exists."""
        # This method can be modified to return the session ID of the currently logged-in user
        if self.sessions:
            return next(iter(self.sessions))  # Return the first active session ID
        return None