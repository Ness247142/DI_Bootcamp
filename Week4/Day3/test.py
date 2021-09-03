Enter a number,
Then ask the user to guess that number
They have 3 tries to guess correctly
At each try you can tell them higher or lower

answer = int(input("Enter your number: "))

for i in range(3):
	guess = int(input("Guess my number: "))
	if guess == answer:
		print("Correct!")
		break
	elif guess > answer:
		print("You guessed too high")
	elif guess < answer:
		print("You guessed too low")
else:
	print("You ran out of guesses!")



Key Value Pair

person = {
	"name":"John",
	"surname": "Spiller",
	"job": "Teacher",
	"pets": 3,
	"pet_names": ["Fluffy", "Jaws", "Robin"]
	"work_experience": {
		"programmer": "Nedcore",
		"teacher": "Developers Institute",
		"waiter": "Burger King"
	}
	"parents": ("Mom", "Dad"),
	99: "Red Ballons",
	("A", "B"): "the alphabet"
}

print(person["surname"])
-> Spiller


# keys can be any immutable object


shopping_dict = {
	0: "Apples",
	1: "Oranges",
	2: "Bananas"
}

# Dictionaries are not ordered

shopping_list = ["Apples", "Oranges", "Bananas"]


sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict["class"]["student"]["marks"]["history"])
-> 80

inventory = {
	"apples": 100,
	"oranges": 500,
	"bananas": 200
}

inventory["oranges"] -= 1
-> "oranges": 499

"bananas" in inventory
-> True

inventory["apples"]
-> 100

inventory.get("apples")
-> 100

# keys and values

my_keys = inventory.keys()
print(my_keys)
-> dict_keys(["apples", "oranges", "bananas"])

type(my_keys)
-> class "dict_keys"

myvalues = inventory.values()
-> dict_values(100, 500, 200)

myitems = inventory.items()
-> dict_items([("apples", 100), ("oranges, 500"), ("bananas", 200)])



# Get the color "green"
countries = [
	("Israel", 
		{
			"population": 8000000,
			"location": "Middle East",
			"flag": ["blue", "white"]
		}
	),
	("South Africa", 
		{
			"population": 6500000,
			"location": "Africa",
			"flag": ["blue", "white", "red", "green", "yellow", "black"]
		}
	),
	("USA", 
		{
			"population": 6500000,
			"location": "North America",
			"flag": ["blue", "white", "red"]
		}
	),
]

mycolor = countries[1][1]["flag"][3]
print(mycolor)
-> "green"


inventory = {
	"apples": 100,
	"oranges": 500,
	"bananas": 200,
	"dogs": 2,
	"chicken": 60,
	"dollars": 150
}

# Loop through the dictionary and print: "I have <number> of <fruit> for each line"

myfruits = inventory.items()

for name, number in inventory.items():
	print(f"I have {number} of {name}")


# Other solutions
# for fruit_item in myfruits:
# 	print(f"I have {fruit_item[0]} of {fruit_item[1]}")


# fruit_names = inventory.keys()
# for single_fruit in myfruits:
# 	number = inventory[single_fruit]
# 	print(f"I have {number} of {single_fruit}")



# Generate a list of numbers from 1 to 1 million

numbers = []
for i in range(1, 1000001):
	numbers.append(i)
print(numbers)


# LIST COMPREHENSION

numbers = [i for i in range(1, 1000001)]


# Generate a list of the first 10 squares

square = number**2

numbers = []
for i in range(1, 11):
	numbers.append(i*i)
print(numbers)

numbers = [i*i for i in range(1,11)]
print(numbers)


Make a dictionary from 100 to 110 where the key is a number and the value is half of the number

{
	100: 50,
	101: 50.5
}

numbers = {}
for i in range(100,111):
	numbers[i] = i/2
print(numbers)

# Dictionary Comprehension
number = {i:i/2 for i in range(100,111)}


# Ask 3 users for their names, put their names in a list

names = []
for i in range(3):
	name = input("What is your name?")
	names.append(name)

names = [input("What is your name: ") for i in range(3)]

print(names)



# Generate a list of numbers between 1 and 100 if number is divisible by 7

numbers = []
for i in range(1,101):
	if i % 7 == 0:
		numbers.append(i)
print(numbers)

numbers = [i if i % 7 == 0 else ":) " for i in range(1, 101)]
print(numbers)
