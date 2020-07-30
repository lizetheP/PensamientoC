def sumaDos (A):
    for i in range(len(A)):
        A[i] = A[i] + 2

def imprime(A):
    print("\n")
    for i in range(len(A)):
        print(" A[", i, "] = ", A[i])
        
B = [0,1,2,3,4,5,6,7,8, 9]
imprime(B)
sumaDos(B)
imprime(B)
