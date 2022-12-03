total = 0
with open("input.txt") as f:
    t = f.readlines()

    groups = []

    group = []

    for i in range(len(t)):
        group.append(t[i].replace("\n", ""))
        if (i+1) % 3 == 0:
            groups.append(group)
            group = []

    for group in groups:
        c = ""
        c_org = c
        for ch in group[0]:
            if ch in group[1] and ch in group[2]:
                c = ch
                c_org = c
        if c == c.upper():
            c = c.lower()
            total -= 6
        else:
            c = c.upper()
        total += ord(c) - ord("A") + 1

print(total)