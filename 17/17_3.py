import math
import bisect

with open("input.txt", 'r') as file:
    lines = [x.strip() for x in file.readlines()]
    n = len(lines)
    m = len(lines[0])
    d = {a + b*1j : int(lines[a][b]) for a in range(n) for b in range(m)}


def valid(x):
    if ((x[0] != (n-1) + (m-1)*1j) or 4<= x[2] <= 10) and (d.get(x[0]) is not None):
        return True
    else:
        return False

def neighbours(position:complex, direction:complex, stretch:int):
    if stretch < 4:
        return [x for x in [(position + direction, direction, stretch+1)] if valid(x)]
    elif 4 <= stretch < 10:
        return [x for x in [(position + direction, direction, stretch+1), (position + direction*1j, direction*1j,1), (position+direction*(-1j), direction*(-1j),1)] if valid(x)]
    elif stretch == 10:
        return [x for x in [(position + direction*1j, direction*1j,1), (position+direction*(-1j), direction*(-1j),1)] if valid(x)]




def dijk(init):
    current = init
    dijkstra = {(x,y,z):math.inf for x in d for y in [1,-1,1j,-1j] for z in range(0,11)}
    dijkstra[init] = 0
    visited = {(x,y,z):0 for x in d for y in [1,-1,1j,-1j] for z in range(0,11)}
    queue = [init]
    end_points = [((n-1)+(m-1)*1j,y,z) for y in [1,1j] for z in range(4,11)]
    best = math.inf
    while (current in end_points) == False:
        visited[current] = 1
        d_current = dijkstra[current]
        current_neighbours = neighbours(*current)
        for neighbour in current_neighbours:
            if d_current+d[neighbour[0]] < dijkstra[neighbour]:
                dijkstra[neighbour] = d_current + d[neighbour[0]]    
                if dijkstra[neighbour] <= best:
                    bisect.insort_left(queue,neighbour,key=dijkstra.get)
            if neighbour in end_points:
                    best = min(best,dijkstra[neighbour])
        k = next((x for x in range(len(queue)) if visited[queue[x]] == 0), None)
        queue = queue[k:]
        current = queue[0]
    return best



print(min([dijk((0,1j,0)),dijk((0,1,0))]))