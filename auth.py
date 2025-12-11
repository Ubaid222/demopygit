"""
Authentication module for user login functionality.
"""

def login(username, password):
    """
    Authenticates a user with username and password.
    
    Args:
        username (str): The username for login
        password (str): The password for login
    
    Returns:
        bool: True if login is successful, False otherwise
    """
    # Use existing validation functions to reduce duplication
    if not validate_username(username):
        return False
    
    if not validate_password(password):
        return False
    
    # In a real application, this would check against a database
    return True


def validate_username(username):
    """
    Validates if the username meets requirements.
    
    Args:
        username (str): The username to validate
    
    Returns:
        bool: True if username is valid, False otherwise
    """
    if not username or not isinstance(username, str):
        return False
    
    # Username must be at least 3 characters
    return len(username) >= 3


def validate_password(password):
    """
    Validates if the password meets requirements.
    
    Args:
        password (str): The password to validate
    
    Returns:
        bool: True if password is valid, False otherwise
    """
    if not password or not isinstance(password, str):
        return False
    
    # Password must be at least 6 characters
    return len(password) >= 6
