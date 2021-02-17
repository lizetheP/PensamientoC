import math

r = float(input("Introduce el radio: "))
h = float(input("Introduce la altura: "))
g = float(input("Introduce la generatriz: "))
a = math.pi*r*g + math.pi*math.pow(r,2) 
v = 1/3*math.pi*math.pow(r,2)*h 
print("Area del cono : %.2f" % a)
print("Volumen del cono : %.2f" % v)

