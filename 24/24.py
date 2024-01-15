import numpy as np
with open("input.txt") as file:
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

a = 200000000000000
b = 400000000000000

print(f"Part 1: {len([z for z in [intersection(x[i], v[i], x[j], v[j]) for i in range(len(x)) for j in range(i, len(x))] if z is not None and a <= z[0] < b and a <= z[1] < b])}")

## Part 2

x = [np.array([np.float64(x[:x.find('@')].split(',')[i]) for i in range(3)]) for x in lines]
v = [np.array([np.float64(x[x.find('@')+1:].split(',')[i]) for i in range(3)]) for x in lines]

## Initial x, v of rock is xr, vr we have xr + t[i]*vr = x[i] + t[i]*v[i] for all i
## This implies that (xr-x[i]) x (vr-v[i]) = 0, or xr x vr = - v[i] x xr + x[i] x vr- x[i] x v[i])
## We can equate two pairs of these to get 6 equations for the 6 unknowns (xr, vr)
## x[1] x v[1] - x[0] x v[0] = (v[0] - v[1]) x xr + (x[1] - x[0]) x vr 
## x[2] x v[2] - x[0] x v[0] = (v[0] - v[2]) x xr + (x[2] - x[0]) x vr 

## Should work for any choice of three points, but rounding errors seem to occur for some choices
i, j, k = 10, 1, 2

v01 = v[i] - v[j]
v02 = v[i] - v[k]
x01 = x[j] - x[i]
x02 = x[k] - x[i]

row1 = [0, -v01[2], v01[1], 0, -x01[2], x01[1]]
row2 = [v01[2], 0, -v01[0], x01[2], 0, -x01[0]]
row3 = [-v01[1], v01[0], 0,-x01[1], x01[0], 0]
row4 = [0, -v02[2], v02[1], 0, -x02[2], x02[1]]
row5 = [v02[2], 0, -v02[0], x02[2], 0, -x02[0]]
row6 = [-v02[1], v02[0], 0,-x02[1], x02[0], 0]

rhs = list(np.cross(x[j],v[j])- np.cross(x[i], v[i])) + list(np.cross(x[k],v[k])- np.cross(x[i], v[i]))
mat = [row1, row2, row3, row4, row5, row6]

print(f"Part 2: {int(sum([x for x in np.linalg.solve(mat, rhs)[:3]]))}")
