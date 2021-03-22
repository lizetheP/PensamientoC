import random
import math

def crea_lista(tam):
    lista = []
    for i in range(0, tam):
        valor = int(input())
        lista.insert(i, valor)
    return lista

def inicializa_lista(lista, valor):
    for i in range(0, len(lista)):
        lista[i] = valor

def suma_impares(lista):
    acum = 0
    for i in range(0, len(lista)):
        if lista[i]%2 != 0:
            acum = acum + lista[i]
    return acum

def modifica_lista(lista, x):
    for i in range(0, len(lista)):
        lista[i] = lista[i]*x

def cuenta_multiplosx(lista, x):
    cont = 0
    for i in range(0, len(lista)):
        if lista[i] % x == 0 and lista[i] > 0:
            cont = cont + 1       
    return cont
        
def menu():
    print("1. Crea lista")
    print("2. Inicializa lista") 
    print("3. Suma impares")
    print("4. Modifica lista") 
    print("5. Cuenta múltiplos") 
    print("6. Salir")

def main():
    #menu()
    opcion = int(input())
    if opcion == 1:
        t = int(input())
        lista = crea_lista(t)
        print(lista)
    elif opcion == 2:
        t = int(input())
        lista = crea_lista(t)
        valor = int(input())
        inicializa_lista(lista, valor)
        print(lista)
    elif opcion == 3:
        t = int(input())
        lista = crea_lista(t)
        res = suma_impares(lista)
        print(res)
    elif opcion == 4:
        t = int(input())
        lista = crea_lista(t)
        x = int(input())
        modifica_lista(lista, x)
        print(lista)
    elif opcion == 5:
        t = int(input())
        lista = crea_lista(t)
        x = int(input())
        res = cuenta_multiplosx(lista, x)
        print(res)
    elif opcion == 6:
        print("Adios")
    else:
        print("Opcion_invalida")
        
main()
