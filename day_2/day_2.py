from itertools import groupby

with open('../day_1/input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

print("Total:", sum(sorted([sum([int(i) for i in group]) for key, group in groupby(lines, lambda x: len(x) != 0) if key], reverse=True)[:3]))
