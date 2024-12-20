import task_1 as t1

program_reversed = t1.program[::-1]


def _iter(a: int = 0, depth: int = 0) -> int:
    print("\t"*depth + f'i: {depth}, a: {a}')

    if len(program_reversed) == depth:
        return a

    for i in range(8):

        t1.pointer = 0
        output = t1.check(t1.register, a * 8 + i)

        if len(output) != 0 and output[0] == program_reversed[depth]:
            next_a: int = a * 8 + i
            if result := _iter(next_a, depth + 1):
                return result

    return 0


print(f'Result: {_iter()}')
