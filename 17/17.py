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
    if stretch<3:
        return [x for x in [(position + direction, direction, stretch+1), (position + direction*1j, direction*1j,1), (position+direction*(-1j), direction*(-1j),1)] if d.get(x[0]) is not None]
    else:
        return [x for x in [(position + direction*1j, direction*1j,1), (position+direction*(-1j), direction*(-1j),1)] if d.get(x[0]) is not None]
    
end_points = [((n-1)+(m-1)*1j,y,z) for y in [1,1j] for z in range(0,4)]

def dijk(init):
    current = init
    dijkstra = {(x,y,z):math.inf for x in d for y in [1,-1,1j,-1j] for z in range(0,11)}
    dijkstra[init] = 0
    visited = {}
    queue = [init]
    k = 0
    while current not in end_points:
        visited[current] = 1
        d_current = dijkstra[current]
        current_neighbours = neighbours(*current)
        for neighbour in current_neighbours:
            if d_current+d[neighbour[0]] < dijkstra[neighbour]:
                dijkstra[neighbour] = d_current + d[neighbour[0]]    
                bisect.insort_left(queue,neighbour,key=dijkstra.get)
        k = next((x for x in range(k, len(queue)) if queue[x] not in visited), None)
        current = queue[k]
    return dijkstra[current]

print(f"Part 1: {min([dijk((0,1j,0)),dijk((0,1,0))])}")

end_points = [((n-1)+(m-1)*1j,y,z) for y in [1,1j] for z in range(4,11)]

def neighbours(position:complex, direction:complex, stretch:int):
    if stretch < 4:
        return [x for x in [(position + direction, direction, stretch+1)] if valid(x)]
    elif 4 <= stretch < 10:
        return [x for x in [(position + direction, direction, stretch+1), (position + direction*1j, direction*1j,1), (position+direction*(-1j), direction*(-1j),1)] if valid(x)]
    elif stretch == 10:
        return [x for x in [(position + direction*1j, direction*1j,1), (position+direction*(-1j), direction*(-1j),1)] if valid(x)]
    
print(f"Part 2: {min([dijk((0,1j,0)),dijk((0,1,0))])}")
