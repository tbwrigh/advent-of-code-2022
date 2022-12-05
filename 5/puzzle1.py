one = ["Q", "S", "W", "C", "Z", "V", "F", "T"]
two = ["Q", "R", "B"]
thr = ["B", "Z", "T", "Q", "P", "M", "S"]
four = ["D", "V", "F", "R", "Q", "H"]
five = ["J", "G", "L", "D", "B", "S", "T", "P"]
six = ["W", "R", "T", "Z"]
sev = ["H", "Q", "M", "N", "S", "F", "R", "J"]
eight = ["R", "N", "F", "H", "W"]
nine = ["J", "Z", "T", "Q", "P", "R", "B"]

arrs = [one,two,thr,four,five,six,sev,eight,nine]

# arrs = [["Z","N"], ["M","C","D"], ["P"]]
# print(arrs)

with open("input.txt") as f:
    lines = map(lambda a: a.replace("\n", ""), f.readlines())

    for line in lines:
        split = line.split(" ")
        num, fr, to = int(split[1]), int(split[3])-1, int(split[5])-1

        print(num, fr, to)
        popped = []
        for i in range(num):
            popped.append(arrs[fr].pop())

        popped.reverse()
        
        for i in range(num):
            arrs[to].append(popped.pop())
        
        # print(arrs)


    for arr in arrs:
        print(arr[len(arr)-1], end="")
    print()
