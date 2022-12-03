import string

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

a_z = string.ascii_lowercase

a = 1
A = 27
group_size = 3

duplicates = 0

for group in [lines[n:n+group_size] for n in range(0, len(lines), group_size)]:

    same_chars = set(group[0]) & set(group[1]) & set(group[2])

    for c in same_chars:

        position = a_z.index(c.lower())
        duplicates += A + position if c.isupper() else a + position

print(f"Total: {duplicates}")
