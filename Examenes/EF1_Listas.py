def crea_lista(tam):
    lista = []
    for i in range(tam):
        valor = int(input("Dame un valor: "))
        lista.insert(i, valor)
    return lista

def esta_ordenado(lista):
    res = True
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            res = False
    return res

def main():
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    print(lista)
    x = esta_ordenado(lista)
    print(x)
    
main()