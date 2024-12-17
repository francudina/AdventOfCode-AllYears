from itertools import groupby

with open('input_2.txt') as f:
    lines = [list(line.strip()) for line in f]

lines = [list(g) for k, g in groupby(lines, key=bool) if k]
warehouse, commands = lines[0], [j for i in lines[1] for j in i]

rows = len(warehouse)
cols = len(warehouse[0])

position: () = [(i, j) for i in range(rows) for j in range(cols) if warehouse[i][j] == '@'][0]
moves = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}


def _print():
    for row in warehouse:
        print('\t'+''.join(row))
    print('\n')


def _test(x: ()) -> bool:
    return 1 <= x[0] < rows - 1 and 2 <= x[1] < cols - 2


def _clone() -> []:
    return [row[:] for row in warehouse]


def _shift(x: (), d: str) -> ():
    global warehouse
    cursor = warehouse[x[0]][x[1]]
    s: () = moves[d]
    n = x[0]+s[0], x[1]+s[1]
    if not _test(x=n):
        return None

    c = warehouse[n[0]][n[1]]
    if c == '#':
        return None

    if c in ('[', ']') and d in ('<', '>'):
        n = _shift(x=n, d=d)
        if n:
            return _shift(x=n, d=d)
        else:
            return None

    if c in ('[', ']') and d in ('^', 'v'):
        check_next = [n]
        if c == '[':
            right = n[0], n[1]+1
            check_next.append(right)
        else:
            left = n[0], n[1]-1
            check_next.append(left)

        w_backup = _clone()
        for t in check_next:
            p = _shift(x=t, d=d)
            if not p:
                warehouse = w_backup
                return None

    warehouse[n[0]][n[1]] = cursor
    warehouse[x[0]][x[1]] = '.'

    return n if cursor == '@' else (x[0]-s[0], x[1]-s[1])


for command in commands:
    p_next = _shift(x=position, d=command)
    if p_next:
        position = p_next

rez = sum(100*i + j for i in range(1, rows-1) for j in range(1, cols-1) if warehouse[i][j] == '[')
print(f'Result: {rez}')
