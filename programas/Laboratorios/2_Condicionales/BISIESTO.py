"""Determinar si un año es bisiesto.
si es divisible entre 4 y no divisible entre 100, y también si es divisible entre 400.  

1. Pedir el año (a)
2. Si ((a%4 es igual a cero) y (a%100 no es igual a cero)) o (a%400 es igual a cero)
      escribir("ES BISIESTO")
   SiNo
      escribir("NO ES BISIESTO")"""

a = int(input("Introduce el año: "))
if (a%4 == 0 and a%100 != 0) or (a%400 == 0):
    print("ES BISIESTO")
else:
    print("NO ES BISIESTO")
    
      