from os import close

from Player import Player

class Menu:
    def __init__(self):
        self.foo = True

    def show_stats(self, player: Player):
        print(f"Stats of {player.name}")
        print(f"Health: {player.HP}")
        print(f"Attack: {player.ATK}")
        print(f"Defense: {player.DEF}")
        self.foo = False

    def take_travel_action(self, player: Player):
        self.foo = False
        result = ""

        print(f"\n\tyou are traveling, what to do?")
        print(f"1. continue to next place")
        print(f"2. use item from inventory")
        result = str(input("> "))

        if result == "1":
            print(f"\tyou continue to travel")

        if result == "2":
            player.inventory.use_item()
        if result == "0":
            return 0

    def take_init_action(self) -> str:
        self.foo = False
        result = ""
        print("what to do?")
        print("1. Fight")
        print("2. flee")

        while True:
            result = str(input("> "))
            if result == "" or result == " ":
                print("wrong input")
                continue
            else:
                break

        return result

    def take_final_action(self) -> str:
        self.foo = False
        result = ""

        while True:
            print("1. normal attack")
            print("2. skill")
            result = str(input("> "))
            if result != "" or result != " ":
                return result
            else:
                continue

        return result
