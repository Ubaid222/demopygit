def greet_user(name="User"):
    """Greet the user with a personalized message."""
    message = f"Hi {name}! Welcome to demopygit!"
    print(message)
    return message

if __name__ == "__main__":
    # Greet with default
    greet_user()
    
    # Greet with custom name
    user_name = input("\nWhat's your name? ").strip()
    if user_name:
        greet_user(user_name)
