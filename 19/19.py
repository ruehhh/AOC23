import operator
import json
import math
import copy

with open("input.txt", 'r') as file:
    [workflows_block, parts_block] = file.read().split('\n\n')
    workflows = {x[:x.find('{')]: x[x.find('{')+1:-1] for x in workflows_block.split()}
    parts = [json.loads(x.replace('x=', '"x":').replace('m=', '"m":').replace('a=', '"a":').replace('s=', '"s":')) for x in parts_block.split()]


workflows['A'] = 'A'
workflows['R'] = 'R'

ops = {'<': operator.lt, '>': operator.gt}


def parse(part, code):
    commands = workflows[code].split(',')
    for command in commands:
        if command == 'A':
            return 1
        elif command == 'R':
            return 0
        else:
            if ':' in command:
                ineq, out = command.split(':')
                if ops[ineq[1]](part[ineq[0]], int(ineq[2:])):
                    return parse(part, out)
            else:
                return parse(part, command)


def eval_part(part):
    return part['x']+part['m']+part['a']+part['s']


print(f"Part 1: {sum([eval_part(part) for part in parts if parse(part, 'in') == 1])}")

## Part 2

with open("input.txt", 'r') as file:
    [workflows_block, parts_block] = file.read().split('\n\n')
    workflows = {x[:x.find('{')]: x[x.find('{')+1:-1] for x in workflows_block.split()}


workflows['A'] = 'A'
workflows['R'] = 'R'
workflows['TEST'] = 'x<2001:A,m<1001:A'

ops = {'<': operator.lt, '>': operator.gt}

parts_init = {'x':[1,4000],'m':[1,4000],'a':[1,4000],'s':[1,4000]}


def eval_ranges(parts):
    return math.prod([parts[x][1]-parts[x][0]+1 for x in parts])


# print(eval_ranges(parts_init))



def count_accepted(parts, code):
    count = 0
    commands = workflows[code].split(',')
    for command in commands:
        if command == 'A':
            count += eval_ranges(parts)
        elif command == 'R':
            count += 0
        else:
            passed = copy.deepcopy(parts)
            if ':' in command:
                ineq, out = command.split(':')
                z, op, m = ineq[0], ineq[1], int(ineq[2:])
                if parts[z] == []:
                    return 0
                if ops[op](passed[z][0],m) and ops[op](passed[z][1],m):
                    parts[z] = []
                    pass
                elif op == '<':
                    passed[z] = [passed[z][0], m-1]
                    parts[z] = [m, parts[z][1]]
                else:
                    passed[z] = [m+1, passed[z][1]]
                    parts[z] = [parts[z][0], m]
                count += count_accepted(passed, out)
            else:
                count += count_accepted(passed, command)
    return count



print(f"Part 2: {count_accepted(parts_init, 'in')}")