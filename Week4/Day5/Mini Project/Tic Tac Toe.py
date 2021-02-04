
# FUNCTION for the Tic Tac Toe board
def display_board(values):
    print(" ")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print(" ")
 
# FUNCTION to see if any player won
def check_win(player_position, current_player):
 
    # All winning combinations
    combo = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # See if any combination is completed
    for x in combo:
        if all(y in player_position[current_player] for y in x):
             return True
    return False       
 
# FUNCTION to know if it's a draw
def player_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False       
 
# FUNCTION for a single game
def play(current_player):
 
    values = [' ' for x in range(9)]
     
    player_position = {'X':[], 'O':[]}
     
    # WHILE LOOP for 1 game
    while True:
        display_board(values)
         
        try:
            print(f"Player ", current_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print(f"Wrong! Give me a number from 1 to 9!")
            continue
 
        if move < 1 or move > 9:
            print(f"Wrong! Give me a number from 1 to 9!")
            continue
 
        if values[move-1] != ' ':
            print(f"Place already occupied. Try another one!")
            continue
 
 
        # Updating the status of the board 
        values[move-1] = current_player
 
        # Updating the players' positions
        player_position[current_player].append(move)
 
        # IF CONDITIONAL for a win
        if check_win(player_position, current_player):
            display_board(values)
            print(f"Player {current_player} won the game! Congratulation!")     
            print(" ")
            return current_player
 
        # IF CONDITIONAL for a draw game
        if player_draw(player_position):
            display_board(values)
            print(f"That's a draw. Wanna play again?")
            print(" ")
            return 'D'
 
        # Change the players' moves
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
 
if __name__ == "__main__":
 
    print("Player 1")
    player1 = input(f"Enter the first name: ")
    print(" ")
 
    print("Player 2")
    player2 = input(f"Enter the second name: ")
    print(" ")
     
    # Player 1 either chooses 'X' or 'O' at the start
    current_player = player1
 
    player_choice = {'X' : "", 'O' : ""}
 
    options = ['X', 'O']
 
    # WHILE LOOP for several games until the players quit
    while True:
 
        # Menu for the players' choices
        print(f"Turn to choose for", current_player)
        print(f"Enter 1 for X")
        print(f"Enter 2 for O")
        print(f"Enter 3 to Quit")
 
        try:
            choice = int(input())   
        except ValueError:
            print(f"Wrong! Give me a number!")
            continue
 
        # Players can choose either 'X' or 'O' before the start of the game
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print(f"See you! Come play again!")
            break  
 
        else:
            print(f"Wrong Choice!")
 
        winner = play(options[choice-1])
        
        # Switch the player who can choose either 'X' or 'O'
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1