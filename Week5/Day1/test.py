
OOP = Object-Oriented Programming

Abstraction
A way to handle complexity bu hiding unnecessary details from the user


Encapsulation
Is when data and method are bundled together


# We can create our own classes with OOP
class Person:
	def __init__(self, name=, age=0):
		self.name = name
		self.age = age
		self.skills = []

	def say_hello(self):
			print(f"Hi my name is {self.name} I'm {self.age} years old")
			print(f"I' good at", ",".join(self.skills))

	def happy_birthday(self):
		self.age += 1

	def learn_something(self, thing):
		self.skills.append(thing)


p1 = Person("Adam", 7)
p1.say_hello()
p1.happy_birthday()
p2 = Person("Betty", 9)
p2.say_hello()

p1.learn_something("Soccer")
p2.learn_something("Soccer")
p1.learn_something("Piano")
p2.learn_something("Violon")

We can add attributes to objects -> p1.pets = ["Fluffy", "Rex"]

# We created a new class called 'Person'
# All methods must have 'self' as their first param
# init... attach variable to self




class User:

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def login(self):
		"""
		Prompts the user for username and password.
		Checks entered data against stored self data.
		"""
		username = input("Enter your username: ")
		username = input("Enter your password: ")
		if username == self.username and password == self.password:
			print("Successfully logged in!")
			return True
		print("Incorrect Username and Password!")
		return False

	def change_password(self):
		""" Allows the user to change their current password"""
		# This is just a comment
		""" This is a doctstring"""
		password_old = input("Enter your current password: ")
		if password_old == self.password:
			password_new = input("Enter your new password: ")
			if len(password_new) < 3:
				print("Password is too short.")
				return False
			self.password = new password
			print("Password changed successfully.")
		else:
			print("Incorrect Password!")
			return False


u1 = User("jon@di.com", "abc")
u2 = User("bob@gmail.com", "123")

result = u1.login("jon@di.com", "abD")
#Output : result -> False

result = u1.login("jon@di.com", "abc")
# Output: result -> True


u1.change_password() -> change the old password with a new one
u1.login() -> login with a new password


