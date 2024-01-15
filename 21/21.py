with open("input.txt", 'r') as file:
    lines = [x.strip('\n') for x in file.readlines()]

d = {a+b*1j: lines[a][b] for a in range(len(lines)) for b in range(len(lines[0])) if lines[a][b] != '#'}


steps = [1,-1,1j,-1j]


### step

k=0
while k < 64:
    d_aux = {}
    for x in d:
        if d[x] == 'S':
            d[x] = '.'
            for step in steps:
                if d.get(x+step) is not None:
                    d_aux[x+step] = 'S'
    for x in d_aux:
        d[x] = d_aux[x]
    k+=1


print(f"Part 1: {len([x for x in d if d[x] == 'S'])}")

## Part 2

import math

with open("input.txt", 'r') as file:
    lines = [x.strip('\n') for x in file.readlines()]
    n = len(lines)
    m = len(lines[0])

d = {a+b*1j: lines[a][b] for a in range(n) for b in range(m)}
S = tuple([a+b*1j for a in range(n) for b in range(m) if lines[a][b] == 'S'])


steps = [1,-1,1j,-1j]

def mod(z):
    return z.real % n + z.imag % m*1j



### recognising that 26501365 = 131*202300 + 65, and interpolating the polynomial for 65, 65+131, 65+131*2 gives

k=0
multiple = 0
pts = []
while k < 2*131+65:
    S = tuple(set([x for x in [y + z for y in S for z in steps if d[mod(y+z)] != '#']]))
    k+=1
    if k % 131 == 65:
        pts += [(multiple, len(S))]
        multiple += 1


def poly(x):
    return int(sum([pts[j][1]*math.prod([(x-pts[i][0])/(pts[j][0]-pts[i][0]) for i in range(3) if i != j]) for j in range(3)]))


print(f"Part 2: {poly(202300)}")
