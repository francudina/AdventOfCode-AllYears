from collections import Counter

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

counts = Counter(lines)
keys = counts.keys()

LOSS, DRAW, WIN = 0, 3, 6

round_score = {
    "A X": LOSS,
    "A Y": DRAW,
    "A Z": WIN,

    "B X": LOSS,
    "B Y": DRAW,
    "B Z": WIN,

    "C X": LOSS,
    "C Y": DRAW,
    "C Z": WIN
}

next_action = {
    "A X": "Z",
    "A Y": "X",
    "A Z": "Y",

    "B X": "X",
    "B Y": "Y",
    "B Z": "Z",

    "C X": "Y",
    "C Y": "Z",
    "C Z": "X"
}

option_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

total = 0

for key, value in counts.items():

    total += option_score[next_action[key]] * value
    total += round_score[key] * value

print(f"\nTotal: {total}")
