from Manager import Manager
from Player import *
from Menu import *
from Battle import *
from Spawner import *

def get_player_name() -> str:
    result = ""
    while True:
        result = input("Enter your Player Name: ")
        if result == "" or result == " ":
            print("CAN NOT DO THIS")
            continue
        break
    return result

def main():
    player = Player("Zubair")  # get_player_name())
    menu = Menu()
    battle = Battle()
    spawner = Spawner()
    manager = Manager(player, menu, battle, spawner)

if __name__ == '__main__':
    main()
