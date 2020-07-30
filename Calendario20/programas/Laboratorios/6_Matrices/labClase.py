def imprimeMatriz(M):
    for i in range(0, len(M)):
        for j in range (len(M[i])):
                print(M[i][j], end= ' ')
        print()

M = [[1,2,3],[4,5,6],[7,8,9]]
x1 = 10
x2 = 20
M[0][0] = x1
M[1][0] = x2
M[0][2] = M[0][0] * x2
imprimeMatriz(M)'