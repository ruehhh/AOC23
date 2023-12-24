with open("input_test.txt", 'r') as file:
    universe = [line.strip('\n') for line in file.readlines()]



n = len(universe)
m = len(universe[0])

def rotate(universe):
    rotated_universe = []
    for j in range(len(universe[0])):
        rotated_universe += [''.join([universe[i][j] for i in range(len(universe))])]
    return(rotated_universe)

empty_rows = [i for i in range(n) if universe[i] == '.'*m]
print(empty_rows)
empty_rows_shifted = [j + empty_rows.index(j) for j in empty_rows]
for i in empty_rows_shifted:
    universe.insert(i,'.'*m)

universe = rotate(universe)


n = len(universe)
m = len(universe[0])
empty_rows = [i for i in range(n) if universe[i] == '.'*m]
print(empty_rows)
empty_rows_shifted = [j + empty_rows.index(j) for j in empty_rows]
for i in empty_rows_shifted:
    universe.insert(i,'.'*m)

universe = rotate(universe)


n = len(universe)
m = len(universe[0])


galaxy_locs = [(i,j) for i in range(n) for j in range(m) if universe[i][j] == '#']

def d(t1,t2):
    return abs(t1[0]-t2[0]) + abs(t1[1]-t2[1])

d_sum = sum([d(t1,t2) for t1 in galaxy_locs for t2 in galaxy_locs])/2


print(galaxy_locs)