import math

def imprimeHola():
    x = 5
    while x >= 5:
        print(" Hola a todos ")

def imprime():
    x =10
    while x > 0:
        print(x)
        x = x - 1
    print("El valor final de x: ", x)

"""funcion imprime10Hola()
    cont = 1
    mientras cont <= 10
        print("Hola a todos")
        cont = cont + 1"""
        
def imprime10Hola():
    cont = 1
    while cont <= 10:
        print("%i Hola a todos" % cont)
        cont = cont + 1

def imprime10Hola2():  
    cont = 0
    while cont < 10:
        print("%i Hola a todos" % cont)
        cont = cont + 1

"""funcion f1(n)
    cont = 1
    acum = 0
    mientras cont <= n
        acum = acum + cont
        cont = cont + 1
    regresar acum"""
    
def f1(n):
    cont = 1
    acum = 0
    while cont <= n:
        acum = acum + cont
        cont = cont + 1
    return acum

"""funcion sumatoria2(n)
    i = 1
    acum = 0
    mientras i <= n
        acum = acum + (i**2 - 3i) / raiz(5i)
        i = i + 1
    regresar acum"""
    
def sumatoria(n):
    i = 1
    acum = 0
    while i <= n:
        acum = acum + (i**2 - 3*i) / math.sqrt(5*i)
        i = i + 1
    return acum    

def main():
    num = int(input("Introduce el valor de n mayor a cero: "))
    if (num > 0):
        res = sumatoria(num)
        print("f1(%i) = %.4f" % (num, res))
    else:
        print("NUMERO INVALIDO")

main()







