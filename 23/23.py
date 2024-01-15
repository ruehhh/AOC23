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

print(f"Part 1: {max(x for x in flatten(walk(1j,{})) if x is not None)}")

## Part 2


def moves(x):
    return [z for z in [1,-1,1j,-1j] if forest.get(x+z) is not None]

start = 1j
end = len(lines)-1 + (len(lines[0])-2)*1j
nodes = [start] + [x for x in forest if len(moves(x)) > 2] + [end]     

history = {}
graph = {(n,m): None for n in nodes for m in nodes}

def count_lengths(node_in, current, last_move, length, history):
    # print(current)
    legal_moves = [move for move in [-1,1,1j,-1j] if move != -1*last_move and forest.get(current+move) is not None and history.get(current+move) is None]
    if current in nodes:
        graph[(node_in, current)] = length
        graph[(current, node_in)] = length
        return [count_lengths(current, current + move, move, 1, history) for move in legal_moves]
    elif len(legal_moves) == 0:
        history[current] = 1
        return
    else:
        history[current] = 1
        count_lengths(node_in, current + legal_moves[0], legal_moves[0], length + 1, history)

count_lengths(start, start, 0, 0, {})

history = {}
def walk_reduced_graph(current, history, end):
    history[current] = 1
    if current == end:
        path = list(history.keys())
        return sum(graph[(path[i], path[i+1])] for i in range(len(path)-1))
    else:
        next_nodes = [ x for x in nodes if graph.get((current, x)) is not None and history.get(x) is None]
    if len(next_nodes) == 0:
        return
    elif len(next_nodes) == 1:
        return walk_reduced_graph(next_nodes[0], history, end)
    else:
        return [walk_reduced_graph(node, history.copy(), end) for node in next_nodes]


def flatten(values):
    flattened = []
    for value in values:
        try:
            flattened.extend(flatten(value))
        except:
            flattened.append(value)
    return flattened


second = [x for x in nodes if graph[(1j,x)] is not None][0]
second_to_last = [x for x in nodes if graph[(x, end)] is not None][0]

print(f"Part 2: {graph[(1j, second)] + max([x for x in flatten(walk_reduced_graph(second, {}, second_to_last)) if x is not None]) + graph[(second_to_last, end)]}")
