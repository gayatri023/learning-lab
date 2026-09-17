"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""



def calculate_age(age):
    days = age * 365.25
    hours = days * 24
    minutes = hours * 60

    return round(days), round(hours), round(minutes)


while True:
    try:
        age = float(input("Enter your age in years: "))

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        days, hours, minutes = calculate_age(age)

        print(f"""
You are approximately:
  - {days:,} days old
  - {hours:,} hours old
  - {minutes:,} minutes old
""")

        again = input("Try again? (y/n): ").strip().lower()

        if again != "y":
            break

    except ValueError as e:
        print(e)
