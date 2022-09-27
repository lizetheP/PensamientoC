def crea_matriz(tam):
    lista = []
    for i in range(tam):
        lista.append('_')
    return lista

def sustituye_letra(lista, lista2, letra):
    for i in range(len(lista)):
        if lista[i] == letra:
            lista2[i] = letra

def main():
    palabra = input("Dame una palabra: ")
    lista = list(palabra)
    print(lista)
    t = len(lista)
    lista2 = crea_matriz(t)
    print(lista2)
    letra = input("Dame una letra: ")
    sustituye_letra(lista, lista2, letra)
    print(lista2)

main()