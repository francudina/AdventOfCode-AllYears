from functools import cache
from collections import defaultdict


with open('input.txt') as f:
    lines = [line.strip().split('-') for line in f]

sets = defaultdict(set)
for f, s in lines:
    sets[f].add(s)
    sets[s].add(f)


@cache
def _largest(nodes: frozenset) -> frozenset:

    connected = frozenset()
    for node in nodes:

        together = {node} | _largest(nodes=nodes & sets[node])
        if len(together) > len(connected):
            connected = frozenset(together)

    return connected


rez = _largest(nodes=frozenset(sets))
rez = ','.join(sorted(rez))
print(f'Result: {rez}')
