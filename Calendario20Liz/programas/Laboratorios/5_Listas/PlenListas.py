def creaLista(tam):
    A=[]
    for i in range(0, tam):
        valor = int(input("Introduce un valor: "))
        A.insert(i, valor)
    return A

def inicializaLista(lista, valor):
    for i in range(0, len(lista)):
        lista[i] = valor
    return lista

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
    return lista

def mayorValor(lista):
    m = lista[0]
    for i in range(0, len(lista)):
        if lista[i]>m:
            m=lista[i]
    return m

def menu():
    print("1. Crea lista")
    print("2. Inicializa lista")
    print("3. Cuenta impares")
    print("4. Invierte lista")
    print("5. Mayor lista")

menu()
opcion = int(input("Introduce una opcion: "))
if opcion == 1:
    t = int(input("Introduce el tamaño del arreglo: "))
    print(creaLista(t))
elif opcion == 2:
    t = int(input("Introduce el tamaño del arreglo: "))
    num = int(input("Introduce el número default: "))
    print(inicializaLista(creaLista(t), num))
elif opcion == 3:
    t = int(input("Introduce el tamaño del arreglo: "))
    res = cuentaImpares(creaLista(t))
    print("El número de impares es: ", res)
elif opcion == 4:
    t = int(input("Introduce el tamaño del arreglo: "))
    print(invierteLista(creaLista(t)))
elif opcion == 5:
    t = int(input("Introduce el tamaño del arreglo: "))
    if t == 0:
        print("False")
    else:
        res = mayorValor(creaLista(t))
        print("El mayor es: ", res)
else:
    print("Opción inválida")

  