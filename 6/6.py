import math
alpha = ':\n abcdefghijklmnopqrstuvwxyz'

with open("input.txt", 'r') as file:
    lines_raw = file.readlines()

lines = [[int(x) for x in y] for y in [i.lower().strip(alpha).split() for i in lines_raw]]

n_races = len(lines[0])
n_winning_strategies = math.prod([len([t_hold for t_hold in range(lines[0][i]+1) if (lines[0][i]-t_hold)*t_hold > lines[1][i]]) for i in range(n_races)])

print(f"Part 1: {n_winning_strategies}")


## Part 2

lines = [int(i.lower().strip(alpha).replace(' ','')) for i in lines_raw]
n_winning_strategies = len([t_hold for t_hold in range(lines[0]+1) if (lines[0]-t_hold)*t_hold > lines[1]])

print(f"Part 2: {n_winning_strategies}")
