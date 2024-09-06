class Enemy:
    def __init__(self):
        self.name = "Not set"
        self.base_HP = 20
        self.HP = 0
        self.base_ATK = 5
        self.ATK = 0
        self.DEF = 0
        self.base_DEF = 10
        self.level: int = 1
        self.foo = True
        self.drops = []

    def get_drops(self) -> []:
        self.foo = False
        return self.drops
    def set_stats(self):
        pass
