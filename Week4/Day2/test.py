>>> text = "testing"
>>> text[2:5]
'sti'
>>> text = "this is a test sentence"
>>> text[10:14]
'test'
>>> text[::2]
'ti sats etne'
>>> test = "123456789"
>>> test[1::2]
'2468'
>>> test[0::2]
'13579'


#<name>@gmail.com
email = "bob@gmail.com"
		"jonathan@gmail.com"
# Hi <name>

print("Hi", email[:-10])

print (text.split('@')[0])

>>> email = "bob@gmail.com"
 
>>> print("Hi", email[0:-10])
Hi bob
>>> result = email.split("@")
>>> result
['bob', 'gmail.com']
>>> type(result)
class 'list'
 

>>> my_hobbies = ["Eat", "Sleep", "Code"]
>>> my_hobbies[1]
'Sleep'
>>> my_hobbies[2]
'Code'
>>> x = 1
>>> my_hobbies[2] = "Cats"
>>> my_hobbies
['Eat', 'Sleep', 'Cats']
>>> my_hobbies[-1]
'Cats'
>>> my_hobbies[::2]
['Eat', 'Cats']


>>> my_hobbies.append("Coffee")
>>> my_hobbies
['Eat', 'Sleep', 'Cats', 'Coffee']

>>> my_hobbies.remove("Sleep")
>>> my_hobbies
['Eat', 'Cats', 'Coffee']

>>> my_hobbies.pop()
'Coffee'
>>> my_hobbies
['Eat', 'Cats']

>>> item = my_hobbies.pop(1)
>>> my_hobbies
['Eat']
>>> item
'Cats'

>>> your_hobbies = ["Fishing", "Cooking", "Cleaning"]
>>> my_hobbies + your_hobbies
['Eat', 'Fishing', 'Cooking', 'Cleaning']

>>> len(your_hobbies)
3

>>> numbers = [1,2,4,6,99]
>>> numbers
[1, 2, 4, 6, 99]
>>> sum(numbers)
112
>>> numbers = [66,4,-12,12,1,50,0]
>>> numbers
[66, 4, -12, 12, 1, 50, 0]
>>> sorted(numbers)
[-12, 0, 1, 4, 12, 50, 66]

>>> numbers
[66, 4, -12, 12, 1, 50, 0]
>>> ordered_numbers = sorted(numbers)
>>> numbers
[66, 4, -12, 12, 1, 50, 0]
>>> ordered_numbers
[-12, 0, 1, 4, 12, 50, 66]

>>> numbers
[66, 4, -12, 12, 1, 50, 0]
>>> numbers.sort()
>>> numbers
[-12, 0, 1, 4, 12, 50, 66]

>>> names = ["Xavier", "Jon", "Zoey", "Adam"]
>>> names
['Xavier', 'Jon', 'Zoey', 'Adam']
>>> names.sort()
>>> names
['Adam', 'Jon', 'Xavier', 'Zoey']

>>> numbers
[-12, 0, 1, 4, 12, 50, 66]
 new_numbers = numbers.sort()
>>> new_numbers
>>> 

>>> letters = ["A", "B", "D", "E"]
>>> letters.insert(2, "C")
>>> letters
['A', 'B', 'C', 'D', 'E']

>>> my_hobbies.extend(your_hobbies)
>>> my_hobbies
['Eat', 'Fishing', 'Cooking', 'Cleaning']

>>> names
['Adam', 'Jon', 'Xavier', 'Zoey']
>>> names.append("Fred")
>>> names
['Adam', 'Jon', 'Xavier', 'Zoey', 'Fred']
>>> names.insert(1, "Bob")
>>> names
['Adam', 'Bob', 'Jon', 'Xavier', 'Zoey', 'Fred']
>>> person = names.pop()
>>> names
['Adam', 'Bob', 'Jon', 'Xavier', 'Zoey']
>>> person
'Fred'
>>> person = names.pop(-1)
>>> person
'Zoey'


>>> myset = {"A", "B", "C"}
>>> myset
{'C', 'B', 'A'}
# SETS ARE NOT ORDERED!!
# SETS CANNOT CONTAIN DUPLICATES!

>>> myset = {"A", "B", "C", "A", "C"}
>>> myset
{'C', 'B', 'A'}

# list.append() adds to the end

# cannot do 
# set.append... because there is no end..

Can do
set.add()

create a list of email adresses.
list must contain duplicates
now cast the list to a set to remove duplicates


list_emails = ["bob@gmail.com","jonathan@gmail.com","bob@gmail.com", "jonathan@gmail.com", "levy@gmail.com"]

>>> newmail = set(list_emails)
>>> newmail
{'bob@gmail.com', 'jonathan@gmail.com', 'levy@gmail.com'}


mylist = ["a", "b", "c", "d", "e"]

mylist[::-1]
['e', 'd', 'c', 'b', 'a']


STRINGS ARE IMMUTABLE


TUPPLES CANNOT BE CHANGED!
my_tuple = [5, 6, 7]

my_tuple[0]
5

my_tuple[2]
7

my_tuple.index(7)

my_tuple


list1 = ["A", "B", "C"]
list1[0] = "Z"

list1 = ["Z", "B", "C"]

list1 = ["x", "y", "z"]
REASSIGN THE LIST

lis2 = list1

list1[0] = "A"

list2 = ["x", "y", "z"]

list1 = ["A", "B"; "C"]


list_of_names = ["Adam", "Bob", "Charlie", "Dave"]
for name in list_of_names:
	print(name)

for name in list_of_names:
	if name == "Bob":
		print("Robert")
	else:
		print(name)

for i in range(10):
	for j in range(10):
		if j == 1:
			print("match")
		else:
			print(i, " "; j)


for i in range(10):
	print(i)

for i in range(1,11,2):
	print(i)

for i in range(10,0, -1):
	print(i)


num = 0
while num < 10:
	print(num)
	num += 1

