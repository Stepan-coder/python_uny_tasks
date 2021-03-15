#Задача 1
Ocean = 1349000000 #объём мирового океана в кубических
inKM = 6 #в одном кубическом км воды 6 тонн золота
mas = Ocean*inKM #тонн золота в океане
p = 19.320 #плотность золота 19.3 тонны кубический метр
VinMeters = (mas/p) ** (1/3)
VinKM = VinMeters/1000
print(VinKM)

#Задача 2
power = 4;
mathtrue = 1024
mathfalse = 1000
disktrue = mathtrue ** power
diskfalse = mathfalse ** power
deltadisk = abs(disktrue - diskfalse)
error = deltadisk/(diskfalse/100)
print(error)

#Задача 3
#вес человека, его пол, количество выпитого алкоголя и количество часов, прошедших после этого события
mass = 80
gender = True #true - мучина, false - женщина
Alko = 100
hours = 1
if gender:
    r = 0.7
else:
    r = 0.6
c = Alko/(mass*r)
cTime = c - 0.15*hours
if cTime > 0.35:
    print("Нельзя")
else:
    print("Можно")

#Задача 4
menu = """
Croissant, jam & butter 3.00
Granola, yoghurt & honey 5.50
Homemade banana bread 4.00
Crashed eggs, chorizo & potatoes 11.50
Eggs royale, florentine or benedict 8.50
Morcilla with scrambled eggs on pugliese toast 7.65
Avocado, smoked salmon & poached egg 10.50
Gee’s breakfast 12.95
"""
course = 80.2
first_text = menu.split('\n')
text = []
for f in first_text:
    if f:
        text.append(f.strip())

for t in text:
    find_cost_index = int(t.rindex(' '))
    string = t[:find_cost_index + 1]
    cost_as_text = t[find_cost_index + 1:]
    cost = float(cost_as_text)
    new_cost = round(course*cost,2)
    new_string = string + str(new_cost) + ' ₽'
    print(new_string)
