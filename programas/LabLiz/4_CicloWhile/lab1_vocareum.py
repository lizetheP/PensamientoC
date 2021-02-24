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
        acum = acum + math.sqrt(3/4*i) / (math.sqrt(potencia(i,5)) - potencia(i,2) + 1)
        i = i + 1
    return acum

def serie(n):
    i = 1
    acum = 0
    num = 10
    signo = 1
    while i <= n:
        acum = acum + num*signo
        signo = signo * -1
        num = num + 1
        i = i + 1
    return acum

def aproximacion_PI(n):
    i = 1
    acum = 0
    signo = 1
    while i <= n:
        acum = acum + 1/i*signo
        signo = signo * -1
        i = i + 2
    return 4*acum

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
    opcion = int(input())
    if opcion == 1:
        x = int(input())
        n = int(input())
        res = potencia(x, n)
        print(res)
    elif opcion == 2:
        n = int(input())
        res = sumatoria(n)
        print("%.2f" % res)
    elif opcion == 3:
        n = int(input())
        res = serie(n)
        print(res)
    elif opcion == 4:
        n = int(input())
        res = aproximacion_PI(n)
        print("%.4f" % res)
    elif opcion == 5:
        n = int(input())
        d = int(input())
        res = division(n, d)
        print(res)
    elif opcion == 6:
        print("Adios")
    else:
        print("ERROR OPCION INVALIDA")

main()