with open("5\input.txt", 'r') as file:
    chunks = file.read().split('\n\n')

alpha = ' :-abcdefghijklmnopqrstuvwxyz\n'


def listize(numlist):
    return [int(x) for x in numlist.split(' ')]


seeds = listize(chunks[0].strip(alpha))

seed_to_soil_map = [listize(z) for z in chunks[1].strip(alpha).split('\n')]
soil_to_fert_map = [listize(z) for z in chunks[2].strip(alpha).split('\n')]
fert_to_water_map = [listize(z) for z in chunks[3].strip(alpha).split('\n')]
water_to_light_map = [listize(z) for z in chunks[4].strip(alpha).split('\n')]
light_to_temp_map = [listize(z) for z in chunks[5].strip(alpha).split('\n')]
temp_to_hum_map = [listize(z) for z in chunks[6].strip(alpha).split('\n')]
hum_to_loc_map = [listize(z) for z in chunks[7].strip(alpha).split('\n')]

m1 = seed_to_soil_map
m2 = soil_to_fert_map
m3 = fert_to_water_map
m4 = water_to_light_map
m5 = light_to_temp_map
m6 = temp_to_hum_map
m7 = hum_to_loc_map


def mapping(x,map):
    for i in map:
        if i[1] <= x <= i[1] + i[2] -1:
            return x - i[1] + i[0]
    return x


def full_mapping(x):
    return mapping(mapping(mapping(mapping(mapping(mapping(mapping(x,m1),m2),m3),m4),m5),m6),m7)


min_loc = full_mapping(seeds[0])


for seed in seeds:
    if full_mapping(seed) < min_loc:
        min_loc = full_mapping(seed)


print(min_loc)
