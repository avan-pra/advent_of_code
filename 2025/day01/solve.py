import math

with open('./input.txt', 'r') as fd:
    lines = fd.readlines()
    amount_zero = 0
    dial = 50
    for line in lines:
        line = line.strip()
        if line.startswith('R'):
            amount_zero += math.floor(abs(dial + int(line[1:])) / 100)
            dial = (dial + int(line[1:])) % 100

        if line.startswith('L'):
            amount_zero += math.floor(int(line[1:]) / 100)
            if dial != 0 and dial - (int(line[1:]) % 100) <= 0:
                amount_zero += 1
            dial = (dial - int(line[1:])) % 100

        print(dial)
        print('===')
    print(amount_zero)