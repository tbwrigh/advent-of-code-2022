input_filename = "simple.txt"
input_filename = "input.txt"

with open(input_filename) as f:
    chunks = f.read().replace("\r\n", "\n").split("\n")
    dirs = list(map(lambda a: a.split(" "), chunks))

    cycles = 0

    x = 1

    imp = [20, 60, 100, 140, 180, 220]

    t = 0

    for i in dirs:
        cycles += 1

        if cycles in imp:
            t += cycles * x

        if i[0] == "addx":
            cycles += 1
            if cycles in imp:
                t += cycles * x
            x += int(i[1])


    
    print(t)