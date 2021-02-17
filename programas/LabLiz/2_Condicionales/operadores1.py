x = float(input("Introduce el valor de x: "))
if (x <= - 1):
    y = 2*x + 3
elif x < 1 and x > -1:
    y = 2
else:
    y = x*x
print("%.1f" % y)