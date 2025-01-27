import logging
import keyring

# Set up logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def store_credentials(username, password):
    """Store the username and password securely."""
    keyring.set_password("my_application", username, password)
    logging.info(f'User  registered: {username}')

def verify_credentials(username, password):
    """Verify the provided credentials."""
    stored_password = keyring.get_password("my_application", username)
    if stored_password is None:
        logging.warning(f'Invalid login attempt for user: {username}')
        return False
    if stored_password == password:
        logging.info(f'User  logged in successfully: {username}')
        return True
    logging.warning(f'Invalid login attempt for user: {username}')
    return False

def register_user(username, password):
    """Register a new user."""
    if keyring.get_password("my_application", username) is not None:
        logging.warning(f'User  registration failed: {username} already exists.')
        return False
    store_credentials(username, password)
    return True