from task_1 import run, nodes

surrounding_factors = [
    (-1, -1, 1),  # top-left
    (0, -1, 2),   # left
    (-1, 0, 4),   # top
    (0, 0, 8)     # current
]
double_cases = [6, 9]
flat_cases = [0, 3, 5, 10, 12, 15]


def _surroundings(x: (), r: int, c: int) -> int:
    return sum(((r + delta_r, c + delta_c) in nodes[x]) * factor
               for delta_r, delta_c, factor in surrounding_factors)


def _edges(x: (), _) -> int:
    rows = set(i for i, j in nodes[x])
    cols = set(j for i, j in nodes[x])

    corners, double = set(), 0
    for r in range(min(rows), max(rows) + 2):
        for c in range(min(cols), max(cols) + 2):

            case = _surroundings(x=x, r=r, c=c)
            if case in double_cases:
                double += 1

            if case not in flat_cases:
                corners.add((r, c))

    return len(corners) + double


if __name__ == '__main__':

    run(edges=_edges)
