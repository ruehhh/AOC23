with open("input.txt", 'r') as file:
    maze = [x.strip('\n') for x in file.readlines()]


n = len(maze)
m = len(maze[0])

d = { (i,j) : maze[i][j] for i in range(n) for j in range(m) if maze[i][j] != '.'}
start = [x for x in d if d[x]=='S'][0]


def tsum(l1, l2):
    return tuple([l1[i]+l2[i] for i in range(len(l1))])


N = (-1,0)
S = (1,0)
E = (0,1)
W = (0,-1)

N_out = ['|','L','J','S']
S_out = ['|','F','7','S']
E_out = ['-','F','L','S']
W_out = ['-','7','J','S']

distance_dict = {start: 0}


distance = 0
current = start
previous_move = None

while (d[current], bool(distance)) != ('S', True):
    print(current)
    if (d.get(current) in S_out and d.get(tsum(current, S)) in N_out) and (previous_move != N):
        current = tsum(current, S)
        distance += 1
        previous_move = S
        distance_dict[current] = distance
    elif (d.get(current) in N_out and d.get(tsum(current, N)) in S_out) and (previous_move != S):
        current = tsum(current, N)
        distance += 1
        previous_move = N
        distance_dict[current] = distance
    elif (d.get(current) in E_out and d.get(tsum(current, E)) in W_out) and (previous_move != W):
        current = tsum(current, E)
        distance += 1
        previous_move = E
        distance_dict[current] = distance
    elif (d.get(current) in W_out and d.get(tsum(current, W)) in E_out) and (previous_move != E):
        current = tsum(current, W)
        distance += 1
        previous_move = W
        distance_dict[current] = distance
    else:    
        print(previous_move, current, distance)
        break


print(current, distance/2)