import os
from assembly import *

def get_distance(fighter1, fighter2):
    fighter1_absolute = 0 - fighter1.position
    fighter2_absolute = 0 - fighter2.position
    return abs(fighter1_absolute + fighter2_absolute)

def game_engine(fighter1, fighter2):
    if fighter1.is_survive() and fighter2.is_survive():
        dist = get_distance(fighter1, fighter2)
        index = random.randint(0, 1)
        if index == 0:
            fighter1.action(dist, fighter2)
        else:
            fighter2.action(dist, fighter1)
        return True
    else:
        if fighter1.is_survive():
            print("Победил: {0}".format(fighter1.name))
        else:
            print("Победил: {0}".format(fighter2.name))
        return False


fighter1, fighter2 = preparation_for_battle()
while game_engine(fighter1, fighter2):
    a = 10
