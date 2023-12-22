import os

print(os.getcwd())

with open('aoc23/5/input.txt', 'r') as file:
    chunks = file.read().split('\n\n')

alpha = ' :-abcdefghijklmnopqrstuvwxyz\n'


def listize(numlist):
    return [int(x) for x in numlist.split(' ')]


seeds_range = listize(chunks[0].strip(alpha))
seeds_start = seeds_range[::2]
seeds_length = seeds_range[1::2]
num_seed_ranges = len(seeds_start)

seeds = (seeds_start[i]+j for i in range(len(seeds_start)-1) for j in range(seeds_length[i]))

seed_to_soil_map = [listize(z) for z in chunks[1].strip(alpha).split('\n')]
soil_to_fert_map = [listize(z) for z in chunks[2].strip(alpha).split('\n')]
fert_to_water_map = [listize(z) for z in chunks[3].strip(alpha).split('\n')]
water_to_light_map = [listize(z) for z in chunks[4].strip(alpha).split('\n')]
light_to_temp_map = [listize(z) for z in chunks[5].strip(alpha).split('\n')]
temp_to_hum_map = [listize(z) for z in chunks[6].strip(alpha).split('\n')]
hum_to_loc_map = [listize(z) for z in chunks[7].strip(alpha).split('\n')]


def map_interval_form(map):
    return [[[m[1], m[1]+m[2]-1], [m[0], m[0]+m[2]-1]] for m in map]


m1 = seed_to_soil_map
m2 = soil_to_fert_map
m3 = fert_to_water_map
m4 = water_to_light_map
m5 = light_to_temp_map
m6 = temp_to_hum_map
m7 = hum_to_loc_map


def backtrack(n,m):
    for i in m:
        if i[1][0]<=n<=i[1][1]:
            return i[0][0]+n-i[1][0]
    return n


def mapping(x,map):
    for i in map:
        if i[1] <= x <= i[1] + i[2] - 1:
            return x - i[1] + i[0]
    return x


def flatten(m1, m2):
    m1_interval = map_interval_form(m1)
    m2_interval = map_interval_form(m2)
    m1_cuts = [l[0][0] for l in m1_interval]+[l[0][1]+1 for l in m1_interval]+[0]
    m2_cuts = [backtrack(l[0][0], m1_interval) for l in m2_interval]+[backtrack(l[0][1]+1, m1_interval) for l in m2_interval]
    cuts = sorted(list(set(m1_cuts) | set(m2_cuts)))
    return [[mapping(mapping(x, m1),m2), x, cuts[cuts.index(x)+1]-x] for x in cuts[:-1]]


totalmap = flatten(m1, flatten(m2, flatten(m3, flatten(m4, flatten(m5, flatten(m6, m7))))))
break_points = [x[1] for x in totalmap]

potential_seeds = seeds_start

for x in break_points:
    for i in range(num_seed_ranges):
        if seeds_start[i] < x < seeds_start[i] + seeds_length[i]:
            potential_seeds += [x]


print(sorted([(mapping(x, totalmap),x) for x in potential_seeds]))


# min_loc = full_mapping(seeds[0])


# for seed in seeds:
#     if full_mapping(seed) < min_loc:
#         min_loc = full_mapping(seed)


# print(min_loc)
