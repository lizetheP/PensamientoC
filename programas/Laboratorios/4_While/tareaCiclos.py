def factorial(n):
    i = 1
    acum = 1
    while i <= n:
        acum = acum*i
        i= i+1
    return acum

def multiplicacion(n1, n2):
    i = 1
    acum = 0
    while i <= n2:
        acum = acum + n1
        i = i + 1
    return acum

def menu():
    print()
    print("1. Factorial")
    print("2. Multiplicación")

while True:
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        num = int(input("Introduce un número: "))
        res = factorial(num)
        print(res)
    elif opcion == 2:
        num1 = int(input("Introduce un número: "))
        num2 = int(input("Introduce otro número: "))
        res = multiplicacion(num1, num2)
        print(res)
    else:
        print("Opción inválida")
        break
