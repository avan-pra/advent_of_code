
num_list: list = []
op_list: list = []

# part 1
# with open('./input.txt', 'r') as fd:
#     for line in fd.readlines():
#         inp = line.strip().split()
#         if len(num_list) == 0:
#             num_list = [[] for _ in range(len(inp))]
#         # We have a number line
#         if inp[0].isnumeric():
#             for i, elem in enumerate(inp):
#                 num_list[i].append(int(elem))
#         else:
#             for elem in inp:
#                 op_list.append(elem)


# part 2
lines = []
op_line = ""
op_len = []
with open('./input.txt', 'r') as fd:
    for line in fd.readlines():
        if not line.strip().split()[0].isnumeric():
            op_line = line.strip('\n')
            for elem in line.strip().split():
                op_list.append(elem)
        else:
            lines.append(line.strip('\n'))


# calculate width of each operations
op_line = op_line[1:]
while op_line != '':
    clen = 0
    while clen < len(op_line) and op_line[clen] == ' ':
        clen += 1
    op_len.append(clen)
    op_line = op_line[clen + 1:]
op_len[-1] += 1

# create an array of array which constist of operations (vertically)
for op in op_len:
    num_list.append([])
    for i in range(op):
        num_list[-1].append([])
        num_list[-1][i] = 0
        for j in range(len(lines)):
            if lines[j][i] != ' ':
                num_list[-1][i] *= 10
                num_list[-1][i] += int(lines[j][i])
    for j in range(len(lines)):
        lines[j] = lines[j][op+1:]

# common for both part
total = 0
for i, lnum_list in enumerate(num_list):
    ltotal = 0
    for elem in lnum_list:
        if op_list[i] == '+':
            ltotal += elem
        else:
            if ltotal == 0:
                ltotal = elem
            else:
                ltotal *= elem
    total += ltotal

print(total)

