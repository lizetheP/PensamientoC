#título          :laboratorio while.py
#descripción     :Ejercicios sobre ciclos.
#autor           :Benjamín Valdés
#python_version  :3.5.2
#===============================================================

# ejemplos para el laboratorio de ciclos en python_version
# dar un numero para seleccionar la funcion que se desea correr
# y despues dar los parametros de cada funcion


 
def crea_lista(tam):
    i = 0
    lista = []

    while(i < tam):
        lista.append(int(input()))
        i = i + 1
    return lista
         
def inicializa_lista(lista, valor):
    i = 0

    for elemento in lista:
        lista[i] = valor
        i = i + 1
        
def cuenta_impares(lista):
    cont = 0

    for num in lista:
        if num % 2 != 0:
            cont = cont + 1
    return cont
    

def invierte_lista(lista):
    tam = len(lista)-1
    i = 0
    
    while (i < tam/2 ):
        aux = lista[i]
        lista[i] = lista[tam - i]
        lista[tam - i] = aux
        i =  i + 1
    return lista
    
def mayor(lista):
    if len(lista) == 0:
        return False
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
           
    return mayor
    
    

opcion = int(input())
if opcion == 1:
    tam = int(input())
    lista = crea_lista(tam)
    print (lista)
elif opcion == 2:
    tam = int(input())
    lista = crea_lista(tam)
    valor = int(input())
    inicializa_lista(lista, valor)
    print (lista)
elif opcion == 3:
    tam = int(input())
    lista = crea_lista(tam)
    print(cuenta_impares(lista))    
elif opcion == 4:
    tam = int(input())
    lista = crea_lista(tam)
    invierte_lista(lista)
    print (lista)
elif opcion == 5:
    tam = int(input())
    lista = crea_lista(tam)
    print(mayor(lista))
else:
    print("entrada no valida")


    