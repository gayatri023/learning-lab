"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

# get dictionary
emoji_map = {
	"love": "❤️",
	"happy": "😊",
	"code": "💻",
    	"tea": "🍵 ",
	"music": "🎵",
	"food": "🍕"
}

#get user message
message = input("what is your message? ")

# process each word
words = message.split(" ")

new_words = []

for word in words:
	cleaned = word.lower().strip(".,!?")
	emoji = emoji_map.get(cleaned, "")
	if emoji:
		punctuation = word[-1] if word[-1] in ",.!?" else ""
		base_word = word[:1] if punctuation else word
		new_words.append(f"{word} {emoji}")
	else:
		new_words.append(word)

updated_message = " ".join(new_words)
print("\n Enhanced message: \n")
print(updated_message)








#
