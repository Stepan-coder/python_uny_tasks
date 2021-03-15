
def have_dividers(num):
    # По умолчанию понятно что ЛЮБОЕ число делится на само себя и единицу
    # следоватнльно если есть хотябы ещё делитеь, то оно нам не подходит
    for f in range(2, int(num)):
        if num % f == 0:
            return False
    return True

def str_permutation(text):
    string = str(text)
    str_list = []
    for i in reversed(string):
        string = string[0:-1]
        string = i + string
        str_list.append(string)
    return str_list

# Для сохранения значений
def list_to_string(str_list):
    string = ""
    for t in str_list:
        string += t + " "
    return string

def write_to_file(text):
    with open("Already_Solve.txt", "w", encoding="utf8") as file:
        for f in text:
            file.write(f + '\n')
# Для сохранения значений

def solve(N):
    # для сохранения значений
    toWrite = []
    # для сохранения значений
    count_circle_nams = 0
    for i in range(2,N):
        value = str_permutation(i)
        isAdd = chek_combinations(value)
        if isAdd:
            toWrite.append(list_to_string(value)) # для сохранения значений
            print(i)
            count_circle_nams += 1
    # для сохранения значений
    count = list()
    count.append("Всего " + str(count_circle_nams))
    toWrite.append(str(count))
    write_to_file(toWrite)
    # для сохранения значений
    return count_circle_nams


def chek_combinations(str_list):
    chekSize = len(str_list)
    cheked = 0
    for f in str_list:
        if have_dividers(int(f)):
            cheked += 1
        else:
            return False
    if cheked == chekSize:
        return True
    else:
        return False

solve(100)

#Вывод программы
# 2
# 3
# 5
# 7
# 11 11
# 31 13
# 71 17
# 13 31
# 73 37
# 17 71
# 37 73
# 97 79
# 79 97
# 311 131 113
# 113 311 131
# 719 971 197
# 919 991 199
# 131 113 311
# 733 373 337
# 337 733 373
# 971 197 719
# 373 337 733
# 991 199 919
# 197 719 971
# 199 919 991
# 3119 9311 1931 1193
# 1193 3119 9311 1931
# 9311 1931 1193 3119
# 9377 7937 7793 3779
# 3779 9377 7937 7793
# 7793 3779 9377 7937
# 1931 1193 3119 9311
# 7937 7793 3779 9377
# 91193 39119 93911 19391 11939
# 11939 91193 39119 93911 19391
# 71993 37199 93719 99371 19937
# 93719 99371 19937 71993 37199
# 93911 19391 11939 91193 39119
# 37199 93719 99371 19937 71993
# 39119 93911 19391 11939 91193
# 99371 19937 71993 37199 93719
# 19391 11939 91193 39119 93911
# 19937 71993 37199 93719 99371
# 919393 391939 939193 393919 939391 193939
# 319993 331999 933199 993319 999331 199933
# 331999 933199 993319 999331 199933 319993
# 933199 993319 999331 199933 319993 331999
# 939193 393919 939391 193939 919393 391939
# 939391 193939 919393 391939 939193 393919
# 391939 939193 393919 939391 193939 919393
# 993319 999331 199933 319993 331999 933199
# 393919 939391 193939 919393 391939 939193
# 193939 919393 391939 939193 393919 939391
# 999331 199933 319993 331999 933199 993319
# 199933 319993 331999 933199 993319 999331
# ['Всего 56']