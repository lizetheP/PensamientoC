import math

def promedio(A):
    acum = 0
    for i in range(len(A)):
        acum = acum + A[i]
    return acum/len(A)

def menor(A):
    m = A[0]
    for i in range(len(A)):
        if A[i] < m:
            m = A[i]
    return m

def longitud(A):
    cont = 0
    for ele in A:
        cont = cont+1
    return cont

def varianza(A):
    acum = 0
    for i in range(len(A)):
        res =A[i] - promedio(A)
        acum = acum + (A[i] - promedio(A))
    return math.sqrt(acum/len(A))

def menu():
    print()
    print("1. Promedio")
    print("2. Menor")
    print("3. Longitud")
    print("4. Varianza")
    
B = [1, 3, 5, 10, -3, 12, 5, 9, 9, -5]
while True:
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        res = promedio(B)
        print("El promedio es: ", res)
    elif opcion == 2:
        men = menor(B)
        print("El menor elemento es: ", men)
    elif opcion == 3:
        l = longitud(B)
        print("La longitud es: ", l)
    elif opcion == 4:
        res = varianza(B)
        print("La varianza es: ", res)
    else:
        print("Opción inválida")
        break
