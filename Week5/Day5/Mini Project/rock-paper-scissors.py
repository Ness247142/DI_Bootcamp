

# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

# get_game_result(self, user_item, computer_item) – Determine the result of the game.

# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss.
# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:

# Get the user’s item (rock/paper/scissors) and remember it
# Get a random item for the computer (rock/paper/scissors) and remember it
# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”
# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

import random
import os
import time

from game import Game
game = Game()

def clear():
    os.system("clear")

def get_user_menu_choice():
    print("Menu:")
    print("(y) Play at Rock-Paper-Scissors")
    print("(x) Show the final scores and leave")
    choice = str(input(": "))
    return choice
    time.sleep(2)
    clear()


def print_results(results):
    print("Here are the results:")
    for key, value in results.items():
        print(key,value)
    print("")
    time.sleep(2)
    clear()


def main():
    while True:
        menu = get_user_menu_choice()
        while menu not in ("y", "x"):
            menu = get_user_menu_choice()
        if menu == "y":
            results = game.play() 
        else:
            print_results(results)
            return False
        time.sleep(2)
        clear()

print(main())
