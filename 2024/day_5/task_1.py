from collections import defaultdict

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

rules = defaultdict(list)
[rules[l.split('|')[0]].append(l.split('|')[1]) for l in lines if '|' in l]


def _check(u: []) -> int:
    found = any(any(next_p for next_p in rules[u[i]] if next_p in u[:i]) for i in range(len(u) - 1, -1, -1))
    return int(u[int(len(u)/2)]) if not found else 0


rez = 0
for update in [l.split(',') for l in lines if '|' not in l and len(l) != 0]:
    rez += _check(update)

print(f'Result: {rez}')
