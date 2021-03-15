import numpy as np
banks = {}
active_banks = {}
countBank, countShots = map(int, input().split())
for i in range(countBank):
    banks[i] = np.array(input().split(), int)
    active_banks[i] = 1
result = np.array([-1]*countShots)
for j in range(countShots):
    pos = np.array(input().split(), int)
    for bank in banks:
        if active_banks[bank] == 1:
            if banks[bank][0] <= pos[0] <= banks[bank][2] and banks[bank][1] <= pos[1] <= banks[bank][3]:
                result[j] = bank + 1
                active_banks[bank] = 0
print(' '.join(map(str, result)))

# 4 10
# 0 0 1 1
# 2 3 3 8
# 15 15 20 20
# 10 12 12 13
# 2 2
# 0 -1
# 23 18
# 13 12
# 10 13
# 16 16
# 17 17
# 3 5
# 3 5
# 3 3
# -1 -1 -1 -1 4 3 -1 2 -1 -1