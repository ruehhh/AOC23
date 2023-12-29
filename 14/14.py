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

print(int(weight))
