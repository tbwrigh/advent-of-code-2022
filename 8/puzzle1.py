input_filename = "simple.txt"
input_filename = "input.txt"

def visible(r, c, grid):

    v = grid[r][c]

    if r == 0 or r == len(grid) - 1:
        return True
    elif c == 0 or c == len(grid[r]) - 1:
        return True
    

    all_smaller = [True, True, True, True]
    
    for i in range(0, c):
        if grid[r][i] >= v:
            all_smaller[0] = False
    if all_smaller[0]:
        return True
    for i in range(c+1, len(grid[r])):
        if grid[r][i] >= v:
            all_smaller[1] = False
    if all_smaller[1]:
        return True

    for i in range(0, r):
        if grid[i][c] >= v:
            all_smaller[2] = False
    if all_smaller[2]:
        return True
    for i in range(r+1, len(grid)):
        if grid[i][c] >= v:
            all_smaller[3] = False
    if all_smaller[3]:
        return True
    
    return False

with open(input_filename) as f:
    chunks = f.read().replace("\r\n", "\n").split("\n")
    chunks = list(map(lambda a: list(map(lambda b: int(b), list(a))),chunks))


    c = 0

    for row_num in range(len(chunks)):
        for col_num in range(len(chunks[row_num])):
            if visible(row_num, col_num, chunks):
                c += 1

    print(c)

    