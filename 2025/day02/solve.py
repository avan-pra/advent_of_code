def check(n: int):
    sn = str(n)
    for div in range(1, len(sn)):
        if len(sn) % div == 0:
            first = sn[:div]
            j = div
            while j < len(sn) and first == sn[j:j+div]:
                j+=div
            if j == len(sn):
                return n

    return 0

with open('./input.txt', 'r') as fd:
    result = 0
    line = fd.readline().strip()
    for entry in line.split(','):
        s = entry.split('-')
        for i in range(int(s[0]), int(s[1]) + 1):
            result += check(i)
    print(result)
