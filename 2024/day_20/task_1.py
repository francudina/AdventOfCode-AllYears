from itertools import combinations


with open('input.txt') as f:
    track = [line.strip() for line in f]


def _grid() -> (dict, tuple, tuple):
    grid = {
        (i + j * 1j): c
        for i, r in enumerate(track)
        for j, c in enumerate(r)
        if c != '#'
    }
    start = [k for k in grid if grid[k] == 'S'][0]
    end = [k for k in grid if grid[k] == 'E'][0]
    return grid, start, end


def _next(x: ()) -> []:
    return [x + s for s in [1, -1, -1j, +1j]]


def _init_path(grid: {}, start: (), end: ()) -> {}:
    path = {start: 0}
    current = start
    while current != end:
        for n in _next(x=current):
            if n not in grid or n in path:
                continue

            path[n] = path[current] + 1
            current = n
            break

    return path


def _cheats(path: [], cheat_size: int) -> int:
    cheats = 0
    for (x, dist_x), (y, dist_y) in combinations(path.items(), 2):
        d = abs((x - y).real) + abs((x - y).imag)
        if d > cheat_size:
            continue
        dist_yx: int = abs(dist_y - dist_x)
        if dist_yx - d < 100:
            continue
        cheats += 1
    return cheats


def run(cheat_size: int) -> int:
    grid, start, end = _grid()
    path: [] = _init_path(grid=grid, start=start, end=end)
    return _cheats(path=path, cheat_size=cheat_size)


if __name__ == '__main__':

    print(f'Result: {run(cheat_size=2)}')
