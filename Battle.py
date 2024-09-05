from Player import *
from Enemy import *
from Menu import *

class Battle:
    def __init__(self):
        self.foo = True
        self.menu = Menu()

    def begin_battle(self, player: Player, enemy: Enemy):
        self.foo = False

        print(f"\n\tEnemy encounter {enemy.name}!")
        print(f"=============================")
        print(f"{enemy.name}'s stats:")
        print(f"Health: {enemy.HP}")
        print(f"Attack: {enemy.ATK}")
        print(f"Defense: {enemy.DEF}")

        while player.HP > 0 and enemy.HP > 0:
            action = self.menu.take_init_action()
            if action == "1":
                action = self.menu.take_final_action()

            else:
                print("you fled")
                break

