"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

from datetime import datetime

number = int(input("How many things did you learn today? "))
learnings = []

for i in range(number):
	learning = input(f"What did you learn # {i+1} ? ")
	learnings.append(learning)

while True:
    try:
        rating = int(input("How productive was your day? (1-5): "))

        if 1 <= rating <= 5:
            break

        print("Please enter a rating between 1 and 5.")

    except ValueError:
        print("Please enter a number between 1 and 5.")

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d — %I:%M %p")

with open("learning_journal.txt", "a") as file:    # create or open a  file and with help to  work with it and then properly close it when I'm finished and "a" shows append
	file.write(f"📅 {timestamp}\n")

	for learning in learnings:
		file.write(f"- {learning}\n")

	file.write(f"Productivity Rating: {rating}/5\n")
	file.write("\n")

print("✅ Journal entry saved successfully!")
