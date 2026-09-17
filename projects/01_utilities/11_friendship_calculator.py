"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

name1 = input("Enter friend A's name: ").lower()
name2 = input("Enter friend B's name: ").lower()

# Shared letters
shared_letters = set(name1) & set(name2)

# Shared vowels
vowels = set("aeiou")
shared_vowels = set(name1) & set(name2) & vowels

# Character positions
same_positions = 0

for i in range(min(len(name1), len(name2))):
    if name1[i] == name2[i]:
        same_positions += 1

# Calculate score
score = (
    len(shared_letters) * 10
    + len(shared_vowels) * 10
    + same_positions * 10
)

score = min(score, 100)

print("\n❤️ Friendship Compatibility ❤️")
print(f"{name1.title()} + {name2.title()} = {score}%")

if score >= 80:
    print("You're like chai and samosa — made for each other! ☕🥟")
elif score >= 50:
    print("Pretty compatible! You two get along well. 😊")
else:
    print("Well... opposites attract, maybe? 😄")
