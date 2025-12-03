def max_line(line):
    my_str = max(line[:-11])
    line_to_search = line[line.find(my_str)+1:]
    for i in range(1, 12):
        if i != 11:
            c = max(line_to_search[:-11+i])
            my_str += c
            line_to_search = line_to_search[line_to_search.find(c)+1:]
        else:
            # line_to_search[:0] doesnt return the full str
            c = max(line_to_search)
            my_str += c

    return int(my_str)

with open('./input.txt', 'r') as fd:
    sum = 0
    for line in fd.readlines():
        line = line.strip()
        sum += max_line(line)

    print(sum)
