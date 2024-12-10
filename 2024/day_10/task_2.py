with open('input.txt') as f:
    lines = [[int(c) for c in line.strip()] for line in f]

rows = len(lines)
cols = len(lines[0])
zeros = [(i, j) for i, r in enumerate(lines) for j, c in enumerate(r) if c == 0]

directions = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}
visited = set()


def _valid(x: (), n: ()) -> bool:
    return 0 <= n[0] < rows and 0 <= n[1] < cols and lines[x[0]][x[1]]+1 == lines[n[0]][n[1]]


def _next(x: (), s: ()) -> (int, int):
    return x[0]+s[0], x[1]+s[1]


def _all_next(x: ()) -> []:
    steps = {}
    for d, s in directions.items():
        n = _next(x=x, s=s)
        if _valid(x=x, n=n):
            steps[s] = n
    return steps


def _iter_next(z: (), x: (), depth: int) -> int:

    print(f'{depth*" "}{lines[x[0]][x[1]]}')

    if lines[x[0]][x[1]] == 9:
        return 1

    total = 0
    for s, n in _all_next(x=x).items():

        total += _iter_next(z=z, x=n, depth=depth+1)

    return total


rez = 0
for p in zeros:
    trailheads: int = _iter_next(z=p, x=p, depth=0)
    print(f'z: {p}, total: {trailheads}')
    rez += trailheads


print(f'\nResult: {rez}')
