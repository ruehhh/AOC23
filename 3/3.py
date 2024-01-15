# Part 1
with open("input_test.txt", 'r') as input:
    lines = ['.'+line.strip('\n')+'.' for line in input.readlines()]

line_length = len(lines[0])
padding = '.'*line_length
schematic = [padding, *lines, padding]

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(schematic)

sum = 0
i = 1
while i <= len(schematic)-2:
    j = 0
    while j <= line_length-1:
        if schematic[i][j] in digits:
            num_length = 0
            k = j
            while schematic[i][k] in digits:
                num_length += 1
                k += 1
            neighbours = schematic[i][j-1]+schematic[i-1][j-1:j+num_length+1]+schematic[i][j+num_length]+schematic[i+1][j-1:j+num_length+1]
            if len([n for n in neighbours if n not in '0123456789.']) > 0:
                sum += int(schematic[i][j:j+num_length])
            j += num_length
        else:
            j += 1
    i += 1

print(f"Part 1: {sum}")

# Part 2

with open("input.txt", 'r') as input:
    lines = ['.'+line.strip('\n')+'.' for line in input.readlines()]

line_length = len(lines[0])
padding = '.'*line_length
schematic = [padding, *lines, padding]

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(schematic)

sum = 0
i = 1
numbers = []
while i <= len(schematic)-2:
    j = 0
    while j <= line_length-1:
        if schematic[i][j] in digits:
            num_length = 0
            k = j
            while schematic[i][k] in digits:
                num_length += 1
                k += 1
            number = int(schematic[i][j:j+num_length])
            if schematic[i][j-1] == '*':
                numbers.append([number, [i, j-1]])
            elif schematic[i][j+num_length] == '*':
                numbers.append([number, [i, j+num_length]])
            elif schematic[i-1][j-1:j+num_length+1].find('*') != -1:
                numbers.append([number, [i-1, j-1+schematic[i-1][j-1:j+num_length+1].find('*')]])
            elif schematic[i+1][j-1:j+num_length+1].find('*') != -1:
                numbers.append([number, [i+1, j-1+schematic[i+1][j-1:j+num_length+1].find('*')]])
            j += num_length
        else:
            j += 1
    i += 1

sum = 0
for i in numbers:
    partners = [j for j in numbers if j[1] == i[1]]
    if len(partners) == 2:
        sum += partners[0][0]*partners[1][0]

sum = int(sum/2)

print(f"Part 2: {sum}")
