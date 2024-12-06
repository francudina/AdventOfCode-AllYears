from task_1 import *


def next_2(area: [], c: (), s: (), o: () = None, log: bool = False) -> (int, set):
    n, turns = (c[0], c[1]), set()
    wall = False
    while True:
        i, j = n[0]+s[0], n[1]+s[1]
        if i < 0 or i >= rows or j < 0 or j >= cols:
            wall = True
            break
        if area[i][j] == '#' or (i, j) == o:
            break

        n = (i, j)
        area[i][j] = 'X'

        turns.add((n, s))

    if log:
        print(f'\nplaces: {len(turns)}')
        a_print(area)

    return n, turns, wall


def check_obstacle(init: (), obstacle: () = None) -> bool:
    current, visited = (init[0], init[1]), set()
    area, s_ind = [row[:] for row in area_map], 0
    area[obstacle[0]][obstacle[1]] = 'O'
    while True:
        visited.add((current, steps[s_ind]))
        current, turns, wall = next_2(area=area, c=current, s=steps[s_ind], o=obstacle, log=False)

        if wall:
            return False

        if visited.intersection(turns):
            return True

        visited.update(turns)
        s_ind = (s_ind + 1) % len(steps)


options = next_path(init=position)

rez = 0
for o in options:
    rez += int(check_obstacle(init=position, obstacle=o))

print(f'Result: {rez}')
