# lib/debug.py

import logging

# Set up logging configuration
logging.basicConfig(
    filename='restaurant_management.log',  # Log file name
    level=logging.DEBUG,                    # Log level set to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format for log messages
)

def log_info(message):
    """Log an informational message."""
    logging.info(message)
    print(f"INFO: {message}")  # Print to console for immediate feedback

def log_warning(message):
    """Log a warning message."""
    logging.warning(message)
    print(f"WARNING: {message}")  # Print to console

def log_error(message):
    """Log an error message."""
    logging.error(message)
    print(f"ERROR: {message}")  # Print to console

def log_exception(exc):
    """Log an exception with details."""
    logging.exception("An exception occurred: %s", exc)
    print(f"ERROR: An exception occurred: {exc}")  # Print to console

def display_debug_info(data):
    """Print debug information to the console."""
    print("Debug Info:")
    print(data)  # Display the provided debug data
