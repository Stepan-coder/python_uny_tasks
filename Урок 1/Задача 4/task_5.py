# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?
# 232792560 получившееся произведение

def megateli(N):
    resalt_deviders = []
    resalt_deviders.append(2)
    for n in range(2, N + 1,1):
        intermediate = n
        for f in resalt_deviders:
            if intermediate == 1:
                break
            if intermediate % f == 0:
                intermediate = int(intermediate / f)
        if intermediate != 1:
            resalt_deviders.append(intermediate)
    print(resalt_deviders)
    return  resalt_deviders

def product_num(megateli):
    product = 1
    for m in megateli:
        product = product*m
    return  product



print(product_num(megateli(20)))
