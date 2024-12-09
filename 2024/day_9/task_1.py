with open('input.txt') as f:
    line = [list(line.strip()) for line in f][0]


def _pairs() -> []:
    return [(int(line[i]), 0 if i+1 >= len(line) else int(line[i+1]))
            for i in range(0, len(line), 2)]


def scan() -> (list, dict, dict):
    disk, files, space = [], {}, {}
    for i, (count, spaces) in enumerate(_pairs()):
        files[i] = (len(disk), count)
        space[len(disk) + count] = spaces

        disk.extend([i] * count)
        disk.extend(['.'] * spaces)
    return disk, files, space


def disk_sum(disk: []) -> int:
    return sum([i*v for i, v in enumerate(disk) if disk[i] != '.'])


if __name__ == '__main__':

    disk, _, _ = scan()
    for i in range(len(disk)-1, -1, -1):
        if disk[i] == '.':
            continue

        for j in range(0, i):
            if disk[j] != '.':
                continue
            disk[j], disk[i] = disk[i], '.'
            break

    print(f'Result: {disk_sum(disk=disk)}')
