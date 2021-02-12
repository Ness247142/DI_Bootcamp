

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


import game

def get_user_menu_choice():
	while True:
 
        # The Game Menu
        print()
        print("Let's Play!!!")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to quit")
        print()

        # Try block to handle the player choice 
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong Choice")   
            continue
 
def  main():
	if choice == 1:
		print(f"Your record is {win_count}-{lose_count}-{tie_count}")
		game()
 
        # Quit the GAME LOOP    
    elif choice == 2:
    	print(f"Thanks for playing! Your final record was {win_count}-{lose_count}-{tie_count}")
    	break
 
        # Other wrong input
    else:
    	clear()
    	print("Wrong choice. Read instructions carefully.")


# The main function
if __name__ == '__main__':
 
    # The mapping between moves and numbers
    game_map = {0:"rock", 1:"paper", 2:"scissors"}
 
    # Win-lose matrix for traditional game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
 
     
    name = input("Enter your name: ")
 