import sys
import hashlib

# Function to hash a password
print('Welcome to Kosher Bytes!')
print('~~~~~~~~~~~~~~~~~~~~~~~~')
def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Function to create a new account
def create_account():
    print("Create a new account")
    username = input("Enter your new username: ")
    password = input("Enter your new password: ")
    hashed_password = hash_password(password)  # Hash the password before storing
    return username, hashed_password

# Function to log in
def login(stored_username, stored_hashed_password):
    print('--------------------------')
    print("Log in")
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        hashed_password = hash_password(password)  # Hash the entered password for comparison

        if username == stored_username and hashed_password == stored_hashed_password:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                attempt_text = "attempt" if attempts == 1 else "attempts"
                print(f"Incorrect login. You have {attempts} {attempt_text} left.")

    print("Too many incorrect attempts. Program ending.")
    sys.exit()  # Ends the program

def main():
    username, hashed_password = create_account()  # Create new account
    login(username, hashed_password)  # Try to log in