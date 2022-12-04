#!/usr/bin/python3

fc = 0

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		start1 = int(line.split(',')[0].split('-')[0])
		end1 = int(line.split(',')[0].split('-')[1])
		start2 = int(line.split(',')[1].split('-')[0])
		end2 = int(line.split(',')[1].split('-')[1])
		if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
			fc += 1

print(fc)
