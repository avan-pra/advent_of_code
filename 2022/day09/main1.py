#!/usr/bin/python3

plansize = 1000
hposy = int(plansize/2)
hposx = int(plansize/2)
tposy = int(plansize/2)
tposx = int(plansize/2)
plan = []
for i in range(plansize):
	c = []
	for j in range(plansize):
		c.append(['.', False])
	plan.append(c)

plan[hposy][hposx][0] = "H"
plan[hposy][hposx][1] = True

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

def update_tail(holdx, holdy):
	global plan, hposx, hposy, tposx, tposy
	if plan[tposy][tposx][0] == '.': # was collapsing or smth
		plan[tposy][tposx][0] = 'T'
		plan[tposy][tposx][1] = True
		return
	if abs(hposx - tposx) < 2 and abs(hposy - tposy) < 2:
		return # dont don anything the rope moved but is still in the vicinity
	else:
		plan[tposy][tposx][0] = '.'
		plan[holdy][holdx][0] = 'T'
		tposx = holdx
		tposy = holdy
		plan[tposy][tposx][1] = True
		return

print_plan()

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		direction,step = line.split()[0],int(line.split()[1])
		if direction == 'R':
			for i in range(0, step):
				holdx = hposx
				holdy = hposy
				plan[hposy][hposx][0] = '.'
				plan[hposy][hposx+1][0] = 'H'
				hposx += 1
				update_tail(holdx, holdy)
		if direction == 'L':
			for i in range(0, step):
				holdx = hposx
				holdy = hposy
				plan[hposy][hposx][0] = '.'
				plan[hposy][hposx-1][0] = 'H'
				hposx -= 1
				update_tail(holdx, holdy)
		if direction == 'U':
			for i in range(0, step):
				holdx = hposx
				holdy = hposy
				plan[hposy][hposx][0] = '.'
				plan[hposy-1][hposx][0] = 'H'
				hposy -= 1
				update_tail(holdx, holdy)
		if direction == 'D':
			for i in range(0, step):
				holdx = hposx
				holdy = hposy
				plan[hposy][hposx][0] = '.'
				plan[hposy+1][hposx][0] = 'H'
				hposy += 1
				update_tail(holdx, holdy)

print_plan()
print(get_score())
