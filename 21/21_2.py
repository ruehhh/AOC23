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

print(pts)


def poly(x):
    return sum([pts[j][1]*math.prod([(x-pts[i][0])/(pts[j][0]-pts[i][0]) for i in range(3) if i != j]) for j in range(3)])


print(poly(202300))
