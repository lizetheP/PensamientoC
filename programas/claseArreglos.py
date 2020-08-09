def inicializa (A):
    for i in range(0,10):
        A.append(i)

def sumaDos (A):
    for i in range(len(A)):
        A[i] = A[i] + 2

def imprime(A):
    for i in range(len(A)):
        print("Arreglo[", i, "] = ", A[i])
        
A = []
inicializa(A)
imprime(A)
sumaDos(A)
print("\nSUMA DOS")
imprime(A)

