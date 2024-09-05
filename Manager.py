
from Player import Player
from Menu import Menu
from Battle import Battle
from Spawner import Spawner

class Manager:
    def __init__(self, player: Player, menu: Menu, battle: Battle, spawner: Spawner):
        self.player = player
        self.menu = menu
        self.battle = battle
        self.spawner = spawner

        menu.show_stats(self.player)
        battle.begin_battle(self.player, self.spawner.get_enemy())
        pass

