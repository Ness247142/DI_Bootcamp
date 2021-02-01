print("hello world!")
hello world!

4 + 5
9
SyntaxError: multiple statements found while compiling a single statement
4 + 5
9
2 ** 8 - 1
255
print ("one string" + " plus another")
one string plus another
help(str)

name = "Bob"
print(name)

type(name)


# ask the user their name
# ask the user for their age
# Print the greeting and how old they will be next year

name = input("What is your name? ")
age = int(input("How old are you? "))
# age = int(age)

print(f"Hello {name.capitalize()}. Next year you will be {age + 1} years old")

age = int(input("How old are you? "))
country = "USA"

if age >= 18 and country == "Israel" or country == "South Africa":
	print("Have a beer")
	print("Pay taxes too")
elif age <= 1:
	print("Have some milk")
elif age <= 75:
	print("Have a whiskey")
else:
	print("Have a soda")	

print("Thanks for coming")


name = "jonathan"

print("j" in name)
print("t" in name)
print("x" in name)

email = input("Enter an email address: ")

if "@" not in email or ".com" not in email:
	print("Invalid Address")
else:
	print("Addes to the spam list")

