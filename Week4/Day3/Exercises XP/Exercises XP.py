# Exercise 1 : Convert Lists Into Dictionaries
# Convert the two following lists, into dictionaries.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

keys_dictionary = dict(zip(keys, values))

print(keys_dictionary)


# Exercise 2
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Here is the object you will work with : family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Using a for loop, the dictionary above, and the instructions, print out how much each family member will need to pay alongside their name
# After the loop print out the family’s total cost for the movies


family_dict = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
prices = [0, 10, 15]
total_price = 0

for person in family_dict:
	if family_dict[person] < 3:
		print(f"{person} has to pay {prices[0]}$")
	elif family_dict[person] >= 3 and family_dict[person] < 12:
		print(f"{person} has to pay {prices[1]}$")
		total_price += 10
	else:
		print(f"{person} has to pay {prices[2]}$")
		total_price += 15

print(f"Your family has to pay {total_price}$")


# Exercise 3: Zara
# Create a dictionary called brand, and translate the information above into keys and values.
keys = ['name', 'creation_date', 'creation_name', 'type_of_clothes', 'international_competitors', 'number_stores', 'major_color']
values = ['Zara', 1975, 'Amancio Ortega Gaona', ['men', 'women', 'children', 'home'], ['Gap', 'H&M', 'Benetton'], 7000, ['France -> blue', 'Spain -> red', 'US -> pink, green']]

brand = dict(zip(keys, values))

print(brand)

{'name': 'Zara', 'creation_date': 1975, 'creation_name': 'Amancio Ortega Gaona', 'type_of_clothes': ['men', 'women', 'children', 'home'], 'international_competitors': ['Gap', 'H&M', 'Benetton'], 'number_stores': 7000, 'major_color': ['France -> blue', 'Spain -> red', 'US -> pink, green']}

# Change the number of stores to 2.
brand['number_stores'] = 2
print(brand)


# Print a sentence that explains who the clients of Zara are.
for clients in brand['type_of_clothes']:
	print(f"The clients of Zara are " + clients)


# Add a key called country_creation with a value of Spain to brand
brand['country_creation'] = 'Spain'
print(brand)

# If the key international_competitors is in the dictionary, add the store Desigual.
if 'international_competitors' in brand:
	brand['international_competitors'].append('Desigual')
print(brand)

# Delete the information about the date of creation.
del brand['creation_date']
print(brand)


# Print the last international competitor.
last_competitor = brand['international_competitors'][3]
print(last_competitor)


# Print in a sentence, the major clothes’ colors in the US.
for colors in brand['major_color'][2]:
	print(f"The major clothes’ colors in the US are " + colors)

# Print the amount of key value pairs (length of the dictionary).
print(len(brand))


# Print only the keys of the dictionary.
print(brand.keys())


# Create another dictionary called more_on_zara with the following information:
keys = ['creation_date', 'number_stores']
values = [1975, 10000]

more_on_zara = dict(zip(keys, values))

print(more_on_zara)


# Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
print(brand)

# Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])

# The previous value of 'number_stores' in 'brand' has been overriden by the new value of the dictionary 'more_on_zara'


# Exercise 4 : Disney Characters
# Use a for loop to recreate the #1 result. Tip : don’t hardcode the numbers
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 

disney_users_A = {users[i]: i for i in range(0, len(users))}
print(disney_users_A)


# Use a for loop to recreate the #2 result. Tip : don’t hardcode the numbers
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 

disney_users_B = dict(enumerate(users))
print(disney_users_B)


# Use a method to recreate the #3 result 
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"] 

users = sorted(users)
disney_users_C = {users[i]: i for i in range (0, len(users))}
print(disney_users_C)


for name in users:
	if "i" in name and name[0] in ["m", "p"]:
		print(name)


