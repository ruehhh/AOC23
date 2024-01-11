import itertools
import copy
import sys

sys.setrecursionlimit(30000)

with open("input.txt", 'r') as file:
    lines = [[[int(y[i].split(',')[j]) for j in range(3)] for i in range(2)] for y in [x.strip('\n').split('~') for x in file.readlines()]]


def fill_in(block):
    return list(itertools.product(*[range(block[0][i], block[1][i]+1) for i in range(3)]))


def sort_bricks(bricks):
    return sorted(bricks,key= lambda x: min(x[0][2],x[1][2]))

bricks = {i: fill_in(sort_bricks(lines)[i]) for i in range(len(lines))}

print(len(bricks))

occupied = {(x, y, 0): 1 for x in range(10) for y in range(10)}

for brick in bricks:
    for block in bricks[brick]:
        occupied[block] = 1



for brick in bricks:
    for block in bricks[brick]:
        del occupied[block]
    level = next(h for h in range(1, 400) if not all([occupied.get((block[0], block[1], block[2]-h)) == None for block in bricks[brick]])) - 1
    bricks[brick] = [(block[0],block[1],block[2]-level) for block in bricks[brick]]
    for block in bricks[brick]:
        occupied[block] = 1


def lower(b):
    return (b[0], b[1], b[2]-1)


def find_supported(brick):
    return [x for x in bricks if any([lower(block) in bricks[brick] for block in bricks[x]]) and x != brick]


def find_supporters(brick):
    return [x for x in bricks if any([lower(block) in bricks[x] for block in bricks[brick]]) and x != brick]

supporter = {}
supported = {}

for brick in bricks:
    supporter[brick] = find_supporters(brick)
    supported[brick] = find_supported(brick)

supporter[0] += ['f']

count = 0
for brick in bricks:
    # print(f"Brick {brick} is supported by {find_supporters(brick)} and supports {find_supported(brick)}")
    count += all([len(supporter[x])>1 for x in supported[brick]])


print(f"Part 1: {count} bricks can be safely disintegrated")

### PART 2 

def disintegrate(brick_list, tower):
    for x in brick_list:
        del tower[x]
    fallers = [y for y in tower if min([z[2] for z in tower[y]]) != 1 and all(tower.get(z) is None for z in supporter[y])]
    if fallers == []:
        return len(brick_list)
    else:
        return len(brick_list)+disintegrate(fallers, tower)



chain_lengths = []

for i in bricks:
    tower = bricks.copy()
    chain_lengths.append(disintegrate([i], tower)-1)


print(f"Part 2: the sum of chain reactions is {sum(chain_lengths)}")
