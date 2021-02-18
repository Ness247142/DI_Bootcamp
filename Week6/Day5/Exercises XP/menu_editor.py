
from menu_manager import MenuManager

def load_manager():
	MenuManager()
	return MenuManager

def show_user_menu():
	print('    Menu\n (a) Add an item \n (b) Delete item\n (c) View menu \n (d) Exit ')
	choice = input(' ')
	if choice == 'a':
		add_item_to_menu()
		show_user_menu()
	elif choice == 'b':
		remove_item_from_menu()
		show_user_menu()
	elif choice == 'c':
		show_restaurant_menu()
		show_user_menu()
	elif choice == 'd':
		menu2.save_to_file()
		print(menu2.menu)

def add_item_to_menu():
	name = input('Name:  ')
	price = input('Price:  ')
	menu2.add_item(name, price)
	print(menu2.menu)

def remove_item_from_menu():
	name = input("Name of the item:  ")
	menu2.remove_item(name)
	print(menu2.menu)

def show_restaurant_menu():
	for item in menu2.menu['items']:
		print(item['name'] + ': $' + str(item['price']))


menu1 = load_manager()
menu2 = menu1()
print(menu2.menu)
print(show_user_menu())
