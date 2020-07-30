def creaLista(tam):
    A=[]
    for i in range(0, tam):
        valor = int(input())
        A.insert(i, valor)
    return A

def inicializaLista(lista, valor):
    for i in range(0, len(lista)):
        lista[i] = valor
    
def cuentaImpares(lista):
    cont = 0
    for i in range(0, len(lista)):
        if lista[i]%2 != 0:
            cont = cont + 1
    return cont

def invierteLista(lista):
    ultimo = len(lista)-1
    limite = len(lista)//2
    for i in range(0, limite):
        temp = lista[i]
        lista[i] = lista[ultimo]
        lista[ultimo] = temp
        ultimo = ultimo -1
    
def mayorValor(lista):
    if len(lista) == 0:
        return False
    else:
        m = lista[0]
        for i in range(0, len(lista)):
            if lista[i]>m:
                m=lista[i]
        return m

opcion = int(input())
if opcion == 1:
    t = int(input())
    lista = creaLista(t)
    print(lista)
elif opcion == 2:
    t = int(input())
    lista = creaLista(t)
    num = int(input())
    inicializaLista(lista, num)
    print(lista)
elif opcion == 3:
    t = int(input())
    lista = creaLista(t)
    res = cuentaImpares(lista)
    print(res)
elif opcion == 4:
    t = int(input())
    lista = creaLista(t)
    invierteLista(lista)
    print(lista)
elif opcion == 5:
    t = int(input())
    lista = creaLista(t)
    res = mayorValor(lista)
    print(res)
else:
    print("Opción inválida")

  