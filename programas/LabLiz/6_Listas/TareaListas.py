import random
import math

def crea_lista(tam):
    lista = []
    for i in range(0, tam):
        valor = int(input("Introduce un valor: "))
        lista.insert(i, valor)
    return lista

def llena_lista(lista, valor):
    for i in range(0, len(lista)):
        lista[i] = valor

def sustituye_lista(lista, x, y):
    for i in range(0, len(lista)):
        if lista[i] == x:
            lista[i] = y
            
def cuenta_pares(lista):
    cont = 0
    for i in range(0, len(lista)):
        if lista[i]%2 == 0:
            cont = cont + 1
    return cont

def suma_multiplosx(lista, x):
    suma = 0
    for i in range(0, len(lista)):
        if lista[i] % x == 0:
            suma = suma + lista[i]       
    if len(lista) > 0:
        return suma
    else:
        return 0
        
def menu():
    print("1. Crea lista")
    print("2. Llena lista") 
    print("3. Sustituye")
    print("4. Cuenta pares") 
    print("5. Suma multiplosx") 
    print("6. Salir")

def main():
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        t = int(input("Introduce el tamaño de la lista: "))
        lista = crea_lista(t)
        print(lista)
    elif opcion == 2:
        t = int(input("Introduce el tamaño de la lista: "))
        lista = crea_lista(t)
        valor = int(input("Introduce el valor default: "))
        llena_lista(lista, valor)
        print(lista)
    elif opcion == 3:
        t = int(input("Introduce el tamaño de la lista: "))
        lista = crea_lista(t)
        x = int(input("Introduce el valor de x: "))
        y = int(input("Introduce el valor de y: "))
        sustituye_lista(lista, x, y)
        print(lista)
    elif opcion == 4:
        t = int(input("Introduce el tamaño de la lista: "))
        lista = crea_lista(t)
        res = cuenta_pares(lista)
        print("El número de pares es : %i" % res)
    elif opcion == 5:
        t = int(input("Introduce el tamaño de la lista: "))
        lista = crea_lista(t)
        x = int(input("Introduce el valor de x: "))
        res = suma_multiplosx(lista, x)
        print("La suma de multiplos es ", res)
    elif opcion == 6:
        print("Adios")
    else:
        print("Opcion_invalida")
        
main()
"""
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
        llena_lista(lista, valor)
        print(lista)
    elif opcion == 3:
        t = int(input())
        lista = crea_lista(t)
        x = int(input())
        y = int(input())
        sustituye_lista(lista, x, y)
        print(lista)
    elif opcion == 4:
        t = int(input())
        lista = crea_lista(t)
        res = cuenta_pares(lista)
        print("%i" % res)      
    elif opcion == 5:
       
    elif opcion == 6:
        print("Adios")
    else:
        print("Opcion_invalida")
main()

def crea_lista(tam):
    lista = []
    for i in range(0, tam):
        valor = int(input("Introduce un valor: "))
        lista.insert(i, valor)
    return lista

def llena_lista(lista, valor):
    for i in range(0, len(lista)):
        lista[i] = valor

def sustituye_lista(lista, x, y):
    for i in range(0, len(lista)):
        if lista[i] == x:
            lista[i] = y
            
def cuenta_pares(lista):
    cont = 0
    for i in range(0, len(lista)):
        if lista[i]%2 == 0:
            cont = cont + 1
    return cont

def suma_multiplosx(lista, x):
    suma = 0
    for i in range(0, len(lista)):
        if lista[i] % x == 0:
            suma = suma + lista[i]       
    if len(lista) > 0:
        return suma
    else:
        return 0
        
def menu():
    print("1. Crea lista")
    print("2. Llena lista") 
    print("3. Sustituye")
    print("4. Cuenta pares") 
    print("5. Suma multiplosx") 
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
        llena_lista(lista, valor)
        print(lista)
    elif opcion == 3:
        t = int(input())
        lista = crea_lista(t)
        x = int(input())
        y = int(input())
        sustituye_lista(lista, x, y)
        print(lista)
    elif opcion == 4:
        t = int(input())
        lista = crea_lista(t)
        res = cuenta_pares(lista)
        print(res)      
    elif opcion == 5:
        t = int(input())
        lista = crea_lista(t)
        x = int(input())
        res = suma_multiplosx(lista, x)
        print(res)
    elif opcion == 6:
        print("Adios")
    else:
        print("Opcion_invalida")

main()

Casos de prueba 1
Introduce una opcion: 1
Introduce el tamaño de la lista: 3
Introduce un valor: 4
Introduce un valor: 5
Introduce un valor: 6
[4, 5, 6]

Caso de prueba 2
Introduce una opcion: 2
Introduce el tamaño de la lista: 3
Introduce un valor: 4
Introduce un valor: 5
Introduce un valor: 6
Introduce el valor default: 7
[7, 7, 7]

Introduce una opcion: 3
Introduce el tamaño de la lista: 5
Introduce un valor: 5
Introduce un valor: 6
Introduce un valor: 7
Introduce un valor: 8
Introduce un valor: 5
Introduce el valor de x: 5
Introduce el valor de y: 1
[1, 6, 7, 8, 1]

Introduce una opcion: 4
Introduce el tamaño de la lista: 3
Introduce un valor: 2
Introduce un valor: 4
Introduce un valor: 6
El número de pares es : 3

Introduce una opcion: 5
Introduce el tamaño de la lista: 5
Introduce un valor: 7
Introduce un valor: 4
Introduce un valor: 3
Introduce un valor: 9
Introduce un valor: 12
Introduce el valor de x: 3
La suma de multiplos es  24
"""