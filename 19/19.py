import operator
import json

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
            # print(command)
            if ':' in command:
                ineq, out = command.split(':')
                if ops[ineq[1]](part[ineq[0]], int(ineq[2:])):
                    # print('TRUE')
                    return parse(part, out)
            else:
                return parse(part, command)


def eval_part(part):
    return part['x']+part['m']+part['a']+part['s']


print(sum([eval_part(part) for part in parts if parse(part, 'in') == 1]))
