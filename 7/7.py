from collections import Counter

with open("aoc23/7/input.txt", 'r') as file:
    lines_raw = file.readlines()

lines = [[i.split()[0], int(i.split()[1])] for i in lines_raw]

card_score = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}


def score_hand_type(hand):
    count = Counter(list(hand))
    hand_vals = set(list(hand))
    if len(hand_vals) == 1:
        return 7
    elif len(hand_vals) == 2:
        if max([x for x in count.values()]) == 4:
            return 6
        else:
            return 5
    elif len(hand_vals) == 3:
        if max([x for x in count.values()]) == 3:
            return 4
        else:
            return 3
    elif len(hand_vals) == 4:
        return 2
    else:
        return(1)


def score_hand(hand):
    return [score_hand_type(hand)] + [card_score[i] for i in hand]


def score_line(line):
    return score_hand(line[0])

sorted_lines = [[sorted(lines, key = score_line)[i],i+1] for i in range(len(lines)) ]

total_score = 0
for i in sorted_lines:
    total_score += i[0][1]*i[1]

print(total_score)