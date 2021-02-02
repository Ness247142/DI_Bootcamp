
# Chaim's notes
# word = input('please input a word we will encrypt: \n')

# encrypted_word = []

# for letter in word:
#     number_version = ord(letter) + 3
#     letter_version = chr(number_version)
#     encrypted_word.append(letter_version)

# print(''.join(encrypted_word))


shift = 3

text_input = "CAESAR CYPHER"

encrypted_word = ""

for letter in text_input:
    if letter.isupper():

        letter_unicode = ord(letter)

        letter_index = ord(letter) - ord("A")

        new_index = (letter_index + shift) % 26

        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        encrypted_word = encrypted_word + new_character

    else:
        encrypted_word += letter
        
print("Plain text:",text_input)

print("Encrypted text:",encrypted_word)
