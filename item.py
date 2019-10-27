class Item():
    def __init__(self):
        self.damage = 0
        self.lvl = 0
        self.worth = 0
        self.name = ""

    def load_item(self, item_dict):
        for i in item_dict:
            value = item_dict[i]
            if i == "damage":
                self.damage = value
            if i == "lvl":
                self.lvl = value
            if i == "worth":
                self.worth = value
            if i == "name":
                self.name = value
