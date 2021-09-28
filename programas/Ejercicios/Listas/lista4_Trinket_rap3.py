def crea_lista(tam):
    lista = []
    for i in range(tam):
        valor = int(input("Dame un valor: "))
        lista.insert(i, valor)
    return lista

def multiplosX_posicion(lista, x):
    for i in range(len(lista)):
        if lista[i] % x == 0:
            print("posición %i, valor %i" % (i, lista[i]))

def main():
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    print(lista)
    x = int(input("Dame el valor de x: "))
    multiplosX_posicion(lista, x)
    
main()