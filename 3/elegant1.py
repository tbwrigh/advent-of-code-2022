with open("input.txt") as f:
    lines = list(map(lambda a: a.replace("\n",""), f.readlines()))
    chars = list(map(lambda a: list(set(a[int(len(a)/2):]).intersection(set(a[:int(len(a)/2)])))[0], lines))
    total = sum(list(map(lambda a: ord(a)-ord("A")+27 if a.isupper() else ord(a)-ord("a")+1, chars)))
print(total)

