# Exercise 1 : Favorite Numbers
# Create a set called my_fav_numbers with your favorites numbers.
# Add two new numbers to it.
# Remove the last one.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

my_fav_numbers = {1, 2, 3, 4, 5}

my_fav_numbers.add(6)
my_fav_numbers.add(7)

my_fav_numbers.remove(7)

friend_fav_numbers = {8, 9, 10, 11, 12}

my_fav_numbers.update(friend_fav_numbers)

print(my_fav_numbers)


# Exercise 2: Tuple
# Given a tuple with integers is it possible to add more integers to the tuple?
You can't add elements to a tuple because of their immutable property. There's no append() or extend() method for tuples, You can't remove elements from a tuple, also because of their immutability.


# Exercise 3: Print A Range Of Numbers
# Use a for loop to print the numbers from 1 to 20, inclusive.

list_numbers = list(range(1, 21))

for number in list_numbers:
    print(number)


# Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way of generating a sequence of floats?
# Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.

Floats represent numbers that are written with a decimal point dividing the integer and fractional parts.
Integers and floats are two different kinds of data. An integer is a number without a decimal point. A float is a number that has a decimal place.

By using a for loop to generate a sequence of floats

for i in range (1, 5):
	print(i + 0.5)
	print(i + 1)

# Exercise 5: Shopping List
# Consider this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Put “Kiwi” at the end of the list.
# Add “Apples” at the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.append(0, "Apples")

fruit_count = basket.count("Apples")
print("The count of apples is: ", fruit_count)

basket.clear()

print(basket)


# Exercise 6 : Loop
# Write a while loop that will keep asking the user for input until the input is the same as your name.

my_name = "Nessim"
your_name = input("What's your name?")
while your_name != my_name:
	your_name = input("What's your name?")
  

# Exercise 7
# Given a list, use a while loop to print out every element which has an even index.

list1 = [10, "K", 4, "T", 66, "G"] 
for i in range (0, len(list1), 2):
    print(list1[i])


# Exercise 8
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

list3 = []

for i in range(3,31,3):
	list3 += [i]  

print(list3)


# Exercise 9
# Use a for loop to find numbers between 1500 and 2700, which are divisible by 7 and multiples of 5.


for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)


# Exercise 10: Favorite Fruits
# Ask the user to type in his/her favorite fruit(s) (one or several fruits). 
# Hint : Use the input built in method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list. (How can we ‘convert’ a string of words into a list of words?).
# Now that we have a list of fruits, ask the user to type in the name of any fruit.
# If the user’s input is a fruit name existing in the list above, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT a fruit name existing in the list above, print, “You chose a new fruit. I hope you enjoy it too!”.
# Bonus: Display the list in a user friendly way : add the word “and” before the last fruit in the list – but only if there are more than 1 favorites!


favorite_fruits = input("Enter a list of your favorite fruits each seperated by a space")

list1 = favorite_fruits

list1 = input("Give me the name of a fruit")

if list1 in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
    list1.insert(len(favorite_fruits) - 1, "+")
    list2 = "".join(favorite_fruits)
    print(list2)
else:
    print("You chose a new fruit. I hope you enjoy it too!")



# Exercise 11: Who Ordered A Pizza ?
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exit print all the toppings on the pizza and what the total is (10 + 2.5 for each topping)

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

toppings = ', '.join(topping)
print(f"You chose those toppings on your pizza: {toppings}.\nThe total is 10$ + {2.5*len(topping)}$ for each topping")


# Exercise 12: Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Apply it to a family, ask the user what the age of each of the people that want a ticket is.
# Store the total cost of all the tickets for this group and print it out.
# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which one can see the movie.
# Tip: Try to add the allowed ones to a list.


people = int(input("How many people are there?"))
age = []
prices = [0, 10, 15]
tickets = []

for i in range (0, people):
    age = int(input(f"How old are you {i+1}? "))
    if age < 3:
        tickets.append(prices[0])
    elif age >= 3 and age < 12:
        tickets.append(prices[1])
    elif age > 16 and age <= 21:
        print("Only people between 16 and 21 are allowed here")
    else:
        tickets.append(prices[2])

total_cost = 0
for i in range (0, len(tickets)):
    total_cost += tickets[i]

print(f"Your final price is: {total_cost}$")



# Exercise 13 : Who Is Under 16?

# This time you have a list of users, and you want to remove every user that is below 16 years old.
# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# At the end, print the final list.

users = []
counter = int(input("How many people to add? "))

for i in range (0, counter):
    users_age = int(input("What is your age? "))
    users.append(users_age)
print(users)


list2 = []

for i in range (0, counter):
    if users[i] < 16:
        continue
    else:
        list2.append(users[i])

print(list2)


# Exercise 14: Family Members
# Using a while loop keep asking a user for input, these inputs will be used to control a menu
# On the menu we will have 4 options:
# Add a name
# If the user selects this ask for the name to add
# Remove an existing name 
# If the user selects this ask for the name to remove
# View family members
# Print a nice list of the family members names
# Exit

family_members = []

while True:
    print("1. Add a name\n2. Remove an existing name\n3. View family members\n4. Exit")
    i = int(input("Choose which option you want: 1, 2, 3 or 4 "))
    if i < 1 and i > 4:
        i = int(input("Choose your option with 1, 2, 3 or 4"))
    elif i == 1:
        name = input("Add your name: ")
        family_members.append(name)
    elif i == 2:
        name_delete = input("Which name should be deleted? ")
        if not family_members:
            print("No name here")
            break
        else:
            family_members.remove(name_delete)
    elif i == 3:
        family_list = "; ".join(family_members)
        print(f"Your family members include: {family_list}")
    else:
        break
