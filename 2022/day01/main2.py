elf = []
c_elf = 0

with open('./input') as fd:
	for line in fd.readlines():
		line = line.strip()
		if line == '':
			elf.append(c_elf)
			c_elf = 0
			continue
		c_elf += int(line)

elf.sort(reverse=True)
print(elf[0] + elf[1] + elf[2])
