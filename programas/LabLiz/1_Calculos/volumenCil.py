import math

PI = 3.141592
r = float(input("Introduce el radio: "))
h1 = float(input("Introduce la altura 1: "))
h2 = float(input("Introduce la altura 2: "))
v = (PI*math.pow(r,2)*(h1+h2))/2 
print("Volumen del cilindro : %.2f" % v)

