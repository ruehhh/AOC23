# Part 1

with open("4\input.txt",'r') as file:
    lines = file.readlines()
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
points = 0
for line in lines:
    winners_str = line[line.find(':')+2:line.find('|')]
    draw_str = line[line.find('|')+2:]+' '
    winners = []
    i = 0
    while i < len(winners_str):
        if winners_str[i] in digits:
            num = ''
            while winners_str[i] in digits:
                num += winners_str[i]
                i += 1
            winners.append(int(num))
        i += 1
    draw = []
    i = 0
    while i < len(draw_str):
        if draw_str[i] in digits:
            num = ''
            while draw_str[i] in digits:
                num += draw_str[i]
                i += 1
            draw.append(int(num))
        i += 1
    match_count = 0
    for i in draw:
        if i in winners:
            match_count += 1
    points += int(2**(match_count-1))
print(points)