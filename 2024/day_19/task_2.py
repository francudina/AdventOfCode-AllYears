from task_1 import designs, match


rez = sum(match(d) for d in designs)

print(f'Result: {rez}')
