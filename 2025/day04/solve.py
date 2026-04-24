def check(grid, x, y, len_x, len_y):
    adjacent = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0) and x + i >= 0 and x + i < len_x and y + j >= 0 and y + j < len_y:
                if grid[x+i][y+j] == '@':
                    adjacent += 1

    if adjacent >= 4:
        return False
    return (x, y)

with open('./input.txt', 'r') as fd:
    grid = []
    for line in fd.readlines():
        grid.append(list(line.strip()))

len_x = len(grid)
len_y = len(grid[0])

post_list = []

count = 0

while True:
    for i in range(0, len_x):
        for j in range(0, len_y):
            if grid[i][j] == '@' and check(grid, i, j, len_x, len_y):
                post_list.append(check(grid, i, j, len_x, len_y))
                count += 1

    for entry in post_list:
        grid[entry[0]][entry[1]] = 'x'

    for entry in grid:
        print(entry)
    print('')
    
    if len(post_list) == 0:
        break
    post_list = []

    print(count)
