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
    
B = [1, 3, 5, 10, -3, 12, 5, 9, 9, -5]
res = promedio(B)
print("El promedio es: ", res)
men = menor(B)
print("El menor elemento es: ", men)
l = longitud(B)
print("La longitud es: ", l)
res = varianza(B)
print("La varianza es: ", res)