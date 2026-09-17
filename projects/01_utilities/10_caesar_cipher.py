"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

message = input("Enter your message: ")
key = int(input("Enter the secret key: "))

choice = input("Do you want to Encrypt (E) or Decrypt (D)? ").lower()

result = ""

for char in message:
    if char.isalpha():
        if char.islower():
            start = ord("a")
        else:
            start = ord("A")

        if choice == "e":
            new_char = chr((ord(char) - start + key) % 26 + start)
        else:
            new_char = chr((ord(char) - start - key) % 26 + start)

        result += new_char

    else:
        result += char

print("Result:", result)
