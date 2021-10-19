def crea_lista(tam):
    lista = []
    for i in range(tam):
        valor = int(input())
        lista.insert(i, valor)
    return lista

def imprime(lista):
    for i in range(len(lista)):
        print("lista[%i] = %i" % (i, lista[i]))

def main():
    t = int(input())
    lista = crea_lista(t)
    imprime(lista)

main()