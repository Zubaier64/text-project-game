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
                print("\tBATTLE BEGIN")
                while True:
                    action = self.menu.take_final_action()
                    if action == "1":
                        player_damage = self.calculate_damage(player, enemy)
                        print(f"{player.name} attacked {enemy.name}")
                        print(f"{player.name} dealt {player_damage} damage to {enemy.name}")
                        enemy.HP -= float(player_damage)

                        if enemy.HP <= 0:
                            print(f"\t{enemy.name} defeated, {player.name} wins!")
                            break
                        print(f"{enemy.name}'s HP = {round(enemy.HP, 1)}")

                        enemy_damage = self.calculate_damage(enemy, player)
                        print(f"{enemy.name} attacked you and delt {enemy_damage} damage")
                        player.HP -= float(enemy_damage)

                        if player.HP <= 0:
                            print(f"\t{player.name} defeated, {enemy.name} wins!")
                            break
                        print(f"{player.name}'s HP = {round(player.HP, 1)}")
                        print("")

            if action == "2":
                print("you fled")
                break
            break


    def calculate_damage(self, attacker, defender) -> str:
        self.foo = False
        damage = round((attacker.ATK/(defender.DEF*0.1)), 1)
        return str(damage)