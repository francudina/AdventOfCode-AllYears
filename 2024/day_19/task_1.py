from functools import cache


with open('input.txt') as f:
    lines = [line.strip() for line in f]

stripes, designs = lines[0].split(', '), lines[2:]


@cache
@cache
def match(d: str) -> int:
    if len(d) == 0:
        return True
    total = 0
    for s in stripes:
        if d.startswith(s):
            total += match(d.removeprefix(s))
    return total


def run():
    rez = 0
    for d in designs:
        if match(d):
            rez += 1
    print(f'Result: {rez}')


if __name__ == '__main__':
    run()
