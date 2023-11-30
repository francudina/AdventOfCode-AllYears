
with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]


cycle_duration = {
    'noop': 1,
    'addx': 2
}
checkpoint_cycle = 40

X = 1
cycle = 0
canvas = []
current_row = []

for iteration, signal in enumerate(lines):

    for _ in range(int(cycle_duration[signal.split(' ')[0]])):

        cycle += 1

        # add new/next row
        if cycle != 1 and (cycle - 1) % checkpoint_cycle == 0:
            canvas.append(current_row)
            X = X if X < 40 else X % checkpoint_cycle
            cycle %= checkpoint_cycle
            current_row = []

        draw_element = '#' if X - 1 <= cycle - 1 <= X + 1 else '.'
        current_row.append(draw_element)

    if len(lines) == iteration + 1:
        canvas.append(current_row)

    # after the cycles
    if signal.split(' ')[0] == 'noop':
        continue

    # addx is received
    X += int(signal.split(' ')[1])

print("Result canvas:")
for row in canvas:
    print(''.join(row))
