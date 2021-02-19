
# Using the following API{:.hi-vis, create a script that will write 10 random countries to your database
# Attributes to save: name, flag, subregion, population


import sqlite3
import requests
import json
import random
import psycopg2
import pprint

countries_api = requests.get('https://restcountries.eu/rest/v2/all')

countries = countries_api.json()

pprint.pprint(type(countries))

name = countries['name']
flag = name['flag']
subregion = name['subregion']
population = name['population']

print(name)
print(subregion)

conn = sqlite3.connect('country.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS countries")

c.execute("CREATE TABLE countries (id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL, flag l
	  
for country in countries:
        c.execute("INSERT INTO countries (name, flag,subregion, population) VALUES ('{name}
        conn.commit()
		  
conn.close()


