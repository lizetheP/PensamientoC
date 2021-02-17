def crea_lista(tam):
    lista = []
    for i in range(0, tam):
        valor = int(input("Introduce un valor: "))
        lista.insert(i, valor)
    return lista

def promedio_impares(lista):
    suma = 0
    cont = 0
    for i in range(0, len(lista)):
        if (lista[i]%2 != 0):
            suma = suma + lista[i]
            cont = cont + 1
    return suma/cont

def menor(lista):
    m = lista[0]
    for i in range(len(lista)):
        if lista[i] < m:
            m=lista[i]
    return m

def mueve_izquierda(lista):
    temp = lista[0]
    ultimo = len(lista)-1
    for i in range(ultimo):
        lista[i] = lista[i+1]
    lista[ultimo] = temp
         
def main():    
    t = int(input("Introduce el tamaño de la lista: "))
    lista = crea_lista(t)
    print(lista)
    mueve_izquierda(lista)
    print(lista)
    
main()