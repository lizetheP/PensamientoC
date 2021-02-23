import math
def imprime10():
    contador = 1
    while contador <= 10: 
        print("%i hola a todos", contador)
        contador = contador + 1

def f1(n):
    contador = 1
    acum = 0
    while contador <= n:
        acum = acum + contador
        contador = contador + 1
    return acum
   
def f(n):
    i = 1
    acum = 0
    while i <= n:
        acum = acum + (i**2 - 3*i)/math.sqrt(5*i)
        i = i + 1
    return acum

def main():
    num = int(input("Introduce un numero: "))
    res = f(num)
    print("f(%i) = %.3f" % (num, res))
    
main()
