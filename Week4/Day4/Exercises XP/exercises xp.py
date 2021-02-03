# Exercise 1 : What Are You Learning ?
# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.

def display_message():
	message = "Everyone, today we are learning about functions in Python"
	print(message)

display_message()

# Exercise 2: What’s Your Favorite Book ?
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
	print(f"One of my favorite books is " + title)

favorite_book("Harry Potter")

# Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city_name, country="Israel"):
	print(city_name + " is in " + country)

describe_city("Paris", "France")
describe_city("London", "England")
describe_city("Berlin", "Germany")

# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message to the user, otherwise show a fail message and display both numbers

import random

def numbers(x, y):
	x = random.randint(0,101)
	print(x)
	y = random.randint(0,101)
	print(y)
	if x == y:
		print(f"Success!")
	else:
		print(f"Fail! Try again")

numbers("x", "y")

# Exercise 5 : Let’s Create Some Personalized Shirts !
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size="large", message="I love Python"):
	print(f"The size of this t-shirt is " + size)
	print(f"It says: " + message)

make_shirt("medium", "Python is interesting")
make_shirt(size="large", message="Let's keep making good t-shirts")

make_shirt()
make_shirt(size="medium", message="I love Python")

make_shirt(size="small", message="Cool-shirt")

# Exercise 6 : Magicians …
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.

magicians = ["Arcana", "Freddy", "Babah"]

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

show_magicians(magicians)

def make_great(magicians):
    great_magicians = []
    while magicians:
    	magician = magicians.pop()
    	great_magician = magician + " the Great "
    	great_magicians.append(great_magician)
    for great_magician in great_magicians:
        	magicians.append(great_magician)

make_great(magicians)
show_magicians(magicians)

# Exercise 7: When Will I Retire ?
# The point of the exercise is to check is a person can retire depending on his age and his gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return it (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age back.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.

# Some Hints
# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message to the user informing them whether they can retire or not.
# As always, test your code to ensure it works.


from datetime import date 

gender = input(f"What is your gender? Enter either M for Male or F for Female: ")
date_of_birth = input(f"When where you born? Give me your birthdate in the following format 'YYYY/MM/DD': ")

def get_age(year, month, day):
    current_year = 2021
    current_month = 2
    current_day = 3
    if current_month >= month:
        if current_day <= day:
            age = current_year - year + 1
        else:
            age = current_year - year
    else:
        age = current_year - year + 1
    return age

def can_retire(gender, date_of_birth):
    year, month, day = date_of_birth.split("/")
    year, month, day = int(year), int(month), int(day)
    age = get_age(year, month, day)
    if gender == "M":
        if age > 67:
            return True
        else:
            return False
    elif gender == "F":
        if age > 62:
            return True
        else:
            return False


if can_retire(gender, date_of_birth):
    input(f"Don't worry. You can retire")
else:
    input(f"Sorry. You can't retire yet")

print(get_age())
print(can_retire())



# Exercise 8:
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example: 
# If X=3 the output when calling our function should be 3702 (3 +33 +333 + 3333)
# Hint: treating our number as a int or a str at different points in our code may be helpful

def digit_letters(x):
    a = int("%s" % x)
    b = int("%s%s" % (x,x))
    c = int("%s%s%s" % (x,x,x))
    d = int("%s%s%s%s" % (x,x,x,x))
    return a+b+c+d
    
print(digit_letters(x="3"))







