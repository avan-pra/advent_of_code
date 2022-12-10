#!/usr/bin/python3

X = 1
cycle = 0
screen = ['.'] * 240

def printscreen():
	global screen
	for i in range(6):
		for j in range(40):
			print(screen[(i * 40) + j], end='')
		print()

def checkcycle(cycle, X, screen):
	if cycle % 40 == X or cycle % 40 == X - 1 or cycle % 40 == X + 1:
		screen[cycle] = '#'

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		if line == "noop":
			for i in range(1):
				checkcycle(cycle, X, screen)
				cycle += 1
			pass
		if line.startswith("addx"):
			for i in range(2):
				checkcycle(cycle, X, screen)
				cycle += 1
			X += int(line.split()[1])

printscreen()
