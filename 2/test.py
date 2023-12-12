list_of_indices = []
list_of_powers = []
with open("2\input_test.txt",'r') as input:
    games = [line.strip('\n')[line.find(':')+2:] for line in input.readlines()]
    for game in games:
        min_number_of_cubes = {"red":0,"blue":0,"green":0}
        rounds = game.split('; ')
        for round in rounds:
            cube_counts = round.split(', ')
            for cube_count in cube_counts:
                cube_count_num = int(cube_count[:cube_count.find(' ')])
                cube_count_colour = cube_count[cube_count.find(' ')+1:]
                if cube_count_num > min_number_of_cubes[cube_count_colour]:
                    min_number_of_cubes[cube_count_colour] = cube_count_num
        print(min_number_of_cubes)
        list_of_powers.append(min_number_of_cubes['red']*min_number_of_cubes['blue']*min_number_of_cubes['green'])
        if min_number_of_cubes['red'] <= 12 and min_number_of_cubes['green'] <= 13 and min_number_of_cubes['blue'] <= 14:
            list_of_indices.append(games.index(game)+1)
print(sum(list_of_indices))
print(list_of_powers)
