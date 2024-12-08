from itertools import product
from collections import defaultdict

with open('input.txt') as f:
    area = [list(line.strip()) for line in f]

rows = len(area)
cols = len(area[0])


def places() -> {}:
    types = defaultdict(list)
    for i in range(rows):
        for j in range(cols):
            c = area[i][j]
            if c != '.':
                types[c].append((i, j))
    return types


def combinations(values: []) -> []:
    return [(x, y) for x, y in product(values, repeat=2) if x != y]


def p_dist(x: (), y: ()) -> (int, int):
    return x[0] - y[0], x[1] - y[1]


def next_an(x: (), dist: ()) -> (int, int):
    return x[0] + dist[0], x[1] + dist[1]


def valid(x: (), visited: set) -> bool:
    v: bool = 0 <= x[0] < rows and 0 <= x[1] < cols
    if v:
        visited.add(x)
    return v


if __name__ == '__main__':

    antinodes = set()
    for antenna, locations in places().items():
        pairs: [] = combinations(values=locations)

        for a1, a2 in pairs:
            dist1, dist2 = p_dist(x=a1, y=a2), p_dist(x=a2, y=a1)
            an1, an2 = next_an(x=a1, dist=dist1), next_an(x=a2, dist=dist2)

            valid(x=an1, visited=antinodes)
            valid(x=an2, visited=antinodes)

    rez = len(antinodes)
    print(f'Result: {rez}')
