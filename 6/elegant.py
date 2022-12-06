with open("input.txt") as f:
    f_contents = f.read()
    f = lambda n, s: ["h" if len(set(s[i-n:i]))==n else "n" for i in range(n,len(s))].index("h")+n
    print(f(4, f_contents), f(14, f_contents))