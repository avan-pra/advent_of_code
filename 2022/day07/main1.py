#!/usr/bin/python3

fs = {}
fs['/'] = {}
current_path = "fs['/']"

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		if line.split(' ')[0] == '$': # command
			if line.split(' ')[1] == 'cd':
				if line.split(' ')[2] == '/':
					current_path = "fs['/']"
				elif line.split(' ')[2] == '..':
					current_path = current_path.rsplit('[', 1)[0]
				else:
					current_path = current_path + "['" + line.split(' ')[2] + "']"
			if line.split(' ')[1] == 'ls':
				pass
		elif line.split(' ')[0] == "dir": # new dir in ls
			exec(current_path + "['" + line.split(' ')[1] + "'] = {}")
		else: # its a file in ls
			exec(current_path + "['" + line.split(' ')[1] + "'] = " + line.split(' ')[0])

total = 0

def traverse_fs(node):
	count = 0

	for i in node:
		if type(node[i]) == int:
			count += node[i]
		elif type(node[i]) == dict:
			count += traverse_fs(node[i])
	if count <= 100000:
		global total
		total += count
		print(total)
	return count

print(traverse_fs(fs))
print("the result isnt the last but the one before")
