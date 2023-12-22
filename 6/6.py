alpha = ':\n abcdefghijklmnopqrstuvwxyz'

with open("aoc23/6/input.txt", 'r') as file:
    lines_raw = file.readlines()

lines = [[int(x) for x in y] for y in [i.lower().strip(alpha).split() for i in lines_raw]]

n_races = len(lines[0])





n_winning_strategies = [len([t_hold for t_hold in range(lines[0][i]+1) if (lines[0][i]-t_hold)*t_hold > lines[1][i]]) for i in range(n_races)]

print(lines)
print(n_winning_strategies)

product = 1
for i in n_winning_strategies:
    product = product*i

print(product)