import numpy as np

with open("input.txt", 'r') as file:
    lines = [x.split() for x in file.read().split('\n\n')]

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

summary = 0
for chunk in lines:
    hc = horiz(chunk)
    if hc > 0:
        summary += 100*hc
    else:
        summary += horiz(transpose(chunk))
    
print(f"Part 1: {summary}")


## Part 2

with open("input.txt", 'r') as file:
    lines = [x.split() for x in file.read().split('\n\n')]


def horiz_2(chunk):
    i = 0
    while i < len(chunk)-1:
        if sum([not(chunk[i-k][j] == chunk[i+1+k][j]) for j in range(len(chunk[0])) for k in range(min([i+1,len(chunk)-i-1]))]) == 1:
            return i+1
        else:
            i += 1
    return 0

summary = 0
for chunk in lines:
    hc = horiz_2(chunk)
    if hc > 0:
        summary += 100*hc
    else:
        summary += horiz_2(transpose(chunk))
    
print(f"Part 2: {summary}")