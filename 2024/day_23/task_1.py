from itertools import combinations
from collections import defaultdict


with open('input.txt') as f:
    lines = [line.strip().split('-') for line in f]

sets = defaultdict(set)
for f, s in lines:
    sets[f].add(s)
    sets[s].add(f)


tripplets = list(combinations(sets.keys(), 3))

groups = set()
for cluster in tripplets:

    if not any(n.startswith('t') for n in cluster):
        continue

    g1 = sets[cluster[0]] | {cluster[0]}
    g2 = sets[cluster[1]] | {cluster[1]}
    g3 = sets[cluster[2]] | {cluster[2]}

    c = set(cluster)
    i = g1 & g2 & g3 & c
    if len(i) == 3:
        groups.add(','.join(c))

print(f'Result: {len(groups)}')
