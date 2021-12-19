fd = open('./data', 'r')
inps = [int(i) for i in fd.readline().split(',')]
lanternfishs = [0 for i in range(9)]
new_lanter = [0 for i in range(9)]

for i in inps:
    lanternfishs[i] += 1

# print(lanternfishs)

for i in range(256):
    for j in range(8):
        if j == 7:
            new_lanter[8] = lanternfishs[0]
            new_lanter[6] += lanternfishs[0]
            new_lanter[7] = lanternfishs[8]
        else:
            new_lanter[j] = lanternfishs[j + 1]

    lanternfishs = new_lanter
    new_lanter = [0 for i in range(9)]
    

# print(lanternfishs)
print(sum(lanternfishs))