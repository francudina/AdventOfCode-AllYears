
def to_int(x):
    return set([int(i) for i in x.split(' ') if i])


# def find_copies(cards: [], copies: {}, ):


cards = list([l.strip().split(':')[1:][0] for l in open('input.txt')])
cards = [c.split('|') for c in cards]

copies = {}
for i, card in enumerate(cards):

    original = len(to_int(card[0]) & to_int(card[1]))
    for j in range(i + 1, i + 1 + original):
        copies[j] = copies.get(j, 0) + 1

        copy = len(to_int(cards[j][0]) & to_int(cards[j][1]))
        for k in range(j + 1, j + 1 + copy):
            copies[k] = copies.get(k, 0) + 1

total = sum(v for k, v in copies.items()) + len(cards)

print("Result:", total)
