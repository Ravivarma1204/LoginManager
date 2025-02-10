import logging

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        filename='app.log',  # Log file name
        level=logging.DEBUG,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
        datefmt='%Y-%m-%d %H:%M:%S'  # Date format
    )

# Call the setup_logging function to configure logging when the module is imported
setup_logging()