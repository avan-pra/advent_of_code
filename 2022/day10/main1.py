#!/usr/bin/python3

X = 1
cycle = 0
ss = 0

def checkcycle(cycle, X):
	global ss
	if cycle == 20 or cycle % 40 == 20:
		ss += cycle * X

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		if line == "noop":
			for i in range(1):
				cycle += 1
				checkcycle(cycle, X)
			pass
		if line.startswith("addx"):
			for i in range(2):
				cycle += 1
				checkcycle(cycle, X)
			X += int(line.split()[1])

print(ss)
