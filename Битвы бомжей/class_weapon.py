class Weapon():
    def __init__(self, name, range_from, range_to, weight, damage, precission, count):
        self.name = str(name) # название
        self.range_from = int(range_from) # дальность действия от
        self.range_to = int(range_to)  # дальность действия до
        self.weight = int(weight) # вес
        self.damage = int(damage) # урон
        self.precission = float(precission) # точность
        self.count = count

    def print_weapon(self):
        print("Название: {0}, Дальность действия: от {1} до {2}, Вес: {3}, Урон: {4}, Точность: {5}".
              format(self.name, self.range_from, self.range_to, self.weight, self.weight, self.damage, self.precission))

    def print_weapon_name(self):
        print(self.name)