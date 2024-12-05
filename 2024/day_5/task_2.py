from collections import defaultdict

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

rules = defaultdict(list)
[rules[l.split('|')[0]].append(l.split('|')[1]) for l in lines if '|' in l]


def _greater(c: str, n: str) -> bool:
    return n not in rules[c]


def _check(u: []) -> int:
    valid = list(u)
    for i in range(len(u) - 1):
        swapped = False
        for j in range(len(u) - i - 1):
            if _greater(valid[j], valid[j + 1]):
                valid[j], valid[j + 1] = valid[j + 1], valid[j]
                swapped = True
        if not swapped:
            break
    return int(valid[int(len(u)/2)]) if valid != u else 0


rez = 0
for update in [l.split(',') for l in lines if '|' not in l and len(l) != 0]:
    rez += _check(update)

print(f'Result: {rez}')
