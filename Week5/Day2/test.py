from cprint import cprint

# Inheritance in OOP

class Person: #Parent/Base/Super Class
	def __init__(self, name, age):
		cprint.err("In the INIT of MAN class")
		self.name = name
		self.age = age
		cprint.err("Finishing INIT of PERSON class")

	def info(self):
		print(f"{self.name} is {self.age} years old")

	def birthday (self):
		self.age += 1
		print("Happy birthday!")


class Man(Person): #Child/Sub Class
	
	def __init__(self, name, age, favorite_beer):
		cprint.info("In the INIT of MAN class")
		super().__init__(name, age)
		self.favorite_beer = favorite_beer
		self.gender = "Male"
		cprint.info("Finishing INIT of PERSON class")


	def birthday(self):
		super().birthday()
		print("Let's get beers!")

	def drink_beer(self):
		print("Glug Glub")

m1 = Man("Adam", 999)
m1.info() -> Adam is 999 years old
m1.birthday() -> Happy Birthday!

Man inherits from Person
Man extends Person

m1 = Man("Adam", 50)
m1.birthday() 
# -> Happy Birthday 
# -> Let's get beers!

m1 = man("Bob", 11, "Castle Lager")
m1.name -> "Bob"
m1.age -> 11
m1.favorite_beer -> "Castle Lager"
m1.gender -> "Male"
m1.info() -> Bob is 11 years old

# Inheritance
# class SubClass(SuperClass)

# We can add new methods
# We can override parent/super methods



from cprint import cprint

class Account:
	def __init__(self, acc_number):
		self.acc_number = acc_number
		private self.balance = 0
		protected self.money = 0
		public self.bank = 0
		self._stuff = 6
		self.__balance = 0
		self.__transaction_history = []

	def depost(self, amount):
		if amount > 0 and amount <= 10000:
			self.__balance += amount
		self.__transaction_history.append(f"Deposit :{amount}")

	def withdraw(self, amount):
		if amount <= self.__balance:
			self.__balance -= amount
			self.__transaction_history.append(f"Withdraw :{amount}")
			return amount
		else:
			print("Insufficient Funds!")

	def info(self):
		print(f"Account {self.acc_number} has balance ${self.__balance}")

		def transaction_history(self):
			for transaction in self.__transaction_history:
				print(transaction)


# OTHER LANGUAGES HAVE:
# public -> Accessible anywhere
# protected -> Accessible in the class and in all subclasses
# private -> Accessible only in the current class

# PYTHON HAS:
# _  single underscore (indication to other programmers that this should "ACT" like protected. 
#		But actually does nothing)
# __ double underscore (acts like private, and cannot be accessed outside the class)


# EXCEPTIONS

animals = ["dog", "cat"]

user_input = int(input("Which animal (number) do you want?"))

try: # if this works
	index = int(user_input)
	print(animals[index])
except ValueError: # else catch crashing code
	print("That input must be a number!")
except: IndexError:
	print(f"Number must be between 0 and {len(animals)}")
except Exception:
	pass # catches all other errors.
finally:
	print("We are done")


print("This is the end.")

# try/except -> if this works, else

class Exception:
	pass

	def info()

class IndexError(Exception):
	pass

class SyntaxError(Exception):
	pass

class TypeError(Exception):
	pass

if
elif
else

try # try this, hope it works
except # it didn't work, so run this
finally # always run this next


# Using exception  handling to add numbers in a list, even when the list contains garbage information
my_list = [2,3,1,2,"four",42,1,5,3,"imanumber", None]


def make_sum(mylist):
	total = 0
	for num in mylist:
		try:
			total += num
		except TypeError:
			continue
	return total

total = make_sum(my_list)
print(total)


def get_age():
	try:
		age = int(input("Enter your age: "))
	except:
		print("Invalid input. Try again.")
		get_age()

	print("You are old!")



# Different ways to generate random numbers with modules

import random
random.randint(1,10)

from random import random
randint(1,10)

import random as r
r.randint(1,10)

from math import sqrt
sqrt(9)
-> 3.0

if __name__ == "__main__":
	print("We are in main")


