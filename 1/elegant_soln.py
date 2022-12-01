with open("input1.txt") as f:
    sums = list(map(lambda a: sum(list(map(lambda b: int(b) if b != "" else 0, a.split("\n")))), f.read().split("\n\n")))
    print(max(sums), sum(sorted(sums)[-3:]), sep="\n")
