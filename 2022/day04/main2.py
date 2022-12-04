#!/usr/bin/python3

fc = 0

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		start1 = int(line.split(',')[0].split('-')[0])
		end1 = int(line.split(',')[0].split('-')[1])
		start2 = int(line.split(',')[1].split('-')[0])
		end2 = int(line.split(',')[1].split('-')[1])
		if (start1 in range(start2, end2+1)) or (end1 in range(start2, end2+1)) or (start2 in range(start1, end1+1)) or (end2 in range(start1, end1+1)):
			fc += 1

print(fc)
