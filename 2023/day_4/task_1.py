to_int = lambda x: set([int(i) for i in x.split(' ') if i])
points = lambda values: 0 if len(values) == 0 else 1*2**(len(values)-1)

cards = list([l.strip().split(':')[1:][0] for l in open('input.txt')])

total = 0
for card in [c.split('|') for c in cards]:
    total += points(to_int(card[0]) & to_int(card[1]))
print("Result:", total)
