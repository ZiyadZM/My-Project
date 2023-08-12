import random
import string
def print_string(input_string):
    print("\nHexa:")
    for char in input_string:
        print(hex(ord(char)), end=' ')
    print()
    print("\nDecimal:")
    for char in input_string:
        print(ord(char), end=' ')
    print()


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")
print_string(plain_text)

#DECRYPT
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print()
print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")
print_string(cipher_text)


