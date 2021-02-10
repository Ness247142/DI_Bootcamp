

Python File I/0

#Old way of creating a file from the Terminal
f = open('blah.txt', 'w')
f.write("Hello")
f.close()


#New way of creating a file with Python from the Terminal
with open("blah.txt", "w") as f: # "Write the word 'Hello" in a new file
	f.write("Hello\n")

with open("blah.txt", "a") as f: # Append the word 'Goodbye' to the file 'blah.txt'
	f.write("Goodbye")

with open("blah.txt", "r") as f: # "Read the entire file
	data = f.readlines()
print(data)


# 'w' -> write
# 'r' -> read
# 'a' -> append
# 'w+' -> write + read
# 'a+' -> append + read


# Writing...
# 'f.write()' -> Writes a string to the file
# 'f.writelines()' -> Writes a list to the file, line by line


# Reading
# 'f.read()' -> Reads the entire file into a single string
# 'f.readline()' -> reads a single line
# 'f.readlines()' -> Reads the entire file into a list of strings

with open("email.txt", "w") as f:
	f.write("adam@gmail.com\n")
	f.write("bob@hotmail.com\n")

with open("email.txt", "a") as f: 
	f.write("charlie@yahoo.com")

with open("email.txt", "r") as f:
	print(f.seek(5))
	data = f.readlines()
	print(f.tell())

for person in data:
	person = person.strip('\n')
	print(f"Sending email to {person}")





JSON
JavaScript Object Notation

class User:

	name
	surname
	email
	accounts = []
	something = {}
	family =[User, User, User]


import json

load 	#read json from a file and convert it to Python 
loads S string 	# convert a json string to Python

dump 	# convert from Python to json and write to file
dumps	# Convert from Python to a json string


thing = [
	{
	'name' : 'Bob',
	'age' : 55,
	'stuff' : True
	},
{
	'nums': [1,2,3],
	'letters': ['a', 'b', 'c']
	},
]


with open('jfile.txt', 'w') as f:
	json.dump(thing, f)

with open('jfile.txt', 'r') as f:
	thing2 = json.load(f)


# JavaScript in the browser
# "user = {
# 	"name": "bob",
# 	"accounts" : ["thing1", "thing2"]
# }"


# XML
# <User>
# 	<name>Bob</name>
# 	<account>
# 		<0>item</0>
# 	</accounts>
# <User>




HTTP
HyperText Transfer Protocol(secure)

# ping google.com -> IP Address of Google. Tip in the Terminal

HTTP Responses

100s
Information Response

200s
Sucess
Things are working

300s
Redirection
Something moved somewhere else

400s
Client Errors
Something in your browser or your code went wrong

500s
Server Errors
Something in our browser or code went wrong


import requests
import json

response = requests.get("https://www.google.com/search?ei=M7QjYOa9E-2CjLsPy6-tsAs&q=sloths&oq=sloths&gs_lcp=CgZwc3ktYWIQAzIHCC4QQxCTAjICCAAyBQgAEMkDMgIIADICCAAyAggAMgQIABAKMgIIADICCAAyAggAOgoILhCwAxBDEJMCOgcIABCwAxBDOg0ILhDHARCjAhCwAxBDOgcILhCwAxBDOgQILhBDOggILhDHARCjAjoECAAQQzoICC4QxwEQrwE6AgguUKDaBVjG4QVgveMFaANwAngAgAGLA4gB0AqSAQcyLjIuMi4xmAEAoAEBqgEHZ3dzLXdpesgBCsABAQ&sclient=psy-ab&ved=0ahUKEwimo5DjjN_uAhVtAWMBHctXC7YQ4dUDCA0&uact=5")

response.json()

with open('sloths.html', 'w') as f:
	f.write(response.text)

for _ in range(10):
    resp = requests.get("http://api.open-notify.org/iss-now")
    data = resp.json()
    print(data['iss_position']['latitude'], data['iss_position']['longitude'])
    time.sleep(1)


