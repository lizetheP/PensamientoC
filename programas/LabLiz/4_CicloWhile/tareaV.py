import math

def f1(n):
    k = 1
    acum = 0
    while k <= n:
        acum = acum + (2*k - 1)
        k = k + 1
    return acum

def f2(n):
    i = 1
    acum = 0
    num = 40
    signo = 1
    while i <= n:
        acum = acum + num*signo
        signo = signo * -1
        num = num + 1
        i = i + 1
    return acum

def f3(n):
    i = 1
    acum = 1
    while i <= n:
        acum = acum * 3*i
        i = i + 1
    return acum

def f4(n):
    k = 1
    acum = 0
    while k <= n:
        acum = acum + (k + 2)/ k**3
        k = k + 1
    return acum

def multiplicacion(n1, n2):
    cont = 1
    acum = 0
    while cont <= n1:
        acum = acum + n2
        cont = cont + 1
    return acum

def menu():
    print("1. Función 1")
    print("2. Función 2")
    print("3. Función 3")
    print("4. Función 4")
    print("5. Multiplicación")
    print("6. Salir")

def main():
    #menu()
    opcion = int(input())
    if opcion == 1:
        n = int(input())
        res = f1(n)
        print(res)
    elif opcion == 2:
        n = int(input())
        res = f2(n)
        print(res)
    elif opcion == 3:
        n = int(input())
        res = f3(n)
        print(res)
    elif opcion == 4:
        n = int(input())
        res = f4(n)
        print("%.2f" % res)
    elif opcion == 5:
        n1 = int(input())
        n2 = int(input())
        res = multiplicacion(n1, n2)
        print(res)
    elif opcion == 6:
        print("Adios")
    else:
        print("Opcion_invalida")

main()