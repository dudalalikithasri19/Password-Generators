import random
import string
print("Welcome to the Simple Password Generator!")
length=int(input("Enter the password length:"))
characters=string.ascii_letters+string.digits+string.punctuation
password=''.join(random.choice(characters)for _ in range(length))
print("Your generated password is:",password)
