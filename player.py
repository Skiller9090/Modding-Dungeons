from inventory import inventory


class player():
    def __init__(self):
        self.Health = 100
        self.Gold = 0
        self.Armor_lvl = 0
        self.inv = inventory()
