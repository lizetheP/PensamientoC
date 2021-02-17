import math

A = float(input("Introduce el valor de A: "))
C = float(input("Introduce el valor de C: "))
B = math.sqrt(math.pow(C,2) - math.pow(A,2))
print("El valor de B es: %.2f" % B)