Inheritance
family IS A person

Composition
family HAS A person

class Person:

class Family:


class Person:
	def __init__(self, name, age, language)


class Language:
	def __init__(self, name, region, first_spoken_date)


class Superman(Person):

	def __init__(self, name, age, powers, planet)


lang = Language("English", "UK", "850BC")

p1 = Person("Bob", A, Language("Greek", "France", "2021"))

# Superman IS A person: therefore Superman inherits from Person
# Superman HAS A language
# Person HAS A language
# So Person is composed of a Language




# Ternary Statement
# IF Statement that sets a variable. In one line.

if age > 18:
	beer = True
else:
	beer = False

beer = True if age > 18 else False




Dunder
Double Under
Methods that start and end with 3 underscores
Dunder methods are exactly like normal methods/functions
But they run autoamticaaly inder certain circumstances...

Gene() __init__

__repr__   show a string representation of the class
# it runs wheneve a variable is dumped in the terminal





__init__ : called when an object is instantiated

__repr__ : called when you dump an object variable on screen

__str__ : called when you print a variable


__str__ is more informal than __repr__


#Example
class Person:
	str return "Hi my name is Bob"
	repr return "Class Person. Name Bob"



class Person:
	def __init__(self, weight, height, facebook_friends):
		self.weight = weight
		self.height = height
		self.facebook_friends = facebook_friends

	def __gt__(self, other):
		if self.facebook_friends > other.facebook_friends:
			return True
		return False



# '>' calls __get__
# '+' calls __add__


#Example
p1 = Person(100, 1)
p2 = Person(50, 2)

p1 > p2
-> Error, impossible to do for the computer

p1_.__gt__(p2)
-> Not implemented

#Example
p1 = Person(100, 1, 100)
p2 = Person(1000, 200, 99)
p1 > p2
-> True




class Dog:
	def __init__(self, name, age, breed):
		self.name = name
		self.age = age
		self.breed = breed

	def woof(self):
		print (f"I'm a {self.breed}, my name is {self.name} and I'm {self.age} years old")


	def mate(self, other):
		puppy_name = (self.name + other.name).capitalize()
		puppy_age = 0.1
		puppy_breed = self.breed if self.breed == other.breed else self.breed
		return Dog(puppy_name, puppy_age, puppy_breed)


d1 = Dog("Lassie", 2, "Collie")
d2 = Dog("Rex", 3, "Shepard")
d3 = d1.mate(d2)
print(d3.name)
->"Lassierex"
print(d3.age)
-> 0.1
print(d3.breed)
-> "CollieShepard"

d3 = d1.__add__(d2)





What is the difference between Class vs Object?
What is an instance?

Instance Attributes vs Class Attributes

class Dog():

	genus = "Canis" # Class Attribute (shared between all dogs)
	
	def __init__(self, name):
		self.name = name

d1 = Dog("Lassie")
d2 = Dog("Rex")


print(Dog.genus)
-> "Canis"

print(d1.genus)
-> "Canis"

d1 is the object
Dog is the class
d1 is an instance of the Dog Class
d1 is an instance of Dog


class Circle:

	PI = 3.14159
	count = 0
	e = 2.71
	GOLDEN_RATIO = 1.1618


	def __init__(self, radius):
		self.radius = radius

	@property # call the method as a property
	def area(self, radius):
		return Circle.PI * self.radius**2

	# @setter
	# @getter

	def circumference(self, diameter):
		return Circle.PI * self.radius * 2

	@classmethod
	def getpi(cls):
		return cls.PI

	@staticmethod
	def info(how_many_times):
		print("A circle's definition")


c1 = Circle(100)
print(c1.area)
# -> 314.159

c2 = Circle(50)

print(Circle.info())
# -> A circle's definition


Circle.info(1)
# -> A circle's definition

print(Circle.count())
-> 0

c1 = Circle(10)
print(Circle.count())
-> 1


#From the Terminal
pip3 --version
If you have pip installed you will see the version number

pip3 install cprint
This will download and install the cprint package


from cprint import cprint

cprint.ok("print in blue")
cprint.info("print in green")
cprint.warn("print in orange")
cprint.err("print in red")



import random
random.randint()

from random import randint
randint()

import random as rd
rd.randint()

print("This is CODE.PY. This will always be printed")
if __name__ == '__main__':
	print("THIS is CODE.PY. This will only print if the file is loaded")


import sys  #access your internal system

print(sys.argv) # list of arguments


if __name__ == "__main__": # It means "if this file was loaded from the terminal"
	
	total = 0
	for num in system.argv[1:]:
		total += float(num)
	
	print(total)

python3 add.py 1 2 3 4 # in the terminal
-> 10


import os
os.mkdir("Movies") # from the terminal, we create a new file called "Movies"



# A simple clock in python using the datetime and time modules.
# Show the current time in the terminal
from time import sleep
from cprint import cprint
from datetime import datetime

while True: # infinite loop
	x = datetime.now() # define the current time with a variable
	cprint.info(x.strftime("%H:%M:%S")) # show in green, the hour, minutes and seconds
	sleep(1) # show the time every 1 second


