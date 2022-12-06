#!/usr/bin/python3

stmc = 0

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		for i in range(0, len(line)):
			if len(set([line[i], line[i + 1], line[i + 2], line[i + 3]])) == 4:
				stmc += i + 3 + 1
				break


print(stmc)
