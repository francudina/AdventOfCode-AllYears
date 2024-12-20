import re


with open('input.txt') as f:
    lines = [line.strip() for line in f]

regs: [] = list(map(int, re.findall(r'-?\d+', ''.join(lines[:3]))))

A, B, C = 'A', 'B', 'C'
operands = {4: A, 5: B, 6: C}
register = {k: v for k, v in zip([A, B, C], regs)}
pointer: int = 0


def _operand(literal: int, kwargs: {}) -> int:
    return kwargs[operands[literal]] if literal in operands.keys() else literal


def _adv(literal: int, kwargs: {}):
    kwargs[A] = kwargs[A] >> _operand(literal, kwargs)


def _bxl(literal: int, kwargs: {}):
    kwargs[B] = kwargs[B] ^ literal


def _bst(literal: int, kwargs: {}):
    kwargs[B] = _operand(literal, kwargs) % 8


def _jnz(literal: int, kwargs: {}):
    if kwargs[A] != 0:
        global pointer
        pointer = literal - 2


def _bxc(literal: int, kwargs: {}):
    kwargs[B] = kwargs[B] ^ kwargs[C]


def _out(literal: int, kwargs: {}) -> int:
    return _operand(literal, kwargs) % 8


def _bdv(literal: int, kwargs: {}):
    kwargs[B] = kwargs[A] >> _operand(literal, kwargs)


def _cdv(literal: int, kwargs: {}):
    kwargs[C] = kwargs[A] >> _operand(literal, kwargs)


instructions = {0: _adv, 1: _bxl, 2: _bst, 3: _jnz, 4: _bxc, 5: _out, 6: _bdv, 7: _cdv}
program: [] = lines[4:][0].split(':')[1].strip().split(',')


def check(kwargs: {}, a: int = None) -> []:
    if a is not None:
        kwargs[A] = a
    global pointer
    reg = dict(kwargs)
    output = []
    while pointer < len(program):
        i, o = int(program[pointer]), int(program[pointer + 1])
        if (v := instructions[i](o, reg)) is not None:
            output.append(str(v))
        pointer += 2
    return output


if __name__ == '__main__':

    rez: [] = check(register)
    print(f'Result: {",".join(rez)}')
