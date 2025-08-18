import math
x = float(input("Dame el valor de x: "))
res = 3 * x * math.sqrt(1/3 * x**2 + 2 * math.pi)
res2 = 3 * x * math.sqrt(1/3 * math.pow(x,2) + 2 * math.pi)
print("El resultado es: %.2f" % res)
print("El resultado es: %.2f" % res2)