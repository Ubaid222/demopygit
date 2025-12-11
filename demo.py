from auth import login, validate_username, validate_password

print("Hello")
print("\n--- User Login Demo ---")

# Demo successful login
username = "user123"
password = "password123"
print(f"\nAttempting login with username: {username}")
if login(username, password):
    print("✓ Login successful!")
else:
    print("✗ Login failed!")

# Demo failed login - short username
username = "ab"
password = "password123"
print(f"\nAttempting login with username: {username}")
if login(username, password):
    print("✓ Login successful!")
else:
    print("✗ Login failed! Username too short.")

# Demo failed login - short password
username = "user123"
password = "12345"
print(f"\nAttempting login with username: {username}")
if login(username, password):
    print("✓ Login successful!")
else:
    print("✗ Login failed! Password too short.")

# Demo validation functions
print("\n--- Validation Demo ---")
print(f"Validating username 'user123': {validate_username('user123')}")
print(f"Validating username 'ab': {validate_username('ab')}")
print(f"Validating password 'password123': {validate_password('password123')}")
print(f"Validating password '12345': {validate_password('12345')}")
