import time
class Person():
    def __init__(self, index, name, weapon, armor, health, luck, start_position):
        self.insex = int(index)
        self.name = str(name)  # имя
        self.weapon = weapon  # оружие
        self.weapon_index = 0
        self.armor = int(armor)  # броня
        self.health = int(health)  # здоровье
        self.luck = float(luck)  # везение
        self.position = start_position

    def print_person(self):
        String_weapon = ''
        for w in self.weapon:
            String_weapon += w.name + ','
        print("Имя: {0}, Оружие: {1}, Броня: {2}, Здоровье: {3}, Везение: {4}, Начальная позиция: {5}".
              format(self.name, String_weapon, self.armor, self.health, self.luck, self.position))

    def move(self, count_steps, dist):
        self.position += count_steps
        time.sleep(0.05)
        print("Боец \"{0}\" переместился на \"{1}\" и теперь находится в \"{2}\", общее расстояние \"{3}\"".
              format(self.name, count_steps, self.position, dist-count_steps))

    def choose_weapon(self, distance_between):
        for w in range(len(self.weapon)):
            if self.can_attack_at_index(distance_between, w):
                self.weapon_index = w

    def attack(self):
        using_weapon = self.weapon[self.weapon_index]
        attack_damage = using_weapon.damage
        self.weapon[self.weapon_index].count -= 1
        print("Боец \"{0}\" использовал \"{1}\" и нанёс урон \"{2}\"".
              format(self.name, using_weapon.name, attack_damage))
        if self.weapon[self.weapon_index].count == 0:
            print("Оружие \"{0}\" закончилось".format(self.weapon[self.weapon_index].name))
        time.sleep(0.25)
        return attack_damage

    def can_attack(self, distance_between):
        using_weapon = self.weapon[self.weapon_index]
        return using_weapon.range_to > distance_between > using_weapon.range_from and using_weapon.count > 0


    def can_attack_at_index(self, distance_between, index):
        using_weapon = self.weapon[index]
        return using_weapon.range_to > distance_between > using_weapon.range_from and using_weapon.count > 0

    def action(self, dist, victim):
        self.choose_weapon(dist)
        if self.can_attack(dist):
            cause_damage = self.attack()
            victim.health -= cause_damage
        else:
            self.move(1, dist)

    def is_survive(self):
        return self.health > 0
