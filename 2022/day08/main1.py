#!/usr/bin/python3

plan = []
visible_trees = 0

def is_visible(y, x, plan):
	if x == 0 or y == 0 or y == len(plan)-1 or x == len(plan[y])-1:
		return 1
	testvec = []

	for i in range(0, y):
		testvec.append(plan[i][x])
	if max(testvec) < plan[y][x]:
		return 1
	testvec.clear()

	for i in range(y + 1, len(plan)):
		testvec.append(plan[i][x])
	if max(testvec) < plan[y][x]:
		return 1
	testvec.clear()
	
	for i in range(0, x):
		testvec.append(plan[y][i])
	if max(testvec) < plan[y][x]:
		return 1
	testvec.clear()

	for i in range(x + 1, len(plan[y])):
		testvec.append(plan[y][i])
	if max(testvec) < plan[y][x]:
		return 1
	testvec.clear()

	return 0

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		plan.append(list([*line]))

for i,y in enumerate(plan):
	for j,x in enumerate(y):
		visible_trees += is_visible(i, j, plan)

print(visible_trees)

#for i in plan:
#	print(i)
