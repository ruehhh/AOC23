import numpy as np
with open("input_test.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]


x = [np.array([int(x[:x.find('@')].split(',')[i]) for i in range(2)]) for x in lines]
v = [np.array([int(x[x.find('@')+1:].split(',')[i]) for i in range(2)]) for x in lines]

def intersection(x1, v1, x2, v2):
    if v1[0]*v2[1] == v1[1]*v2[0]:
        return None
    else:
        m1, m2 = v1[1]/v1[0], v2[1]/v2[0]
        c1, c2 = x1[1]-m1*x1[0], x2[1]-m2*x2[0]
        xint = (c2-c1)/(m1-m2)
        yint = m1*xint + c1
        if (xint - x1[0])/v1[0] > 0 and (xint - x2[0])/v2[0] > 0:
            return np.array([xint, yint])
        else:
            return None

a = 7
b = 27

print(len([z for z in [intersection(x[i], v[i], x[j], v[j]) for i in range(len(x)) for j in range(i, len(x))] if z is not None and a <= z[0] < b and a <= z[1] < b]))
