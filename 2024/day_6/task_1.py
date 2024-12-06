with open('input.txt') as f:
    area_map = [list(line.strip()) for line in f]

rows, cols = len(area_map), len(area_map[0])

position = [(i, j) for i in range(rows) for j in range(cols) if area_map[i][j] == '^'][0]
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

area_map[position[0]][position[1]] = 'X'


def a_print(area: []):
    for row in area:
        print(''.join(row))


def next(area: [], c: (), s: (), o: () = None, log: bool = False) -> (int, [], int):
    n, places = (c[0], c[1]), []
    wall = False
    while True:
        i, j = n[0]+s[0], n[1]+s[1]
        if i < 0 or i >= rows or j < 0 or j >= cols:
            wall = True
            break
        if area[i][j] == '#' or (i, j) == o:
            break

        n = (i, j)
        if area[i][j] == '.':
            places.append(n)
        area[i][j] = 'X'

    if log:
        print(f'\nplaces: {len(places)}')
        a_print(area)

    return n, places, wall


def next_path(init: ()) -> []:
    current, path = (init[0], init[1]), []
    area, s_ind = [row[:] for row in area_map], 0
    while True:
        current, visited, end = next(area=area, c=current, s=steps[s_ind])
        path += visited
        if end:
            break
        s_ind = (s_ind + 1) % len(steps)
    return path


if __name__ == '__main__':

    rez: [] = next_path(init=position)

    print(f'Result: {len(rez) + 1}')
