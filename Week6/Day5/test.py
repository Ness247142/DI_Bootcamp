
import psycopg2  #importing a module to connect to postgres
import pyscopg2.extras # importing to get a dictionary as a result

# defining our connection criteria
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'Hollywood'

# making the connection to the database
connection = psycopg2.connect( host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )


def connect(host, user, password, dbname):
	pass


# accessing the query editor
cursor = connection.cursor()
# cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # accessing for dictionaries

# defining the query
query = "SELECT * FROM actors"
# query = "INSERT INTO actors (first_name"

# running the query
cursor.execute(query)

# fetching the results
results = cursor.fetchall()

# closing the connection
connection.close()


# display the results
for item in results:
	print(item)

# We have a list of turples


# class RealDictRow(Dict):


__________________________________________

# Connecting with SQlite

import sqlite3 as sl

def update(data):
	cursor = connection.cursor()
	query = f"SELECT quantity FROM fruits WHERE fruit = '{data}'"
	cursor.execute(query)
	# fetching the results
	results = cursor.fetchall()
	quantity = results[0][0] + 1
	query = f"UPDATE fruits SET quantity = {quantity} WHERE fruit = '{data}'"
	cursor.execute(query)
	connection.commit()

def add(data):
	try:
		cursor = connection.cursor()
		query = f"INSERT INTO fruits (fruit, quantity) VALUES ('{data}', 1)"
		cursor.execute(query)
		connection.commit()
	except:
		update(data)
	print("Saved!")

def connect():
	return sl.connect('database.db')

def disconnect():
	connection.close()


connection = connect()

while True:
	fruit = input("Enter a fruit: ")
	if fruit == 'quit':
		break	
	add(fruit)

print('bye')
disconnect()

__________________________________________

SQL Injection

import sqlite3 as sl

con = sl.connect('test.db')

def get_details():
	name = input("What is your name? ")
	pin_number = input("What is your pin number? ")

	with con:
		query = f"SELECT * FROM employees WHERE first_name = '{name}' AND pin_number = '{pin_number}';"
		print(query)
		data = con.execute(query)
		for row in data:
			print(row)


# CREATE TABLE employees
# (
# 	id INTEGER PRIMARY KEY AUTOINCREMENT,
#   first_name TEXT,
#   last_name TEXT,
#   pin_number TEXT,
#   salary NUMERIC
# );


# INSERT INTO employees 
# (first_name, last_name, pin_number, salary)
# VALUES 
# ('Adam', 		'Adamson',	'aaa', 20000),
# ('Bobby', 	'Brown', 	'bbb', 25000),
# ('Charlie', 	'Chaplain', 'ccc', 33000),
# ('Davey', 	'Dobson', 	'ddd', 17000),
# ('Eli', 		'Emmerson', 'eee', 12000),
# ('Freddie', 	'Farrah', 	'fff', 22000)

# USE THIS AS PIN: ' or ''='

__________________________________________

import sqlite3 as sl

from faker import Faker

from time import time

f = Faker()

connection = sl.connect('database.db')

cursor = connection.cursor()

start = time()

for i in range(100):
	query = f"INSERT INTO people (name, email) VALUES('{f.name()}', '{f.email()}')"
	cursor.execute(query)

connection.commit()

connection.close()

end = time()

print(end - start)	

__________________________________________

import sqlite3 as sl
from time import time 
import requests

connection = sl.connect('database.db')

cursor = connection.cursor()

start = time()

for i in range(100):
	data = requests.get('URL')
	data = data.json()
	joke = data['value']
	joke = joke.replace('"', '`')
	joke = joke.replace("'", '`')
	query = f"INSERT INTO jokes (joke) VALUES('{joke}')"
	cursor.execute(query)

connection.commit()

connection.close()

end = time()

print(end - start)	



