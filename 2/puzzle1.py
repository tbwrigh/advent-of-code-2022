score = 0

score_guide = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

counts = []

with open("input.txt") as f:
    t = f.read()
    for entry in score_guide.keys():
        counts.append(t.count(entry))
    for c, p in zip(counts, score_guide.keys()):
        score += c * score_guide[p]

print(score)
