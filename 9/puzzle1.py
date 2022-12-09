input_filename = "simple.txt"
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

    xt = ctr
    yt = ctr

    board[yt][xt].visited = True
    board[yt][xt].h = True
    board[yt][xt].t = True

    for i in dirs:
        # print(i)
        for n in range(i[1]):
            board[yh][xh].h = False
            board[yt][xt].h = False

            if i[0] == "R":
                xh += 1
            elif i[0] == "L":
                xh -= 1
            elif i[0] == "U":
                yh -= 1
            elif i[0] == "D":
                yh += 1
            
            board[yh][xh].h = True

            if abs(xh - xt) > 1 or abs(yh - yt) > 1:
                if xh > xt:
                    xt += 1
                elif xh < xt:
                    xt -= 1
                if yh > yt:
                    yt += 1
                elif yh < yt:
                    yt -= 1
            
            board[yt][xt].visited = True
            board[yt][xt].t = True

    count = 0

    for row in board:
        for col in row:
            if col.visited:
                count += 1
    print(count)
