score = 0

score_guide = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

counts = []

with open("input.txt") as f:
    t = f.read()
    for entry in score_guide.keys():
        counts.append(t.count(entry))
    for c, p in zip(counts, score_guide.keys()):
        score += c * score_guide[p]

print(score)