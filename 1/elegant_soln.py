with open("input1.txt") as f:
    chunks = f.read().split("\n\n")
    sums = list(map(lambda a: sum(list(map(lambda b: int(b) if b != "" else 0, a.split("\n")))), chunks))
    print(max(sums))
    sorted_sums = sorted(sums)
    print(sum(sorted_sums[-3:]))
