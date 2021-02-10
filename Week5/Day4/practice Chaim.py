
#Functions
#Exercise 1
def employee_info(name, salary=9000):
	print(f"The employee's name is {name} and their salary is {salary}")


employee_info("Bob", 10000)
employee_info("Bob")



#Exercise 2
def day_of_the_week(num):
	if num == 1:
		print("sunday")
	elif num == 2:
		print("monday")
	elif num == 0 or num > 7:
		print("None")


day_of_the_week(1)




#Exercise 3
def traffic_light(color):
	if color == "red":
		print("Stop!")
	elif color == "orange":
		print("Slow down!")
	elif color == "green":
		print("Go!")
	else:
		print("")

traffic_light("green")



#Exercise 4
# Create a function that takes a list of names as a parameter and prints out a new list with all the names that begin with the letter a

def list_names(names):
	my_list = []
	for name in names:
		if name[0] == "A":
			my_list.append(name) 
	print(my_list)


list_names(["Alex", "Diego", "Max", "Alexander", "Alia", "Levy"])




# Classes
#Exercise 1
class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def rectangle_area(self):
	    return self.length*self.width

new_rectangle = Rectangle(15, 12)
print(new_rectangle.rectangle_area())



# Exercise 2
class Circle():
	def __int__(self, radius):
		self.radius = radius
		
	def area(self):
	    return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

new_circle = Circle(12)

print(new_circle.area())
print(new_circle.perimeter())

