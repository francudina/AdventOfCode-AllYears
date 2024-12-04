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

    return int(''.join(chars) == w) or int(''.join(chars[::-1]) == w)


rez = 0
for i in range(rows + 1):
    for j in range(cols + 1):
        left_right = _search(r=i, c=j, w='MAS', steps=[(-1, -1), (0, 0), (1, 1)])    # left to right diagonal
        right_left = _search(r=i, c=j, w='MAS', steps=[(-1, 1), (0, 0), (1, -1)])    # right to left diagonal

        if left_right and right_left:
            rez += 1

print(f'Result: {rez}')
