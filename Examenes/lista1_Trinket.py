def crea_lista(tam):
    lista = []
    for i in range(tam):
        valor = int(input("Dame un valor: "))
        lista.insert(i, valor)
    return lista

def imprime(lista):
    for i in range(len(lista)):
        print("lista[%i] = %i" % (i, lista[i]))

def main():
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    imprime(lista)

main()