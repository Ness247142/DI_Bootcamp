# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher, the user entries the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Chaim's notes
# word = input('please input a word we will encrypt: \n')

# encrypted_word = []

# for letter in word:
#     number_version = ord(letter) + 3
#     letter_version = chr(number_version)
#     encrypted_word.append(letter_version)

# print(''.join(encrypted_word))


shift = 3

text_input = input("Give me a text in capital letters that you want to encrypt: ")

encrypted_word = ""

for letter in text_input:
    if letter.isupper():

        letter_code = ord(letter)

        letter_index = ord(letter) - ord("A")

        new_index = (letter_index + shift) % 26

        new_code = new_index + ord("A")

        new_character = chr(new_code)

        encrypted_word = encrypted_word + new_character

    else:
        encrypted_word += letter
        
print("Decrypted text:",text_input)

print("Encrypted text:",encrypted_word)
