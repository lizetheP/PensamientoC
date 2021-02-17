def suma_dos (A):
    for i in range(len(A)):
        A[i] = A[i] + 2

def main():
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    suma_dos(A)
    print(A)
    
main()

