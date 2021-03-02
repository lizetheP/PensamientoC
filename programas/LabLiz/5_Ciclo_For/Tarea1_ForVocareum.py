import math

def f1(n):
    acum = 0
    for i in range(0,n+1):
        acum = acum + 2**i
    return acum

def f2(n):
    acum = 1
    for i in range(1,n+1):
        acum = acum * (3 * i - 1)
    return acum

def f3(n):
    acum = 0
    num = 1
    signo = 1
    for i in range(1,n+1):
        acum = acum + num*signo
        num = num + 1
        signo = signo * -1
    return acum

def decremento(ls, li, dec):
    for i in range(ls,li-1,-dec):
        print(i)

def pares(a, b):
    if a % 2 == 0:
        for i in range(a, b+1, 2):
            print(i)
    else:
        for i in range(a+1, b+1, 2):
            print(i)
        
def menu():
    print("\n MENU")
    print("1. Sumatoria")
    print("2. Multiplicatoria")
    print("3. Serie alterna")
    print("4. Incremento")
    print("5. Impares ")
    print("6. Salir")
    
def main():
    #menu()
    opcion =  int(input())
    if opcion == 1:
        num = int(input())
        res = f1(num)
        print(res)
    elif opcion == 2:
        num = int(input())
        res = f2(num)
        print(res)
    elif opcion == 3:
        num = int(input())
        res = f3(num)
        print(res)
    elif opcion == 4:
        ls = int(input())
        li = int(input())
        dec = int(input())
        decremento(ls, li, dec)
    elif opcion == 5:
        li = int(input())
        ls = int(input())
        pares(li, ls)
    elif opcion == 6:
        print("Adios")
    else:
        print("Opcion_invalida")

main()

"""
f1(4) = 31
f2(5) = 12320
f3(7) = 4
decremento(28,7,4) = 28 24 20 16 12 8
pares(-7, 4) = -6 -4 -2 0 2 4


"""
