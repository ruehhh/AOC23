with open("input.txt", 'r') as file:
    lines = [line.strip('\n') for line in file.readlines()]
    d = { a + b*1j : lines[a][b] for a in range(len(lines)) for b in range(len(lines[0])) if lines[a][b] != '.'}
    for y in range(len(lines[0])):
        d[-1+y*1j] = '#'


def calc_new_pos(rock):
    current = rock
    r_rocks = 0
    while d.get(current) != '#':
        current += -1
        if d.get(current) == 'O':
            r_rocks += 1
    return current + r_rocks+1

new_pos = [calc_new_pos(x) for x in d if d[x] == 'O']

weight = 0
for rock in new_pos:
    weight += len(lines) - rock.real

print(f"Part 1: {int(weight)}")

## Part 2
for j in range(len(lines[0])):
    d[-1+j*1j] = '#'
    d[len(lines)+j*1j] = '#'
for i in range(len(lines)):
    d[i - 1j] = '#'
    d[i + len(lines)*1j] = '#'

directions = { 'N': -1, 'S':1, 'E':1j, 'W':-1j}

def calc_new_pos(rock,dict,direction):
    if dict.get(rock) == '#':
        return rock
    else:
        w = directions[direction]
        current = rock
        r_rocks = 0
        while dict.get(current) != '#':
            current += w
            if dict.get(current) == 'O':
                r_rocks += 1
        return current - (r_rocks+1)*w

def new_pos(dict, direction):
    return {calc_new_pos(x, dict, direction):dict[x] for x in dict}

def spin(rocks):
    return new_pos(new_pos(new_pos(new_pos(rocks, 'N'),'W'),'S'),'E')

### ASSUMES THAT CYCLE APPEARS IN FIRST 200 SPINS
n = 200

pos = d

m = 0
weights = []
while m < n:
    weight = sum([len(lines) - rock.real for rock in pos if pos[rock] == 'O'] )
    weights.append(weight)
    pos = spin(pos)
    m+=1

for i in range(int(n/2)):
    for k in range(1,int(n/2)):
        if weights[i:i+k] == weights[i+k:i+2*k]:
            start, period = i, k
            break

offset = (1000000000 - i) % k

print(f"Part 2: {int(weights[i + offset])}")
