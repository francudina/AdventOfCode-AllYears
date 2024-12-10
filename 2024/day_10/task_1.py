from typing import Callable

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


def _iter_next(z: (), x: (), depth: int, test: Callable) -> int:
    if lines[x[0]][x[1]] == 9:
        return int(test(z=z, x=x))

    return sum(_iter_next(z=z, x=n, depth=depth+1, test=test)
               for s, n in _all_next(x=x).items())


def run(test: Callable):
    rez = sum(_iter_next(z=p, x=p, depth=0, test=test)
              for p in zeros)
    print(f'\nResult: {rez}')


def _test(z: (), x: ()) -> bool:
    if (z, x) in visited:
        return False
    visited.add((z, x))
    return True


if __name__ == '__main__':
    visited = set()
    run(test=_test)
