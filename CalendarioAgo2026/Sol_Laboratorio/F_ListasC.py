import math
import random

def crea_lista(tam):
    lista = []
    for i in range(0, tam):
        num = int(input("Dame un valor: "))
        lista.append(num)
    return lista

def cuenta_multiplos(lista, x):
    cont = 0
    for i in range(len(lista)):
        if lista[i] % x == 0 and lista[i] > 0: 
         cont = cont + 1
    return cont

def suma_impares(lista):
    acum = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0: 
         acum = acum + lista[i]
    return acum

def menu():
    print()
    print("1. Cuenta múltiplos")
    print("2. Suma impares")
    print("3. Salir")  
    
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            t = int(input("Dame el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
            x = int(input("Dame el valor de x: "))
            res = cuenta_multiplos(lista, x)
            print("Cantidad de múltiplos:", res) 
        elif opcion == 2:
            t = int(input("Dame el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
            res = suma_impares(lista)
            print("La suma de impares es:", res) 
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()

def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            t = int(input("Dame el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)

        elif opcion == 2:
            pass
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()


