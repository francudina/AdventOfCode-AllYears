import heapq
from collections import defaultdict


with open('input.txt') as f:
    lines = [line.strip() for line in f]


def dijkstra(graph: {}, start: (), end_nodes: []):
    all_shortest_paths = []
    min_cost = float('inf')
    pq = [(0, s := 0, start, [start])]
    path_costs = defaultdict(lambda: float('inf')) | {start: 0}

    while pq:
        cost, _, current_node, path = heapq.heappop(pq)
        if cost > min_cost:
            break

        if current_node in end_nodes:
            if cost < min_cost:
                min_cost = cost
                all_shortest_paths = [path]
            elif cost == min_cost:
                all_shortest_paths.append(path)
            continue

        for neighbor, edge_cost in graph[current_node].items():
            new_cost = cost + edge_cost
            if new_cost <= path_costs[neighbor]:
                path_costs[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, s := s + 1, neighbor, path + [neighbor]))

    return all_shortest_paths, min_cost


def parse():
    grid = {(y + x * 1j): c for y, l in enumerate(lines) for x, c in enumerate(l)}
    graph = defaultdict(dict)

    for n in grid:
        if grid[n] == '#':
            continue

        graph[(n, True)][(n, False)] = 1000
        graph[(n, False)][(n, True)] = 1000

        for d in [-1, 1j, 1, -1j]:
            if grid[n + d] != '#':
                graph[(n, bool(d.imag))][(n + d, bool(d.imag))] = 1

    start = [m for m in grid if grid[m] == 'S'][0]
    end = [m for m in grid if grid[m] == 'E'][0]

    return graph, start, end


if __name__ == '__main__':

    graph, start, end = parse()
    path, cost = dijkstra(graph=graph, start=(start, True), end_nodes=[(end, True), (end, False)])

    print(f'Result: {cost}')
