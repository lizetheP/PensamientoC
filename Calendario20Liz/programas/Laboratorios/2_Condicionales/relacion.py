# Determina la relación existente entre dos números (mayor, menor o igual).

"""
1. Pedir num1
2. Pedir num2
3. Si num1 > num2
      escribir(num1 es mayor que num2)
   SiNo
     Si num1 < num2
        escribir(num1 es menor que num2)
     SiNo
        escribir(num1 es igual a num2)"""
        
num1 = int(input("Introduce el num1: "))
num2 = int(input("Introduce el num2: "))
if num1 > num2:
    print(num1, "es mayor que", num2)
elif num1 < num2:
    print(num1, "es menor que", num2)
else:
    print(num1, "es igual a", num2)