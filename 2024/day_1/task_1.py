with open('input.txt') as f:
    lines = [l.strip().split() for l in f.readlines()]

rez = sum([abs(l - r)
           for l, r in
           zip(sorted([int(c[0]) for c in lines]),
               sorted([int(c[1]) for c in lines]))])
print(f'Result: {rez}')
