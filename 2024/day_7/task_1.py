from itertools import product


def _read() -> []:
    with open('input.txt') as f:
        return [l.strip().split(':') for l in f.readlines()]


def _combinations(n: int, values: []) -> []:
    return [list(c) for c in product(values, repeat=n)]


def _combine(operators: [], pairs: []) -> int:
    r = int(pairs[0])
    for i in range(len(operators)):
        if operators[i] == '+':
            r += int(pairs[i+1])
        elif operators[i] == '*':
            r *= int(pairs[i+1])
        elif operators[i] == '||':
            r = int(str(r) + pairs[i+1])
    return r


def run(operators: []):
    rez = 0
    for l in _read():
        left, right = int(l[0]), l[1].strip().split()

        for o in _combinations(n=len(right) - 1, values=operators):
            comb: int = _combine(operators=o, pairs=right)
            if left == comb:
                rez += left
                break

    print(f'Result: {rez}')


if __name__ == '__main__':
    run(operators=['+', '*'])
