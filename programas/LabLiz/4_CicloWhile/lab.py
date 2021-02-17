import math

def potencia(x, n):
    cont = 1
    acum = 1
    while cont <= n:
        acum = acum * x
        cont = cont + 1
    return acum

def sumatoria(n):
    i = 1
    acum = 0
    while i <= n:
        acum = acum + math.sqrt(7/5*potencia(i,2))/(math.sqrt(potencia(i,5) - potencia(i,2)) + 10)
        i = i + 1
    return acum

def sumatoria(n):
    i = 1
    acum = 0
    while i <= n:
        acum = acum + math.sqrt(7/5*potencia(i,2))/(math.sqrt(potencia(i,5) - potencia(i,2)) + 10)
        i = i + 1
    return acum

def serie(n):
    i = 1
    acum = 0
    num = 31
    signo = 1
    while i <= n:
        acum = acum + num*signo
        signo = signo * -1
        num = num + 1
        i = i + 1
    return acum

def aproximacion_PI(n):
    i = 2
    acum = 0
    while i <= n:
        acum = acum + 1/i**2
        i = i + 2
    return math.sqrt(24 * acum)

def division(num, den):
    cont = 0
    while num >= den:
        num = num - den
        cont = cont + 1
    return cont

def menu():
    print("1. Potencia")
    print("2. Sumatoria")
    print("3. Serie")
    print("4. Aproximación PI")
    print("5. División")
    print("6. Salir")

def main():
    continua = True
    while continua:
        print("\n")
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            x = int(input("Introduce la base: "))
            n = int(input("Introduce la potencia: "))
            res = potencia(x, n)
            print("El resultado es:", res)
        elif opcion == 2:
            n = int(input("Introduce el valor de n: "))
            res = sumatoria(n)
            print("El resultado es: %.2f" % res)
        elif opcion == 3:
            n = int(input("Introduce el valor de n: "))
            res = serie(n)
            print("El resultado es:", res)
        elif opcion == 4:
            n = int(input("Introduce el valor de n: "))
            res = aproximacion_PI(n)
            print("El resultado es: %.4f" % res)
        if opcion == 5:
            n = int(input("Introduce el numerador: "))
            d = int(input("Introduce el denominador: "))
            res = division(n, d)
            print("El resultado es:", res)
        elif opcion == 6:
            print("Adios")
            continua = False
        else:
            print("ERROR OPCION INVALIDA")
            continua = False

main()