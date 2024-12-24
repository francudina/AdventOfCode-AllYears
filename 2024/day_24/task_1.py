from itertools import groupby

with open('input.txt') as f:
    lines = [line.strip() for line in f]

lines = [list(g) for k, g in groupby(lines, key=bool) if k]


def _replace(s: str) -> str:
    return s.replace('AND', '&').replace('XOR', '^').replace('OR', '|')


wires = {l.split(': ')[0]: int(l.split(': ')[1]) for l in lines[0]}
gates = {l.split(' -> ')[1]: _replace(s=l.split(' -> ')[0]) for l in lines[1]}


def _evaluate(w: str) -> int:
    if w in wires:
        return wires[w]

    gate: str = gates[w]
    for k in [i for i in gate.split() if i not in ('&', '|', '^')]:

        v: int = _evaluate(w=k)
        gate = gate.replace(k, str(bin(v)))

    v: int = eval(gate)
    wires[w] = v

    return v


def resolve() -> {}:
    z_gates = {g: -1 for g in gates if g.startswith('z')}
    for g in z_gates:
        z_gates[g] = _evaluate(w=g)
    return z_gates


if __name__ == '__main__':

    g: {} = resolve()

    rez = ''.join(map(lambda k: str(g[k]), sorted(g, reverse=True)))
    print(f'Result: {int(rez, 2)}')
