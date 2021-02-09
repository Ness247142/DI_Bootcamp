# #Exercise 1
# Python has many built-in functions, and if you do not know how to use it, you can read document online. 
# But Python has a built-in document function for every built-in functions.

# Write a program to print some Python built-in functions documents, such as abs(), int(), raw_input().
# And add documentation for your own function

print (abs.__doc__)

def abs(number):
    """The abs() method returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude."""
    pass
print('')


print (int.__doc__)

def int(integer):
    """The int() method returns an integer object from any number or string."""
    pass
print('')


print(raw_input.__doc__)

def raw_input(values):
    """raw_input function is used to get the values from the user. We call this function to tell the program to stop and wait for the user to input the values."""
    pass
print('')



#Exercise 2

class Currency:
    def __init__(self, currency, value):
        self.value = value
        if self.value > 1:
            self.currency = currency + "x"
        else: 
            self.currency = currency

    
    def __str__(self):
        return f"{self.value} {self.currency}"

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"{self.value} {self.currency}"

    def __add__(self, other):
        if type(other) == int:
            return self.value + other
        elif self.currency == other.currency:
                return self.value + other.value
        else:
            print(f"TypeError: Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self, other):
        if type(other) == int:
            self.value = self.value + other
            return self
        elif self.currency == other.currency:
            self.value = self.value + other.value
            return self
        else:
            print(f"TypeError: Cannot add between Currency type <{self.currency}> and <{other.currency}>")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)



# Exercise 3:
# Create a function that displays the amount of time left from now until January 1st. 
# (Example: the 1st January is in 10 days and 10:34:01hours)

from datetime import date, timedelta, datetime

dt = date.today() - timedelta(325)
print("Today's Date : ", date.today())

import datetime

def january():
    print(f"January 1st is in {datetime.datetime(2022, 1, 1) - datetime.datetime.today().replace()}")

print(january())



# Exercise 4:
# Write a function that display today’s date, the amount of time left from now until the next holiday, additionally print what holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours)
# Hint: Start with hardcoding the datetime and name of the holiday

from datetime import date, timedelta, datetime

dt = date.today() + timedelta(16)
print("Today's Date : ",date.today())

import datetime

def next_holiday():
    print(f"The next holiday in Israel, Purim, is in {datetime.datetime(2021, 2, 25)-datetime.datetime.today().replace()}")
    
next_holiday()



# Exercise 5:
# Create a function that accepts a birthdate as an argument (in the format of your choice), and then display to the user the number of minutes he lived in his life.

from datetime import datetime

birdthay_input = input("Give me your birthdate in the format YYYY/MM/DD: ")

def age_minutes(birthdate):
    birth = datetime.strptime(birthdate, "%Y/%m/%d")
    today_date = datetime.now()
    minutes = today_date - birth
    print(f"You are {minutes} minutes old")

print(age_minutes(birdthay_input))



# Exercise 6 : How Old Are You In Jupiter ?
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you were told someone were 1,000,000,000 seconds old, you should be able to say that they’re 31.69 Earth-years old.

def earth_age(seconds):
    minute = seconds/60
    hour = minute/60
    day = hour/24
    earth_year = day/365.25

    mercury_year = earth_year/0.2408467
    venus_year = earth_year/0.61519726
    mars_year = earth_year/1.8808158
    jupiter_year = earth_year/11.862615
    saturn_year = earth_year/29.447498
    uranus_year = earth_year/84.016846
    neptune_year = earth_year/164.79132
    
    print(f"You are {earth_year} Earth years old")
    print(f"On Mercury, you are {mercury_year} Earth years old") 
    print(f"On Venus, you are {venus_year} Earth years old")
    print(f"On Mars, you are {mars_year} Earth years old")
    print(f"On Jupiter, you are {jupiter_year} Earth years old")
    print(f"On Saturn, you are {saturn_year} Earth years old")
    print(f"On Uranus, you are {uranus_year} Earth years old") 
    print(f"on Neptune, you are {neptune_year} Earth years old")

print(earth_age(1000000000))



# Exercise 7 : Faker Module
# Install the faker module, and read the documentation.
# Create an empty list called users. Tip: It’s a list of dictionaries
# Create a function that adds dictionaries to the users list. Each user has the properties: name, adress, langage_spoken. Use faker to populate them with fake data.

from faker import Faker

faker = Faker()

users = []
users_dict = {}

def faker_module(quantity):

    for _ in range(quantity):
        users_dict["name"] = faker.name()
        users_dict["email"] = faker.email()
        users_dict["adress"] = faker.address()
        users.append(users_dict)

    print(users)
        
print(faker_module())

