import numpy as np
with open("input.txt") as file:
    lines = [x.strip('\n') for x in file.readlines()]


x = [np.array([np.float64(x[:x.find('@')].split(',')[i]) for i in range(3)]) for x in lines]
v = [np.array([np.float64(x[x.find('@')+1:].split(',')[i]) for i in range(3)]) for x in lines]


## Initial x, v of rock is xr, vr we have xr + t[i]*vr = x[i] + t[i]*v[i] for all i
## This implies that (xr-x[i]) x (vr-v[i]) = 0, or xr x vr = - v[i] x xr + x[i] x vr- x[i] x v[i])
## We can equate two pairs of these to get 6 equations for the 6 unknowns (xr, vr)
## x[1] x v[1] - x[0] x v[0] = (v[0] - v[1]) x xr + (x[1] - x[0]) x vr 
## x[2] x v[2] - x[0] x v[0] = (v[0] - v[2]) x xr + (x[2] - x[0]) x vr 

v01 = v[0] - v[1]
v02 = v[0] - v[2]
x01 = x[1] - x[0]
x02 = x[2] - x[0]

row1 = [0, -v01[2], v01[1], 0, -x01[2], x01[1]]
row2 = [v01[2], 0, -v01[0], x01[2], 0, -x01[0]]
row3 = [-v01[1], v01[0], 0,-x01[1], x01[0], 0]
row4 = [0, -v02[2], v02[1], 0, -x02[2], x02[1]]
row5 = [v02[2], 0, -v02[0], x02[2], 0, -x02[0]]
row6 = [-v02[1], v02[0], 0,-x02[1], x02[0], 0]

rhs = list(np.cross(x[1],v[1])- np.cross(x[0], v[0])) + list(np.cross(x[2],v[2])- np.cross(x[0], v[0]))


mat = [row1, row2, row3, row4, row5, row6]

# print(rhs)
# print(mat)
print(sum(np.linalg.solve(mat, rhs)[:3]))