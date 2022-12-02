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
		if (outcome[1] == 'X'): # loose
			outcome[1] = chr(ord(outcome[0]) + 23 + 2)
		elif (outcome[1] == 'Y'): # draw
			outcome[1] = chr(ord(outcome[0]) + 23)
		elif (outcome[1] == 'Z'): # win
			outcome[1] = chr(ord(outcome[0]) + 23 + 1)
		if outcome[1] == chr(ord('Z') + 1):
			outcome[1] = 'X'
		elif outcome[1] == chr(ord('Z') + 2):
			outcome[1] = 'Y'
		score += getscore(outcome)

print(score)
