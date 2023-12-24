import numpy as np

with open("input.txt", 'r') as file:
    lines = [x.split() for x in file.read().split('\n\n')]

# print([len(line) for line in lines])

def horiz(chunk):
    i = 0
    while i < len(chunk)-1:
        if all([chunk[i-k] == chunk[i+1+k] for k in range(min([i+1,len(chunk)-i-1]))]):
            return i+1
        else:
            i += 1
    return 0

def transpose(chunk):
    return [ ''.join([chunk[i][j] for i in range(len(chunk))]) for j in range(len(chunk[0])) ]


sum = 0
for chunk in lines:
    hc = horiz(chunk)
    if hc > 0:
        sum += 100*hc
    else:
        sum += horiz(transpose(chunk))
    
print(sum)