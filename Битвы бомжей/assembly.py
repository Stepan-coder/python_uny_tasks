import random
from class_person import *
from class_weapon import *



def get_weapons_list():
    weapons = []
    print("Создаётся оружие...")
    weapons.append(Weapon(name="рука", range_from=0, range_to=2, weight=1, damage=1, precission=0.9, count= 100))
    weapons.append(Weapon(name="ножик", range_from=0, range_to=2, weight=1, damage=5, precission=0.8, count= 20))
    weapons.append(Weapon(name="меч", range_from=2, range_to=6, weight=5, damage=10, precission=0.7, count= 5))
    weapons.append(Weapon(name="топор", range_from=2, range_to=6, weight=5, damage=15, precission=0.6, count= 5))
    weapons.append(Weapon(name="палка", range_from=6, range_to=10, weight=5, damage=3, precission=0.5, count= 10))
    weapons.append(Weapon(name="нунчаки", range_from=6, range_to=10, weight=5, damage=4, precission=0.4, count= 10))
    weapons.append(Weapon(name="камень", range_from=10, range_to=30, weight=5, damage=7, precission=0.3, count= 5))
    weapons.append(Weapon(name="копьё", range_from=30, range_to=60, weight=6, damage=5, precission=0.2, count= 3))
    weapons.append(Weapon(name="лук", range_from=30, range_to=60, weight=3, damage=3, precission=0.1, count= 15))
    for w in weapons:
        w.print_weapon()
    return weapons


def get_weapon_set_for_one_peple(weapons, set_count):
    return random.choices(population=weapons, k=3)


def creare_fighter(index, name, weapon, count_weapon, armor, luck, start_position):
    print("Создаётся боец: {0}".format(name))
    weapon = get_weapon_set_for_one_peple(weapon, count_weapon)
    person = Person(index=index, name=name, weapon=weapon, armor=armor, health=100, luck=luck, start_position=start_position)
    return person

def preparation_for_battle():
    weapons = get_weapons_list()
    fighter1 = creare_fighter(index=0, name='Poopa', weapon= weapons, count_weapon=3, armor=0, luck=1, start_position= -100)
    fighter1.print_person()
    fighter2 = creare_fighter(index=1, name='Loopa', weapon=weapons, count_weapon=3, armor=0, luck=1, start_position= -100)
    fighter2.print_person()
    return fighter1, fighter2


