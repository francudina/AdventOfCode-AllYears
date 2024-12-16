from statistics import variance

from task_1 import robots

rows = 103
cols = 101


def _move(robot: (), step: (), seconds: int) -> ():
    r = (robot[0] + step[0] * seconds) % rows
    c = (robot[1] + step[1] * seconds) % cols
    return r, c


def run():
    bx, c_var = 0, 10 * 100
    by, r_var = 0, 10 * 1000

    for t in range(max(cols, rows)):

        moves: [] = [_move(robot=robot, step=step, seconds=t) for robot, step in robots()]

        r_v = variance([m[0] for m in moves])
        c_v = variance([m[1] for m in moves])

        if r_v < r_var:
            by, r_var = t, r_v

        if c_v < c_var:
            bx, c_var = t, c_v

    rez = bx + (pow(cols, -1, rows) * (by - bx)) % rows * cols
    print(f'Result: {rez}')


if __name__ == '__main__':
    run()
