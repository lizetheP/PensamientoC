import math
import random

def crea_lista(tam):
    lista = []
    for i in range(0, tam):
        num = int(input("Dame un valor: "))
        lista.append(num)
    return lista

def inicializa_lista(lista):
    for i in range(0, len(lista)):
        lista[i] = random.randint(-25, 25)

def lista_positiva(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = lista[i]*-1

def media(lista):
    acum = 0
    for i in range(len(lista)):
        acum = acum + lista[i]
    return acum / len(lista)

def menu():
    print()
    print("1. Inicializa lista")
    print("2. Lista positiva")
    print("3. Media")
    print("4. Salir")  
    
def main():
    continua = True
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            print(lista)
            inicializa_lista(lista)
            print(lista)
        elif opcion == 2:
            print(lista)
            lista_positiva(lista)
            print(lista)
        elif opcion == 3:
            print(lista)
            if len(lista) > 0:
                res = media(lista)
                print("La media es %.2f" % res)
            else:
                print("Error la lista está vacia")
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Error Opción inválida")
    
main()
"""

def main():
    continua = True
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:

        elif opcion == 2:

        elif opcion == 3:
        
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()

def main():
    continua = True
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:

        elif opcion == 2:
             pass
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()

"""