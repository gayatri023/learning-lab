"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time

seconds = int(input("Enter timer duration in seconds: "))

while seconds > 0:
    minutes = seconds // 60
    remaining_seconds = seconds % 60

    print(f"{minutes:02d}:{remaining_seconds:02d}", end="\r")

    time.sleep(1)
    seconds -= 1

print("00:00")
print("⏰ Time's up! \a")
