input_filename = "simple.txt"
input_filename = "input.txt"

with open(input_filename) as f:
    chunks = f.read().replace("\r\n", "\n").split("$ ")
    chunks = list(map(lambda a: a.split("\n"), chunks))
    for chunk in chunks:
        blanks_count = 0
        for elem in chunk:
            if elem == "":
                blanks_count += 1
        for i in range(blanks_count):
            chunk.remove("")
    
    empty_count = 0
    for chunk in chunks:
        if chunk == []:
            empty_count += 1
    for i in range(empty_count):
        chunks.remove([])

    dir = {}

    working_path = []
    
    for chunk in chunks:
        if chunk[0] == "cd ..":
            working_path.pop()
        elif chunk[0].split(" ")[0] == "cd":
            working_path.append(" ".join(chunk[0].split(" ")[1:]))
        else:
            dir["".join(working_path)] = []
            for i in chunk[1:]:
                if i.split(" ")[0] == "dir":
                    dir["".join(working_path)].append("".join(working_path) + i.split(" ")[1])
                else:
                    dir["".join(working_path)].append((int(i.split(" ")[0]), i.split(" ")[1]))

    collapse_order = list(dir.keys())
    collapse_order.sort(key=len)
    collapse_order.reverse()

    collapsed_dirs = {}

    for i in collapse_order:
        size = 0
        for item in dir[i]:
            if isinstance(item, str):
                size += collapsed_dirs[item]
            else:
                size += item[0]
        collapsed_dirs[i] = size


    used= max(list(collapsed_dirs.values()))

    closest = 3000000000

    left = 70000000 - used
    needed = 30000000 - left
    for s in collapsed_dirs.values():
        if s < closest and s > needed:
            closest = s
    print(closest)