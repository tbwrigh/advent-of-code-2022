with open("input.txt") as f:
    pairs = f.read().replace("\r\n", "\n").split("\n\n")

# def conv_str_arr(s):
#     arr = []
#     buf = ""
#     buf_arrs = []
#     sub_arr_c = 0
#     for c_i in range(len(s)):
#         c = s[c_i]
#         if c not in ["[", "]", ","]:
#             buf += c
#         if c == "," or c_i == len(s) - 1:
#             if buf == "" and sub_arr_c <= 1:
#                 pass
#             elif sub_arr_c == 0:
#                 arr.append(int(buf))
#                 buf = ""
#             elif sub_arr_c > 0:
#                 if buf != "":
#                     buf_arrs[sub_arr_c-1].append(int(buf))
#                 buf = ""
#         if c == "[":
#             sub_arr_c += 1
#             buf_arrs.append([])
#         if c == "]":
#             if buf != "":
#                 buf_arrs[sub_arr_c-1].append(int(buf))
#                 buf = ""

#             if sub_arr_c > 1:
#                 t = buf_arrs.pop()
#                 buf_arrs[-1].append(t)
#                 sub_arr_c -= 1
#             else:
#                 arr.append(buf_arrs.pop())
#                 sub_arr_c -= 1

#     return arr


def conv_str_arr(s):
    return eval(s)

def compare(l,r, recur=False):
    if len(r) < len(l):
        return False

    same = True

    for i in range(min(len(l), len(r))):
        if type(l[i]) == int and type(r[i]) == int:
            same = same and (l[i] <= r[i])
        elif type(l[i]) != int and type(r[i]) != int:
            same = same and compare(l[i], r[i])
        elif type(l[i]) != int and l[i] != []:
            same = same and list_int_comp(l[i][0], r[i], True)
        elif type(r[i]) != int and r[i] != []:
            same = same and list_int_comp(r[i][0], l[i], False)
        else:
            same = False
        if not same:
            return False
    
    return same

def list_int_comp(l, i, lr):
    if l == []:
        return False
    if type(l) == int:
        return l <= i if lr else i <= l
    else:
        return list_int_comp(l[0], i, lr)

t = 0

for pair_i in range(len(pairs)):
    left = pairs[pair_i].split("\n")[0]
    right = pairs[pair_i].split("\n")[1]

    # print(left)
    # print(right)
    # print()

    l = conv_str_arr(left)
    r = conv_str_arr(right)

    # print(l)
    # print(r)

    if compare(l,r):
        t += pair_i + 1
    
print(t)



    