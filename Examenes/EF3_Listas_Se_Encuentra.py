def crea_lista(tam):
    lista = []
    for i in range(tam):
        valor = int(input("Dame un valor: "))
        lista.insert(i, valor)
    return lista

def se_encuentra(lista, x):
    esta = False
    for i in range(len(lista)):
        if lista[i] == x:
            esta = True
    return esta
    
def main():
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    print(lista)
    x = int(input("Dame el valor a buscar: "))
    res = se_encuentra(lista, x)
    print(res)
    
main()