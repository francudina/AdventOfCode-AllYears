from typing import Callable


with open('input.txt') as f:
    lines = [int(line.strip()) for line in f]


def _iter(s: int, func: Callable) -> int:
    s = func(s) ^ s
    return s % 16777216


def new(s: int, count: int) -> []:
    vals = []
    for i in range(count):
        s = _iter(s=s, func=lambda x: x << 6)
        s = _iter(s=s, func=lambda x: x >> 5)
        s = _iter(s=s, func=lambda x: x << 11)
        vals.append(s)
    return vals


if __name__ == '__main__':

    rez = sum(new(s=n, count=2000)[-1] for n in lines)
    print(f'Result: {rez}')
