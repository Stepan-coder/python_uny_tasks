def read_from_file():
    with open("pyramid.txt", "r", encoding="utf8") as file:
        text = file.readlines()
    clean_text = []
    for t in text:
        clean_text.append(t.strip())
    return clean_text



def split_strings_to_2D(text):
    array = []
    array.clear()
    for s in text:
        string_nums = []
        for n in s.split(' '):
            if n.isdigit():
                string_nums.append(int(n))
        array.append(string_nums)
    return array


def get_array():
    text = read_from_file()
    array = split_strings_to_2D(text)
    return array


def solve():
    array = get_array()
    for row in range(len(array) - 1, 0, -1):
        for col in range(0, row):
            array[row - 1][col] += max(array[row][col], array[row][col + 1])
    return array[0][0]

print(solve())

