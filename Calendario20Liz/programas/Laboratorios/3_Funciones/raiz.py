import math
def raiz(num):
    res = math.sqrt(num)
    print("La raiz cuadrada de ", num, " es %.3f"% res)
    
numero = float(input("Introduce un número: "))
raiz(numero)
