from collections import defaultdict


with open('input.txt') as f:
    area = [list(line.strip()) for line in f]

rows = len(area)
cols = len(area[0])

steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = set()
nodes = defaultdict(set)


def _next(x: (), s: ()) -> ():
    return x[0]+s[0], x[1]+s[1]


def _test(x: ()) -> bool:
    return 0 <= x[0] < rows and 0 <= x[1] < cols


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


if __name__ == '__main__':

    rez = 0
    for i in range(rows):
        for j in range(cols):

            x = (i, j)
            if x in visited:
                continue

            b = _neighborhood(r=x, x=x)
            rez += len(nodes[x]) * b

    print(f'Result: {rez}')
