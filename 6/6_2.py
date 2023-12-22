alpha = ':\n abcdefghijklmnopqrstuvwxyz'

with open("aoc23/6/input.txt", 'r') as file:
    lines_raw = file.readlines()

lines = [int(i.lower().strip(alpha).replace(' ','')) for i in lines_raw]

print(lines)


n_winning_strategies = len([t_hold for t_hold in range(lines[0]+1) if (lines[0]-t_hold)*t_hold > lines[1]])

print(n_winning_strategies)