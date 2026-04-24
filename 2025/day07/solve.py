grid = []
start_position = 0

total = 0

# part 1
# def backtrack(grid: list, posy: int, posx: int, leny: int, lenx: int):
#     if posy + 1 >= leny:
#         return

#     if grid[posy + 1][posx] == '.':
#         grid[posy + 1][posx] = '|'
#         backtrack(grid, posy + 1, posx, leny, lenx)
#     elif grid[posy + 1][posx] == '^':
#         splitted = 0
#         if grid[posy + 1][posx - 1] != '|':
#             splitted += 1
#             backtrack(grid, posy, posx - 1, leny, lenx)
#         if grid[posy + 1][posx + 1] != '|':
#             splitted += 1
#             backtrack(grid, posy, posx + 1, leny, lenx)
#         if splitted >= 1:
#             global total
#             total += 1

# part 2
def backtrack(grid: list, posy: int, posx: int, leny: int, lenx: int):
    if posy + 1 >= leny:
        grid[posy][posx] = 1
        return

    if grid[posy][posx] == '.':
        backtrack(grid, posy + 1, posx, leny, lenx)
        grid[posy][posx] = grid[posy + 1][posx]
    elif grid[posy][posx] == '^':
        backtrack(grid, posy, posx - 1, leny, lenx)
        backtrack(grid, posy, posx + 1, leny, lenx)
        if isinstance(grid[posy][posx], int):
            grid[posy][posx] += grid[posy][posx - 1] + grid[posy][posx + 1]
        else:
            grid[posy][posx] = grid[posy][posx - 1] + grid[posy][posx + 1]

with open('./input.txt', 'r') as fd:
    for line in fd.readlines():
        if 'S' in line:
            start_position = line.find('S')
        grid.append(list(line.strip()))

grid[0][start_position] = '.'
lenx = len(grid[0])
leny = len(grid)




backtrack(grid, 0, start_position, leny, lenx)

# part 1
print(total)

# part 2
print(grid[0][start_position])
