with open("input_test.txt", 'r') as file:
    lines = [x.strip('\n') for x in file.readlines()]

d = {a+b*1j: lines[a][b] for a in range(len(lines)) for b in range(len(lines[0])) if lines[a][b] != '#'}


steps = [1,-1,1j,-1j]


### step

k=0
while k < 5000:
    d_aux = {}
    for x in d:
        if d[x] == 'S':
            d[x] = '.'
            for step in steps:
                if d.get(x+step) is not None:
                    d_aux[x+step] = 'S'
    for x in d_aux:
        d[x] = d_aux[x]
    k+=1


print(len([x for x in d if d[x] == 'S']))
