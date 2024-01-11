import sys
sys.setrecursionlimit(10000)

with open("input.txt", 'r') as file:
    lines = [line.strip('\n') for line in file.readlines()]

forest = {a + b*1j: lines[a][b] for a in range(len(lines)) for b in range(len(lines[0])) if lines[a][b] != '#'}

moves = {'.':[1,-1,1j,-1j], '>' : [1j], '<': [-1j], 'v': [1], '^': [-1]}


def walk(current, history):
    history[current] = 1
    if current == len(lines)-1 + (len(lines[0])-2)*1j:
        return len(history) - 1
    legal_moves = [move for move in moves[forest[current]] if forest.get(current+move) is not None and history.get(current+move) is None]
    if len(legal_moves) == 0:
        return
    if len(legal_moves) == 1:
        return walk(current + legal_moves[0], history)
    else:
        return [walk(current + move, history.copy()) for move in legal_moves]


def flatten(values):
    flattened = []
    for value in values:
        try:
            flattened.extend(flatten(value))
        except:
            flattened.append(value)
    return flattened

print(max(x for x in flatten(walk(1j,{})) if x is not None))