#!/usr/bin/python3

r = [
['V','Q','W','M','B','N','Z','C'],
['B','C','W','R','Z','H'],
['J','R','Q','F'],
['T','M','N','F','H','W','S','Z'],
['P','Q','N','L','W','F','G'],
['W','P','L'],
['J','Q','C','G','R','D','B','V'],
['W','B','N','Q','Z'],
['J','T','G','C','F','L','H']
]

# kekw
for i in r:
	i.reverse()

# top of tower is at the end of each list

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		amount = int(line.split()[1])
		origin = int(line.split()[3])
		dest = int(line.split()[5])
		for i in range(0, amount):
			crate = r[origin-1][-1]
			del r[origin-1][-1]
			r[dest-1].append(crate)

for i in r:
	print(i)

for i in r:
	print(i[-1], end='')
print()

