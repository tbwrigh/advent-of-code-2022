input_filename = "simple.txt"
input_filename = "input.txt"

with open(input_filename) as f:
    chunks = f.read().replace("\r\n", "\n").split("\n")
    dirs = list(map(lambda a: a.split(" "), chunks))

    cycles = 0

    x = 1

    sp = x

    row = 0

    rows = ["" for i in range(6)]

    lc = 0

    for i in dirs:
        if abs(lc - x) == 0 or abs(lc - x) == 1:
            rows[row] += "#"
        else:
            rows[row] += " "
        
        cycles += 1
        lc += 1

        if cycles % 40 == 0:
            row += 1
            lc = 0

        if i[0] == "addx":
            if abs(lc - x) == 0 or abs(lc - x) == 1:
                rows[row] += "#"
            else:
                rows[row] += " "

            lc += 1
            cycles += 1

            if cycles % 40 == 0:
                row += 1
                lc = 0
            
            x += int(i[1])
    
    for row in rows:
        print("".join(row))