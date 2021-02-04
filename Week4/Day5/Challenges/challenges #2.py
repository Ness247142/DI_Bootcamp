# Exercise 1
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["tuna", "ham", "chicken", "cheese", "beef"]
finished_sandwiches =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich ")
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich + " is done ")

# Exercise 2
# Using the list sandwich_orders from Exercise 1, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["pastrami", "tuna", "ham", "chicken", "cheese", "beef", "pastrami", "pastrami"]
finished_sandwiches =[]

print("The deli has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made a " + current_sandwich + " sandwich ")
    finished_sandwiches.append(current_sandwich)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + " sandwich " + " is done")


# Exercise 3
# Draw the following patterns using for loops

#Pattern 1
size = 3
m = size - 1
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 
    for j in range(0, i + 1 ):
        print("*", end=' ')
    print(" ")


# Pattern 2
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")


# Pattern 3
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")



# Exercise 4
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

my_list = [2, 24, 12, 354, 233] # Create a list of numbers
for i in range(len(my_list) - 1): # Create a For Loop to check the length of 'my_list', we are counting every number within 'my_list' with a step of '-1'.
    minimum = i # The variable 'minimum' is given the value 'i' 
    for j in range(i + 1, len(my_list)): # Create a For Loop to count every number within 'my_list' starting with the variable 'i' + 1 unit
        if(my_list[j] < my_list[minimum]): # An IF conditional for if my mist
            minimum = j # The variable 'minimum' is given the value of 'j' in the conditional
            if(minimum != i): # Another IF conditional: if 'minimum' is not equal to 'i'
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # then all the values inside 'my_list' are changed bewteen 'i' and 'minimum'
print(my_list) # Call the function

The final output is : [2, 12, 24, 233, 354]

# The purpose of this code was to sort the numbers from the lowest to the highest
