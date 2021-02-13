import random
import os
import time

win_count = 0
lose_count = 0
tie_count = 0

def clear():
    os.system("clear")
 
def game_instructions():
 
    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()
 
 
def game():
     
    global rps_table
    global game_map
    global name
 
    # Game Loop for each game of Rock-Paper-Scissors
    while True:
 
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\",\"Paper\",\"Scissors\" to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
 
        print()
 
        # Player Input
        inp = input("Enter your move : ")
 
        if inp.lower() == "help":
            clear()
            game_instructions()
            continue
        elif inp.lower() == "exit":
            clear()
            break  
        elif inp.lower() == "rock":
            player_move = 0
        elif inp.lower() == "paper":
            player_move = 1    
        elif inp.lower() == "scissors":
            player_move = 2
        else:
            clear()
            print("Wrong Input!!")
            game_instructions()  
            continue
 
        print("Computer making a move....")
 
        print()
        time.sleep(2)
 
        # Get the computer move randomly
        comp_move = random.randint(0, 2)
 
        # Print the computer move
        print("Computer chooses ", game_map[comp_move].upper())
 
        # Find the winner of the match
        winner = rps_table[player_move][comp_move]
        
        # Declare the winner 
        if winner == player_move:
            print(name, "WINS!! THE COMPUTER LOSES!!")
        elif winner == comp_move:
            print("THE COMPUTER WINS!! YOU LOSE!!")
        else:
            print("IT'S A DRAW!! WANNA PLAIN AGAIN?")

        print()
        time.sleep(2)
        clear()
 
# The main function
if __name__ == '__main__':
 
    # The mapping between moves and numbers
    game_map = {0:"rock", 1:"paper", 2:"scissors"}
 
    # Win-lose matrix for traditional game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
 
     
    name = input("Enter your name: ")
 
    # The GAME LOOP
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
 
        # Play the game
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
 
