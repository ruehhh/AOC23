import math

with open("input.txt", 'r') as file:
    lines = [x.strip('\n') for x in file.readlines()]

lnodes = [x.split(':')[0] for x in lines]
lgraph = {}
for line in lines:
    node = line.split(':')[0]
    for connection in line.split(':')[1].split():
        lgraph[(node, connection)] = 1

def opp(edge):
    return (edge[1], edge[0])

graph = {}
for x in lgraph:
    graph[x] = 1
    graph[opp(x)] = 1

nodes = list(set([x[0] for x in graph]))
connections = {x:set([y for y in nodes if graph.get((x,y)) is not None]) for x in nodes }


## Thanks 4HbQ
S = set(nodes)
count = lambda v: len(connections[v] - S)
while sum(map(count, S)) != 3:
    S.remove(max(S, key=count))
print(f"Part 1: {len(S) * len(set(nodes)-S)}")