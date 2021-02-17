def crea_lista(tam):
    lista = []
    for i in range(tam):
        valor = int(input())
        lista.insert(i, valor)
    return lista

def imprime(lista):
    for i in range(len(lista)):
        print("lista[%i] = %i" % (i, lista[i]))

def promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma/len(lista)

def main():
    t = int(input())
    lista = crea_lista(t)
    if t > 0:
        res = promedio(lista)
        print("%.1f" % res)
    else:
        print(0)
        
main()