import math

def f1(n):
    cont = 1
    acum = 0
    num = 20
    signo = 1
    while cont <= n:
        acum = acum + 1/num*signo
        num = num + 1
        cont = cont + 1
        signo = signo * -1
    return acum

def f4(n):
    k = 1
    acum = 0
    while k <= n:
        acum = acum + (k + 2) / k**3
        k = k + 1
    return acum
def menu():
    print("1. f1")
    print("2. f4")
    print("3. Salir")

def main():
    menu()
    opcion = int(input("Dame una opcion: "))
    if opcion == 1:
        num = int(input("Dame un número: "))
        res = f1(num)
        print("f1(%i) = %.5f" % (num, res))
    elif opcion == 2:
        num = int(input("Dame un número: "))
        res = f4(num)
        print("f4(%i) = %.2f" % (num, res))
    elif opcion == 3:
        print("Adiós")
    else:
        print("Error opción inválida")

main()