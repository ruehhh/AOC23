import sys
sys.setrecursionlimit(2500)

with open("input.txt", 'r') as file:
    lines = [x.strip('\n') for x in file.readlines()]
    d = { a + b*1j: lines[a][b] for a in range(len(lines)) for b in range(len(lines[0]))}


position = 0
direction = 1j
energized_init = {x: [] for x in d}

def propagate(position, direction, energized):
    if d.get(position) == None:
        return energized
    elif direction in energized.get(position):
        return energized
    else:
        energized[position].append(direction)
        if d.get(position) == '.':
            return propagate(position+direction, direction, energized)
        elif d.get(position) == "\\":
            direction = direction.imag + direction.real*1j 
            return  propagate(position+direction, direction, energized)
        elif d.get(position) == '/':
            direction = - direction.imag - direction.real*1j
            return  propagate(position+direction, direction, energized)
        elif d.get(position) == '-':
            if direction.real == 0:
                return propagate(position+direction, direction, energized)
            else:
                intermediate = propagate(position + 1j, 1j, energized)
                return propagate(position - 1j, -1j, intermediate)
        elif d.get(position) == '|':
            if direction.imag == 0:
                return propagate(position+direction, direction, energized)
            else:
                intermediate = propagate(position+1,1, energized)
                return propagate(position-1,-1, intermediate)


energized = propagate(0,1j,energized_init)

print(f"Part 1: {len([x for x in energized if energized[x] != []])}")

## Part 2
position = 0
direction = 1j
energized_init = {x: [] for x in d}

def propagate(position, direction, energized):
    if d.get(position) == None:
        return energized
    elif direction in energized.get(position):
        return energized
    else:
        energized[position].append(direction)
        if d.get(position) == '.':
            return propagate(position+direction, direction, energized)
        elif d.get(position) == "\\":
            direction = direction.imag + direction.real*1j 
            return  propagate(position+direction, direction, energized)
        elif d.get(position) == '/':
            direction = - direction.imag - direction.real*1j
            return  propagate(position+direction, direction, energized)
        elif d.get(position) == '-':
            if direction.real == 0:
                return propagate(position+direction, direction, energized)
            else:
                intermediate = propagate(position + 1j, 1j, energized)
                return propagate(position - 1j, -1j, intermediate)
        elif d.get(position) == '|':
            if direction.imag == 0:
                return propagate(position+direction, direction, energized)
            else:
                intermediate = propagate(position+1,1, energized)
                return propagate(position-1,-1, intermediate)



top_row = [len([x for x in propagate(i*1j,1,{x: [] for x in d}).values() if x != []]) for i in range(len(lines[0]))]
bottom_row = [len([x for x in propagate(len(lines)+i*1j,-1,{x: [] for x in d}).values() if x != []]) for i in range(len(lines[0]))]

l_col = [len([x for x in propagate(i,1j,{x: [] for x in d}).values() if x != []]) for i in range(len(lines))]
r_col = [len([x for x in propagate(i+len(lines[0])*1j,-1j,{x: [] for x in d}).values() if x != []]) for i in range(len(lines))]


print(f"Part 2: {max(top_row+bottom_row+l_col+r_col)}")


