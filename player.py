from inventory import inventory
from item import item


class player():
    def __init__(self):
        self.Health = 100
        self.Gold = 0
        self.Armor_lvl = 0
        self.inv = inventory()
        Hand = item()
        Hand.load_item(damage=1, lvl=1, worth=0, name="hand")
        self.inv.add_item(Hand)
