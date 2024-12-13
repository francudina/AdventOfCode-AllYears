import re
from itertools import groupby


with open('input.txt') as f:
    lines = [line.strip() for line in f]


prize_prefix: int = 0


def _group() -> []:
    return [list(g) for k, g in groupby(lines, key=bool) if k]


def _num(s: str) -> []:
    return [int(n) for n in re.findall(r'\d+', s)]


def _press(button_a: str, button_b: str, prize: str) -> (float, float):
    (ax, ay), (bx, by), (px, py) = _num(s=button_a), _num(s=button_b), _num(s=prize)

    px, py = int(prize_prefix + px), int(prize_prefix + py)

    a_count = (px*by - py*bx) / (ax*by - ay*bx)
    b_count = (ax*py - ay*px) / (ax*by - ay*bx)

    return a_count, b_count


def run():
    rez = 0
    for a, b, p in _group():
        A, B = _press(button_a=a, button_b=b, prize=p)

        if A.is_integer() and B.is_integer():
            rez += A*3 + B

    print(f'Result: {rez}')


if __name__ == '__main__':
    run()
