def all_uniq(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

with open("input.txt") as f:
    text = f.read()

    # print(text, len(text))

    buffer = text[:14]

    if all_uniq(buffer):
        print("4")

    for i in range(14, len(text)):
        buffer = buffer[1:] + text[i]
        if all_uniq(buffer):
            print(i+1)
            break