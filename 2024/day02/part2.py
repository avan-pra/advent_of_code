from typing import List

def verify(entry: List[int]) -> bool:
    if (entry == sorted(entry) or entry == sorted(entry, reverse=True)) and all(1<=abs(entry[k]-entry[k+1])<=3 for k in range(len(entry)-1)):
        return True
    return False

data = []

for line in open('./input').readlines():
    data.append([int(x) for x in line.split(' ')])

total = 0
for entry in data:
    for i in range(len(entry)):
        c = entry.copy()
        c.pop(i)
        if verify(c):
            print(entry)
            total += 1
            break
print(total)
