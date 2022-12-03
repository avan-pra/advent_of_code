#!/usr/bin/python3

score = 0

store = []

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		store.append(line)
		if len(store) != 3:
			continue
		cscore = ord((''.join(set(store[0]).intersection(store[1]).intersection(store[2])))[0])
		if cscore - 96 > 0:
			score += cscore - 96
		else:
			score += cscore - 38
		store.clear()

print(score)
