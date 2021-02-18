
# Using the following API{:.hi-vis, create a script that will write 10 random countries to your database
# Attributes to save: name, flag, subregion, population

import sqlite3 as sl
import requests
import random

connection = sl.connect('database.db')

cursor = connection.cursor()


for i in range(10):
	data = requests.get('https://restcountries.eu/rest/v2/name/united'['name']['flag']['subregion']['population'])
	data = data.json()
	country = data['value']
	country = country.replace('"', '`')
	country = country.replace("'", '`')
	query = f"INSERT INTO countries (country) VALUES('{country}')"
	cursor.execute(query)

connection.commit()

connection.close()


