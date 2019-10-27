import math

def calc_level(xp):
    level = int((1+math.sqrt(1+16*xp/50))/2)
    return level
