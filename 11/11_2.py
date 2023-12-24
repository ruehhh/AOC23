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

print(d_sum)