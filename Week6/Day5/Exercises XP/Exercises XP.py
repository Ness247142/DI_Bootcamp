
# Find and review your code for the restaurant manager : Week 5 - Day 4 - Exercise XP Gold
# You will need to reuse the file menu_editor.py (the user cli interface)

# Write a new class called MenuItem, the attributes will be the name and price of each item.

# Write several methods (save, delete, update) to manage the menu items saving to a database.
# Write a class method all for our MenuItem class that will return a list of all our MenuItem objects
# Write a class method get_by_name that will return a single MenuItem object based off of a string, if an object is not found return None



import sqlite3 as sl

class MenuItem:
	def __init__(self, name, price):
		self.name = name
		self.price = price


	def sql_query(self, query):
		connection = sl.connect("menu_database.db")
		cursor = connection.cursor()
		cursor.execute(query)
		connection.commit()
		connection.close()


	def save(self):
		try:
			query = f"INSERT INTO restaurant_items (name, price) VALUES ('{self.name}', {self.price})"
			print(self.sql_query(query))
		except:
			return False


	def delete(self):
		query = f"DELETE FROM restaurant_items WHERE name = '{self.name}'"
		print(self.sql_query(query))


	def update(self, old_item):
		query = f"UPDATE restaurant_items SET name = '{self.name}' WHERE name = '{old_item}'"
		print(self.sql_query(query))
		query = f"UPDATE restaurant_items SET price = {self.price} WHERE name = '{self.name}'" 
		print(self.sql_query(query))


	@classmethod
	def all(cls):
		query = f"SELECT name, price FROM restaurant_items"
		connection = sl.connect("menu_database.db")
		cursor = connection.cursor()
		cursor.execute(query)
		results = cursor.fetchall()
		connection.close()
		if results:
			return results
		return "Database is empty"


	@classmethod
	def get_by_name(cls, obtain_item):
		query = f"SELECT name, price FROM restaurant_items WHERE name = '{obtain_item}'"
		connection = sl.connect("menu_database.db")
		cursor = connection.cursor()
		cursor.execute(query)
		results = cursor.fetchall()
		connection.close()
		if results:
			return results
		return "Item not in Database"


item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
items = MenuItem.all()
