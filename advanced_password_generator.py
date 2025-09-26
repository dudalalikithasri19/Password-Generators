import random
import string
print("Advanced Password Generator")
length = int(input("Enter the password length: "))
include_letters = input("Include letters? (y/n): ").lower() == "y"
include_numbers = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"
characters = ""
if include_letters:
    characters += string.ascii_letters
if include_numbers:
    characters += string.digits
if include_symbols:
    characters += string.punctuation
if not characters:
    print("You must choose at least one option!")
    exit()
password = []
if include_letters:
    password.append(random.choice(string.ascii_letters))
if include_numbers:
    password.append(random.choice(string.digits))
if include_symbols:
    password.append(random.choice(string.punctuation))
while len(password) < length:
    password.append(random.choice(characters))
random.shuffle(password)
password = ''.join(password)
print("\nYour strong password is:", password)
count = int(input("\nHow many more passwords to generate? (0 for none): "))
for i in range(count):
    pw = ''.join(random.choice(characters) for _ in range(length))
    print(f"Password {i+1}: {pw}")
