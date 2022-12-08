input_filename = "simple.txt"
input_filename = "input.txt"

def score(r, c, grid):

    v = grid[r][c]

    r_val = 0
    l_val = 0
    t_val = 0
    b_val = 0

    for i in range(c-1, -1, -1):
        r_val += 1
        if grid[r][i] >= v:
            break

    for i in range(c+1, len(grid[r])):
        l_val += 1
        if grid[r][i] >= v:
            break

    for i in range(r-1, -1, -1):
        t_val += 1
        if grid[i][c] >= v:
            break

    for i in range(r+1, len(grid)):
        b_val += 1
        if grid[i][c] >= v:
            break
    
    return r_val * l_val * b_val * t_val

with open(input_filename) as f:
    chunks = f.read().replace("\r\n", "\n").split("\n")
    chunks = list(map(lambda a: list(map(lambda b: int(b), list(a))),chunks))


    c = 0

    for row_num in range(len(chunks)):
        for col_num in range(len(chunks[row_num])):
            s =  score(row_num, col_num, chunks)
            if s > c:
                c = s

    print(c)

    