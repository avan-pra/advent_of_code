fd = open('./data', 'r')

inps = []
Matrix = [[0 for x in range(1000)] for y in range(1000)]

while True:
    line = fd.readline()
    line = line.strip('\n')
    if not line:
        break
    line = line.split('->')
    inps.append([line[0].split(','), line[1].split(',')])

for inp in inps:
    x = int(inp[0][0])
    y = int(inp[0][1])
    xend = int(inp[1][0])
    yend = int(inp[1][1])
    # swap if superior
    if (xend < x):
        tmp = xend
        xend = x
        x = tmp
    if (yend < y):
        tmp = yend
        yend = y
        y = tmp

    # print(x, xend, x == xend, type(x))
    if x == xend:
        while y <= yend:
            Matrix[x][y] += 1
            y += 1
    elif y == yend:
        while x <= xend:
            Matrix[x][y] += 1
            x += 1
    # elif :
    #     while x <= xend and y < yend:
    #         Matrix[x][y] += 1
    #         x += 1
    #         y += 1

# print(Matrix)

count = 0

for i in range(1000):
    for j in range(1000):
        if Matrix[i][j] >= 2:
            count += 1

print(count)