"""
Project: Personal Profile Generator
Day 1 — Python Fundamentals

Build a command-line program that collects basic information
from a user and generates a personalized self-introduction.

Requirements:
1. Collect name, age, city, profession, and favorite hobby.
2. Generate a warm, natural-language introduction.
3. Display the introduction in a clean terminal format.
4. Include the current date.
5. Add a decorative border around the final output.

Goal:
Practice user input, variables, strings, formatting,
and basic program output.
"""

from datetime import date

# Get information from the user
name = input("What is your name? ")
age = input("How old are you? ")
city = input("Which city do you live in? ")
profession = input("What is your profession? ")
hobby = input("What is your favorite hobby? ")

# Get today's date
today = date.today()

# Create the introduction
introduction = (
    f"Hi! My name is {name}. I am {age} years old and I live in {city}. "
    f"I work as a {profession}, and in my free time, I enjoy {hobby}."
)

# Decorative border
border = "=" * 60

# Display the final profile
print()
print(border)
print("              PERSONAL PROFILE")
print(border)
print()
print(introduction)
print()
print(f"Profile generated on: {today}")
print()
print(border)
