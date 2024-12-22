from functools import cache


with open('input.txt') as f:
    lines = [list(line.strip()) for line in f]

dirs = {
    '^': 1j,
    'A': 2j,
    '<': 1,
    'v': (1 + 1j),
    '>': (1 + 2j)
}
numpad = {
    '7': 0,
    '8': 1j,
    '9': 2j,
    '4': 1,
    '5': (1 + 1j),
    '6': (1 + 2j),
    '1': 2,
    '2': (2 + 1j),
    '3': (2 + 2j),
    '0': (3 + 1j),
    'A': (3 + 2j)
}
dirs_vals = dirs.values()
numpad_vals = numpad.values()


def _num(s: []) -> int:
    return int(''.join([i for i in s if i.isdigit()]))


@cache
def _directions(iters: int, reproduce_path: str) -> int:
    if iters == 0:
        return len(reproduce_path)

    start, s = dirs['A'], 0
    for c in reproduce_path:
        s += _move(dirs_vals, start=start, end=dirs[c], iters=iters)
        start = dirs[c]

    return s


def _move(valid_grid: [], start: (), end: (), iters: int) -> int | None:
    queue, min_path = [(start, '')], float('inf')
    while len(queue) != 0:

        current, output = queue.pop(0)
        if current not in valid_grid:
            continue

        if current == end:
            next_robot = _directions(reproduce_path=output + 'A', iters=iters-1)
            min_path = min(min_path, next_robot)

        n = end - current
        if n.imag < 0:
            queue.append((current - 1j, output + '<'))
        if n.imag > 0:
            queue.append((current + 1j, output + '>'))
        if n.real < 0:
            queue.append((current - 1, output + '^'))
        if n.real > 0:
            queue.append((current + 1, output + 'v'))

    return min_path


def passcode(robots: int) -> int:
    start, s = numpad['A'], 0
    for output in lines:

        total = 0
        for o in output:
            total += _move(valid_grid=numpad_vals, start=start, end=numpad[o], iters=robots)
            start = numpad[o]
        s += total * _num(s=output)

    return s


if __name__ == '__main__':

    rez = passcode(robots=1+2)
    print(f'Result: {rez}')
