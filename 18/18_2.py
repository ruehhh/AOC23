with open("input.txt", 'r') as file:
    lines = [[int(x.strip()[-2]), int(x.strip()[-7:-2], 16)] for x in file.readlines()]

d = {3: -1, 1: 1, 0: 1j, 2: -1j}


polygon = [0]
current = 0

for line in lines:
    current += d[line[0]]*line[1]
    polygon.append(current)


perimeter = sum([x[1] for x in lines])


def shoelace(p):
    return abs(sum([p[i].real*p[i+1].imag - p[i].imag*p[i+1].real for i in range(len(p)-1)]))/2 + perimeter/2 + 1


print(shoelace(polygon))

# h_min = int(min([x.real for x in dig]))
# w_min = int(min([x.imag for x in dig]))

# print(h_min,w_min)

# dig = {x - h_min - w_min*1j : dig[x] for x in dig}



# count = len(dig)
# row = 0
# col = 0
# h_max = int(max([x.real for x in dig]))
# w_max = int(max([x.imag for x in dig]))
# in_out = 0

# while row < h_max+1:
#     col = 0
#     in_out = 0
#     while col < w_max:
#         if dig.get(row+col*1j) is None:
#             col += 1
#         else:
#             edge_length = next((l for l in range(w_max+2) if dig.get(row+col*1j+l*1j) is None))
#             if dig.get(row+1+col*1j) == dig.get(row-1+(col+edge_length-1)*1j):
#                 in_out = 1 - in_out
#             col += edge_length
#             if in_out == 1:
#                 # print(f"Filling at row {row} col {col + edge_length}")
#                 dig_length = next((l for l in range(w_max+1) if dig.get(row+col*1j+l*1j) is not None))
#                 count += dig_length
#                 col += dig_length
#                 # print(f"Count + {dig_length} is {count}")
#     row += 1

# print(count)
