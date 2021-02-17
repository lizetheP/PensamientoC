import math

def f1(n):
    acum = 0
    for i in range(1,n+1):
        acum = acum + 3**i / i
    return acum

def f2(n):
    acum = 1
    for i in range(1,n+1):
        acum = acum * i / (2*i -1)
    return acum

def f3(n):
    acum = 0
    num = 2
    signo = 1
    for i in range(1,n+1):
        acum = acum + num*signo
        num = num + 1
        signo = signo * -1
    return acum

def incremento(li, ls, inc):
    for i in range(li,ls+1,inc):
        print(i)

def impares(a, b):
    if a % 2 != 0:
        for i in range(a, b+1, 2):
            print(i)
    else:
        for i in range(a+1, b+1, 2):
            print(i)
        
def menu():
    print("\n\nMENU")
    print("1. Sumatoria")
    print("2. Multiplicatoria")
    print("3. Serie alterna")
    print("4. Incremento")
    print("5. Impares ")
    print("6. Salir")
    
def main():
    menu()
    opcion =  int(input("Introduce una opcion: "))
    if opcion == 1:
        num = int(input("Introduce un número positivo: "))
        res = f1(num)
        print("%.1f" % res)
    elif opcion == 2:
        num = int(input("Introduce un número positivo: "))
        res = f2(num)
        print("%.2f" % res)
    elif opcion == 3:
        num = int(input("Introduce un número positivo: "))
        res = f3(num)
        print("%i" % res)
    elif opcion == 4:
        li = int(input("Introduce el límite inferior: "))
        ls = int(input("Introduce el límite superior: "))
        inc = int(input("Introduce el incremento: "))
        incremento(li, ls, inc)
    elif opcion == 5:
        li = int(input("Introduce el límite inferior: "))
        ls = int(input("Introduce el límite superior: "))
        impares(li, ls)
    elif opcion == 6:
        print("Adios")
    else:
        print("Opcion_invalida")

main()

    
