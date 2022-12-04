overlaps = 0
with open("input.txt") as f:
    pairs = list(map(lambda a: a.replace("\n","").split(","), f.readlines()))

    pairs = list(map(lambda a : list(map(lambda b: [i for i in range(int(b.split("-")[0]), int(b.split("-")[1])+1)], a)), pairs))

    for pair in pairs:
        if set(pair[0]).intersection(set(pair[1])) != set():
            overlaps += 1
    
print(overlaps)