input_filename = "simple.txt"
input_filename = "input.txt"

with open(input_filename) as f:
    chunks = f.read().replace("\r\n", "\n").split("Monkey ")
    monkeys = list(map(lambda a: a.split("\n")[1:], chunks))
    for m in range(len(monkeys)):
        while "" in monkeys[m]:
            monkeys[m].remove("")
    monkeys = monkeys[1:]

    counts = [0 for i in range(len(monkeys))]
    items = [list(map(lambda a: int(a), monkey[0].split(": ")[1].split(", "))) for monkey in monkeys]
    operators = [monkey[1].split("= ")[1] for monkey in monkeys]
    tests = [int(monkey[2].split(" ")[-1]) for monkey in monkeys]
    t_throw = [int(monkey[3].split(" ")[-1]) for monkey in monkeys]
    f_throw = [int(monkey[4].split(" ")[-1]) for monkey in monkeys]

    for i in range(20):
        for m in range(len(monkeys)):
            for item in items[m]:
                counts[m] += 1

                new_val = eval(operators[m].replace("old", str(item))) // 3 

                if new_val % tests[m] == 0:
                    items[t_throw[m]].append(new_val)
                else:
                    items[f_throw[m]].append(new_val)

            items[m] = []
    
    counts.sort()

    print(counts[-1] * counts[-2])
