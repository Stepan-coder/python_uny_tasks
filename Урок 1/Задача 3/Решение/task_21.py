def have_dividers(num):
    s = []
    for f in range(1, int(num)):
        if num % f == 0:
            s.append(f)
    return s

def get_summ(s):
    summ = 0
    for f in s:
        summ += int(f)
    return summ


def write_to_file(text):
    with open("Already_Solve.txt", "w", encoding="utf8") as file:
        for f in text:
            file.write(f + '\n')

def solve(N):
    summ = 0
    chek_text = []
    for f in range(1,N,1):
        summN = get_summ(have_dividers(f))
        frend = get_summ(have_dividers(summN))
        if frend == f:
            summ += f
            chek_text.append(str(f) + " " + str(summN))
            print(f)
    chek_text.append(str("Всего: ") + str(summ))
    write_to_file(chek_text)

solve(10000)
# Ответ
# 6 6
# 28 28
# 220 284
# 284 220
# 496 496
# 1184 1210
# 1210 1184
# 2620 2924
# 2924 2620
# 5020 5564
# 5564 5020
# 6232 6368
# 6368 6232
# 8128 8128
# Всего: 40284
