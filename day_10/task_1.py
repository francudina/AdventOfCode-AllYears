
with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]


cycle_duration = {
    'noop': 1,
    'addx': 2
}
checkpoint_cycles = [20, 60, 100, 140, 180, 220]

X = 1
cycles = 0
signal_strengths = []

for signal in lines:

    if len(checkpoint_cycles) == 0:
        break

    for c in range(int(cycle_duration[signal.split(' ')[0]])):

        if len(checkpoint_cycles) == 0:
            break

        cycles += 1

        if checkpoint_cycles[0] == cycles:

            signal_strengths.append(X * cycles)

            # remove element from start for next iteration
            checkpoint_cycles.pop(0)

    # after the cycles
    if signal.split(' ')[0] == 'noop':
        continue

    # addx is received
    X += int(signal.split(' ')[1])

print(f"Total signal strength: {sum(signal_strengths)}")
