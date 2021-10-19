def crea_lista(tam):
    lista = []
    for i in range(tam):
        valor = int(input("Dame un valor: "))
        lista.insert(i, valor)
    return lista

def promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma/len(lista)

def main():
    t = int(input("Dame el tamaño de la lista: "))
    lista = crea_lista(t)
    if t > 0:
        res = promedio(lista)
        print("El promedio es: %.2f" % res)
    else:
        print(0)
        
main()