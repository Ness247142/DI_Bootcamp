
# Exercise 1

# Create a function called get_words_from_file that will read the file’s contents and return them as a collection. What data type should you use?

# Create another function called get_random_sentence. It should have a single parameter, length, which will be used to determine how many words the sentence should have. The function should get the words list, and choose random words from it, according to the amount specified by length.

# The words should be joined together into a string, which should be formatted in lower case (or title case) and returned.

# Create a main function. It should:

# Print a message explaining what the program does.

# Ask the user how long the sentence should be. Acceptable values: an integer between 2 and 20. Validate your data, and test your validation!

# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, user your functions to create a random sentence, and then display it proudly to the user.


import json
import random


def get_words_from_file():
	with open("sowpods.txt", "r") as f:
		data = f.readlines()
		return data


def get_random_sentence(lenght):
    data = get_words_from_file()
    sentence = rd.sample(data, lenght)
    sentence = map(lambda s: s.strip(), sentence)
    sent_string = ""
    sent_string += " ".join(sentence).title()
    print(sent_string)


def main():
    print("This Programm lets you pick a sentence lenght between 2 and 20 words to print out a random sentence")
    sentence_lenght = int(input("Give me a number between 2 and 20: "))
    while sentence_lenght < 2 or sentence_lenght > 20:
        print("Your number is too small or too big. Try again...")
        sentence_lenght = int(input("Give me a number between 2 and 20: "))
    
    print(get_words_from_file())

    print(get_random_sentence(sentence_lenght))

main()



# Exercise 2

import json

sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}


# Access the nested key “salary” from the above JSON-string
# Add a key “birth_date” at the same level of the key “name”
# Save the dictionary as JSON to a file


with open("sampleJson.jfile", "r") as f:
    key = json.load(f)
print(key["company"]["employee"]["payable"]["salary"])

key["company"]["employee"]["birth_date"] = "20/09/1990"
print(key)


import json

with open("sampleJson.jfile", "w") as f:
    json.dump(key, f, indent = 3)

print(sampleJson)