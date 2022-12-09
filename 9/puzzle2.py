input_filename = "simple2.txt"
input_filename = "input.txt"


class Loc:
    def __init__(self):
        self.visited = False
        self.h = False
        self.t = False
    
with open(input_filename) as f:
    chunks = f.read().replace("\r\n", "\n").split("\n")
    dirs = list(map(lambda a: a.split(" "), chunks))

    m = 0

    for i in range(len(dirs)):
        dirs[i][1] = int(dirs[i][1])
        if dirs[i][1] > m:
            m = dirs[i][1]
    
    m += 2
    if m % 2 == 1:
        m += 1
    m *= m * 2

    board = [[Loc() for j in range(m)] for i in range(m)]

    ctr = m//2

    xh = ctr
    yh = ctr

    xts = [ctr for i in range(9)]
    yts = [ctr for i in range(9)]

    board[yts[0]][xts[0]].visited = True

    for j in dirs:
        for n in range(j[1]):
            if j[0] == "R":
                xh += 1
            elif j[0] == "L":
                xh -= 1
            elif j[0] == "U":
                yh -= 1
            elif j[0] == "D":
                yh += 1
            
            if abs(xh - xts[0]) > 1 or abs(yh - yts[0]) > 1:
                if xh > xts[0]:
                    xts[0] += 1
                elif xh < xts[0]:
                    xts[0] -= 1
                if yh > yts[0]:
                    yts[0] += 1
                elif yh < yts[0]:
                    yts[0] -= 1
            
            for i in range(1,9):
                if abs(xts[i-1] - xts[i]) > 1 or abs(yts[i-1] - yts[i]) > 1:
                    if xts[i-1] > xts[i]:
                        xts[i] += 1
                    elif xts[i-1] < xts[i]:
                        xts[i] -= 1
                    if yts[i-1] > yts[i]:
                        yts[i] += 1
                    elif yts[i-1] < yts[i]:
                        yts[i] -= 1
                
                if i == 8:
                    board[yts[i]][xts[i]].visited = True



    count = 0

    for row in board:
        for col in row:
            if col.visited:
                count += 1
    print(count)
