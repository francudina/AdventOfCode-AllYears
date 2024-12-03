import re
import math

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

rez, enabled = 0, True
for m in re.findall("do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)", lines[0]):
    if 'do' in m:
        enabled = 'do()' == m
        continue
    if not enabled:
        continue

    rez += math.prod([int(n) for n in re.findall(f'\d+', m)])

print(f'Result: {rez}')
