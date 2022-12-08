
with open('input.txt') as f:
    lines = [[*l.strip()] for l in f.readlines()]

visibility_test = lambda target, elements: len(list(filter(lambda x: int(x) < target, elements))) == len(elements)

total = 0
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines) - 1):

        element = int(lines[i][j])

        r_l = visibility_test(element, lines[i][0:j])
        r_r = visibility_test(element, lines[i][j+1:len(lines)])
        row = True if r_l or r_r else False

        c_u = visibility_test(element, [r[j] for r in lines[0:i]])
        c_d = visibility_test(element, [r[j] for r in lines[i+1:len(lines)]])
        column = True if c_u or c_d else False

        total += 1 if row or column else 0

total += 2 * len(lines) + 2 * (len(lines[0]) - 2)
print(f"Total: {total}")
