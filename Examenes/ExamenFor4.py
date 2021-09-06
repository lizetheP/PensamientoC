i = 0
res = 18
for i in range (6, 0, -1):
    if res < 24:
        res = res + i
    else:
        res = res - i
print(res)