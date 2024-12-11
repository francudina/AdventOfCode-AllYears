from functools import cache

with open('input.txt') as f:
    stones = [[int(c) for c in line.split()] for line in f][0]


def _split(stone: int) -> []:
    s: str = str(stone)
    l: int = len(s)

    if stone == 0:
        return [1]
    elif l % 2 == 0:
        i = int(l/2)
        return [int(s[:i]), int(s[i:])]
    else:
        return [stone*2024]


@cache
def stone_split(stone: int, blink: int) -> []:
    if blink == 0:
        return 1
    total = 0
    for next_stone in _split(stone=stone):
        total += stone_split(stone=next_stone, blink=blink-1)
    return total


def run(blink: int):
    rez = 0
    for stone in stones:
        rez += stone_split(stone=stone, blink=blink)
    print(f'Result: {rez}')


if __name__ == '__main__':

    run(blink=25)
