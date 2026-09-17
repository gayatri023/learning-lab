"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import random
import string

password = input("Enter your password: ")

missing = []

if len(password) < 8:
    missing.append("at least 8 characters")

if not any(char.isupper() for char in password):
    missing.append("an uppercase letter")

if not any(char.islower() for char in password):
    missing.append("a lowercase letter")

if not any(char.isdigit() for char in password):
    missing.append("a digit")

if not any(char in "@#$%&*!" for char in password):
    missing.append("a special character")

if missing:
    print("\nYour password is weak.")
    print("You are missing:")

    for item in missing:
        print("-", item)

    characters = string.ascii_letters + string.digits + "@#$%&*!"
    suggestion = ""

    for i in range(12):
        suggestion += random.choice(characters)

    print("\nSuggested password:", suggestion)

else:
    print("\nYour password is strong! ✓")
