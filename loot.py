import random

from item import Item
from level import calc_level


def generate_weapon(xp):
    level = calc_level(xp)
    adjfile = open("adjectives", "r")
    adjlist = adjfile.readlines()
    adjfile.close()
    min_dam = int(10 + (level / 2))
    max_dam = int(30 + (level / 2))
    dam = random.randint(min_dam, max_dam)
    worth = random.randint(int(2 * dam + 2 * level), int(3 * dam + 3 * level))
    adj = random.choice(adjlist)
    name = adj + " Sword"
    item_dict = {"damage": dam,
                 "lvl": 0,
                 "worth": worth,
                 "name": name}

    weapon = Item()
    weapon.load_item(item_dict)
    return weapon
