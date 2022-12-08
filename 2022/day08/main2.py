#!/usr/bin/python3

plan = []
visible_trees = 0
all_score = []

def is_visible(y, x, plan):
	if x == 0 or y == 0 or y == len(plan)-1 or x == len(plan[y])-1:
		return 1
	testvec = []
	score = 1

	cs = 0
	for i in range(0, y):
		testvec.append(plan[i][x])
	testvec.reverse()
	for i in testvec:
		if i >= plan[y][x]:
			cs += 1
			break
		cs += 1
	score *= cs
	testvec.clear()

	cs = 0
	for i in range(y + 1, len(plan)):
		testvec.append(plan[i][x])
	for i in testvec:
		if i >= plan[y][x]:
			cs += 1
			break
		cs += 1
	score *= cs
	testvec.clear()
	
	cs = 0
	for i in range(0, x):
		testvec.append(plan[y][i])
	testvec.reverse()
	for i in testvec:
		if i >= plan[y][x]:
			cs += 1
			break
		cs += 1
	score *= cs
	testvec.clear()

	cs = 0
	for i in range(x + 1, len(plan[y])):
		testvec.append(plan[y][i])
	for i in testvec:
		if i >= plan[y][x]:
			cs += 1
			break
		cs += 1
	score *= cs
	testvec.clear()

	global all_score
	all_score.append(score)

	return 0


with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		plan.append(list([*line]))

for i,y in enumerate(plan):
	for j,x in enumerate(y):
		visible_trees += is_visible(i, j, plan)

print(max(all_score))

#for i in plan:
#	print(i)
