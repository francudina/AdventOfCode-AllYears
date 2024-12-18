from task_1 import bits_load, generate, dijkstra, size, use_bits


possible_bits: [] = bits_load(limit_bits=False)

bits, path = [], None
for i, b in enumerate(possible_bits):
    bits.append(b)

    if i < use_bits or (path and b not in path):
        continue

    graph: {} = generate(bits=bits)
    path = dijkstra(graph=graph, start=(0, 0), end=(size - 1, size - 1))
    if path:
        continue

    print(f'Result: {b[1],b[0]}')
    break
