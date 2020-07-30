import math
def raiz(num):
    res = math.sqrt(num)
    return res
    
numero = float(input("Introduce un número: "))
res = raiz(numero)
print("La raiz de: ", numero, " es: %.2f"%res)
