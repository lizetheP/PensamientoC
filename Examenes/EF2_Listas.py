def crea_lista(tam):
    lista = []
    for i in range(tam):
        valor = int(input("Dame un valor: "))
        lista.insert(i, valor)
    return lista

def pares_impares(lista):
    pares = []
    impares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
        else:
            impares.append(lista[i])
    print("Pares ", pares)
    print("Impares ", impares)
    
def main():
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    print(lista)
    pares_impares(lista)
    
main()