
from random import randint
import sys

answer = randint(1, 10)

while True:
	try:
		print(answer)
		guess = int(input('guess a number between 1 and 10:  '))
		if 0 < guess < 11:
			if guess == answer:
				print('You are a genius')
			break
		else:
			print('I said 1 to 10')
	except ValueError:
		print('Please enter a number')
		continue