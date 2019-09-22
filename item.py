class item():
    def __init__(self):
        self.damage = 0
        self.lvl = 0
        self.worth = 0

    def load_item(self, **kwargs):
        for i in kwargs:
            print(i)


Hand = item()
Hand.load_item(damage=10, lvl=10, worth=10)
print(Hand.damage)
