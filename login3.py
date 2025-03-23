import sys
import hashlib
attempts = 3
print("Create a new account")
correct_username = input("Enter your new Username: ")
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
correct_password = input("Please enter your new password: ")
hashed_password = hash_password(correct_password)
print('Login')
for attempt in range(attempts):
    username = input("Username: ")
    password = input("Password: ")
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        remaining_attempts = attempts - (attempt + 1)
        if remaining_attempts > 1:
            print(f"Incorrect login. You have {remaining_attempts} tries left.")
        elif remaining_attempts == 1:
            print(f"Incorrect login. You have {remaining_attempts} try left.")
        else:
            print("Incorrect login. No attempts left. Access denied.")