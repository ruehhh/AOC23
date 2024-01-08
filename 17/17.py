import math

with open("input.txt", 'r') as file:
    lines = [x.strip('\n') for x in file.readlines()]
    d = {a + b*1j : int(lines[a][b]) for a in range(len(lines)) for b in range(len(lines[0]))}


def neighbours(position:complex, direction:complex, stretch:int):
    if stretch<3:
        return [x for x in [(position + direction, direction, stretch+1), (position + direction*1j, direction*1j,1), (position+direction*(-1j), direction*(-1j),1)] if d.get(x[0]) is not None]
    else:
        return [x for x in [(position + direction*1j, direction*1j,1), (position+direction*(-1j), direction*(-1j),1)] if d.get(x[0]) is not None]

# dijkstra = {(x,y,z): math.inf for x in d for y in [1,-1,1j,-1j] for z in range(1,4)}

full_graph = {(x,y,z): math.inf for x in d for y in [1,-1,1j,-1j] for z in range(1,4)}

dijkstra = {}
# unvisited = {(x,y,z): None for x in d for y in [1,-1,1j,-1j] for z in range(1,4)}

unvisited = {}

dijkstra[(0,1,0)] = 0
unvisited[(0,1,0)] = 0


current = (0,1,0)

# end_points = [x for x in full_graph if x[0] == len(lines)-1 + (len(lines[0])-1)*1j]

while unvisited != {}:
    del unvisited[current]
    current_neighbours = neighbours(*current)
    for neighbour in current_neighbours:
        if dijkstra.get(neighbour) != None:
            dijkstra[neighbour] = min([dijkstra[current]+d[neighbour[0]], dijkstra[neighbour]])
        else:
            dijkstra[neighbour] = dijkstra[current]+d[neighbour[0]]
            unvisited[neighbour] = dijkstra[neighbour]
    try:
        current = min(unvisited, key=dijkstra.get)
    except:
        current = None

# print(dijkstra)

print(min([dijkstra[x] for x in dijkstra if x[0] == len(lines)-1 + (len(lines[0])-1)*1j]))