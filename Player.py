from Inventory import Inventory

class Player:
    def __init__(self, name: str):
        self.inventory = Inventory()
        self.inventory.add_item("Potion")

        if name == "" or name == " ":
            print("cant set name as blank!")
        else:
            self.name: str = name
            print(f"your name is {name}")
        self.base_HP = 25
        self.HP= None
        self.base_ATK = 7
        self.ATK = None
        self.DEF = None
        self.base_DEF = 12
        self.level: int = 1

        self.set_stats()

    def set_stats(self):
        self.HP = round(self.base_HP * self.level * 1.2, 1)
        self.ATK = round(self.base_ATK * self.level * 1.2, 1)
        self.DEF = round(self.base_DEF * self.level * 1.2, 1)

