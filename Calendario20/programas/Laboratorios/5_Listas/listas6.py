def sumaDos (B):
    for i in range(len(B)):
        B[i] = B[i] + 2

def imprime(B):
    for i in range(len(B)):
        print(" Arreglo[", i, "] = ", B[i])

A = [0,1,2,3,4,5,6,7,8, 9]
imprime(A)
sumaDos(A)
imprime(A)
