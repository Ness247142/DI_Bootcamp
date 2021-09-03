# Exercise 1
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

list = ["Hello World","Hello World","Hello World","Hello World", "I love python", "I love python", "I love python", "I love python"] 
for i in list:  
    print(i, end = " ")  


# Exercise 2
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month = input("Give me a month" )
day = int(input("Give me a day in this month" ))

if month in ("January", "February", "March"):
	season = "winter"
elif month in ("April", "May", "June"):
	season = "spring"
elif month in ("July", 'August', 'September'):
	season = "summer"
else:
	season = "autumn"

if (month == "March") and (day > 3):
	season = "spring"
elif (month == "June") and (day > 6):
	season = "summer"
elif (month == "September") and (day > 9):
	season = "autumn"
elif (month == "December") and (day > 12):
	season = "winter"

print("Season is",season)
