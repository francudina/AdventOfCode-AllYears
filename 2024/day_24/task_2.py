from task_1 import gates


gates = [v.split() + [k] for k, v in gates.items()]
highest = 'z45'

to_swap = set()
for left, op, right, r in gates:
    if r[0] == 'z' and op != '^' and r != highest:
        to_swap.add(r)
    if op == '^' and left[0] not in ['x', 'y', 'z'] and right[0] not in ['x', 'y', 'z'] and r[0] not in ['x', 'y', 'z']:
        to_swap.add(r)
    if op == '&' and 'x00' not in [left, right]:
        for sub_left, sub_op, sub_right, sub_res in gates:
            if (r == sub_left or r == sub_right) and sub_op != '|':
                to_swap.add(r)
    if op == '^':
        for sub_left, sub_op, sub_right, sub_res in gates:
            if (r == sub_left or r == sub_right) and sub_op == '|':
                to_swap.add(r)

rez = ','.join(sorted(to_swap))
print(f'Result: {rez}')
