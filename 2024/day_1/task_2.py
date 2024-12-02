with open('input.txt') as f:
    lines = [l.strip().split() for l in f.readlines()]

r = [int(c[1]) for c in lines]
rez = sum([int(c[0])*r.count(int(c[0])) for c in lines])
print(f'Result: {rez}')
