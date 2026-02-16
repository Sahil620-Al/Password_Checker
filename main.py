import re
import random
import string

# Common weak passwords list
common_passwords = ["123456", "password", "123456789", "qwerty", "abc123", "111111"]

def check_strength(password):
    score = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add lowercase letter")

    # Digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Add numbers")

    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add special character")

    # Common password check
    if password.lower() in common_passwords:
        return "Very Weak !", ["This is a very common password"]

    # Strength rating
    if score <= 2:
        return "Weak !", remarks
    elif score == 3 or score == 4:
        return "Medium !", remarks
    else:
        return "Strong ..", ["Good password "]

# Generate strong password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

# Main program
while True:
    print("\n==== Password Strength Checker ====")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        password = input("Enter password: ")
        strength, feedback = check_strength(password)

        print(f"\nStrength: {strength}")
        print("Suggestions:")
        for msg in feedback:
            print("-", msg)

    elif choice == "2":
        print("\nGenerated Password:", generate_password())

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
