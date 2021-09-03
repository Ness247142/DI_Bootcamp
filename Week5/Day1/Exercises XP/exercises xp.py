# Exercise 1: Cats
# Instantiate 3 Cat objects using our class
# Create a function that finds the oldest cat and returns the cat
# Print out: “The oldest cat is , and is years old.” using the method previously created


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Sylvester", 4)
cat2 = Cat("Felix", 5)
cat3 = Cat("Molly", 7)


def oldest(cat1, cat2, cat3):
    cats = [cat1.age, cat2.age, cat3.age]
    return max(cats)

print(f"The oldest cat is {oldest(cat1, cat2, cat3)} years old.")


# Exercise 2 : Dogs
# Create a class Dog.
# In this class, create a method __init__, that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method named bark that prints “ goes woof!”
# Create a method jump that prints the following “ jumps cm high!” where x is the height*2.
# Outside of the class, create an object davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog by calling the methods.
# Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog by calling the methods.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof")

    def jump(self):
      jump_height = self.height *2        
      print(f"{self.name} jumps {jump_height} cm high")

davids_dog = Dog("Rex", 50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name)
print(dsarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()


if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
else:
    print(f"{sarahs_dog.name} is bigger")


# Exercise 3 : Who’s The Song Producer ?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics(a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# Create an object, for example:
# Then, call the method sing_me_a_song. The output should be:
# # There’s a lady who's sure
# # all that glitters is gold
# # and she’s buying a stairway to heaven


class Song:
	def __init__(self, lyrics):
		self.lyrics = lyrics
		lyrics = []

	def sing_me_a_song(self):
		for lines in self.lyrics:
			print(lines)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# Create a class Zoo
# In this class create a method __init__ that takes one parameter: zoo_name
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list, only if the new_animal isn’t already in the list.
# Create a method get_animal that prints all the of animals in the zoo.
# Create a method sell_animal that takes one parameter animal_sold. This method removes the animal from the list, only if he was already in the list.
# Create a method sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# 

# Create a method get_groups that prints the animal/animals inside each group.
# Create an object ramat_gan_safari and call all the methods. 
# Tip: for each method, the argument should be the answer of the zoo keeper.


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.animal_dict = {}


    def add_animal(self, new_animal):
        print(f"Which animal should we add to the zoo ? --> {new_animal}")
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        print(self.animals)


    def get_animal(self, animals):
        for animal in self.animals:
            print(f"{animal}")


    def sell_animal(self, animal_sold):
        print(f"{animal_sold} has been sold")
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)


    def sort_animals(self):
        sorted_list = []
        self.animals.sort()
        print(f"New list of animals in order: {self.animals}")
        print(sorted_list)


    def get_groups(self):
        for groups in self.animal_dict.items():
            print(f"list of animals: {groups}")


ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Monkey")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Turtle")
ramat_gan_safari.add_animal("Rabbit")

ramat_gan_safari.get_animal("Lion")

ramat_gan_safari.sell_animal("Rabbit")

ramat_gan_safari.sort_animals()

ramat_gan_safari.get_groups()

