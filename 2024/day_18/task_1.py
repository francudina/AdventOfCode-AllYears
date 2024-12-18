import heapq


with open('input.txt') as f:
    lines = [line.strip() for line in f]


steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
size = 71
use_bits = 1024


def _test(x: ()) -> bool:
    return 0 <= x[0] < size and 0 <= x[1] < size


def _reverse(x: (), history: {}) -> []:
    path = []
    while x:
        path.append(x)
        x = history[x]
    return path[::-1]


def bits_load(limit_bits: bool = True) -> []:
    bits = [tuple(map(int, l.split(',')[::-1])) for l in lines]
    return bits[:use_bits] if limit_bits else bits


def generate(bits: []):
    graph = {(r, c): set() for r in range(size) for c in range(size)}
    for r, c in graph:
        x = r, c
        if x in bits:
            continue

        for s_r, s_c in steps:
            n = r + s_r, c + s_c
            if not _test(x=n):
                continue
            if n in bits:
                continue

            graph[(r, c)].add(n)

    return graph


def dijkstra(graph: {}, start: (), end: ()):
    d, moves = {v: float('inf') for v in graph}, {}
    moves[start] = None
    d[start] = 0
    pq = [(0, start)]
    while pq:
        dist, u = heapq.heappop(pq)
        if u == end:
            return _reverse(x=u, history=moves)
        for v in graph[u]:
            n = d[u] + 1
            if n < d[v]:
                d[v], moves[v] = n, u
                heapq.heappush(pq, (n, v))
    return None


if __name__ == '__main__':

    bits = bits_load()
    graph: {} = generate(bits=bits)
    path = dijkstra(graph=graph, start=(0, 0), end=(size-1, size-1))

    rez = len(path) - 1
    print(f'Result: {rez}')
