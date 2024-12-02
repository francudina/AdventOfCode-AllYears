def read() -> []:
    with open('input.txt') as f:
        return [[int(num) for num in l.strip().split()] for l in f.readlines()]


def scan(line: []) -> int:
    prev = None
    for i in range(len(line) - 1):

        d = line[i + 1] - line[i]
        if not (1 <= abs(d) <= 3):
            return 0

        curr = True if d > 0 else False

        if prev is None:
            prev = curr
        elif prev != curr:
            return 0

    return 1


if __name__ == '__main__':

    rez = sum(scan(l) for l in read())
    print(f'Result: {rez}')
