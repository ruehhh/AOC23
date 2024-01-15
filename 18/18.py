import sys
sys.setrecursionlimit(30000)

with open("input.txt", 'r') as file:
    lines = [x.strip()[:-10] for x in file.readlines()]
    dirs = [[x[0], int(x[2:])] for x in lines]

d = {'U': -1, 'D': 1, 'R': 1j, 'L': -1j}

dig = {0: '#'}

current = 0

for x in dirs:
    for i in range(1, 1+x[1]):
        dig[current+d[x[0]]] = '#'
        current += d[x[0]]


h_min = int(min([x.real for x in dig]))
w_min = int(min([x.imag for x in dig]))


dig_shift = {x- h_min - w_min*1j : dig[x] for x in dig}


# def print_dig(dict):
#     h_max = int(max([x.real for x in dict]))
#     w_max = int(max([x.imag for x in dict]))
#     print(h_max, w_max)
#     return '\n'.join([''.join([dict.get(a+b*1j, '.') for b in range(w_max+1)]) for a in range(h_max+1)])


# with open("map.txt", 'w') as file:
#     file.write(print_dig(dig_shift))


def fill(dig, point):
    dig[point] = '#'
    neighbours = [point + x for x in [1, -1, 1j, -1j]]
    for neighbour in neighbours:
        if dig.get(neighbour) is None:
            fill(dig, neighbour)


fill(dig_shift, 100+100j)

print(f"Part 1: {len(dig_shift)}")

## Part 2

with open("input.txt", 'r') as file:
    lines = [[int(x.strip()[-2]), int(x.strip()[-7:-2], 16)] for x in file.readlines()]

d = {3: -1, 1: 1, 0: 1j, 2: -1j}


polygon = [0]
current = 0

for line in lines:
    current += d[line[0]]*line[1]
    polygon.append(current)


perimeter = sum([x[1] for x in lines])


def shoelace(p):
    return int(abs(sum([p[i].real*p[i+1].imag - p[i].imag*p[i+1].real for i in range(len(p)-1)]))/2 + perimeter/2 + 1)


print(f"Part 2: {shoelace(polygon)}")