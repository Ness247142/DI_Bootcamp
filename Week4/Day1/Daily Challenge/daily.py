
# Exercise
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”
# If it’s more than 10 characters, print a message which states “string too long”
# Then, print the first and last characters of the given text
# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
# Example:
# The user enters “Hello Word”
# Then, you have to construct the string character by character
# H
# He
# Hel
# … etc
# Hello World
# Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
# Example:
# Hlrolelwod

string = input("Give me a word with 10 characters: ")
string_ch = int(len(string))

if string_ch > 10:
	print("string too long")
elif string_ch < 10:
	print("string not long enough")
else:
	print("")


def text_first_last_ch():
  if len(string) < 1:
    return ""

  return string[0:1] + string[-1:]
  print(text_first_last_ch)


for i in range(0,len(string)):
   print(string[i])


import random

string = list(range(10))
print(string)

random.shuffle(string)
print(string)
