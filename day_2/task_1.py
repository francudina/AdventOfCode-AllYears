from collections import Counter

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

counts = Counter(lines)

LOSS, DRAW, WIN = 0, 3, 6

round_score = {
    "A X": DRAW,
    "A Y": WIN,
    "A Z": LOSS,

    "B X": LOSS,
    "B Y": DRAW,
    "B Z": WIN,

    "C X": WIN,
    "C Y": LOSS,
    "C Z": DRAW
}

option_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

total = 0

for key, value in counts.items():

    total += option_score[key[2]] * value
    total += round_score[key] * value

print(f"Total: {total}")
