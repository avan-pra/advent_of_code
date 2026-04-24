

with open('./input.txt', 'r') as fd:
    range_list = []
    while True:
        line = fd.readline().strip()
        if line== '':
            break
        start, end = [int(x) for x in line.split('-')]
        range_list.append((start, end+1))

    new_range_list = []
    while True:
        for i in range_list:
            added = 0
            for j in range_list:
                if min(i) <= max(j) and min(j) <= max(i) and i != j:
                    new_range_list.append((min(min(i), min(j)), max(max(i), max(j))))
                    added = 1
            if added == 0:
                new_range_list.append(i)
        if range_list == new_range_list:
            break
        range_list = list(set(new_range_list))
        new_range_list = []

    total = 0
    for entry in list(set(new_range_list)):
        total += entry[1] - entry[0]

    print(total)

    # part 1
    # total = 0
    # for ingredient in fd.readlines():
    #     for l in range_list:
    #         if int(ingredient.strip()) in l:
    #             total += 1
    #             break

