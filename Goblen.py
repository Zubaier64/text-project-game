from Enemy import Enemy

class Goblin (Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Goblin"
        self.drops = ["Club", "Cloth", "Shield"]

        self.set_stats()

    def set_stats(self):
        self.HP = round(self.base_HP * self.level * 1.1, 1)
        self.ATK = round(self.base_ATK * self.level * 1.1, 1)
        self.DEF = round(self.base_DEF * self.level * 1.1, 1)