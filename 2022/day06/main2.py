#!/usr/bin/python3

stmc = 0

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		for i in range(0, len(line)):
			if len(set([line[i], line[i + 1], line[i + 2], line[i + 3], line[i + 4], line[i + 5], line[i + 6], line[i + 7], line[i + 8], line[i + 9], line[i + 10], line[i + 11], line[i + 12], line[i + 13]])) == 14:
				stmc += i + 13 + 1
				break


print(stmc)
