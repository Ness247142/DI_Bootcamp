# Exercise 1
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

print("Hello World "*4)

# Other solution
# list = ["Hello World","Hello World","Hello World","Hello World"] 
# for i in list:  
#     print(i, end = " ")  


# Exercise 2
# Calculate the result of: (99^3) * 8
print((99^3) * 8)


# Exercise 3
# Predict the output of the following code snippets:
# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"

5 < 3 -> False
3 == 3 -> True
3 == "3" -> False
"3" > 3 -> TypeError: '>' not supported between instances of 'str' and 'int'

"Hello" == "hello" -> False


# Exercise 4
# Create a variable called computer_brand that contains the brand of your computer.
# Insert and print the above variable in a sentence,like "I have a razer computer".
computer_brand = "Macintosh"
print(f"I have a {computer_brand} computer")


# Exercise 5
# Create a variable called name, and give it your name as a value (text)
# Create a variable called age, and give it your age as a value (number)
# Create a variable called shoe_size, and give it your shoe size as a value
# Create a variable called info. Its value should be an interesting sentence about yourself, including your name, age, and shoe size. Use the variables you created earlier.
# Have your code print the info message.
# Run your code

name = "Nessim"
age = 24
shoe_size = "42"
info = f"My name is {name}, I am {age} and my shoe size is {shoe_size}"
print(info)


# Exercise 6
# Given two variables a and b that you need to define, make a program that print Hello World only if a is greater than b.

a = int(input("Assign a number to a "))
b = int(input("Assign a number to b "))
if a > b:
	print("Hello World")
else:
	print("")


# Exercise 7
# Write a script that asks the user for a number and determines whether this number is odd or even.

number = int(input("Give me a number"))
if (number % 2) == 0:	
	print("This number is even")
else:
	print("This number is odd")


# Exercise 8
# Write a script that asks the user for his name and determines whether or not you have the same name, print out a funny message based on the outcome

my_name = "Nessim"
name = input("What's your name?")
if my_name != name:
	print(f"We have the same name! So good!")
else:
	print(f"We don't have the same name... See you later!")


# Exercise 9
# Write a script that will ask the user for their height in inches, print a message if they can ride a roller coaster or not based on if they are taller than 145cm
# Please note that the input is in inches and you’re calculating vs cm, you’ll need to convert your data accordingly

height = int(input("What is your height?"))
feet = int(input("Feet: "))
inch = int(input("Inches: "))

inch += feet * 12
cm = round(inch * 2.54, 1)
if height > int(145):	
	print("You can ride a roller coaster")
else:
	print("You are not tall enough to ride a roller coaster")
