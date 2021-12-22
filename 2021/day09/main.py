def is_low_point(i, j):
    if i == 0 and j == 0:                                   #corner 1
        if mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j + 1]:
            return True
    elif i == 0 and j == len(mymap[i]) - 1:                 # corner 2
        if mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j - 1]:
            return True
    elif i == len(mymap) - 1 and j == 0:                    # corner 3
        if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i][j + 1]:
            return True
    elif i == len(mymap) - 1 and j == len(mymap[i]) - 1:    # corner 4
        if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i][j - 1]:
            return True
    elif i == 0:                                            # top
        if mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j - 1] and mymap[i][j] < mymap[i][j + 1]:
            return True
    elif i == len(mymap) - 1:                               # bottom
        if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i][j - 1] and mymap[i][j] < mymap[i][j + 1]:
            return True
    elif j == 0:                                            # left
        if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j + 1]:
            return True
    elif j == len(mymap[i]) - 1:                            # right
        if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j - 1]:
            return True
    else:                                                   # center
        if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j - 1] and mymap[i][j] < mymap[i][j + 1]:
            return True
    return False

fd = open('./data', 'r')

mymap = []

for line in fd.readlines():
    mymap.append([int(c) for c in line.strip('\n')])

def flood_fill(x, y, visited: list):
    if (x, y) in visited or x == -1 or y == -1 or x == len(mymap) or y == len(mymap[0]) or mymap[x][y] == 9:
        return visited
    visited.append((x, y))
    global basin_size
    basin_size += 1
    # print(visited)
    visited = flood_fill(x - 1, y, visited)
    visited = flood_fill(x + 1, y, visited)
    visited = flood_fill(x, y - 1, visited)
    visited = flood_fill(x, y + 1, visited)

    return visited

basin_size = 0
all_basin_size = []

for i in range(0, len(mymap)):
    for j in range(0, len(mymap[i])):
        if is_low_point(i, j):
            basin_size = 0
            flood_fill(i, j, [])
            all_basin_size.append(basin_size)

all_basin_size.sort()
print(all_basin_size[-3:])

# for line in mymap:
#     print(line)
        # elif #postion

