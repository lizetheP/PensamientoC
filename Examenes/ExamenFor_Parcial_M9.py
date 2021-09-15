i = 0
res = 5
for i in range (5, 0, -1):
    if res < 15:
        res = res + i
    else:
        res = res - i
print(res)