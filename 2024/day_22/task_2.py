from collections import defaultdict, deque

from task_1 import lines, new


sequences = defaultdict(int)
for s in lines:

    first, counted, seq = s % 10, set(), deque(maxlen=4)
    for second in new(s=s, count=2000):

        second %= 10
        seq.append(second - first)
        first = second

        k = tuple(seq)
        if len(seq) != 4 or k in counted:
            continue

        sequences[k] += second
        counted.add(k)


rez = max(v for _, v in sequences.items())
print(f'Result: {rez}')
