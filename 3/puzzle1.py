total = 0
with open("input.txt") as f:
    t = f.readlines()

    for line in t:
        line = line.replace("\n", "")
        ll = len(line)
        sl = int(ll/2)
        f, s = list(line[:sl]), list(line[sl:])
        c = ""
        c_org = c
        for ch in f:
            if ch in s:
                c = ch
                c_org = c
        if c == c.upper():
            c = c.lower()
            total -= 6
        else:
            c = c.upper()
        total += ord(c) - ord("A") + 1

print(total)