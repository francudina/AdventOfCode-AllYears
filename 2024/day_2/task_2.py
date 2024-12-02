from task_1 import read, scan


rez = 0
for l in read():

    if scan(l):
        rez += 1
        continue

    for i in range(len(l)):
        if scan([e for j, e in enumerate(l) if i != j]):
            rez += 1
            break

print(f'Result: {rez}')
