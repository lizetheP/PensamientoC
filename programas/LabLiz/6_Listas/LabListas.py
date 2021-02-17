import random
import math

def crea_lista(tam):
    lista = []
    for i in range(0, tam):
        valor = int(input("Introduce un valor: "))
        lista.insert(i, valor)
    return lista

def inicializa_lista(lista):
    for i in range(0, len(lista)):
        lista[i] = random.randint(-5,15)

def promedio(lista):
    suma = 0
    for i in range(0, len(lista)):
        suma = suma + lista[i]       
    if len(lista) > 0:
        return suma/len(lista)
    else:
        return False

def varianza(A):
    acum = 0
    for i in range(len(A)):
        acum = acum + math.pow((A[i] - promedio(A)), 2)
    if len(A) > 0:
        return acum/len(A)
    else:
        return 0

def mayor(lista):
    if len(lista) == 0:
        return 0
    else:
        m = lista[0]
        for i in range(0, len(lista)):
            if lista[i]>m:
                m=lista[i]
        return m

def mueve_derecha(lista):
    ultimo = len(lista)-1
    temp = lista[ultimo]
    for i in range(ultimo, 0, -1):
        lista[i] = lista[i - 1]
    lista[0] = temp
    return lista
        
def menu():
    print("1. Crea lista")
    print("2. Inicializa lista") 
    print("3. Promedio")
    print("4. Varianza") 
    print("5. Mayor") 
    print("6. Mueve lista")
    print("7. Salir")
    
def main():    
    continua = True    
    while continua:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
        elif opcion == 2:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            inicializa_lista(lista)
            print(lista)
        elif opcion == 3:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            res = promedio(lista)
            print("El promedio es: %.2f" % res)
        elif opcion == 4:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            res = varianza(lista)
            print("La varianza es: %.2f" % res)
        elif opcion == 5:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            res = mayor(lista)
            print("El mayor es ", res)
        elif opcion == 6:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            mueve_derecha(lista)
            print(lista)
        elif opcion == 7:
            print("Adios")
            continua = False
        else:
            print("Opcion_invalida")

main()
"""
def main():    
    continua = True    
    while continua:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
        elif opcion == 2:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            inicializa_lista(lista)
            print(lista)
        elif opcion == 3:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            res = promedio(lista)
            print("El promedio es: %.2f" % res)
        elif opcion == 4:
      
        elif opcion == 5:
        
        elif opcion == 6:
        
        elif opcion == 7:
            print("Adios")
            continua = False
        else:
            print("Opcion_invalida")
main()
"""