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

def desviacion(lista):
    acum = 0
    for i in range(len(lista)):
        acum = acum + (lista[i] - media(lista))**2
    return math.sqrt(acum / len(lista))

def sustituye(lista, x, y):
    for i in range(len(lista)):
        if lista[i] == x:
            lista[i] = y

def mayor(lista):
    m = lista[0]
    for i in range(len(lista)):
        if lista[i] > m:
            m = lista[i]
    return m

def menu():
    print()
    print("1. Crea lista")
    print("2. Inicializa lista")
    print("3. Lista positiva")
    print("4. Media")
    print("5. Desviación estándar")
    print("6. Sustituye lista")
    print("7. Mayor")
    print("8. Salir")  
    
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
            t = int(input("Dame el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
            inicializa_lista(lista)
            print(lista)
        elif opcion == 3:
            t = int(input("Dame el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
            inicializa_lista(lista)
            print(lista)
            lista_positiva(lista)
            print(lista)
        elif opcion == 4:
            t = int(input("Dame el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
            if len(lista) > 0:
                res = media(lista)
                print("La media es %.2f" % res)
            else:
                print("Error la lista está vacia")
        elif opcion == 5:
            t = int(input("Dame el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
            if len(lista) > 0:
                res = desviacion(lista)
                print("La desviación estándar es %.2f" % res)
            else:
                print("Error la lista está vacia")
        elif opcion == 6:
            t = int(input("Dame el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
            x = int(input("Dame el valor a buscar: "))
            y = int(input("Dame el valor a sustituir: "))
            sustituye(lista, x, y)
            print(lista)
        elif opcion == 7:
            t = int(input("Dame el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
            if len(lista) > 0:
                res = mayor(lista)
                print("El mayor es %i" % res)
            else:
                print("Error la lista está vacia")
        elif opcion == 8:
            print("Adiós")
            continua = False
        else:
            print("Error Opción inválida")
    
main()