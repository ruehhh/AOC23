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


print(f"Part 1: {int(distance/2)}")

## Part 2

loop = [start]
distance = 0
current = start
previous_move = None

while (d[current], bool(distance)) != ('S', True):
    if (d.get(current) in S_out and d.get(tsum(current, S)) in N_out) and (previous_move != N):
        current = tsum(current, S)
        distance += 1
        previous_move = S
        loop += [current]
    elif (d.get(current) in N_out and d.get(tsum(current, N)) in S_out) and (previous_move != S):
        current = tsum(current, N)
        distance += 1
        previous_move = N
        loop += [current]
    elif (d.get(current) in E_out and d.get(tsum(current, E)) in W_out) and (previous_move != W):
        current = tsum(current, E)
        distance += 1
        previous_move = E
        loop += [current]
    elif (d.get(current) in W_out and d.get(tsum(current, W)) in E_out) and (previous_move != E):
        current = tsum(current, W)
        distance += 1
        previous_move = W
        loop += [current]
    else:    
        print(previous_move, current, distance)
        break

d[start] = 'F'

count = 0
in_out = 0
i = 0
j = 0


def increment(i,j,in_out):
    if j == len(maze[0])-1:
        i += 1
        j = 0
        in_out = 0
    else:
        j += 1
    return (i,j,in_out)


opening = [('F','J'),('L','7')]
closing = [('F','7'),('L','J')]

while i < len(maze):
    if (i,j) in loop:
        if d[(i,j)] == '|':
            in_out = 1-in_out
        else:
            in_symb = d[(i,j)]
            seg_length = 1
            while d[(i,j+seg_length)] == '-':
                seg_length += 1
            j += seg_length
            out_symb = d[(i,j)]
            if (in_symb,out_symb) in opening:
                in_out = 1-in_out
    else:
        count += in_out
    (i,j,in_out) = increment(i,j,in_out)

print(f"Part 2: {count}")