def crea_lista(tam):
    lista = []
    for i in range(tam):
        valor = int(input("Dame un valor: "))
        lista.insert(i, valor)
    return lista

def suma_pares(lista):
    suma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            suma = suma + lista[i]
    return suma

def main():
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    if t > 0:
        res = suma_pares(lista)
        print("La suma es: ", res)
    else:
        print(0)
        
main()