from collections import defaultdict


with open('input.txt') as f:
    area = [list(line.strip()) for line in f]

rows = len(area)
cols = len(area[0])

steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
surrounding_factors = [
    (-1, -1, 1),  # Top-left
    (0, -1, 2),   # Left
    (-1, 0, 4),   # Top
    (0, 0, 8)     # Current position
]
double_cases = [6, 9]
flat_cases = [0, 3, 5, 10, 12, 15]

visited = set()
nodes = defaultdict(set)


def _next(x: (), s: ()) -> ():
    return x[0]+s[0], x[1]+s[1]


def _test(x: ()) -> bool:
    return 0 <= x[0] < rows and 0 <= x[1] < cols


def _surroundings(x: (), r: int, c: int) -> int:
    return sum(((r + delta_r, c + delta_c) in nodes[x]) * factor
               for delta_r, delta_c, factor in surrounding_factors)


def _edges(x: ()) -> int:
    c_possible = set(x for y, x in nodes[x])
    r_possible = set(y for y, x in nodes[x])

    corners, double = set(), 0
    for r in range(min(r_possible), max(r_possible) + 2):
        for c in range(min(c_possible), max(c_possible) + 2):

            case = _surroundings(x=x, r=r, c=c)
            if case in double_cases:
                double += 1

            if case not in flat_cases:
                corners.add((r, c))

    return len(corners) + double


def _neighborhood(r: (), x: ()) -> int:
    if x in visited:
        return 0

    visited.add(x)
    nodes[r].add(x)

    b: int = 0
    for s in steps:

        n: () = _next(x=x, s=s)
        if not _test(x=n):
            b += 1
            continue

        if area[x[0]][x[1]] != area[n[0]][n[1]]:
            b += 1
            continue

        b += _neighborhood(r=r, x=n)

    return b


rez = 0
for i in range(rows):
    for j in range(cols):

        if (i, j) in visited:
            continue

        b = _neighborhood(r=(i, j), x=(i, j))
        e = _edges(x=(i, j))
        rez += len(nodes[(i, j)]) * e

print(f'Result: {rez}')
