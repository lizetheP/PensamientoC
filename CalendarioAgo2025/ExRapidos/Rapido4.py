i = 0
res = 19
for i in range (7, 1, -1):
    if res < 27:
        res = res + i
    else:
        res = res - i
    print("i, res: ", (i, res))
print(res)