with open('input.txt') as f:
    line = [list(line.strip()) for line in f][0]

pairs = [(int(line[i]), 0 if i+1 >= len(line) else int(line[i+1])) for i in range(0, len(line), 2)]

disk = []
for i, (count, spaces) in enumerate(pairs):
    disk.extend([i]*count)
    disk.extend(['.']*spaces)

for i in range(len(disk)-1, -1, -1):
    if disk[i] == '.':
        continue

    for j in range(0, i):
        if disk[j] != '.':
            continue

        disk[j], disk[i] = disk[i], '.'

        break

rez = sum([i*v for i, v in enumerate(disk) if disk[i] != '.'])

print(f'Result: {rez}')
