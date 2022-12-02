#!/usr/bin/python3

score = 0

def getscore(outcome):
	cscore = 0
	i = ord(outcome[1]) - ord(outcome[0]) - 23
	
	if i == 0: # draw
		cscore = 3
	elif i == 1 or i == -2: #victory
		cscore = 6
	cscore += ord(outcome[1]) - ord('W')
	return cscore


with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		outcome = line.split(' ')
		score += getscore(outcome)

print(score)
