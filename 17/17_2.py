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



def insert(x,list):
    k = 0
    while x[0] > list[k]:
        k+=1
    list.insert(k-1,x)






def dijk(init):
    current = init
    dijkstra = {init:0}
    unvisited = [init]
    end_points = [((n-1)+(m-1)*1j,y,z) for y in [1,1j] for z in range(4,11)]
    best = math.inf
    while unvisited != []:
        if current[0] == (n-1) + (m-1)*1j:
            return best
        current_neighbours = neighbours(*current)
        for neighbour in current_neighbours:
            if dijkstra.get(neighbour) != None:
                dijkstra[neighbour] = min([dijkstra[current]+d[neighbour[0]], dijkstra[neighbour]])
            else:
                dijkstra[neighbour] = dijkstra[current]+d[neighbour[0]]
                if dijkstra[neighbour] <= best:
                    bisect.insort_left(unvisited,neighbour,key=dijkstra.get)
            if neighbour in end_points:
                    best = min(best,dijkstra[neighbour])
        unvisited.pop(0)
        try:
            current = unvisited[0]
        except:
            current = None
    return best



print(min([dijk((0,1j,0)),dijk((0,1,0))]))