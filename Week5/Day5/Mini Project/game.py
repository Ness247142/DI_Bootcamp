import random
import os
import time

def clear():
    os.system("clear")

class Game:
    def __init__(self):
        self.results = {
            "win": 0,
            "loss": 0,
            "draw": 0
        }

    
    def get_user_item(self):
        user_item = input("Choose (r) for Rock, (p) for Paper or (s) for Scissors: ")
        while user_item not in ("r", "p", "s"):
            user_item = input("Choose (r) for Rock, (p) for Paper or (s) for Scissors: ")
        return user_item
        time.sleep(2)


    def get_computer_item(self):
        item_list = ["r", "p", "s"]
        computer_item = random.choice(item_list)
        return computer_item
        time.sleep(2)


    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            print(f"Both you and the computer chose {user_item}. It's a draw!")
            return "draw"
        
        elif user_item == "r":
            if computer_item == "p":
                print(f"You chose {user_item} and the computer chose {computer_item}. You lost")
                return "loss"
            else:
                print(f"You chose {user_item} and the computer chose {computer_item}. You won")
                return "win"
        
        elif user_item == "p":
            if computer_item == "s":
                print(f"You chose {user_item} and the computer chose {computer_item}. You lost")
                return "loss"
            else:
                print(f"You chose {user_item} and the computer chose {computer_item}. You won")
                return "win"

        else:
            if computer_item == "r":
                print(f"You chose {user_item} and the computer chose {computer_item}. You lost")
                return "loss"
            else:
                print(f"You chose {user_item} and the computer chose {computer_item}. You won")
                return "win"
        time.sleep(2)
        clear()


    def play(self):

        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        if result == "win":
            self.results["win"] += 1
        elif result == "loss":
            self.results["loss"] += 1
        else:
            self.results["draw"] += 1
        return self.results
        time.sleep(2)
        clear()
