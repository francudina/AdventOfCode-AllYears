with open('input.txt') as f:
    matrix = [list(line.strip()) for line in f]

rows = len(matrix)
cols = len(matrix[0])


def _test(r: int, c: int, s: ()) -> bool:
    return 0 <= r+s[0] <= rows - 1 and 0 <= c+s[1] <= cols - 1


def _search(r: int, c: int, w: str, steps: []) -> int:
    chars = []
    for s in steps:
        if not _test(r=r, c=c, s=s):
            return 0
        chars.append(str(matrix[r+s[0]][c+s[1]]))

    return int(''.join(chars) == w)


rez = 0
for i in range(rows):
    for j in range(cols):
        rez += _search(r=i, c=j, w='XMAS', steps=[(0, 0), (0, -1), (0, -2), (0, -3)])       # left
        rez += _search(r=i, c=j, w='XMAS', steps=[(0, 0), (0, 1), (0, 2), (0, 3)])          # right
        rez += _search(r=i, c=j, w='XMAS', steps=[(0, 0), (1, 0), (2, 0), (3, 0)])          # down
        rez += _search(r=i, c=j, w='XMAS', steps=[(0, 0), (-1, 0), (-2, 0), (-3, 0)])       # up

        rez += _search(r=i, c=j, w='XMAS', steps=[(0, 0), (-1, -1), (-2, -2), (-3, -3)])    # left up
        rez += _search(r=i, c=j, w='XMAS', steps=[(0, 0), (-1, 1), (-2, 2), (-3, 3)])       # right up
        rez += _search(r=i, c=j, w='XMAS', steps=[(0, 0), (1, -1), (2, -2), (3, -3)])       # left down
        rez += _search(r=i, c=j, w='XMAS', steps=[(0, 0), (1, 1), (2, 2), (3, 3)])          # right down

print(f'Result: {rez}')
