from itertools import groupby

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

print("Max result is:", max([sum([int(i) for i in group]) for key, group in groupby(lines, lambda x: len(x) != 0) if key]))
