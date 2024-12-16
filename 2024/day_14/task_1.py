import re
import math
from collections import defaultdict

rows = 103
cols = 101


def _num(s: str) -> []:
    m = list(map(int, re.findall(r'-?\d+', s)))[::-1]
    return m[2:], m[:2]


def robots() -> {}:
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
    return [_num(s=l) for l in lines]


def run(seconds: int):
    quadrant = defaultdict(int)
    for (r, c), (step_r, step_c) in robots():

        r = (r + step_r * seconds) % rows
        c = (c + step_c * seconds) % cols

        margin_r, margin_c = rows // 2, cols // 2
        if margin_r == r or margin_c == c:
            continue

        q = int(r > margin_c) * 2 + int(c > margin_c)
        quadrant[q] += 1

    rez = math.prod(quadrant.values())
    print(f'Result: {rez}')


if __name__ == '__main__':
    run(seconds=100)
