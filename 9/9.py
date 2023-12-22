import math

with open("input.txt", 'r') as file:
    lines = [[int(y) for y in x.strip().split()] for x in file.readlines()]


def extend(seq):
    d = [seq]
    power = 0
    while all([i == 0 for i in d[-1]]) is False:
        d += [[d[-1][i+1]-d[-1][i] for i in range(len(d[-1])-1)]]
        power += 1
    D = len(d)
    d[D-1] += [0]
    for i in range(D-1):
        d[D-2-i] += [d[D-2-i][-1] + d[D-1-i][-1]]
    return d[0]

print(sum([extend(line)[-1] for line in lines]))