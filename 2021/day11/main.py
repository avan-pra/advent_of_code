fd = open('./data', 'r')

octopuses = []

positions = []

flashes = 0

for line in fd.readlines():
    octopuses.append([int(c) for c in line.strip('\n')])

def hasnt_flashed(x, y):
    if (x, y) in positions:
        return False
    return True

def in_map(x, y):
    if x < 0 or x > len(octopuses) - 1 or y < 0 or y > len(octopuses[0]) - 1:
        return False
    return True

def flash(x, y):
    position = [
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    ]
    for pos in position:
        if in_map(pos[0], pos[1]) and octopuses[pos[0]][pos[1]] != 0:
            if octopuses[pos[0]][pos[1]] == 9:
                octopuses[pos[0]][pos[1]] = 0
                positions.append(pos)
                global flashes
                flashes += 1
                flash(pos[0], pos[1])
            else:
                octopuses[pos[0]][pos[1]] += 1
        elif in_map(pos[0], pos[1]) and hasnt_flashed(pos[0], pos[1]):
            octopuses[pos[0]][pos[1]] += 1

for i in range(100):
    for x in range(len(octopuses)):
        for y in range(len(octopuses[x])):
            if octopuses[x][y] != 0:
                if octopuses[x][y] == 9:
                    octopuses[x][y] = 0
                    positions.append((x, y))
                    flashes += 1
                    flash(x, y)
                else:
                    octopuses[x][y] += 1
            elif hasnt_flashed(x, y):
                octopuses[x][y] += 1
    positions = []

print(flashes)

for row in octopuses:
    print(row)
