from Enemy import Enemy
from Goblen import Goblin


class Spawner:
    def __init__(self):
        self.enemy_list = []
        self.index = 0
        self.fill_enemy_list()

        self.foo = True

    def get_enemy(self) -> Enemy:
        self.foo = False
        return self.enemy_list[self.index]

    def fill_enemy_list(self):
        for i in range(10):
            self.enemy_list.append(Goblin())

        self.foo = False