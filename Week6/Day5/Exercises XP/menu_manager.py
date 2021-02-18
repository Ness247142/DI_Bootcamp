
{
    "items": [
        {
            "name": "Vegetable soup",
            "price": 30
        },
        {
            "name": "Hamburger",
            "price": 44.9
        },
        {
            "name": "Milkshake",
            "price": 22.5
        },
        {
            "name": "Artichoke",
            "price": 18
        },
        {
            "name": "Beef stew",
            "price": 52.5
        }
    ]
}


import json


class MenuManager:
	def __init__(self):
		f = open('menu.txt')
		self.menu = json.load(f)

	def add_item(self, name, price):
		x=''
		for item in self.menu['items']:
			if name == item['name'] and price == item['price']:
				x='on'
				print(f'{name} is already on your menu:')
				print(self.menu)
				break
		if x!= 'on':
			self.menu['items'].append({'name': name, 'price': price})
			print(self.menu)


	def remove_item(self, name):
		for item in self.menu['items']:
			if name == item['name']:
				self.menu['items'].remove(item)
		print(self.menu)

	def save_to_file(self):
		with open('menu.txt', 'w') as f:
			json.dump(self.menu, f)


menu1=MenuManager()
menu1.add_item('drink', 10)
menu1.remove_item('drink')
menu.save_to_file()

