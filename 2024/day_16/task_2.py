from task_1 import parse, dijkstra


graph, start, end = parse()
path, cost = dijkstra(graph=graph, start=(start, True), end_nodes=[(end, True), (end, False)])

rez = len({e[0] for p in path for e in p})
print(f'Result: {rez}')
