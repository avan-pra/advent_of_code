fd = open('./data', 'r')

mymap = []

for line in fd.readlines():
    mymap.append([int(c) for c in line.strip('\n')])

low_points = 0

for i in range(0, len(mymap)):
    for j in range(0, len(mymap[i])):
        if i == 0 and j == 0:                                   #corner 1
            if mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j + 1]:
                low_points += mymap[i][j] + 1
        elif i == 0 and j == len(mymap[i]) - 1:                 # corner 2
            if mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j - 1]:
                low_points += mymap[i][j] + 1
        elif i == len(mymap) - 1 and j == 0:                    # corner 3
            if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i][j + 1]:
                low_points += mymap[i][j] + 1
        elif i == len(mymap) - 1 and j == len(mymap[i]) - 1:    # corner 4
            if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i][j - 1]:
                low_points += mymap[i][j] + 1
        elif i == 0:                                            # top
            if mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j - 1] and mymap[i][j] < mymap[i][j + 1]:
                low_points += mymap[i][j] + 1
        elif i == len(mymap) - 1:                               # bottom
            if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i][j - 1] and mymap[i][j] < mymap[i][j + 1]:
                low_points += mymap[i][j] + 1
        elif j == 0:                                            # left
            if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j + 1]:
                low_points += mymap[i][j] + 1
        elif j == len(mymap[i]) - 1:                                            # right
            if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j - 1]:
                low_points += mymap[i][j] + 1
        else:
            if mymap[i][j] < mymap[i - 1][j] and mymap[i][j] < mymap[i + 1][j] and mymap[i][j] < mymap[i][j - 1] and mymap[i][j] < mymap[i][j + 1]:
                low_points += mymap[i][j] + 1
        # elif #postion
print(low_points)