from warnings import catch_warnings


class Inventory:
    def __init__(self):
        self.foo = False
        self.inv = []

    def show(self):
        print(self.inv)

    def add_item(self, item):
        self.inv.append(item)

    def remove_item(self, item):
        try:
            self.inv.remove(item)
            print(f"{item} have been removed from your Inventory")
        except NameError:
            print("Invalid item input")

    def use_item(self):
        self.foo = False
        print(f"\twhat to use?")
        print(self.inv)

        while True:
            inpt = str(input("> "))
            if inpt not in self.inv:
                print("you dont have this item")
                continue
            else:
                break
        print(f"you used {inpt}")
        self.remove_item(inpt)