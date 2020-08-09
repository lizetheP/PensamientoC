def creaLista(tam):
    lista = []
    for i in range(0,tam):
        lista.append(i)
    return lista

def sumaDos(A):
    for i in range(len(A)):
        A[i] = A[i] + 2

def imprime(A):
    for i in range(len(A)):
        print("Arreglo[", i, "] = ", A[i])
        
        
t = int(input("Introduce el tamaño de la lista: "))        
A = creaLista(t)
imprime(A)
sumaDos(A)
print("\nSUMA DOS")
imprime(A)


