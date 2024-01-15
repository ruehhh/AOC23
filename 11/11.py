with open("input.txt", 'r') as file:
    universe = [line.strip('\n') for line in file.readlines()]

n = len(universe)
m = len(universe[0])

def rotate(universe):
    rotated_universe = []
    for j in range(len(universe[0])):
        rotated_universe += [''.join([universe[i][j] for i in range(len(universe))])]
    return(rotated_universe)

empty_rows = [i for i in range(n) if universe[i] == '.'*m]
empty_rows_shifted = [j + empty_rows.index(j) for j in empty_rows]
for i in empty_rows_shifted:
    universe.insert(i,'.'*m)

universe = rotate(universe)


n = len(universe)
m = len(universe[0])
empty_rows = [i for i in range(n) if universe[i] == '.'*m]
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


print(f"Part 1: {int(d_sum)}")


## Part 2
with open("input.txt", 'r') as file:
    universe = [line.strip('\n') for line in file.readlines()]

expansion_rate = 1000000

n = len(universe)
m = len(universe[0])
initial_galaxy_locs = [a+b*1j for a in range(n) for b in range(m) if universe[a][b] == '#']
n_galaxies = len(initial_galaxy_locs)

initial_galaxy_rows = [int(x.real) for x in initial_galaxy_locs]
initial_empty_rows = [x for x in range(max(initial_galaxy_rows)) if x not in initial_galaxy_rows]
expanded_galaxy_rows = [int(x + len([y for y in initial_empty_rows if y < x])*(expansion_rate-1)) for x in initial_galaxy_rows]


initial_galaxy_cols = [int(x.imag) for x in initial_galaxy_locs]
initial_empty_cols = [x for x in range(max(initial_galaxy_cols)) if x not in initial_galaxy_cols]
expanded_galaxy_cols = [int(x + len([y for y in initial_empty_cols if y<x])*(expansion_rate-1)) for x in initial_galaxy_cols]

expanded_galaxy_locs = [expanded_galaxy_rows[i]+expanded_galaxy_cols[i]*1j for i in range(n_galaxies)]

d_sum = int(sum([abs((x-y).real) + abs((x-y).imag) for x in expanded_galaxy_locs for y in expanded_galaxy_locs])/2)

print(f"Part 2: {d_sum}")