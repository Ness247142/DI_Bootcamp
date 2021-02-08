
# 1. Create a Farm class. How do we implement that?
# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3. How many method does the Farm class need ?
# 4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# 5. Test that your code works and gives the same results as the example above.
# 6. Bonus: line up the text nicely in columns like in the example using string formatting


# Expand The Farm
# Add a method to the Farm class called get_animal_types. It should return a sorted list of all the animal types (names) that the farm has in it. For the example above, the list should be: ['cow', 'goat', 'sheep']
# Add another method to the Farm class called get_short_info. It should return a string like this: “McDonald’s farm has cows, goats and sheep.” 
# It should call the get_animal_types function. 
# How would we make sure each of the animal names printed has a comma after it aside from the one before last (has an and after) and the last(has a period after)?.


class Farm:
    def __init__(self, species):
        self.name = species
        self.animal_dict = {}

    def add_animal(self, animal, number=1):
        if animal not in self.animal_dict:
            self.animal_dict[animal] = number
        else:
            self.animal_dict[animal] += number

    def get_info(self): 
        print("Mcdonald's farm\n")
        for info in self.animal_dict.items():
            print(f"{info[0]}: {info[1]}")
        print("\tE-I-E-I-O!")

    def get_animal_types(self):
        animal_list = []
        for animal_type in self.animal_dict.keys():
            animal_list.append(animal_type)
        animal_list.sort()
        print(animal_list)
        return animal_list
        

    def get_short_info(self):
        animal_list = self.get_animal_types()
        total_animal_farm = ", ".join(animal_list) + "."
        print(f"McDonald’s farm has {total_animal_farm}")



macdonald = Farm("McDonald")
macdonald.add_animal('cows',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goats', 12)

print(macdonald.get_info())

macdonald.get_animal_types()

macdonald.get_short_info()
