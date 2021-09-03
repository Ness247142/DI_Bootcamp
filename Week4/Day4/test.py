# FUNCTIONS
# Longer version
def letter(thing):
	output = thing[0].upper() + thing[1:]
	return output

# Shorter version
def letter(thing):
	return thing[0].upper() + thing[1:]

letter("hello")
letter("goodbye")

# this function has 1 "parameter" called thing

# the data that you pass into function parameters is called "argument"

# "sum" takes a list of numbers for example

def get_total(numbers=[]):
	total = 0
	for num in numbers:
		total += num
	return total

# Default argument
def say_hello(name="Stranger"):
	print(f"Hello {name}")


# Multiple arguments and Positional Arguments
def say_happy_birthday(name, age, from_name=None):
	print(f"Happy birthday {name}! You are {age} years old.")
	if from_name is not None:
		print(f"From {from_name}")

# You can define a function with as many parameters as you want

# keywords arguments : choose the position of the arguments with their keywords (age=25, name="Bob", from_name="Fred")

y = 10

def something(name):
	x = 5
	name = name.upper()
	print(x)
	print(name)

# variables inside a function only exist inside this function
# We can do print(y) but not print(x), we need to call the function for "x" and "name"

def order_hamburger():
	print(hamburger)
	return hamburger

# with "return", we can use the result again, with "print" we can't


# 1. Create a function that has 2 parameters:
# your age and your friend's age
# return the older age


# 2. Create a function that takes 2 words
# It must return the length of the longer word

# 3. Write the max() function yourself...

# 4. Create a function that takes 1 dictionary as an argument
# the dictionary should contain 2 items
# each entrey should have a name and grade
# return the name of the person with the highest grade



# Exercise 1
def ages(my_age, friend_age):
	if my_age < friend_age:
		return friend_age
	else:
		return my_age

ages(24, 28)


# Exercise 2
def words(word_1, word_2):
	word_1 = "hello"
	word_2 = "goodbye"
	if len(word_1) < len(word_2):
        return len(word_2)
    else:
        return("")

print(len(words2))


# Exercise 3
def max(numbers=[]):
    numbers = [1, 2, 6, 9, 10]
    for num in numbers:
    largest_number = max(number)
	return largest_number

print(numbers)

