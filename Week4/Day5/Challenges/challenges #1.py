# Exercise 1
# Write a script that inserts an item at a defined index in a list.

word = ['w', 'r', 'd']
word.insert(1, 'o')

print('Updated List: ', word)


# Exercise 2
# Write a script that counts the number of spaces in a string.

str=input("Give me a sentence: ")
spaces=0
for i in range(0,len(str)):
	if(str[i]==' '):
		spaces=spaces+1

print("The number of spaces is: ",spaces)


# Exercise 3
# Write a script that calculates the number of upper case letters and lower case letters in a string.

def string_0(numbers):
    cases={"UPPER_CASE":0, "LOWER_CASE":0}
    for number in numbers:
        if number.isupper():
           cases["UPPER_CASE"]+=1
        elif number.islower():
           cases["LOWER_CASE"]+=1
        else:
           pass
    print ("No. of Upper case characters : ", cases["UPPER_CASE"])
    print ("No. of Lower case Characters : ", cases["LOWER_CASE"])

print(string_0('Hello World of Python'))


#Exercise 4
def myMax(list1): 
	max = list1[0]
	for x in list1: 
	    if x > max : 
	        max = x 
	        return max

list1 = [50, 20, 1, 40, 100] 
print(max(list1)) 





