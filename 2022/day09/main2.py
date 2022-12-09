#!/usr/bin/python3

plansize = 16
gposy = []
gposx = []
for i in range(10):
	gposy.append(int(plansize/2))
	gposx.append(int(plansize/2))

plan = []
for i in range(plansize):
	c = []
	for j in range(plansize):
		c.append(['.', False])
	plan.append(c)

plan[gposy[0]][gposx[0]][0] = "0"
plan[gposy[0]][gposx[0]][1] = True

def print_plan():
	global plan
	for i in plan:
		for j in i:
			print(j[0], end='')
		print()
	print()

def get_score():
	global plan
	score = 0
	for i in plan:
		for j in i:
			if j[1] == True:
				score += 1
	return score

def update_tail(holdx, holdy, hposx, hposy, tposx, tposy, headchar, ropechar, direction):
	global plan, gposx, gposy
	if plan[tposy][tposx][0] == '.': # was collapsing or smth
		plan[tposy][tposx][0] = ropechar
		
		if ropechar == '9':
			plan[tposy][tposx][1] = True
		return
	if abs(hposx - tposx) < 2 and abs(hposy - tposy) < 2:
		return # dont do anything the rope moved but is still in the vicinity
	else:
		
		plan[tposy][tposx][0] = '.'
		plan[holdy][holdx][0] = ropechar
		gposx[int(ropechar)] = holdx
		gposy[int(ropechar)] = holdy
		tposx = holdx
		tposy = holdy
		if ropechar == '9':
			plan[tposy][tposx][1] = True
		return

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		direction,step = line.split()[0],int(line.split()[1])
		if direction == 'R':
			for i in range(0, step):
				holdx = gposx[0]
				holdy = gposy[0]
				plan[gposy[0]][gposx[0]][0] = '.'
				plan[gposy[0]][gposx[0]+1][0] = '0'
				gposx[0] += 1
				headchar = '0'
				for i in range(9):
					ropechar = str(int(headchar)+1)
					if i != 0:
						holdx = savex
						holdy = savey
					savex = gposx[int(ropechar)]
					savey = gposy[int(ropechar)]
					update_tail(holdx, holdy, gposx[int(headchar)], gposy[int(headchar)], gposx[int(ropechar)], gposy[int(ropechar)], headchar, ropechar, direction)
					headchar = str(int(headchar)+1)
		if direction == 'U':
			for i in range(0, step):
				holdx = gposx[0]
				holdy = gposy[0]
				plan[gposy[0]][gposx[0]][0] = '.'
				plan[gposy[0]-1][gposx[0]][0] = '0'
				gposy[0] -= 1
				headchar = '0'
				for i in range(9):
					ropechar = str(int(headchar)+1)
					if i != 0:
						holdx = savex
						holdy = savey
					savex = gposx[int(ropechar)]
					savey = gposy[int(ropechar)]
					update_tail(holdx, holdy, gposx[int(headchar)], gposy[int(headchar)], gposx[int(ropechar)], gposy[int(ropechar)], headchar, ropechar, direction)
					headchar = str(int(headchar)+1)

print("no day 2")
