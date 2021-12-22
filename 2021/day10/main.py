fd = open('./data', 'r')

points = 0

symbols = {
    ']': '[',
    ')': '(',
    '}': '{',
    '>': '<'
}

value = {
    ']': 57,
    ')': 3,
    '}': 1197,
    '>': 25137
}

def get_validity(inp: list):
    mylist = []
    
    for c in inp:
        if c == '[' or c == '(' or c == '{' or c == '<':
            mylist.append(c)
        else:
            if mylist.pop() != symbols[c]:
                return value[c]

    return 0


for line in fd.readlines():
    inp = [c for c in line.strip('\n')]
    points += get_validity(inp)

print(points)