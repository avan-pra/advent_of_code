symbols = {
    ']': '[',
    ')': '(',
    '}': '{',
    '>': '<'
}

value = {
    '[': 2,
    '(': 1,
    '{': 3,
    '<': 4
}

def get_validity(inp: list):
    mylist = []
    
    for c in inp:
        if c == '[' or c == '(' or c == '{' or c == '<':
            mylist.append(c)
        else:
            if mylist.pop() != symbols[c]:
                return 1
    return 0

def autocomplete(inp: list):
    mylist = []
    score = 0

    for c in inp:
        if c == '[' or c == '(' or c == '{' or c == '<':
            mylist.append(c)
        else:
            if mylist.pop() != symbols[c]:
                print('BIG ERROR')

    while len(mylist) != 0:
        score = (score * 5) + value[mylist.pop()]
    
    return score

fd = open('./data', 'r')

points = []

for line in fd.readlines():
    inp = [c for c in line.strip('\n')]
    if (get_validity(inp) == 0):
        points.append(autocomplete(inp))

import math

points.sort()
# print(points)
print(points[math.floor(len(points) / 2)])