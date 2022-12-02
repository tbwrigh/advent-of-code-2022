import sys

out = 0
amts = []
for line in sys.stdin:
    inp = line.split()
    if len(inp) == 0:

        continue
    
    a, b = inp[0], inp[1]
    if b == 'X':
        if a == 'A':
            b = 'Z'
        elif a == 'B':
            b = 'X'
        else:
            b = 'Y'
    elif b == 'Y':
        # draw
        if a == 'A':
            b = 'X'
        elif a == 'B':
            b = 'Y'
        else:
            b = 'Z'
    else:
        if a == 'A':
            b = 'Y'
        elif a == 'B':
            b = 'Z'
        else:
            b = 'X'

    if b == 'X':
        out += 1
        if a == 'A':
            out += 3
        elif a == 'C':
            out += 6
    elif b == 'Y':
        out += 2
        if a == 'B':
            out += 3
        elif a == 'A':
            out += 6
    elif b == 'Z':
        out += 3
        if a == 'C':
            out += 3
        elif a == 'B':
            out += 6
    print(out)

        

print(out)