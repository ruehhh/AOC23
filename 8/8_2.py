import math

with open("input.txt", 'r') as file:
    lines = [i.strip('\n') for i in file.readlines()]
    lines.pop(1)

directions = [int(x) for x in list(lines[0].replace('L','0').replace('R','1'))]
lines.pop(0)

nodes_paths = {line[:3]:[line[-9:-6],line[-4:-1]] for line in lines}

all_nodes = [i for i in nodes_paths]
nodes = [i for i in nodes_paths if i[2] == 'A']


def distance_to_Z(node):
    counter = 0
    current_node = node
    while current_node[2] != 'Z':
        current_node = nodes_paths[current_node][directions[counter % len(directions)]]
        counter += 1
    return counter




print(math.lcm(*[distance_to_Z(node) for node in nodes]))

# def check_ends(nodes):
#     return all((i[2]=='Z' for i in nodes))


# n_paths = len(nodes)
# counter = 0
# while check_ends(nodes) is not True:
#     nodes = [nodes_paths[i][directions[counter % len(directions)]] for i in nodes]
#     counter += 1
#     print(nodes[0], counter)



# print(counter)