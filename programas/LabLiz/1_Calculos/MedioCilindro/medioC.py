import math

PI = 3.141592
r = float(input("Introduce el radio: "))
h = float(input("Introduce la altura: "))
v = (PI*math.pow(r,2)*h)/2 
print("Volumen del cilindro : %.3f" % v)

