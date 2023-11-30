from itertools import groupby


def row_stack(row: [str], N=4):
    return [list(filter(str.isalnum, g)) for g in [row[n:n + N] for n in range(0, len(row), N)]]


def get_stack(stack_data: [str]):
    total_stacks = len(list(filter(str.isdigit, stack_data[-1].strip().split(' '))))
    stack = [[] for i in range(total_stacks)]

    for row in [[*l.replace('\n', '')] for l in stack_data[:-1][::-1]]:
        for i, state in enumerate(row_stack(row)):
            if len(state) == 0:
                continue
            stack[i].append(state[0])

    return stack


def get_moves(data: [str]):
    moves = []
    for m in data:
        l = m.split()
        moves.append({l[i]: int(l[i + 1]) for i in range(0, len(l), 2)})
    return moves


with open('input.txt') as f:
    groups = [list(group) for key, group in groupby(f.readlines(), lambda x: len(x.strip()) != 0) if key]

stack = get_stack(groups[0])
moves = get_moves(groups[1])

for move in moves:

    e_l = stack[move['from'] - 1][-move['move']:][::-1]
    stack[move['to'] - 1].extend(e_l)

    del stack[move['from'] - 1][-move['move']:]

print("Result top crates:", ''.join([s[-1] for s in stack]))
