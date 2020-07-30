def iniciaMatriz (M):
    for i in range(0, len(M)):
        for j in range(0, len(M[i])):
            M[ i ][ j ] = 5;

def imprimeMatriz(M):
    print()
    for i in range(0, len(M)):
        for j in range(0, len(M[i])):
            print("%3i"%(M[ i ][ j ]), end= '')
        print()

def iniciaMatriz2 (M):
    num = 1
    for i in range(0, len(M)):
        for j in range(0, len(M[i])):
            M[ i ][ j ] = num
            num = num + 1

def sumaMatrices (A, B, C):
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            C[ i ][ j ] = A[i][j] + B[i][j]

m = [ [1, 2, 3 ],[4, 5, 6],[7, 8, 9] ]
m2 = [ [1, 2, 3 ],[4, 5, 6],[7, 8, 9] ]
m3 = [ [1, 2, 3 ],[4, 5, 6],[7, 8, 9] ]

iniciaMatriz(m)
imprimeMatriz(m)

iniciaMatriz2(m2)
imprimeMatriz(m2)

sumaMatrices(m, m2, m3)
imprimeMatriz(m3)
