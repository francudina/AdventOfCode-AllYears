
def visibility_test(target: int, elements: [str]):
    s = 0
    for e in elements:
        s += 1
        if int(e) >= target:
            break
    return s


with open('input.txt') as f:
    lines = [[*l.strip()] for l in f.readlines()]

total = []
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines) - 1):

        element = int(lines[i][j])

        r_l = visibility_test(element, lines[i][0:j][::-1])
        r_r = visibility_test(element, lines[i][j+1:len(lines)])
        row = r_l * r_r

        c_u = visibility_test(element, [r[j] for r in lines[0:i]][::-1])
        c_d = visibility_test(element, [r[j] for r in lines[i+1:len(lines)]])
        column = c_u * c_d

        total += [row * column]

print(f"Total: {max(total)}")
