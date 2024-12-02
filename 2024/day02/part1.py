from typing import List

def verify(entry: List[int]) -> bool:
    f = lambda a, b : abs(a - b) > 3
    if entry[0] - entry[1] < 0:
        for i in range(len(entry) - 1):
            if entry[i] - entry[i+1] >= 0 or f(entry[i], entry[i+1]):
                return False
    else:
        for i in range(len(entry) - 1):
            if entry[i] - entry[i+1] <= 0 or f(entry[i], entry[i+1]):
                return False
    return True


data = []

for line in open('./input').readlines():
    data.append([int(x) for x in line.split(' ')])

total = 0
for entry in data:
    total += int(verify(entry))
print(total)
