with open("input.txt", 'r') as file:
    lines_raw =[x.strip(' \n').split() for x in file.readlines()]

rows = [x[0] for x in lines_raw]

groups = [[int(y) for y in x[1].split(',')] for x in lines_raw]

cache = {}
def count(row, group):
    i = 0
    row = row.strip('.')+'.'
    if row == '.':
        if group == []:
            return 1
        else:
            return 0
    else:
        if row[i] == '#':
            l = min([k for k in range(len(row)) if row[i+k]!='#'])
            if group == []:
                return 0
            elif l > group[0]:
                return 0
            elif l < group[0] and row[i+l] == '.':
                return 0
            elif l == group[0] and row[i+l] == '.':
                return count(row[i+l:], group[1:])
            else:
                return count(row[:i+l]+'#'+row[i+l+1:], group) + count(row[:i+l]+'.'+row[i+l+1:], group)
        else:
            return count(row[:i]+'#'+row[i+1:], group) + count(row[:i]+'.'+row[i+1:], group)

print(f"Part 1: {sum([count(rows[i],groups[i]) for i in range(len(rows))])}")

## Part 2

rows = [((x[0]+'?')*5)[:-1] for x in lines_raw]
groups = [[int(y) for y in x[1].split(',')]*5 for x in lines_raw]

cache = {}
def count_cache(row,group):
    if (row,tuple(group)) in cache:
        return cache[(row,tuple(group))]
    else:
        cache[row,tuple(group)] = count(row,group)
        return cache[row,tuple(group)]


def count(row, group):
    if (row,tuple(group)) in cache:
        return cache[(row,tuple(group))]
    # print(row, group)
    i = 0
    row = row.strip('.')+'.'
    if row == '.':
        if group == []:
            return 1
        else:
            return 0
    else:
        if row[i] == '#':
            l = min([k for k in range(len(row)) if row[i+k]!='#'])
            if group == []:
                cache[(row,tuple(group))] = 0
                return 0
            elif l > group[0]:
                cache[(row,tuple(group))] = 0
                return 0
            elif l < group[0] and row[i+l] == '.':
                cache[(row,tuple(group))] = 0
                return 0
            elif l == group[0] and row[i+l] == '.':
                cache[(row,tuple(group))] = count(row[i+l:], group[1:])
                return cache[(row,tuple(group))]
            else:
                cache[(row,tuple(group))] = count(row[:i+l]+'#'+row[i+l+1:], group) + count(row[:i+l]+'.'+row[i+l+1:], group)
                return cache[(row,tuple(group))]
        else:
            cache[(row,tuple(group))] = count(row[:i]+'#'+row[i+1:], group) + count(row[:i]+'.'+row[i+1:], group)
            return cache[(row,tuple(group))]

print(f"Part 2: {sum([count_cache(rows[i],groups[i]) for i in range(len(rows))])}")