import re
import math

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

rez = sum(math.prod([int(n) for n in re.findall(f'\d+', m)])
          for m in re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", lines[0]))

print(f'Result: {rez}')
