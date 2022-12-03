with open("input.txt") as f:
    lines = list(map(lambda a: set(a.replace("\n","")), f.readlines()))
    groups = [lines[i:i+3] for i in range(0,len(lines),3)]
    chars = list(map(lambda a: list(a[0].intersection(a[1].intersection(a[2])))[0], groups))
    total = sum(list(map(lambda a: ord(a)-ord("A")+27 if a.isupper() else ord(a)-ord("a")+1, chars)))
print(total)

