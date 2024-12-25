from itertools import groupby
from itertools import product


with open('input.txt') as f:
    lines = [line.strip() for line in f]

lines = [list(g) for k, g in groupby(lines, key=bool) if k]
rows, cols = len(lines[0]), len(lines[0][0])


def _transpose(m: []) -> []:
    return list(map(list, zip(*m)))


def _vector(m: []) -> []:
    return [r.count('#') for r in _transpose(m=m)]


locks = [_vector(m=l) for l in lines if '#' * cols == l[0]]
keys = [_vector(m=l) for l in lines if '#' * cols == l[rows-1]]


rez = 0
for k, l in product(keys, locks):
    rez += all([k[i]+l[i] <= rows for i in range(cols)])

print(f'Result: {rez}')
