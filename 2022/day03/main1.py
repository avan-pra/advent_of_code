#!/usr/bin/python3

score = 0

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		line = [line[i:i+int(len(line)/2)] for i in range(0, len(line), int(len(line)/2))]
		cscore = ord((''.join(set(line[0]).intersection(line[1])))[0])
		if cscore - 96 > 0:
			score += cscore - 96
		else:
			score += cscore - 38

print(score)
