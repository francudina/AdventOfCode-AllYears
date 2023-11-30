
with open('input.txt') as f:
    line = [*f.readline().strip()]

windows_size = 14
for i in range(windows_size, len(line) + 1, 1):

    if len(set(line[i-windows_size:i])) == windows_size:
        print(f"First index is: {i}")
        print(f"Result pair is: {''.join(line[i-windows_size:i])}")
        break
