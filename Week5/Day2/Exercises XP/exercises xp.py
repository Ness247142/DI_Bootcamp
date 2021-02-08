# Exercise 1 : Pets
# Add another cat breed
# Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
# Instantiate the Pet class with all your cats. Use the variable my_pets
# Output all of the cats walking using the my_pets instance

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"

class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Persian(Cat):
    def sing(self, sounds):
        return f"{sounds}"

cat_1 = Bengal("Cheeta", 12)
cat_2 = Chartreux("Sassy", 10)
cat_3 = Persian("Jasmine", 8)

my_cats = [cat_1, cat_2, cat_3]

my_pets = Pets(my_cats)

my_pets.walk()



# Exercise 2 : Dogs
# Create a class named Dog with the attributes name, age, weight
# Implement the following methods for the class:
# bark: returns a string of “ barks”.
# run_speed: returns the dogs running speed (weight/age *10).
# fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speedweight* should win.
# Create 3 dogs and use some of your methods

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print("Woof! Woof!")

    def run_speed(self):
        running_speed = self.weight/(self.age*10)
        return running_speed


    def fight(self, other_dog):
        running_speed = self.run_speed()
        if running_speed*self.weight > other_dog.run_speed()*other_dog.weight:
            print(f"{self.name} is the winner!")
        else:
            print(f"{other_dog.name} is the winner!")


dog1 = Dog("Bella", 5, 40)
dog2 = Dog("Charlie", 7, 90)
dog3 = Dog("Max", 10, 60)

print(dog1.fight(dog3))
print(dog3.fight(dog2))
print(dog2.fight(dog1))


# Exercise 3 : Dogs Domesticated

# Create a new python file and import your Dog class from the previous exercise.
# Create a class named PetDog that inherits from Dog.
# Add the attribute trained (boolean) to the PetDog class, should always start False
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
# play: gets parameter of any amount of other dogs (look up args) and prints “the dogs: dog_names play together” each of the dogs that plays has their trained boolean switched to False
# do_a_trick: will print one of the following sentences randomly ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
# “dog_name does a barrel roll”
# “dog_name stands on their back legs”
# “dog_name shakes your hand”
# “dog_name plays dead”

import random

class PetDog(Dog):

    def __init__(self, name, age, weight):
        super().__init__(self, name, age, weight)
        self.trained = False

    def train(self):
        self.bark()
        return self.trained == True

    def play(self, *dog_names):
        dogs = ', '.join(dog_names.name)
        print(f"the dogs: {dogs} play together")
        return dog_names.trained == False

    def do_a_trick(self, *dog_names):
        trick = random.randint(0, 3)
        if self.trained == True:
            if trick == 0:
                print(f"{dog_names.name} does a barrel roll")
                dog_names.trained = False
            elif trick == 1:
                print(f"{dog_names.name} stands on their back legs")
                dog_names.trained = False
            elif trick == 2:
                print(f"{dog_names.name} shakes your hand")
                dog_names.trained = False
            else:
                print(f"{dog_names.name} plays dead")
                dog_names.trained = False


dog1 = PetDog("Bella", 5, 40)
dog2 = PetDog("Charlie", 7, 90)
dog3 = PetDog("Max", 10, 60)

print(dog1.train())
print(dog2.play("Charlie"))
print(dog3.do_a_trick("Max"))



# Exercise 4 : Family
# Write a Family class and implement the following attributes:
# members: list of dictionaries with the keys name, age and gender (‘Male’/’Female’) and is_child.
# last_name (string)
# Initial members data:
# [ {'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False} ]

# Implement the following methods:
# born: adds a child to the members list (look up **kwargs), don’t forget to print a Congratulation message
# is_18: accept the name of one member and returns True if he is over 18, False otherwise
# a method that nicely presents the family (use the info you find relevant)


class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        new_member = {}
        for key, value in kwargs.items():
            new_member[key] = value
        self.members.append(new_member)
        print(f"Congratulation {self.members[-1]['name']}! Welcome to the family! ")

    def is_18(self):
        value = input("Give me the name of a family member: ")
        if self.members[value]["age"] < 18:
            print(f"Sorry, {self.members[value]['name']} but you're too young")
            return False
        else:
            print(f"Great, {self.members[value]['name']}, let's continue!")
            return True

    def family_presentation(self):
        print(f"In our little family there is {self.members[2]['name']}, the Baby. He is {self.members[2]['age']} years old. There are also {self.members[0]['name']} and {self.members[1]['name']} {self.last_name}, his parents.")
            

family_1 = Family([ {'name':'Michael','age':35,'gender':'Male','is_child':False}, 
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}], "Rogers")

family_1.born(name="Ethan", age=0, gender="Male", is_child=True)

family_1.is_18()

family_1.family_presentation()


# Exercise 5 : TheIncredibles Family
# Write a TheIncredibles class that inherits from the Family class:
# It is an Incredible Family, so they have powers, therefore the dictionaries get new keys called power and incredible_name
# implement a method use_power, that prints the power of a member only if the said member is over 18
# if the member isn’t over 18 raise an Exception (check how !!) saying (‘You have no power here !!’)
# add a incredible_presentation method to present them with their incredible names and powers
# Look up the names of The Incredibles characters on google and build the family (if you don’t find some information just improvise). Excluding baby jack !
# Print their normal presentation and their incredible presentation
# Use the ‘born’ method inherited from the family class to add Baby Jack with the power: “Unknown Power”
# Print both presentations again to check Baby Jack is born and that his power is showing when using the incredible representation


class Incredibles(Family):
    def __init__(self, members, last_name, power, incredible_name):
        super().__init__(self, members, last_name)
        self.power = power
        self.incredible_name = incredible_name

    def use_power(self):
        try:
            if self.members['age'] > 18:
                print(f"Your power is: {self.members['power']}. Amazing!")
        except:
            print(f"{self.members['name']} you have no power!!")

    def incredible_presentation(self):
        for incredible in self.members:
            print(incredible)
        for incredible in self.power:
            print(incredible)
        for incredible in self.incredible_name:
            print(incredible)

        
incredible_family = Incredibles([ {'name':'Bob','age':35,'gender':'Male','is_child':False}, {'name':'Helen','age':32,'gender':'Female','is_child':False}, {'name':'Violet','age':12,'gender':'Female','is_child':True}, {'name':'Dashiell','age':8,'gender':'Male','is_child':True}], "Parr", [{'power': 'super-strength'}, {'power': 'invisible'}, {'power': 'force-shield'}, {'power': 'super-speed'}], [{'incredible_name': 'Mr. Incredible'}, {'incredible_name': 'Elastigirl'}, {'incredible_name': 'Vi'}, {'incredible_name': 'Dash'}])

print(incredible_family.family_presentation())

print(incredible_family.incredible_presentation())

incredible_family.born(name="Jack", age=3, gender="Male", is_child=True, incredible_name='Jack-Jack', power='Unknown power')

print(incredible_family.incredible_presentation())
                  
