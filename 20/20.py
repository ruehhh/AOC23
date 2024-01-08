import copy
import math


with open("input.txt", 'r') as file:
    lines = [x.strip('\n') for x in file.readlines()]

d = {}
for x in lines:
    if "broadcaster" in x:
        d["broadcaster"] = {"type":"broadcaster", "state":0, "outputs": x[x.index('>')+2:].split(', ')}
    elif x[0] == '%':
        d[x[1:3]] = {"type":'%', "state":0, "outputs": x[x.index('>')+2:].split(', ')}
    else:
        d[x[1:3]] = {"type":'&', "state":{}, "outputs": x[x.index('>')+2:].split(', ')}
for x in lines:
    if x[0] == '&':
        d[x[1:3]] = {"type":'&', "state":{z:0 for z in d if x[1:3] in d[z]["outputs"]}, "outputs": x[x.index('>')+2:].split(', ')}
d['rx'] = {"type":"output", "state":0}

def state(system):
    print('\n'.join([f"{x} in state {system[x]['state']}" for x in system if x != 'broadcaster']))


def update_state(initial_queue):
    queue = copy.deepcopy(initial_queue)
    high_count = 0
    low_count = 0
    while queue != []:
        mod_out, pulse, mod_in = queue[0][0], queue[0][1], queue[0][2]
        queue.pop(0)
        if pulse == 1:
            high_count += 1
        else:
            low_count +=1
        if mod_in == 'rx':
            pass
        # is it flip-flop?
        elif d[mod_in]["type"] == "broadcaster":
            queue += [[mod_in, pulse, x] for x in d[mod_in]["outputs"]]
        elif d[mod_in]["type"] == '%':
            # implement flip-flop logic
            if pulse == 0:
                d[mod_in]["state"] = 1 - d[mod_in]["state"]
                queue += [[mod_in, d[mod_in]["state"],x] for x in d[mod_in]["outputs"]]
        elif d[mod_in]["type"] == '&':
            d[mod_in]["state"][mod_out] = pulse
            if all([d[mod_in]["state"][x] == 1 for x in d[mod_in]["state"]]) == 1:
                queue += [[mod_in, 0, x] for x in d[mod_in]["outputs"]]
            else:
                queue += [[mod_in, 1, x] for x in d[mod_in]["outputs"]]
    return [high_count, low_count]


initial = [['', 0, 'broadcaster']]


k = 0
high_count = 0
low_count = 0
while k < 1000:
    update = update_state(initial)
    high_count += update[0]
    low_count += update[1]
    k += 1

print(f"Part 1 : {high_count*low_count}")

### PT 2


def cycle_lengths(initial_queue, k):
    queue = copy.deepcopy(initial_queue)
    cycle_length = {'mr':[],'kk':[],'gl':[],'bb':[]}
    while queue != []:
        mod_out, pulse, mod_in = queue[0][0], queue[0][1], queue[0][2]
        if mod_out in cycle_length and pulse == 1:
            d[mod_out] += [k]
        queue.pop(0)
        if mod_in == 'rx':
            pass
        # is it flip-flop?
        elif d[mod_in]["type"] == "broadcaster":
            queue += [[mod_in, pulse, x] for x in d[mod_in]["outputs"]]
        elif d[mod_in]["type"] == '%':
            # implement flip-flop logic
            if pulse == 0:
                d[mod_in]["state"] = 1 - d[mod_in]["state"]
                queue += [[mod_in, d[mod_in]["state"],x] for x in d[mod_in]["outputs"]]
        elif d[mod_in]["type"] == '&':
            d[mod_in]["state"][mod_out] = pulse
            if all([d[mod_in]["state"][x] == 1 for x in d[mod_in]["state"]]) == 1:
                queue += [[mod_in, 0, x] for x in d[mod_in]["outputs"]]
            else:
                queue += [[mod_in, 1, x] for x in d[mod_in]["outputs"]]
    return cycle_length


k = 0
cycle_length = {'mr':[],'kk':[],'gl':[],'bb':[]}

## Run for long enough to see cycles
while any([len(cycle_length[x]) < 2 for x in cycle_length]):
    queue = initial = [['', 0, 'broadcaster']]
    while queue != []:
        mod_out, pulse, mod_in = queue[0][0], queue[0][1], queue[0][2]
        if mod_out in cycle_length and pulse == 1:
            cycle_length[mod_out] += [k]
        queue.pop(0)
        if mod_in == 'rx':
            pass
        # is it flip-flop?
        elif d[mod_in]["type"] == "broadcaster":
            queue += [[mod_in, pulse, x] for x in d[mod_in]["outputs"]]
        elif d[mod_in]["type"] == '%':
            # implement flip-flop logic
            if pulse == 0:
                d[mod_in]["state"] = 1 - d[mod_in]["state"]
                queue += [[mod_in, d[mod_in]["state"],x] for x in d[mod_in]["outputs"]]
        elif d[mod_in]["type"] == '&':
            d[mod_in]["state"][mod_out] = pulse
            if all([d[mod_in]["state"][x] == 1 for x in d[mod_in]["state"]]) == 1:
                queue += [[mod_in, 0, x] for x in d[mod_in]["outputs"]]
            else:
                queue += [[mod_in, 1, x] for x in d[mod_in]["outputs"]]
    k += 1

print(f"Part 2 : {math.prod([cycle_length[x][1]-cycle_length[x][0] for x in cycle_length])}")
