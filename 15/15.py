with open("input.txt", 'r') as file:
    sequence = [x.strip('\n') for x in file.read().split(',')]


print(sequence)

def my_hash(string):
    result = 0
    for x in string:
        result = ((result + ord(x))*17)%256
    return result


# print(sum([my_hash(x) for x in sequence]))

def label(string):
    return string.strip('-=1234567890')

def symbol(string):
    return string.strip('1234567890abcdefghijklmnopqrstuvwxyz')

def focus(string):
    return int(string.strip('-=abcdefghijklmnopqrstuvwxyz'))

d = {}
for x in sequence:
    if symbol(x) == '-':
        try:
            d[my_hash(label(x))].pop(label(x))
            if d[my_hash(label(x))] == {}:
                del d[my_hash(label(x))]
        except:
            pass
    else:
        if d.get(my_hash(label(x))) == None:
            d[my_hash(label(x))] = { label(x): focus(x)}
        else:
            d[my_hash(label(x))][label(x)] = focus(x)
        



focusing_power = sum([(x+1)*sum([list(d[x].values())[i]*(i+1) for i in range(len(d[x]))]) for x in d])


print(focusing_power)