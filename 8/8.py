with open("input.txt", 'r') as file:
    lines = [i.strip('\n') for i in file.readlines()]
    lines.pop(1)

directions = [int(x) for x in list(lines[0].replace('L','0').replace('R','1'))]
lines.pop(0)

nodes_paths = {line[:3]:[line[-9:-6],line[-4:-1]] for line in lines}

node = 'AAA'
counter = 0

while node != 'ZZZ':
    node = nodes_paths[node][directions[counter % len(directions)]]
    counter += 1

print(f"Part 1: {counter}")


## Part 2

import math

all_nodes = [i for i in nodes_paths]
nodes = [i for i in nodes_paths if i[2] == 'A']

def distance_to_Z(node):
    counter = 0
    current_node = node
    while current_node[2] != 'Z':
        current_node = nodes_paths[current_node][directions[counter % len(directions)]]
        counter += 1
    return counter

print(f"Part 2: {math.lcm(*[distance_to_Z(node) for node in nodes])}")