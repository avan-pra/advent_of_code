fd = open('./data', 'r')
inps = [int(x) for x in (fd.readline().split(','))]
result = []

for i in range(max(inps)):
    fuelcost = 0
    for j in inps:
        fuelcost += (abs(j - i) * (abs(j - i) + 1) / 2)
    result.append(fuelcost)

print(min(result))